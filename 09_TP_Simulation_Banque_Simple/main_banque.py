#### Création Simple d'un Système Bancaire

## == DATA ==
Banque = {
    "bea": 100,
    "Bertrand": 100,
}

## == FONCTIONS ==
def nom():
    recup_nom = input("Tapez votre nom s'il vous plaît ou 4 pour quitter \nTapez ici --> ")
    return recup_nom

def print_solde(nom, solde):
    print(f"Votre solde est actuellement de : {solde} €, {nom}.")

def deposer_solde(solde):
    depot = float(input("Entrez le montant de votre dépôt ici --> "))
    solde += depot
    print(f"Merci, la somme de {depot} € a bien été ajoutée.")
    print(f"Votre compte est maintenant de {solde} €")
    return solde

def retirer_solde(solde):
    somme = float(input("Entrez la somme que vous voulez retirer ici --> "))
    if somme <= solde:
        solde -= somme
        print(f"Vous avez retiré {somme} €")
        print(f"Votre nouveau solde sur votre compte est de {solde} €")
        return solde
    else:
        print("Vous n'avez pas assez d'argent sur votre compte !")
    return solde

def quit_programme():
    print("Merci, à bientôt")

## == ACTIONS ==
action_1 = "\nPour afficher votre solde, tapez 1"
action_2 = "\nPour déposer de l'argent, tapez 2"
action_3 = "\nPour retirer de l'argent, tapez 3"
action_4 = "\nPour quitter le programme, tapez 4"
action_5 = "\nTapez ici ----> "

## == PROGRAMME BANQUE ==
def banque_programme(Banque_data):
    while True:
        recup_nom = nom()
        if recup_nom == "4":
            quit_programme()
            break

        if recup_nom in Banque_data:
            while True:
                try:
                    user_input = int(input(f"\nIdentification réussie ! \nBonjour {recup_nom}, que voulez-vous faire ? \n{action_1}\n{action_2}\n{action_3}\n{action_4}\n{action_5}"))
                    somme_work = Banque_data[recup_nom]

                    if user_input == 1:
                        print_solde(recup_nom, somme_work)
                    elif user_input == 2:
                        somme_work = deposer_solde(somme_work)
                        Banque_data[recup_nom] = somme_work
                    elif user_input == 3:
                        somme_work = retirer_solde(somme_work)
                        Banque_data[recup_nom] = somme_work
                    elif user_input == 4:
                        quit_programme()
                        break
                    else:
                        print("Veuillez entrer une action valide, de 1 à 4.")
                except ValueError:
                    print("Veuillez entrer un nombre valide.")
        else:
            print(f"Nous n'avons pas trouvé {recup_nom} dans notre base de données. Merci de réessayer.")

    return Banque_data

## == START ==
Banque = banque_programme(Banque)
