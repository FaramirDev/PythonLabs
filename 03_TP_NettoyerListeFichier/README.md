===========================================
## NETTOYEUR DE FICHIER CSV - README
===========================================

**1. DESCRIPTION**
--------------
Ce script Python nettoie un fichier CSV contenant une liste de noms de fichiers en :
- Supprimant les doublons
- Supprimant les entrées vides
- Ne gardant que les fichiers avec les extensions .txt ou .csv
- Enregistrant le résultat dans un nouveau fichier CSV

**2. FONCTIONNALITÉS**
-------------------
- Lecture d'un fichier CSV d'entrée
- Nettoyage des données selon les critères spécifiés :
  * Suppression des doublons
  * Suppression des entrées vides
  * Filtrage par extension (.txt et .csv par défaut)
- Affichage des statistiques de nettoyage
- Écriture des résultats dans un fichier CSV de sortie
- Gestion des erreurs (fichier introuvable, etc.)

**3. STRUCTURE DES FICHIERS**
-------------------------

**Fichier d'entrée (fichiers_bruts.csv) :**
```
log.txt
""
log.txt
data.csv
temp.tmp
notes.txt
data.csv
report.pdf
```


**Fichier de sortie (fichiers_nettoyes.csv) :**
```
Nom du fichier
log.txt
data.csv
notes.txt
```


**4. PRÉREQUIS**
------------
- Python 3.x
- Un fichier CSV d'entrée nommé 'fichiers_bruts.csv' dans le même répertoire

**5. INSTALLATION ET UTILISATION**
-------------------------------
**Etape 1.** 
- Créez un fichier 'fichiers_bruts.csv' avec vos données (un nom de fichier par ligne)

**Etape 2.**  
- Placez-le dans le même répertoire que le script

**Etape 3.**  
-Exécutez le script :
   python nettoyage_csv.py

**Etape 4.**  
- Les résultats seront :
   - Affichés à l'écran
   - Enregistrés dans 'fichiers_nettoyes.csv'

**6. PERSONNALISATION**
-------------------
Vous pouvez modifier ces paramètres dans le code :
- EXTENSIONS_VALIDES : Ensemble des extensions valides (par défaut {'.txt', '.csv'})
- fichier_entree : Chemin vers le fichier d'entrée (par défaut "fichiers_bruts.csv")
- fichier_sortie : Chemin vers le fichier de sortie (par défaut "fichiers_nettoyes.csv")

**7. EXEMPLE D'EXÉCUTION**
----------------------
```
=== NETTOYAGE DE FICHIER CSV ===

Lecture du fichier fichiers_bruts.csv...
Nettoyage des données...

=== RÉSULTATS DU NETTOYAGE ===
Fichiers originaux: 8
Fichiers après nettoyage: 3
Fichiers supprimés: 5

Liste des fichiers conservés:
1. log.txt
2. data.csv
3. notes.txt

Écriture du fichier nettoyé fichiers_nettoyes.csv...
Nettoyage terminé avec succès!
```

**8. STRUCTURE DU FICHIER CSV D'ENTRÉE**
-----------------------------------
Le fichier d'entrée doit contenir une colonne avec les noms de fichiers.
Exemple minimal :
```
log.txt
data.csv
temp.tmp
```

**9. NOTES IMPORTANTES**
--------------------
- Le script suppose que les noms de fichiers sont dans la première colonne du CSV
- Les entrées vides (lignes vides ou cellules vides) sont automatiquement ignorées
- Les doublons sont détectés et supprimés (seule la première occurrence est conservée)
- Le script crée automatiquement le dossier de sortie s'il n'existe pas
- Les extensions valides par défaut sont .txt et .csv (modifiables dans le code)