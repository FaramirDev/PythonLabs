# Système de Gestion de Bibliothèque avec Emprunts

Ce script Python permet de gérer une bibliothèque en offrant des fonctionnalités pour ajouter, supprimer, emprunter et retourner des livres. Les livres et les emprunts sont stockés dans des fichiers texte pour une persistance des données.

## Fonctionnalités

- **Ajouter un livre** : Ajoute un nouveau livre à la bibliothèque avec des informations comme le titre, l'auteur, l'année de publication, et un statut de disponibilité.
- **Supprimer un livre** : Supprime un livre existant de la bibliothèque.
- **Emprunter un livre** : Change le statut d'un livre à "Indisponible" et enregistre un emprunt avec une date de début et une date de retour prévue.
- **Retourner un livre** : Change le statut d'un livre à "Disponible" et supprime l'enregistrement d'emprunt correspondant.
- **Afficher tous les livres** : Affiche tous les livres avec leur statut de disponibilité.
- **Afficher tous les emprunts** : Affiche tous les emprunts en cours.
- **Quitter le programme** : Sauvegarde les modifications et quitte le programme.

---

## Structure des Fichiers

**Lecture de Fichier et Ecriture**

- **livres.csv** : Stocke les informations sur les livres. Chaque ligne du fichier représente un livre avec le format suivant : `ID,Titre,Auteur,Année,Disponibilité`.
- **emprunts.csv** : Stocke les informations sur les emprunts. Chaque ligne du fichier représente un emprunt avec le format suivant : `ID_Emprunt,ID_Livre,Titre,Lecteur,Date_Emprunt,Date_Retour`.

## Utilisation

1. **Exécuter le script** : Lancez le script dans un environnement Python.
2. **Choisir une action** : Une fois le script lancé, vous pouvez choisir parmi les actions suivantes :
   - Tapez `1` pour ajouter un livre.
   - Tapez `2` pour supprimer un livre.
   - Tapez `3` pour emprunter un livre.
   - Tapez `4` pour retourner un livre.
   - Tapez `5` pour afficher tous les livres et leur statut.
   - Tapez `6` pour afficher tous les emprunts en cours.
   - Tapez `7` pour quitter le programme.

---
## Exemples

### Ajouter un livre

```
=== MENU PRINCIPAL ===
1. Ajouter un livre
2. Supprimer un livre
3. Emprunter un livre
4. Retourner un livre
5. Afficher tous les livres
6. Afficher les emprunts en cours
7. Quitter

Votre choix (1-7): 1

--- Ajout d'un nouveau livre ---
Titre du livre: Running
Auteur: Faramir
Année de publication: 2025

Livre ajouté avec succès (ID: 1)

```


### Afficher tous les Livres
```

=== MENU PRINCIPAL ===
1. Ajouter un livre
2. Supprimer un livre
3. Emprunter un livre
4. Retourner un livre
5. Afficher tous les livres
6. Afficher les emprunts en cours
7. Quitter

Votre choix (1-7): 5

--- Liste des livres ---

ID: 1
Titre: Running
Auteur: Faramir
Année: 2025
Statut: Disponible

ID: 2
Titre: Bien mangé
Auteur: Faram
Année: 2021
Statut: Disponible
```

### Emprunter un Livre
```
=== MENU PRINCIPAL ===
1. Ajouter un livre
2. Supprimer un livre
3. Emprunter un livre
4. Retourner un livre
5. Afficher tous les livres
6. Afficher les emprunts en cours
7. Quitter

Votre choix (1-7): 3

--- Emprunt d'un livre ---
Titre du livre à emprunter: Running
Nom de l'emprunteur: Alex

Sélectionnez la date de début (format: AAAA-MM-JJ)
Date (AAAA-MM-JJ): 2025-12-04

Sélectionnez la date de retour (format: AAAA-MM-JJ)
Date (AAAA-MM-JJ): 2026-02-18

Livre 'Running' emprunté avec succès par Alex (ID emprunt: E4878)
```

### Afficher tous les Emprunts en cours
```
=== MENU PRINCIPAL ===
1. Ajouter un livre
2. Supprimer un livre
3. Emprunter un livre
4. Retourner un livre
5. Afficher tous les livres
6. Afficher les emprunts en cours
7. Quitter

Votre choix (1-7): 6

--- Liste des emprunts ---

ID Emprunt: E4878
Livre: Running (ID: 1)
Emprunteur: Alex
Date emprunt: 2025-12-04
Date retour: 2026-02-18
```

### Retourne run Livre
```
=== MENU PRINCIPAL ===
1. Ajouter un livre
2. Supprimer un livre
3. Emprunter un livre
4. Retourner un livre
5. Afficher tous les livres
6. Afficher les emprunts en cours
7. Quitter

Votre choix (1-7): 4

--- Retour d'un livre ---
ID de l'emprunt: E4878
Livre 'Running' retourné avec succès.
```