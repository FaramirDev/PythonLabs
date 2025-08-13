# Mini ETL sans Pandas

Ce script Python est un exemple simple de processus ETL (Extract, Transform, Load) qui lit un fichier CSV brut, nettoie et filtre les données, puis sauvegarde les données nettoyées dans un nouveau fichier CSV.
Fonctionnalités

**Extraction** : 
- Lit les données depuis un fichier CSV brut.

**Transformation et Nettoyage :**
- Filtre les lignes qui ont exactement 5 colonnes non vides.
- Vérifie que la colonne d'âge est un entier valide.


**Chargement** : 
- Sauvegarde les données nettoyées dans un nouveau fichier CSV.

---

## Structure des Données

**Fichier d'entrée (data_employer_brut.csv)**
Le fichier d'entrée doit être un fichier CSV avec 5 colonnes. 
- Voici un exemple de format attendu :

```
id,nom,age,departement,poste
1,Jean Dupont,30,Informatique,Ingénieur
2,Marie Martin,25,Marketing,Analyste
3,Pierre Durand,,Informatique,Technicien
4,Lucie Bernard,35,Ressources Humaines,Manager
5,Paul Leroy,29,Finance,Comptable
6,Incomplete,Line,,,
7,Sophie Moreau,40,Informatique,Développeur
```

**Fichier de sortie (data_employer_clean.csv)**
Le fichier de sortie contiendra uniquement les lignes qui ont passé les critères de filtrage et de nettoyage. 
- Voici un exemple de ce que pourrait contenir le fichier de sortie :

```
id,nom,age,departement,poste
1,Jean Dupont,30,Informatique,Ingénieur
2,Marie Martin,25,Marketing,Analyste
4,Lucie Bernard,35,Ressources Humaines,Manager
5,Paul Leroy,29,Finance,Comptable
7,Sophie Moreau,40,Informatique,Développeur

```

## Utilisation

**Préparation des données :**
- Assurez-vous que le fichier data_employer_brut.csv est placé dans le dossier 01_TP_Data_MiniETL/data_IN/.


**Exécuter le script :** 
- Lancez le script dans un environnement Python.


**Résultat :**
- Le script va générer un fichier data_employer_clean.csv dans le dossier 01_TP_Data_MiniETL/data_Output/ contenant les données nettoyées.