# Système de Gestion de Transactions Financières

Ce script Python permet de gérer des transactions financières (revenus et dépenses), de calculer le solde actuel, et d'afficher des rapports mensuels. Les transactions sont sauvegardées dans un fichier texte pour persister entre les exécutions du programme.

## Fonctionnalités

- **Ajouter une transaction** : Ajoute une nouvelle transaction (revenu ou dépense) avec une description, un montant et une date.
- **Afficher toutes les transactions** : Affiche toutes les transactions enregistrées.
- **Calculer le solde actuel** : Calcule et affiche le solde actuel en fonction des transactions.
- **Afficher un rapport mensuel** : Génère un rapport pour un mois et une année spécifiques, affichant les revenus, les dépenses et le solde pour cette période.
- **Sauvegarder les données** : Sauvegarde les transactions dans un fichier CSV pour une utilisation ultérieure.

## Structure des Données

Les transactions sont sauvegardées dans un fichierCSV : 
- `15_TP_Gestion_Budget/data/data_transaction.csv`

Avec le format suivant : 
- ID[Id_1234]--Type[Revenu]--Montant[100]--Description[Salaire]--Date[2025-10-01]


## Utilisation

1. **Exécuter le script** : Lancez le script dans un environnement Python.
2. **Choisir une action** : Une fois le script lancé, vous pouvez choisir parmi les actions suivantes :
   - Tapez `1` pour entrer une nouvelle transaction.
   - Tapez `2` pour afficher toutes les transactions.
   - Tapez `3` pour afficher le solde actuel.
   - Tapez `4` pour afficher un rapport mensuel.
   - Tapez `5` pour quitter le programme.

## Exemples

### Ajouter une transaction

```
*********************
Pour Entrer une nouvelle Transaction Tappez 1 - De Type Revenu ou Depense
Pour Afficher toutes les Transactions. Tappez 2
Pour Afficher votre Solde Actuelle Tapper 3.
Pour Afficher un rapport spécifique, par Mois, Année tappez 4.

Pour Quitter tappez 5.

Veuillez Entrer votre action ici --> 1

----------
Vous allez rentrer une nouvelle transaction.
-------
Les Types établis sont :
Revenu - Tappez 1
Depense - Tappez 2

De Quel Type est la Transaction ? Tappez Ici => 1
Vous avez choisi : Revenu
Veuillez Entrez le Montant ici --> 1000
Merci, vous avez entré 1000 €
Veuillez Entrez une Descriptions Breves
Entrez Ici --> Salaire Octobre
Merci.
Veuillez Entrez une Date Valide YEAR puis Month et Day
Entez l'année --> 2025
Entez le Mois --> 10
Entez le Jours --> 15
Merci, vous avez entré 2025-10-15
-----------
Voici un Récapitulatif que vous avez entré :
Type : Revenu
Montant : 1000 €
Description : Salaire Octobre
Date : 2025-10-15
-----------
```

### Afficher le solde actuel
```
*********************
Pour Entrer une nouvelle Transaction Tappez 1 - De Type Revenu ou Depense
Pour Afficher toutes les Transactions. Tappez 2
Pour Afficher votre Solde Actuelle Tapper 3.
Pour Afficher un rapport spécifique, par Mois, Année tappez 4.

Pour Quitter tappez 5.

Veuillez Entrer votre action ici --> 3

Après étude de nos données, nous avons établi que la nouvelle solde est de maintenant 6000 €,
avec une solde de départ de 5000 €
```

### Afficher un rapport mensuel
```
*********************
Pour Entrer une nouvelle Transaction Tappez 1 - De Type Revenu ou Depense
Pour Afficher toutes les Transactions. Tappez 2
Pour Afficher votre Solde Actuelle Tapper 3.
Pour Afficher un rapport spécifique, par Mois, Année tappez 4.

Pour Quitter tappez 5.

Veuillez Entrer votre action ici --> 4

-------
Veuillez Entrez l'année --> 2025
Veuillez Entrez le Mois --> 10
Vous avez choisi : 2025-10
********
Rapport Mensuel pour la date du : 2025-10

Etude des Données :
Solde Total des Revenues : 1000 €
Solde Total des Depenses : 200 €

Le Total des Transactions est de : 800 €

------
Votre Solde de Départ était de : 5000 €

La nouvelle Solde sera de : 5800 €  avec une différence de 800 €
----------

```
