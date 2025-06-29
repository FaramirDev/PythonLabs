## Objectif Clean list 
## Clean doublons, Vide, Extension Incrorrect ici - Garder que les .tkt et .csv

fichiers = ["log.txt", "", "log.txt", "data.csv", "temp.tmp", "notes.txt"]

fichiers_clean = []

for data in fichiers:
    if data not in fichiers_clean and data != "": 
        if ".txt" in data or ".csv" in data:
            fichiers_clean.append(data)

##AFFICHAGE FICHIER CLEAN 
print(fichiers_clean)

