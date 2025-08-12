## == DATA ==
data_bibliotheque = {}

## == FONCTIONS ==
def ajouter_livre():
    recup_nom = input("Quel est le nom du livre ? --> ")
    print("D'accord, répondez à quelques questions pour finaliser votre ajout.")
    recup_auteur = input("\nQuel est l'auteur du livre ? --> ")
    recup_date = input("Quelle est l'année de publication du livre ? --> ")
    recup_dispo = int(input("\nL'empruntez-vous directement ? \nPour oui, tapez 1 \nPour non, tapez 2 \nTapez ici --> "))
    if recup_dispo == 1:
        recup_dispo = True
    elif recup_dispo == 2:
        recup_dispo = False
    else:
        print("Choix invalide, le livre sera marqué comme disponible.")
        recup_dispo = True

    print("\nD'accord, merci pour votre ajout.")
    new_name = {
        "titre": recup_nom,
        "auteur": recup_auteur,
        "annee publication": recup_date,
        "Disponibilité": recup_dispo
    }
    return new_name, recup_nom

def del_livre(data):
    recup_livre = input("\nQuel livre voulez-vous supprimer ? \nTapez ici --> ")
    if recup_livre in data:
        del data[recup_livre]
        print(f"Le livre '{recup_livre}' a bien été supprimé.")
    else:
        print(f"Le livre '{recup_livre}' n'est pas encore dans notre bibliothèque.")
    return data

def afficher_bibliotheque(data):
    print("\nVoici notre bibliothèque de livres : ")
    for livre in data:
        recup_data_titre = data[livre]["titre"]
        recup_data_dispo = data[livre]["Disponibilité"]
        if recup_data_dispo:
            print(f"\nNous avons le livre '{recup_data_titre}' qui est actuellement disponible !")
        else:
            print(f"\nNous avons le livre '{recup_data_titre}' qui n'est malheureusement plus disponible !")

def emprunter_livre(data):
    recup_livre = input("\nQuel livre voulez-vous emprunter ? \nTapez ici --> ")
    if recup_livre in data:
        etat_livre = data[recup_livre]["Disponibilité"]
        if etat_livre:
            choix = int(input(f"Oui, il est bien disponible. Confirmez votre choix ? Tapez 1 --> "))
            if choix == 1:
                data[recup_livre]["Disponibilité"] = False
                print("Le livre est maintenant à vous. Bonne lecture !")
            else:
                print("Veuillez réessayer.")
        else:
            print("Le livre est déjà emprunté, désolé !")
    else:
        print("Désolé, nous n'avons malheureusement pas trouvé le livre en question.")
    return data

def rendre_livre(data):
    recup_livre = input("\nQuel livre voulez-vous rendre ? \nTapez ici --> ")
    if recup_livre in data:
        etat_livre = data[recup_livre]["Disponibilité"]
        if not etat_livre:
            data[recup_livre]["Disponibilité"] = True
            print("Merci beaucoup, votre retour a bien été enregistré.")
        else:
            print("Ce livre est déjà disponible, merci de vérifier.")
    else:
        print("Désolé, nous n'avons malheureusement pas trouvé le livre en question.")
    return data

## == ACTIONS PROGRAMME ==
action_0 = "\nPour afficher la bibliothèque, tapez 0"
action_1 = "\nPour ajouter un nouveau livre, tapez 1"
action_2 = "\nPour supprimer un livre existant, tapez 2"
action_3 = "\nPour emprunter un livre, tapez 3"
action_4 = "\nPour rendre un livre, tapez 4"
action_5 = "\nPour quitter le programme, tapez 5"
action_6 = "\nTapez ici ---> "

## == PROGRAMME ==
def programme_bibliotheque(data):
    print("Bonjour, bienvenue sur notre plateforme de livres !")
    new_data = data
    while True:
        try:
            recup_user = int(input(f"\nQue voulez-vous faire ? \n{action_0}{action_1}{action_2}{action_3}{action_4}{action_5}{action_6}"))
            if recup_user == 0:
                afficher_bibliotheque(new_data)
            elif recup_user == 1:
                new_name, recup_nom = ajouter_livre()
                new_data[recup_nom] = new_name
            elif recup_user == 2:
                new_data = del_livre(new_data)
            elif recup_user == 3:
                new_data = emprunter_livre(new_data)
            elif recup_user == 4:
                new_data = rendre_livre(new_data)
            elif recup_user == 5:
                print("À bientôt !")
                break
            else:
                print("Veuillez entrer un nombre entre 0 et 5.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")
    return new_data

## == START ==
data_bibliotheque = programme_bibliotheque(data_bibliotheque)
