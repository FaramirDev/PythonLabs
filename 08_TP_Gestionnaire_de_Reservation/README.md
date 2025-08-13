===========================================
GESTIONNAIRE DE RÉSERVATIONS
===========================================

## 1. DESCRIPTION
--------------
Ce programme est un gestionnaire de réservations de salles qui permet :
- Créer de nouvelles réservations avec validation des données
- Annuler des réservations existantes
- Afficher toutes les réservations en cours
- Rechercher des réservations spécifiques
- Sauvegarder les réservations dans un fichier CSV

## 2. FONCTIONNALITÉS
-------------------
- Saisie guidée des informations de réservation
- Validation des dates, heures et noms
- Gestion des salles disponibles (A, B, C, D)
- Affichage clair des réservations
- Recherche par nom de réservation
- Annulation de réservations
- Persistance des données dans un fichier CSV

## 3. STRUCTURE DES DONNÉES
-------------------------
Les réservations sont stockées dans un fichier CSV avec le format :
salle,date,heure,nom

**Exemple :**
Salle_A,2024-12-25,14:30,Faramir
Salle_B,2025-01-15,09:00,Alexis

## 4. INSTALLATION ET EXÉCUTION
-------------------------------
**Prérequis :**
- Python 3.6 ou supérieur
- Aucune bibliothèque externe requise

**Exécution :**
1. Enregistrez le script dans un fichier nommé gestion_reservations.py
2. Exécutez avec Python :
   python gestion_reservations.py
3. Le fichier de données sera créé automatiquement s'il n'existe pas

5. UTILISATION
--------------
Le programme propose un menu interactif avec 5 options :

**1. Nouvelle réservation :**
   - Sélection de la salle (A, B, C ou D)
   - Saisie de la date (année ≥ 2024, mois 1-12, jour valide)
   - Saisie de l'heure (6h-23h)
   - Saisie du nom du réservataire
   - Affichage d'un récapitulatif

**2. Annuler une réservation :**
   - Saisie du nom de la réservation à annuler
   - Confirmation de l'annulation

**3. Afficher toutes les réservations :**
   - Liste complète des réservations en cours
   - Format clair avec numérotation

**4. Rechercher une réservation :**
   - Recherche par nom (partiel ou complet)
   - Affichage des résultats correspondants

**5. Quitter :**
   - Sauvegarde des données
   - Fermeture du programme

## 6. VALIDATION DES DONNÉES
---------------------------
**Le programme valide systématiquement :**
- Les années (doivent être ≥ 2024)
- Les mois (1-12)
- Les jours (valides pour le mois donné)
- Les heures (6h-23h)
- Les minutes (0-59)
- Les noms (non vides)

## 7. EXEMPLE D'UTILISATION
```
-------------------------

=== Gestionnaire de Réservations ===
1. Nouvelle réservation
2. Annuler une réservation
3. Afficher toutes les réservations
4. Rechercher une réservation
5. Quitter

Entrez votre choix (1-5) : 1

-- Sélection de la salle --
Salle_A => Tapez 1
Salle_B => Tapez 2
Salle_C => Tapez 3
Salle_D => Tapez 4
Quelle salle souhaitez-vous réserver ? 2

-- Sélection de la date de réservation --
Entrez l'année (>= 2024) : 2025
Entrez le mois (1-12) : 6
Entrez le jour (1-31) : 15

-- Sélection de l'heure de réservation --
La tranche horaire disponible est de 6h à 23h
Sélectionnez l'heure (6-23) : 14
Sélectionnez les minutes (0-59) : 30

-- Nom de la réservation --
Entrez un nom pour confirmer la réservation : Réunion équipe

-- Récapitulatif de la réservation --
Salle : Salle_B
Date : 2025-06-15
Heure : 14:30
Nom : Réunion équipe
```

8. PERSONNALISATION
-------------------
Vous pouvez modifier ces paramètres dans le code :
- DATA_FILE : Chemin vers le fichier de sauvegarde
- SALLES_DISPONIBLES : Dictionnaire des salles disponibles
- HEURE_MIN/HEURE_MAX : Plage horaire disponible
- ANNEE_MIN : Année minimale autorisée

9. STRUCTURE DU CODE
----------------------
Le code est organisé en fonctions modulaires :
- initialiser_fichier() : Création du fichier de données
- valider_*() : Fonctions de validation
- saisir_*() : Fonctions de saisie utilisateur
- creer_reservation() : Création d'une nouvelle réservation
- charger/sauvegarder_reservations() : Gestion du fichier
- afficher/rechercher/annuler_reservation() : Opérations CRUD
- menu_principal() : Interface utilisateur
- main() : Fonction principale

10. GESTION DES ERREURS
-----------------------
Le programme gère les erreurs courantes :
- Saisies non numériques
- Dates/heures invalides
- Fichiers introuvables
- Noms vides
- Choix de menu invalides

11. LICENCE
-----------
Ce programme est sous licence MIT. 

