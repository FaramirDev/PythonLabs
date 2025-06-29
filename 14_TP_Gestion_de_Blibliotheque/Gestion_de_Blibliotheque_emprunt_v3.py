import os, random as rd

## OBJECTIF : GESTION BIBLIO 

## == DATA == ## 
path_data_book = "D:/03_Script/02_projet_Training/Gestion_de_Blibliotheque/data/data_book.txt"
path_data_emprunt = "D:/03_Script/02_projet_Training/Gestion_de_Blibliotheque/data/data_emprunt.txt"

list_path = [path_data_book, path_data_emprunt]

## == FONCTION == ## 
## creation des data if no exist
def create_date_no(list_path):
    for path in list_path:
        if not os.path.exists(path):
            with open(path, 'w') as f:
                f.write()

### RECUP DATA Book & Emprunt 
def recup_book(path_book):
    list_book = []
    list_id_book = []

    with open(path_book, 'r') as f:
        list_book = f.readlines()
    
    all_book = {}

    for book in list_book:
        element = book.split(',')

        id_livre = int(element[0])
        titre = element[1]
        auteur = element[2]
        annee = element[3]
        disponibilite = element[4].strip()

        dico_book = {
            "titre" : titre,
            "auteur" : auteur,
            "annee" : annee,
            "disponibilite" : disponibilite,
            }
        
        all_book[id_livre] = dico_book

        list_id_book.append(id_livre)

    return all_book, list_id_book
    
def recup_data_emprunt(path_emprunt):
    list_data_emprunt = []
    list_id_emprunt = []

    dico_all_emprunt = {}

    with open(path_emprunt, 'r') as f:
        list_data_emprunt = f.readlines()

    for ligne in list_data_emprunt:
        ligne.strip()

    for emprunt in list_data_emprunt:
        element = emprunt.split(',')
       
        id_livre = element[0]
        id_emprunt = element[1]
        titre = element[2]
        lecteur = element[3]
        date_start = element[4]
        date_end = element[5]

        data_emprunt = {
            "id_livre" : id_livre,
            "titre" : titre,
            "lecteur" : lecteur,
            "date_emprunt" : date_start,
            "date_retour": date_end,
            }
        
        dico_all_emprunt[id_emprunt] = data_emprunt

        list_id_emprunt.append(id_emprunt)

    return dico_all_emprunt, list_id_emprunt

### SAVE DATA Book & Emprunt
def save_book(path_book, dico):
    with open(path_book, 'w') as f:
        for book in dico:
            recup_titre = dico[book]['titre']
            recup_auteur = dico[book]['auteur']
            recup_annee = dico[book]['annee']
            recup_dispo = dico[book]['disponibilite']

            data = f'{book},{recup_titre},{recup_auteur},{recup_annee},{recup_dispo}\n'
              
            f.write(data)

def save_emprunt(path_emprunt, dico):
    with open(path_emprunt, 'w') as f:
        for book in dico:
            recup_id = str(dico[book]['id_livre']).strip()
            recup_titre = dico[book]['titre'].strip()
            recup_lecteur = dico[book]['lecteur'].strip()
            recup_date_emprunt = dico[book]['date_emprunt'].strip()
            recup_date_retour = dico[book]['date_retour'].strip()

            data = f'{book},{recup_id},{recup_titre},{recup_lecteur},{recup_date_emprunt},{recup_date_retour}\n'
    
            f.write(data)

### AJOUT Book in Data
def ajout_book(data_book, list_id_book):
    print("\n---------------")
    print("Vous allez Enregistrer un nouveau Livre.\n")

    list_titre = []
    for book in data_book:
        list_titre.append(data_book[book]["titre"])

    a = True
    while a == True:
        choix_titre = str(input("Veuillez entrer le Titre du Libre -->")) 
        if choix_titre not in list_titre:
            a = False
        else: 
            print("Mince, le livre est deja enregistrer dans la Bibliothèque")
            a = True

    a = True
    while a == True:
        choix_auteur = str(input("Veuillez Entrer le Nom de l'auteur -->"))
        if type(choix_auteur) == str:
            a = False
        else:
            print("Veuillez Entrer une valeur Correct.")
            a = True

    a = True
    while a == True:
        choix_date = int(input("Veuillez Entrer la Date de Parrution -->"))
        if type(choix_date) == int and choix_date >= 500 and choix_date <= 3000:
            a = False
        else:
            print("Veuillez entrer une année.")
            a = True

    choix_statut = "Disponible"

    print("-------- RECAP DE L'AJOUT -------")
    print(f'Titre : {choix_titre}')
    print(f'Auteur : {choix_auteur}')
    print(f'Date : {choix_date}')
    print(f'Statut : {choix_statut}')

    set_id = list_id_book[-1]
    id_book = set_id + 1

    list_id_book.append(id_book)

    book = {
        "titre" : choix_titre,
        "auteur" : choix_auteur,
        "annee" : choix_date,
        "disponibilite" : choix_statut,
        }

    data_book[id_book] = book

    print("\nAjout Reussi avec Succes.")

    return data_book,list_id_book

### SUPP Book
def sup_book(data_book, list_id_book):
    key = "vasco"
    print("***")
    print("Vous allez supprimer un livre.")
    print("\nVeuillez entré le Mot de Passe d'Authentification :")
    
    choix_mdp = str(input("****Tappez ici -->"))
    if choix_mdp == key:
        print("Authentification Reussi.")
        choix_titre = str(input("Veuillez entré le Titre du Livre a Supprimé : -->"))
        
        for cle in list(data_book.keys()):
            if data_book[cle]['titre'] == choix_titre: 
                del data_book[cle]
                print(f'Le Livre {choix_titre} a bien été supprimé.')
            
    else: 
        print("Autentification Echec.")

    return data_book, list_id_book

### Afficher Book
def affiche_book(data_book):
    print("Voici la liste de Livre :")

    for data in data_book:
        recup_titre = data_book[data]['titre']
        recup_auteur = data_book[data]['auteur']
        recup_annee = data_book[data]['annee']
        recup_dispo = data_book[data]['disponibilite']

        print("\n------")
        print(f'Tire : {recup_titre}')
        print(f'Auteur : {recup_auteur}')
        print(f'Annee : {recup_annee}')
        print(f'Statut : {recup_dispo}')

### EMPRUNT BOOK
def select_date():
    a = True
    while a == True:
        choix_annee = int(input("Entré l'année -->"))

        if choix_annee >= 2022 and choix_annee <= 3000:
            a = False
        else: 
            a = True

    a = True
    while a == True:
        choix_month = int(input("Entré le Mois -->"))

        if choix_month >= 1 and choix_month <= 12:
            a = False
        else: 
            a = True

    a = True
    while a == True:
        choix_day = int(input("Entré le Jour -->"))

        if choix_day >= 1 and choix_day <= 31:
            a = False
        else: 
            a = True

    recup_date = f'{choix_annee}--{choix_month:02d}--{choix_day:02d}'

    return recup_date

## Check Date
def check_date(date_start,date_end):
    # motif XXXX--MM--DD
    start = date_start.split('--')  
    end= date_end.split('--')  

    calc_annee = int(end[0]) - int(start[0])
    calc_month = int(end[1]) - int(start[1])
    calc_day = int(end[2]) - int(start[2])

    if calc_annee == 0 and calc_month == 0 and calc_day > 0:
        check = True
    elif calc_annee == 0 and calc_month > 0: 
        check = True
    elif calc_month > 0:
        check = True

    else:
        check = False

    return check

def selection_date():
    a = True
    while a == True:
        recup_date = select_date()

        print(f'\nVous avez entré la Date : {recup_date}')
        print("--")
        print("1. Ok")
        print("2. No\n")

        choix_valide = int(input("Voulez-vous Confirmer votre Choix ?"))

        if choix_valide == 1:
            print("Date de Début Validé")
            a = False    
        else:
            a = True

    return recup_date

## Crea ID      
def creation_id():
    id_random = rd.randint(1000,9999)
    id = 'Id_' + str(id_random)

    return id

def init_id(list_avec_all_id):
    a = True
    
    while a == True:
        id = creation_id()

        if id not in list_avec_all_id:
            list_avec_all_id.append(id)
            a = False
        else:
            a = True

        return list_avec_all_id, id
    
def emprunt(data_book, list_id_emprunt, data_emprunt):
    list_titre = []
    for book in data_book:
        titre = data_book[book]["titre"]
        list_titre.append(titre)

    print("-------------")
    print("Service D'emprunt\n")

    choix_emprunt = str(input("Entré ici le Titre -->"))
   
    if choix_emprunt in list_titre:
        for book in data_book:
            recup_titre = data_book[book]["titre"]
            if choix_emprunt == recup_titre:
                recup_dispo = data_book[book]['disponibilite']
                if recup_dispo == "Disponible":
                    print("\n Livre selectionné est bien Disponible")

                    print("\n-------")
                    print("\n une date de début -->")

                    date_debut = selection_date()

                    print("\n-------")
                    print("\n une date de fin -->")

                    a = True
                    while a == True:
                        date_fin = selection_date()
            
                        check = check_date(date_debut,date_fin)
                        if check == True:
                            a = False
                        else:
                            print("\nLa Nouvelle Date n'est pas valide.")
                            a = True

                    print("\nPour finaliser votre commande\n")
                    choix_nom = str(input("Entrez un nom ici -->"))

                    print("\n***---   RECAP  ---***\n")
                    print(f'Livre Emprunté : {choix_emprunt}')
                    print(f'Date de Début : {date_debut}')
                    print(f'Date de Fin : {date_fin}')
                    print(f'Nom de Reservation : {choix_nom}')

                    ## Passage Indispo 
                    data_book[book]['disponibilite'] = "Indisponible"

                    print("\nMerci pour votre Emprunt, bonne lecture !")

                    ## SET UP DU DICO EMPRUNT
                    ##
                    id_book = book
                    list_id_emprunt, id = init_id(list_id_emprunt)

                    emprunt = {
                        "id_livre" : id_book,
                        "titre" : data_book[book]["titre"],
                        "lecteur" : choix_nom,
                        "date_emprunt" : date_debut,
                        "date_retour" : date_fin,
                    }

                    data_emprunt[id] = emprunt


                ##--
                elif recup_dispo == "Indisponible":
                    print("Mince le Livre est deja emprunté.")
                    pass
            ## -- 
            else:
                pass

    elif choix_emprunt not in list_titre:
        print("Nous n'avons pas trouvé le livre.")
    
    return data_book, list_id_emprunt, data_emprunt
    
def rendre_emprunt(data_book, list_id_emprunt, data_emprunt):
    print("----- Service Retour Livre Emprunté -----")

    choix_retour_titre = str(input("Entrez le Nom du Livre que vous avez Emprunté -->"))
    choix_nom_resa = str(input("Entrez le Nom de Reservation -->"))

    recup_key = []

    a = False

    for emprunt in data_emprunt:
        if choix_nom_resa == data_emprunt[emprunt]["lecteur"]  and choix_retour_titre == data_emprunt[emprunt]["titre"] :
            recup_key.append(emprunt)
            a = True

    a = False

    for cle in list(data_emprunt.keys()):
            if data_emprunt[cle]['titre'] == choix_retour_titre: 
                del data_emprunt[cle]
                print("Nous avons bien enregistré votre remise du Livre. Merci")
                a = True
                    
    if a == True:
        for book in data_book:
            if data_book[book]["titre"] == choix_retour_titre:
                data_book[book]["disponibilite"] = "Disponible"

    for data in data_emprunt:
        for key in data:
            key.strip()
    
    return data_book, list_id_emprunt, data_emprunt

def affiche_emprunt(data_emprunt):
    for emprunt in data_emprunt:
        recup_id = data_emprunt[emprunt]["id_livre"]
        recup_titre = data_emprunt[emprunt]["titre"]
        recup_lecteur = data_emprunt[emprunt]["lecteur"]
        recup_date_debut = data_emprunt[emprunt]["date_emprunt"]
        recup_date_fin = data_emprunt[emprunt]["date_retour"]

        print("\n----------\n")
        print(f"Emprunt ID : {emprunt}")
        print(f"ID Livre : {recup_id}")
        print(f"titre : {recup_titre}")
        print(f"Nom Reservation : {recup_lecteur}")
        print(f"Date Debut : {recup_date_debut}")
        print(f"Date Fin : {recup_date_fin}")


### == PROGRAMME == ## 
def big_programme(path_book, path_emprunt):

    print("**********************")
    print("Bonjour, vous entrez dans le Systeme de la Bibliotheque")

    create_date_no(list_path)
    ## Charge Data_book & Data Emprunt
    data_all_book, list_id_book = recup_book(path_book)
    all_data_emprunt, list_id_emprunt = recup_data_emprunt(path_emprunt)


    while True:
        try:
            print("\nSelectionné une action : ")
            print("1 - Ajouter un Livre")
            print("2 - Supprimer un Livre")
            print("3 - Emprunter un Livre")
            print("4 - Retourner un Livre")
            print("5 - Afficher tous les livres & Statut")
            print("6 - Afficher tous les Emprunts")

            print("\n7 - Quittez le Programme\n")
        
            a = True
            while a == True:
                choix_user = int(input("Entrez ici -->"))
                if choix_user >= 1 and choix_user <= 7:
                    a = False
                else:
                    print("Entrer une valeur valide.")
                    a = True
        
            if  choix_user == 1:
                data_all_book, list_id_book = ajout_book(data_all_book, list_id_book)
        
            elif choix_user == 2:
                data_all_book, list_id_book = sup_book(data_all_book, list_id_book)

            elif choix_user == 3:
                data_all_book, list_id_emprunt, all_data_emprunt = emprunt(data_all_book, list_id_emprunt, all_data_emprunt)

            elif choix_user == 4:
                data_all_book, list_id_emprunt, all_data_emprunt = rendre_emprunt(data_all_book, list_id_emprunt, all_data_emprunt)

            elif choix_user == 5:
                affiche_book(data_all_book)

            elif choix_user == 6:
                affiche_emprunt(all_data_emprunt)

            elif choix_user == 7:
                print("Merci, Au Revoir.")

                save_book(path_book, data_all_book)
                save_emprunt(path_emprunt, all_data_emprunt)

                break

        except ValueError:
            print("Nous avons rencontré une Error.")

## == START == ##        
big_programme(path_data_book, path_data_emprunt)
