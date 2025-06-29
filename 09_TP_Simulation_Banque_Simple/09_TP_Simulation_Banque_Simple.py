#### Creation Simple d'un Systeme banquaire 
## == DATA == ##
Banque = { "bea" : 100,
          "Bertrand" : 100,
          }

## == FONCTION == ##
def nom():
    recup_nom = input("Tapez votre nom s'il vous plait ou 4 pour quitter \n Tappez Ici -->")
    return recup_nom

def print_solde(solde, nom):
    print(f"Votre Solde est actuellement de : {solde} € {nom}.")

def deposer_solde(solde):
    depot = float(input("Entrez le montant de votre dépot ici -->"))
    solde += depot
    print(f"Merci, la somme de {depot} € a bien été ajouté.")
    print(f"Votre Compte est maintenant de {solde} €")

    return solde

def retirer_solde(solde):
    somme = float(input("Entrez la somme que vous voulez Retirer ici -->"))
    if somme <= solde:
        solde -= somme
        print(f"Vous avez retiré {somme} €")
        print(f"Votre nouvelle solde sur votre compte est de {solde} €")
        return solde
    else:
        print("Vous n'avez pas assez !")

def quit_programme():
    print("Merci, a bientot")

## == ACTION == ## 
action_1 = "\n Pour Afficher Votre Solde. TAPEZ 1"
action_2 = "\n Pour Deposer de l'argent. TAPEZ 2"
action_3 =  "\n Pour Retirer. TAPEZ 3"
action_4 = "\n Pour Qutter le Programme. Tappez 4"
action_5 = "\n \n Tappez ICI ---->"

## == PROGRAMME BANQUE == ##
def banque_programme(Banque_data):
    recup_nom = nom()
    for user in Banque_data:
        if user == recup_nom:
            while True:
                try:
                    user_input = int(input(f"\n Identification Reussi ! \n Bonjour {recup_nom}, que voulez-vous faire ? \n {action_1} {action_2} {action_3} {action_4} {action_5} "))
                    new_solde = Banque_data[recup_nom] 
                    somme_work = new_solde

                    if user_input == 1:
                        print_solde(recup_nom, somme_work)
                         

                    elif user_input == 2:
                        somme_work = deposer_solde(somme_work) 
                        Banque_data[recup_nom]  = somme_work


                    elif user_input == 3:
                        somme_work = retirer_solde(somme_work)
                        Banque_data[recup_nom]  = somme_work

                    elif user_input == 4:
                        quit_programme()
                        break

                except ValueError:
                    print("Veuillez Entrer une Action Valide, de 1 à 4. ")
        else: 
            print(f"Nous n'avons pas trouvé de {recup_nom} dans notre Base de Données, Merci de réessayé.")

            
        return Banque_data

## == START == ##
Banque = banque_programme(Banque)


