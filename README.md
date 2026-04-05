# AJCD DOCUMENT SORTER
Automatiser le classement et le fusion de fichiers PDF pour les dossiers orphelins pour l'association AJCD !

# 🎯 Objectif
Ce programme Python permet de :

1. Trier automatiquement les fichiers PDF placés dans le dossier Documents.
2. Créer des dossiers numérotés dans AJCD_ORPHAN_FILES.
3. Déplacer et copier les fichiers nécessaires (AN, AD, AM, CNI) selon les règles métier.
4. Fusionner tous les fichiers PDF de chaque dossier en un seul fichier dossier_complet.pdf.
5. Maintenir les fichiers originaux tout en nettoyant Documents pour qu’il ne reste aucun fichier PDF en vrac.
6. Fusionner également les fichiers PDF déjà présents dans les dossiers existants.

# 📂Structure attendue
Avant traitement :

```bash
  Documents/
├── AJCD_ORPHAN_FILES/
├── AN ALI.pdf
├── AN SAADA.pdf
├── AD.pdf
├── AM.pdf et/ou CNI.pdf
```
Après traitement :
```bash
Documents/
└── AJCD_ORPHAN_FILES/
    ├── 432/
    │   ├── AN ALI.pdf
    │   ├── AD.pdf
    │   ├── AM.pdf
    │   ├── CNI.pdf
    │   └── dossier_complet.pdf
    ├── 433/
    │   └── ...
```

# 🛠️ Fonctionnalités principales
```bash
✅ Tri automatique : les fichiers AN multiples sont traités dans l’ordre chronologique (plus ancien → plus récent).
✅ Fusion PDF : création d’un fichier dossier_complet.pdf par dossier, ordre : AN → AD → AM → CNI.
✅ Traitement manuel : le programme attend que l’utilisateur tape start pour lancer le tri et la fusion.
✅ Fusion dossiers existants : les anciens dossiers sont automatiquement fusionnés lors de chaque démarrage.
✅ Nettoyage : aucun fichier PDF ne reste dans Documents après traitement.
✅ Conservation des fichiers originaux : les PDF originaux restent dans chaque dossier après fusion.
```
# ⚙️ Prérequis
Python ≥ 3.7

Bibliothèque Python :
```bash
pip install PyPDF2
```

Structure minimale :
```bash
...Documents/
...Documents/AJCD_ORPHAN_FILES/ (sera créé automatiquement si manquant)
```
# 🚀 Utilisation
1. Placer vos fichiers PDF dans le dossier Documents/ :
```bash
...AN (obligatoire, peut être multiple)
...AD (obligatoire)
...AM ou CNI (au moins un)
```

2. Aller dans le dossier du programme (ex: Desktop/ajcd_document_sorter) :
```bash
cd Desktop/ajcd_document_sorter
```
3. Lancer le script :
```bash
python script.py
```
**Démarrer le traitement** :

4. Le script attend ton signal
```bash
start
```
5. Résultat :
```bash
...Tous les fichiers sont triés dans AJCD_ORPHAN_FILES/
...Chaque dossier contient un dossier_complet.pdf fusionné
...Documents/ est vide de PDF
```

# 🧩 Fonctionnement interne
1. Le script scanne Documents pour détecter tous les fichiers requis.
2. Vérifie les conditions :
 ```bash
 . au moins un AN
 . AD présent
 . AM ou CNI présent
 ```
3. Fusion des anciens dossiers déjà présents dans AJCD_ORPHAN_FILES.
4. Pour chaque fichier AN :
```bash
    Crée un nouveau dossier numéroté
    Déplace AN
    Copie AD, AM, CNI selon disponibilité
    Fusionne les fichiers dans dossier_complet.pdf
 ```
5. Supprime les fichiers originaux de Documents (mais pas ceux copiés dans les dossiers).

# 💡 Conseils d’utilisation
    - Toujours placer les fichiers dans Documents/ avant de taper start.
    - Vérifier que les fichiers PDF sont correctement nommés (AN, AD, AM, CNI).
    - Les dossiers sont numérotés automatiquement en suivant le dernier existant.
    - Le script peut être relancé plusieurs fois, il fusionnera toujours les dossiers existants et traitera les nouveaux fichiers.

# 🛡️ Gestion des erreurs
    Le script ignore les dossiers qui ne contiennent pas les fichiers obligatoires.
    Si un PDF est manquant, il attend que tous les fichiers nécessaires soient présents.
    Les fichiers originaux ne sont pas écrasés lors de la fusion.

# 🔖 Auteur

- [@hamoudabass](https://www.github.com/hamoudabass)