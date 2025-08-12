===========================================
## ANALYSE DES LOGS D'UTILISATEURS (CSV) 
===========================================

### 1. DESCRIPTION
--------------
Ce script Python analyse les logs de connexions utilisateurs stockés dans un fichier CSV.
Il permet de :
- Compter le nombre total d'accès par utilisateur
- Identifier les utilisateurs les plus actifs (plus de 3 accès par défaut)
- Afficher les résultats sous forme de tableau
- Sauvegarder les résultats dans un fichier CSV

## 2. FONCTIONNALITÉS
-------------------
- Lecture des logs depuis un fichier CSV structuré
- Comptage automatique des accès par utilisateur
- Filtrage des utilisateurs actifs selon un seuil configurable
- Affichage clair des résultats dans la console (format tableau)
- Sauvegarde des résultats dans un fichier CSV avec timestamp
- Gestion des erreurs (fichier introuvable, format invalide)

## 3. STRUCTURE DES DONNÉES
------------------------
**Fichier d'entrée (user_logs.csv) :**
```
utilisateur
alice
faramir
bob
faramir
alice
charlie
bob
faramir
bob
david
bob
farmair
dabid
alice
faramir
alice
faramir

```

------------------------
**Terminal :**
```
--- Tous les utilisateurs ---
Utilisateur     | Accès 
-------------------------
faramir         | 5     
alice           | 4     
bob             | 4     
charlie         | 1     
david           | 1     
farmair         | 1     
dabid           | 1     

--- Utilisateurs actifs (plus de 3 accès) ---
Utilisateur     | Accès 
-------------------------
faramir         | 5     
alice           | 4     
bob             | 4  
```   


**Fichier de sortie (resultats_analyse_YYYYMMDD_HHMMSS.csv) :**
```

Statistiques d'accès aux logs

Tous les utilisateurs
Utilisateur,Nombre d'accès
faramir,5
alice,4
bob,4
charlie,1
david,1
farmair,1
dabid,1

Utilisateurs actifs (plus de 3 accès)
Utilisateur,Nombre d'accès
faramir,5
alice,4
bob,4
```

## 4. PRÉREQUIS
------------
- Python 3.x
- Un fichier CSV contenant les logs (voir structure ci-dessus)

## 5. INSTALLATION ET UTILISATION
-------------------------------
1. Créez un fichier 'user_logs.csv' avec vos données (un utilisateur par ligne)
2. Placez-le dans le même répertoire que le script
3. Exécutez le script : python analyse_logs_csv.py
4. Les résultats s'affichent à l'écran et sont sauvegardés dans un fichier CSV



## 6. EXEMPLE D'EXÉCUTION
```
----------------------
=== ANALYSE DES LOGS D'UTILISATEURS (CSV) ===

===== STATISTIQUES D'ACCÈS =====

--- Tous les utilisateurs ---
Utilisateur     | Accès
-------------------------
bob             | 4
alice           | 2
charlie         | 1
david           | 1

--- Utilisateurs actifs (plus de 3 accès) ---
Utilisateur     | Accès
-------------------------
bob             | 4

Les résultats ont été sauvegardés dans resultats_analyse_20231115_143022.csv
```

## 7. NOTES IMPORTANTES
--------------------
- Le script suppose que les noms d'utilisateurs sont dans la première colonne du CSV
- Pour de très grands jeux de données, envisagez d'utiliser pandas pour de meilleures performances
- Les fichiers de sortie sont automatiquement timestampés pour éviter les écrasements
- Le script crée automatiquement le fichier de sortie s'il n'existe pas
