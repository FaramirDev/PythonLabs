# Gestionnaire de Bibliothèque

Ce script Python est un outil simple pour gérer une bibliothèque de livres. Il permet d'ajouter des livres, de supprimer des livres, d'emprunter et de rendre des livres, ainsi que d'afficher la liste complète des livres disponibles.

## Fonctionnalités

- **Ajouter un livre** : Ajoute un nouveau livre à la bibliothèque.
- **Supprimer un livre** : Supprime un livre existant de la bibliothèque.
- **Emprunter un livre** : Marque un livre comme emprunté.
- **Rendre un livre** : Marque un livre comme disponible après retour.
- **Afficher la bibliothèque** : Affiche la liste complète des livres avec leur statut de disponibilité.
- **Quitter le programme** : Permet de quitter le programme proprement.

## Utilisation

1. **Exécuter le script** : Lancez le script dans un environnement Python.
2. **Choisir une action** : Une fois le script lancé, vous pouvez choisir parmi les actions suivantes :
   - Tapez `0` pour afficher la bibliothèque.
   - Tapez `1` pour ajouter un nouveau livre.
   - Tapez `2` pour supprimer un livre existant.
   - Tapez `3` pour emprunter un livre.
   - Tapez `4` pour rendre un livre.
   - Tapez `5` pour quitter le programme.

## Exemples

### Ajouter un livre
```
Que voulez-vous faire ?
Pour afficher la bibliothèque, tapez 0
Pour ajouter un nouveau livre, tapez 1
Pour supprimer un livre existant, tapez 2
Pour emprunter un livre, tapez 3
Pour rendre un livre, tapez 4
Pour quitter le programme, tapez 5
Tapez ici ---> 1

Quel est le nom du livre ? --> Le Petit Prince
D'accord, répondez à quelques questions pour finaliser votre ajout.
Quel est l'auteur du livre ? --> Antoine de Saint-Exupéry
Quelle est l'année de publication du livre ? --> 1943
L'empruntez-vous directement ?
Pour oui, tapez 1
Pour non, tapez 2
Tapez ici --> 2

D'accord, merci pour votre ajout.
```

### Afficher la bibliothèque
```
Que voulez-vous faire ?
Pour afficher la bibliothèque, tapez 0
Pour ajouter un nouveau livre, tapez 1
Pour supprimer un livre existant, tapez 2
Pour emprunter un livre, tapez 3
Pour rendre un livre, tapez 4
Pour quitter le programme, tapez 5
Tapez ici ---> 0

Voici notre bibliothèque de livres :
Nous avons le livre 'Le Petit Prince' qui est actuellement disponible !
```

### Emprunter un livre
```
Que voulez-vous faire ?
Pour afficher la bibliothèque, tapez 0
Pour ajouter un nouveau livre, tapez 1
Pour supprimer un livre existant, tapez 2
Pour emprunter un livre, tapez 3
Pour rendre un livre, tapez 4
Pour quitter le programme, tapez 5
Tapez ici ---> 3

Quel livre voulez-vous emprunter ?
Tapez ici --> Le Petit Prince
Oui, il est bien disponible. Confirmez votre choix ? Tapez 1 --> 1

Le livre est maintenant à vous. Bonne lecture !
```

### Rendre un livre
```
Que voulez-vous faire ?
Pour afficher la bibliothèque, tapez 0
Pour ajouter un nouveau livre, tapez 1
Pour supprimer un livre existant, tapez 2
Pour emprunter un livre, tapez 3
Pour rendre un livre, tapez 4
Pour quitter le programme, tapez 5
Tapez ici ---> 4

Quel livre voulez-vous rendre ?
Tapez ici --> Le Petit Prince

Merci beaucoup, votre retour a bien été enregistré.
