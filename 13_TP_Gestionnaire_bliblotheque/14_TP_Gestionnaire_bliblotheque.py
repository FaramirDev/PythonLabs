## == DATA == ## 
data_blibliotheque = {

}

## == FONCTION == ## 
def ajouter_livre():
    recup_nom = input("Quel est le nom du Livre ? -->")
    print("Daccord, repondz a quelques questions pour finaliser votre ajouts")
    recup_auteur = input("\n Quel est l'auteur du Libre ? -->")
    recup_date = input("Quelle est l'année de publication du Libre ? -->")
    recup_dispo = int(input("\nL'emprunté vous directement ? \n Pour oui Tapez 1 \n Pour non taper 2 \n Tapez ici -->"))
    if recup_dispo == 1:
        recup_dispo = True
    elif recup_dispo == 2:
        recup_dispo = False

    print("\n Daccord, merci pour votre ajouts")

    new_name = "data_" + recup_nom

    new_name = {
        "titre" : recup_nom,
        "auteur" : recup_auteur,
        "annee publication" : recup_date,
        "Disponibilité" : recup_dispo

    }

    return new_name, recup_nom

def del_livre(data):
    recup_livre = input("\nQuel livre voulez-vous supprimé ? \nTapez ici -->")
    if recup_livre in data:
        del data[recup_livre]
        print(f"Le Livre {recup_livre} à bien été supprimé")
    else: 
        print(f"Le livre {recup_livre} n'est pas encore dans notre bibliothèque.")
    return data

def afficher_bliblio(data,titre, dispo):
    print("\nVoici notre Blibliothèque de Livre : ")
    for livre in data:
        recup_data_titre = data[livre][titre]
        recup_data_dispo = data[livre][dispo]
        if recup_data_dispo == True:
            print(f"\nNous avons le Livre {recup_data_titre} qui est acutellement Disponible !")
        else:
            print(f"\nNous avons le Livre {recup_data_titre} qui n'est malheureusement plus Disponible !")
  
def enprunter_livre(data):
    recup_livre = input("\n Quel Livre voulez-vous emprunter ? \n Tapez ici -->")
    etat_livre = data[recup_livre]["Disponibilité"]
    if recup_livre in data:
        if etat_livre == True:
            choix = int(input(f"Oui il est bien disponible ? Confirmé votre Choix ? Taper 1"))
            if choix == 1:
                etat_livre = False
                print("Le Libre est maintenant à vous. Bonne Lecture")
            else: 
             print("Veuillez Ressayer")
        else:
            print("Le Livre est deja emprunté, désolé !")
    else:
        print("Désolé nous n'avons malheureusement pas trouvé le livre en question.")

    return recup_livre, etat_livre

def rendre_livre(data):
    recup_livre = input("\n Quel Livre voulez-vous rendre ? \n Tapez ici -->")
    etat_livre = data[recup_livre]["Disponibilité"]
    if recup_livre in data:
        if etat_livre == False:
            print("Merci beaucoup, votre retour à bien été enregistré.") 
            etat_livre = True   
        else:
            print("Nous ne pouvons pas donner suite désolé")
    else:
        print("Désolé nous n'avons malheureusement pas trouvé le livre en question.")
    
    return recup_livre, etat_livre
            
## == ACTION PROGRAMME == ## 
action_0 = "\n Pour Afficher la Bibliothèque. Tapez 0"
action_1 = "\n Pour Ajouter un nouveau Livre. Tapez 1"
action_2 = "\n Pour Supprimer un livre existant. TAPEZ 2"
action_3 =  "\n Pour Emprunté un livre. TAPEZ 3"
action_4 =  "\n Pour Rendre un livre. TAPEZ 4"
action_5 = "\n Pour Qutter le Programme. Tappez 5"
action_6 = "\n \n Tappez ICI ---->"

## == PROGRAMME == ## 
def programme_bliblio(data):
    print("Bonjour, Bienvenue sur Notre Plateforme de Livre !")
    new_data = data

    while True:
        try:
            recup_user = int(input(f"\nQue Voulez-vous faire ? \n {action_0} {action_1}{action_2}{action_3}{action_4}{action_5}{action_6}"))

            if recup_user == 1:
                new_name, recup_nom = ajouter_livre()
                new_data[recup_nom] = new_name

            elif recup_user == 2:
                new_data = del_livre(new_data)

            elif recup_user == 0:
                titre = "titre"
                dispo = "Disponibilité"
                afficher_bliblio(new_data,titre, dispo)

            elif recup_user == 3:
                recup_livre, etat_livre = enprunter_livre(new_data)
                dispo = "Disponibilité"
                new_data[recup_livre][dispo] = etat_livre
            
            elif recup_user == 4:
                recup_livre, etat_livre = rendre_livre(new_data)
                dispo = "Disponibilité"
                new_data[recup_livre][dispo] = etat_livre

            elif recup_user == 5:
                print("A bientot !")
                break
 

        except ValueError:
            print("Veuillez Entrer un Nombre valide.")

    return new_data

## == START == ## 
data_blibliotheque = programme_bliblio(data_blibliotheque)







