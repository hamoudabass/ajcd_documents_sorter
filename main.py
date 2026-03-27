import os
import shutil
from PyPDF2 import PdfMerger

# 📂 Chemins
DOCUMENTS_PATH = os.path.expanduser("~/Documents")
TARGET_PATH = os.path.join(DOCUMENTS_PATH, "AJCD_ORPHAN_FILES")


def get_next_folder_number():
    """Retourne le prochain numéro de dossier"""
    existing = [int(name) for name in os.listdir(TARGET_PATH) if name.isdigit()]
    return max(existing, default=0) + 1


def scan_files():
    """Récupère les fichiers nécessaires"""
    files = os.listdir(DOCUMENTS_PATH)

    an_files = [f for f in files if f.startswith("AN") and f.endswith(".pdf")]
    ad_file = next((f for f in files if f.startswith("AD") and f.endswith(".pdf")), None)
    am_file = next((f for f in files if f.startswith("AM") and f.endswith(".pdf")), None)
    cni_file = next((f for f in files if f.startswith("CNI") and f.endswith(".pdf")), None)

    # 🔢 Trier les AN par date (plus ancien → plus récent)
    an_files.sort(key=lambda f: os.path.getmtime(os.path.join(DOCUMENTS_PATH, f)))

    return an_files, ad_file, am_file, cni_file


def merge_pdfs(folder_path, files_order):
    """Fusionne les PDF dans l'ordre donné"""
    merger = PdfMerger()

    for file in files_order:
        file_path = os.path.join(folder_path, file)
        if os.path.exists(file_path):
            merger.append(file_path)

    output_path = os.path.join(folder_path, "dossier_complet.pdf")
    merger.write(output_path)
    merger.close()


def process():
    """Traitement principal déclenché par 'start'"""
    while True:
        command = input("👉 Tapez 'start' pour lancer le traitement : ").strip().lower()

        if command != "start":
            print("❌ Commande inconnue")
            continue

        print("🔄 Mise à jour des anciens dossiers...")
        merge_existing_folders()

        an_files, ad_file, am_file, cni_file = scan_files()

        # ❌ Vérification
        if not an_files or not ad_file or not (am_file or cni_file):
            print("⚠️ Fichiers incomplets, traitement annulé.")
            continue

        print("✅ Traitement en cours...")

        for an in an_files:
            folder_number = get_next_folder_number()
            new_folder = os.path.join(TARGET_PATH, str(folder_number))
            os.makedirs(new_folder)

            # 🚚 Déplacer AN
            shutil.move(
                os.path.join(DOCUMENTS_PATH, an),
                os.path.join(new_folder, an)
            )

            # 📄 Copier AD
            shutil.copy(
                os.path.join(DOCUMENTS_PATH, ad_file),
                os.path.join(new_folder, ad_file)
            )

            files_to_merge = [an, ad_file]

            # 📄 Copier AM et/ou CNI
            if am_file:
                shutil.copy(
                    os.path.join(DOCUMENTS_PATH, am_file),
                    os.path.join(new_folder, am_file)
                )
                files_to_merge.append(am_file)

            if cni_file:
                shutil.copy(
                    os.path.join(DOCUMENTS_PATH, cni_file),
                    os.path.join(new_folder, cni_file)
                )
                files_to_merge.append(cni_file)

            # 🔗 Fusion PDF (ordre respecté)
            merge_pdfs(new_folder, files_to_merge)

            print(f"📁 Dossier {folder_number} créé + fusion OK")

        # 🧹 Suppression des fichiers restants
        os.remove(os.path.join(DOCUMENTS_PATH, ad_file))

        if am_file:
            os.remove(os.path.join(DOCUMENTS_PATH, am_file))
        if cni_file:
            os.remove(os.path.join(DOCUMENTS_PATH, cni_file))

        print("🧹 Nettoyage terminé. Documents est propre.\n")

def merge_existing_folders():
    """Fusionne les PDF dans tous les dossiers existants"""
    folders = [f for f in os.listdir(TARGET_PATH) if f.isdigit()]

    for folder in folders:
        folder_path = os.path.join(TARGET_PATH, folder)
        files = os.listdir(folder_path)

        # Détection fichiers
        an = next((f for f in files if f.startswith("AN")), None)
        ad = next((f for f in files if f.startswith("AD")), None)
        am = next((f for f in files if f.startswith("AM")), None)
        cni = next((f for f in files if f.startswith("CNI")), None)

        if not an or not ad:
            continue

        files_to_merge = [an, ad]

        if am:
            files_to_merge.append(am)
        if cni:
            files_to_merge.append(cni)

        merge_pdfs(folder_path, files_to_merge)

        print(f"🔁 Fusion mise à jour pour dossier {folder}")

if __name__ == "__main__":
    if not os.path.exists(TARGET_PATH):
        os.makedirs(TARGET_PATH)

    print("🚀 Programme prêt...")
    process()