# Système de Gestion de Stock

## Description

Cette application de gestion de stock développée en Python avec Tkinter permet de :
- Ajouter, modifier et supprimer des articles
- Visualiser l'état du stock avec coloration des dates périmées
- Rechercher des articles
- Charger et sauvegarder les données dans des fichiers CSV
- Gérer les informations des articles (nom, quantité, prix, date d'expiration)

## Fonctionnalités

### Gestion des articles
- **Ajout** : Ajouter de nouveaux articles avec validation des données
- **Modification** : Modifier les informations des articles existants
- **Suppression** : Supprimer des articles du stock
- **Recherche** : Rechercher des articles par nom ou prix

### Visualisation
- Affichage sous forme de tableau avec :
  - Colorisation des dates périmées (rouge) et valides (vert)
  - Tri et organisation claire des données
  - Affichage complet du stock

### Gestion des fichiers
- Chargement de données depuis un fichier CSV
- Sauvegarde des données dans un fichier CSV
- Possibilité d'enregistrer sous un nouveau nom

### Validation des données
- Vérification des formats de date (YYYY-MM-DD)
- Validation des quantités et prix (doivent être positifs)
- Vérification des doublons de noms d'articles

## Structure du code

### Variables globales
- `elements` : Liste contenant tous les articles
- `tree` : Composant Treeview pour l'affichage tabulaire
- `path_save_data` : Chemin vers le fichier de sauvegarde par défaut

### Fonctions principales

#### Gestion des données
- `charge_data(path)` : Charge les données depuis un fichier
- `save_data()` : Sauvegarde les données dans le fichier par défaut
- `save_as_data()` : Sauvegarde les données dans un nouveau fichier
- `clear_elements()` : Vide la liste des articles

#### Opérations CRUD
- `ajoute_article()` : Ajoute un nouvel article
- `supp_article()` : Supprime un article
- `modif_article()` : Modifie un article existant
- `rechercher()` : Recherche des articles

#### Affichage
- `affiche_all()` : Affiche tous les articles dans le tableau
- `affiche_entre_ajout()` : Affiche les champs pour ajouter un article
- `affiche_entre_sup()` : Affiche les champs pour supprimer un article
- `ouvrir_fenetre_ajout()` : Ouvre une fenêtre pour ajouter un article
- `ouvrir_fenetre_choix_modify()` : Ouvre une fenêtre pour modifier un article

#### Validation
- `validate_input(new_value)` : Valide les entrées numériques
- `validate_date(date)` : Valide le format des dates

#### Interface utilisateur
- Fenêtre principale avec boutons d'action
- Fenêtres secondaires pour l'ajout et la modification
- Système de notification des erreurs

## Interface Utilisateur

### Fenêtre principale
![Interface principale](16_APP_Systeme_Gestion_de_Stock/images/capture_start_programme.png)

1. **Barre de titre** : "Gestion de Stock"
2. **Boutons principaux** :
   - Ajouter un article
   - Supprimer un article
   - Modifier un article
   - Afficher le stock
   - Sauvegarder
3. **Zone d'affichage** : Tableau des articles avec coloration
4. **Barre de recherche** : Pour filtrer les articles
5. **Indicateurs** :
   - Fichier actuel
   - Statut de chargement
   - Chemin du fichier

![Interface principale](16_APP_Systeme_Gestion_de_Stock/images/capture_start_view_programme.png)


### Fenêtre d'ajout
![Fenêtre d'ajout](16_APP_Systeme_Gestion_de_Stock/images/capture_ajout_reussi.png)


1. Champs pour :
   - Nom de l'article
   - Quantité
   - Prix
   - Date d'expiration
2. Bouton de validation
3. Zone de notification des erreurs


### Fenêtre de modification
![Fenêtre de modification](16_APP_Systeme_Gestion_de_Stock/images/capture_modification.png)


1. Sélection des champs à modifier
2. Champs pour les nouvelles valeurs
3. Bouton de validation
4. Zone de notification des erreurs


## Installation et Exécution

### Prérequis
- Python 3.x
- Bibliothèques standard (tkinter, os, datetime)

### Exécution
1. Cloner le dépôt ou télécharger le script
2. Exécuter avec Python :
   ```bash
   python gestion_stock.py
