import os, random as rd, re


###### SET UP LIST DATA
list_id = []
data_all_transaction = {}
data_compte = {
    "solde_compte_depart" : 5000,
}

####### Regroupe ALL data
##########################
all_data = {
    "list_id" : list_id,
    "data_transaction" : data_all_transaction,
    "data_compte" : data_compte
}

### Fonction Crea Transac 
#########################
def creation_id():
    id_random = rd.randint(1000,9999)
    id = 'Id_' + str(id_random)

    return id

def init_id(list_avec_all_data):
    a = True
    
    while a == True:
        id = creation_id()

        if id not in list_avec_all_data:
            list_avec_all_data.append(id)
            a = False
        else:
            a = True

        return list_avec_all_data, id

def choix_type():
    data_type = ["Revenu - Tappez 1", "Depense - Tappez 2"]
    print("-------")
    print("Les Types établis sont : ")
    for data in data_type:
        print(data)
    
    
    a = True
    while a == True:
        choix_type = int(input("\nDe Quel Type est la Transaction ? Tappez Ici =>"))
        if choix_type == 1:
            rec_type = "Revenu"
            print(f"Vous avez choisi : {rec_type}")
            a = False
        elif choix_type == 2:
            rec_type = "Depense"
            print(f"Vous avez choisi : {rec_type}")
            a = False

        else:
            print("Veuillez entrer un Type Etabli.")
            a = True

        return rec_type

def choix_montant():
    montant = int(input("Veuillez Entrez le Montant ici --> "))
    print(f"Merci, vous avez entré {montant} €")

    return montant

def enter_description():
    print("Veuillez Entrez une Descriptions Breves")
    description = input("Entrez Ici -->")
    print("Merci.")

    return description

def entrer_date():
    print("Veuillez Entrez une Date Valide YEAR puis Month et Day")
    
    a = False
    while a == False:
        year = int(input("Entez l'année -->"))
        if year >= 2020 and year <= 9999: 
            a = True
        else:
            a = False

    a = False
    while a == False:
        month = int(input("Entez le Mois -->"))
        if month >= 1 and month <= 12: 
            a = True
        else:
            a = False
            
    a = False
    while a == False:
        day = int(input("Entez le Jours -->"))
        if day >= 1 and day <= 31: 
            a = True
        else:
            a = False
        
    date = f"{year}-{month:02d}-{day:02d}"
    print(f"Merci, vous avez entré {date}")

    return date

#### Programe Creation Transaction ##
############################
def creation_transaction(data):
    print("----------")
    print("Vous allez rentrer une nouvelle transaction.")

    select_type = choix_type()
    select_montant = choix_montant()
    select_descrip = enter_description()
    select_date = entrer_date()

    recup_list_id = data["list_id"]
    recup_list_id, recup_id = init_id(recup_list_id)

    recup_all_data_transaction = data["data_transaction"]

    new_transaction = {
        "type" : select_type,
        "montant" : select_montant,
        "description" : select_descrip,
        "date" : select_date,
    }

    recup_all_data_transaction[recup_id] = new_transaction
    print("-----------")
    print("Voici un Récapitulatif que vous avez entré :")
    print(f"Type : {select_type}")
    print(f"Montant : {select_montant} €")
    print(f"Description : {select_descrip}")
    print(f"Date : {select_date}")
    print("-----------")

    return data

#### SET UP & Charge and SAVE DATA ####
#### ============================= ####
data_path_transaction = "D:/03_Script/02_projet_Training/Gestion_Budget/data/data_transaction.txt"
## si not create
if not os.path.exists(data_path_transaction) :
    with open(data_path_transaction, 'w') as f:
        f.write('')  

## Save Data in doc
def save_data_transac(data):
    recup_transaction = data["data_transaction"]
    
    list_data_transac = []

    for transaction in recup_transaction:
        recup_type = recup_transaction[transaction]["type"]
        recup_montant = recup_transaction[transaction]["montant"]
        recup_description = recup_transaction[transaction]["description"]
        recup_date= recup_transaction[transaction]["date"]
        save_data = f"ID[{transaction}]--Type[{recup_type}]--Montant[{recup_montant}]--Description[{recup_description}]--Date[{recup_date}]\n"
        list_data_transac.append(save_data)

 
    with open(data_path_transaction, 'w') as f:
        for transaction in list_data_transac:
            f.write(f"{transaction}")
    
## Charge Data doc
def charge_data():
    list_id = []
    data_all_transaction = {}
    data_compte = {
        "solde_compte_depart" : 5000,
    }

    all_data = {
        "list_id" : list_id,
        "data_transaction" : data_all_transaction,
        "data_compte" : data_compte,
        }
    

    list_data_recup = []
    with open(data_path_transaction, 'r') as f:
        data_recup = f.readlines()

    if data_recup:
        for data in data_recup:
            list_data_recup.append(data)

    
    ## Search Expression reguliere
    

    for transa in list_data_recup:
        recup_id = re.search(r'ID\[([^\]]+)\]', transa)
        recup_type = re.search(r'Type\[([^\]]+)\]', transa)
        recup_montant = re.search(r'Montant\[([^\]]+)\]', transa)
        recup_description = re.search(r'Description\[([^\]]+)\]', transa)
        recup_date = re.search(r'Date\[([^\]]+)\]', transa)

        if recup_id and recup_type and recup_montant and recup_date:
            id = recup_id.group(1)
            type = recup_type.group(1)
            montant = recup_montant.group(1)
            description = recup_description.group(1)
            date = recup_date.group(1).strip()

            transaction = {
                "type" : type,
                "montant" : int(montant),
                "description" : description,
                "date" : date,
            }

            data_all_transaction[id] = transaction
            list_id.append(id)

        else:
            print("Nous n'avons rien chargé")
        
    return all_data

# ====================
### Calcul de Solde ###
def calcul_solde(data):
    recup_data_solde = data["data_compte"]["solde_compte_depart"]
    recup_data_transaction = data["data_transaction"]
    new_solde = recup_data_solde

    for transaction in recup_data_transaction :
        if recup_data_transaction[transaction]["type"] == "Revenu" :
            new_solde = new_solde + recup_data_transaction[transaction]["montant"]
        elif recup_data_transaction[transaction]["type"] == "Depense" :
            new_solde = new_solde - recup_data_transaction[transaction]["montant"]

    print(f"\nAprès étude de nos donnés, nous avons établis que la nouvelle solde est de maintenant {new_solde} €,\navec une solde de départ de {recup_data_solde} €\n")

def afficher_all_transaction(data):
    print("Voici toute votre Transaction Enregistrer :\n")
    recup_transaction = data["data_transaction"]

    recup_type = "type"
    recup_montant = "montant"
    recup_description = "description"
    recup_date = "date"

    for transaction in recup_transaction:
        print("----------------")
        print(f"Id de Transaction : {transaction}")
        print(f"Les Type de la Transaction est : {recup_transaction[transaction][recup_type]}")
        print(f"Le Montant de la Transaction est de : {recup_transaction[transaction][recup_montant]} €")
        print(f"La Descriptions enregistré est :   {recup_transaction[transaction][recup_description]}")
        print(f"La Transaction est enregistré sur la date de : {recup_transaction[transaction][recup_date]}\n")

    print("Merci")
    
def afficher_transaction_date(data):
    recup_transaction = data["data_transaction"]
    recup_data_solde = data["data_compte"]["solde_compte_depart"]
    calcul_solde = recup_data_solde
    calcul_solde_revenu = 0
    calcul_solde_depense = 0
    
    

    print("-------")
    choix_year = int(input("Veuillez Entrez l'année -->"))
    choix_mont = int(input("Veuillez Entrez le Mois -->"))
    search_data = f"{choix_year}-{choix_mont:02d}"
    print(f"Vous avez choisi : {search_data}")

    ## SET UP List for calcul
    for transaction in recup_transaction:
        if search_data in recup_transaction[transaction]["date"] and recup_transaction[transaction]["type"] == "Revenu":
            calcul_solde = calcul_solde + recup_transaction[transaction]["montant"]
            calcul_solde_revenu = calcul_solde_revenu + recup_transaction[transaction]["montant"]

        elif search_data in recup_transaction[transaction]["date"] and recup_transaction[transaction]["type"] == "Depense":
            calcul_solde = calcul_solde - recup_transaction[transaction]["montant"]
            calcul_solde_depense = calcul_solde_depense + recup_transaction[transaction]["montant"]

    
    calcul_solde_trans = calcul_solde_revenu - calcul_solde_depense
    calcul_dif_solde =  calcul_solde - recup_data_solde 

    print("********")
    print(f"Rapport Mensuel pour la date du : {search_data}")
    print("\n")
    print("Etude des Données :") 
    print(f"Solde Total des Revenues : {calcul_solde_revenu} €")
    print(f"Solde Total des Depenses : {calcul_solde_depense} €")
    print(f"\nLe Total des Transactions est de : {calcul_solde_trans} €")
    print("\n------")
    print(f"Votre Solde de Départ était de : {recup_data_solde} €")
    print(f"\nLa nouvelle Solde sera de : {calcul_solde} €  avec une différence de {calcul_dif_solde} €")
    print("----------\n")

  
## == Big Programme == ###
##########################
def big_programme():
    print("Bonjour, Bienvenu sur la plateforme de votre Wallet\n")

    data = charge_data()

    while True:
        try:
            print("*********************")
            print("Pour Entrer une nouvelle Transaction Tappez 1 - De Type Revenu ou Depense")
            print("Pour Afficher toutes les Transactions. Tappez 2")
            print("Pour Afficher votre Solde Actuelle Tapper 3.")
            print("Pour Afficher un rapport spécifique, par Mois, Année tappez 4.\n")
            print("Pour Quittez tappez 5.\n")

            choix_user = int(input("Veuillez Entrer votre action ici -->"))

            if choix_user == 1:
                data = creation_transaction(data)

            elif choix_user == 2:
                afficher_all_transaction(data)

            elif choix_user == 3:
                calcul_solde(data)

            elif choix_user == 4:
                afficher_transaction_date(data)

            elif choix_user == 5:
                print("Merci, Aurevoir")
                save_data_transac(data)
                break


        except ValueError:
            print("Veuillez entrer une action Valide")
        
            

big_programme()