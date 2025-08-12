import os
import random as rd
import re

# == OBJECTIF : GESTION DE TRANSACTIONS FINANCIÈRES ==

# == CHEMINS DES FICHIERS ==
DATA_DIR = "15_TP_Gestion_Budget/data"
TRANSACTIONS_FILE = os.path.join(DATA_DIR, "data_transaction.csv")

# == FONCTIONS D'INITIALISATION ==
def init_data_dir():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    if not os.path.exists(TRANSACTIONS_FILE):
        with open(TRANSACTIONS_FILE, 'w') as f:
            pass

# == FONCTIONS DE GESTION DES TRANSACTIONS ==
def creation_id(list_avec_all_data):
    """identifiant unique pour une transaction"""
    while True:
        id = f"Id_{rd.randint(1000, 9999)}"
        if id not in list_avec_all_data:
            list_avec_all_data.append(id)
            return list_avec_all_data, id

def choix_type():
    """Demande à l'utilisateur de choisir le type de transaction"""
    print("\n-------")
    print("Types de transactions disponibles : ")
    print("1. Revenu")
    print("2. Dépense")

    while True:
        try:
            choix_type = int(input("\nQuel est le type de la transaction ? Tapez 1 ou 2 => "))
            if choix_type == 1:
                return "Revenu"
            elif choix_type == 2:
                return "Depense"
            else:
                print("Veuillez entrer 1 ou 2.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

def choix_montant():
    """Demande à l'utilisateur d'entrer le montant de la transaction"""
    while True:
        try:
            montant = int(input("Veuillez entrer le montant ici (en €) --> "))
            if montant > 0:
                print(f"Merci, vous avez entré {montant} €")
                return montant
            else:
                print("Le montant doit être positif.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

def enter_description():
    """Demande à l'utilisateur d'entrer une description pour la transaction"""
    print("Veuillez entrer une description brève :")
    return input("Entrez ici --> ")

def entrer_date():
    """Demande à l'utilisateur d'entrer une date valide"""
    print("Veuillez entrer une date valide (année, mois, jour) :")

    while True:
        try:
            year = int(input("Entrez l'année --> "))
            if 2020 <= year <= 9999:
                break
            else:
                print("L'année doit être entre 2020 et 9999.")
        except ValueError:
            print("Veuillez entrer une année valide.")

    while True:
        try:
            month = int(input("Entrez le mois --> "))
            if 1 <= month <= 12:
                break
            else:
                print("Le mois doit être entre 1 et 12.")
        except ValueError:
            print("Veuillez entrer un mois valide.")

    while True:
        try:
            day = int(input("Entrez le jour --> "))
            if 1 <= day <= 31:
                break
            else:
                print("Le jour doit être entre 1 et 31.")
        except ValueError:
            print("Veuillez entrer un jour valide.")

    date = f"{year}-{month:02d}-{day:02d}"
    print(f"Merci, vous avez entré {date}")
    return date

def creation_transaction(data):
    """Crée une nouvelle transaction"""
    print("\n----------")
    print("Vous allez entrer une nouvelle transaction.")

    select_type = choix_type()
    select_montant = choix_montant()
    select_descrip = enter_description()
    select_date = entrer_date()

    recup_list_id = data["list_id"]
    recup_list_id, recup_id = creation_id(recup_list_id)

    recup_all_data_transaction = data["data_transaction"]
    new_transaction = {
        "type": select_type,
        "montant": select_montant,
        "description": select_descrip,
        "date": select_date,
    }
    recup_all_data_transaction[recup_id] = new_transaction

    print("\n-----------")
    print("Voici un récapitulatif de ce que vous avez entré :")
    print(f"Type : {select_type}")
    print(f"Montant : {select_montant} €")
    print(f"Description : {select_descrip}")
    print(f"Date : {select_date}")
    print("-----------")

    return data

# == FONCTIONS DE SAUVEGARDE ET CHARGEMENT ==
def save_data_transac(data):
    """Sauvegarde les transactions dans un fichier"""
    recup_transaction = data["data_transaction"]

    with open(TRANSACTIONS_FILE, 'w') as f:
        for transaction_id, transaction in recup_transaction.items():
            line = f"ID[{transaction_id}]--Type[{transaction['type']}]--Montant[{transaction['montant']}]--Description[{transaction['description']}]--Date[{transaction['date']}]\n"
            f.write(line)

def charge_data():
    """Charge les transactions depuis le fichier"""
    list_id = []
    data_all_transaction = {}
    data_compte = {
        "solde_compte_depart": 5000,
    }

    if not os.path.exists(TRANSACTIONS_FILE):
        return {
            "list_id": list_id,
            "data_transaction": data_all_transaction,
            "data_compte": data_compte,
        }

    with open(TRANSACTIONS_FILE, 'r') as f:
        for line in f:
            if line.strip():
                recup_id = re.search(r'ID\[([^\]]+)\]', line)
                recup_type = re.search(r'Type\[([^\]]+)\]', line)
                recup_montant = re.search(r'Montant\[([^\]]+)\]', line)
                recup_description = re.search(r'Description\[([^\]]+)\]', line)
                recup_date = re.search(r'Date\[([^\]]+)\]', line)

                if recup_id and recup_type and recup_montant and recup_date:
                    id = recup_id.group(1)
                    type = recup_type.group(1)
                    montant = int(recup_montant.group(1))
                    description = recup_description.group(1) if recup_description else ""
                    date = recup_date.group(1).strip()

                    transaction = {
                        "type": type,
                        "montant": montant,
                        "description": description,
                        "date": date,
                    }
                    data_all_transaction[id] = transaction
                    list_id.append(id)

    return {
        "list_id": list_id,
        "data_transaction": data_all_transaction,
        "data_compte": data_compte,
    }

# == FONCTIONS DE CALCUL ET D'AFFICHAGE ==
def calcul_solde(data):
    """Calcule et affiche le solde actuel"""
    recup_data_solde = data["data_compte"]["solde_compte_depart"]
    recup_data_transaction = data["data_transaction"]
    new_solde = recup_data_solde

    for transaction in recup_data_transaction.values():
        if transaction["type"] == "Revenu":
            new_solde += transaction["montant"]
        elif transaction["type"] == "Depense":
            new_solde -= transaction["montant"]

    print(f"\nAprès étude de nos données, nous avons établi que le nouveau solde est de {new_solde} €,")
    print(f"avec un solde de départ de {recup_data_solde} €\n")

def afficher_all_transaction(data):
    """Affiche toutes les transactions enregistrées"""
    print("\nVoici toutes vos transactions enregistrées :\n")
    recup_transaction = data["data_transaction"]

    if not recup_transaction:
        print("Aucune transaction enregistrée.")
        return

    for transaction_id, transaction in recup_transaction.items():
        print("----------------")
        print(f"ID de Transaction : {transaction_id}")
        print(f"Type : {transaction['type']}")
        print(f"Montant : {transaction['montant']} €")
        print(f"Description : {transaction['description']}")
        print(f"Date : {transaction['date']}\n")

def afficher_transaction_date(data):
    """Affiche un rapport mensuel des transactions"""
    print("\n-------")
    while True:
        try:
            choix_year = int(input("Veuillez entrer l'année --> "))
            if 2020 <= choix_year <= 9999:
                break
            else:
                print("L'année doit être entre 2020 et 9999.")
        except ValueError:
            print("Veuillez entrer une année valide.")

    while True:
        try:
            choix_mont = int(input("Veuillez entrer le mois --> "))
            if 1 <= choix_mont <= 12:
                break
            else:
                print("Le mois doit être entre 1 et 12.")
        except ValueError:
            print("Veuillez entrer un mois valide.")

    search_data = f"{choix_year}-{choix_mont:02d}"
    print(f"\nVous avez choisi : {search_data}")

    recup_transaction = data["data_transaction"]
    recup_data_solde = data["data_compte"]["solde_compte_depart"]

    calcul_solde = recup_data_solde
    calcul_solde_revenu = 0
    calcul_solde_depense = 0

    for transaction in recup_transaction.values():
        if search_data in transaction["date"]:
            if transaction["type"] == "Revenu":
                calcul_solde += transaction["montant"]
                calcul_solde_revenu += transaction["montant"]
            elif transaction["type"] == "Depense":
                calcul_solde -= transaction["montant"]
                calcul_solde_depense += transaction["montant"]

    calcul_solde_trans = calcul_solde_revenu - calcul_solde_depense
    calcul_dif_solde = calcul_solde - recup_data_solde

    print("\n******")
    print(f"Rapport Mensuel pour la date du : {search_data}")
    print("\nEtude des Données :")
    print(f"Solde Total des Revenus : {calcul_solde_revenu} €")
    print(f"Solde Total des Dépenses : {calcul_solde_depense} €")
    print(f"\nLe Total des Transactions est de : {calcul_solde_trans} €")
    print("\n------")
    print(f"Votre Solde de Départ était de : {recup_data_solde} €")
    print(f"\nLe nouveau solde sera de : {calcul_solde} € avec une différence de {calcul_dif_solde} €")
    print("----------\n")

# == PROGRAMME PRINCIPAL ==
def big_programme():
    """Programme principal pour gérer les transactions financières"""
    print("Bonjour, Bienvenue sur la plateforme de votre Wallet\n")
    init_data_dir()
    data = charge_data()

    while True:
        try:
            print("\n*********************")
            print("1 - Entrer une nouvelle transaction (Revenu ou Dépense)")
            print("2 - Afficher toutes les transactions")
            print("3 - Afficher votre solde actuel")
            print("4 - Afficher un rapport mensuel")
            print("5 - Quitter\n")

            choix_user = int(input("Veuillez entrer votre action ici --> "))

            if choix_user == 1:
                data = creation_transaction(data)
            elif choix_user == 2:
                afficher_all_transaction(data)
            elif choix_user == 3:
                calcul_solde(data)
            elif choix_user == 4:
                afficher_transaction_date(data)
            elif choix_user == 5:
                print("Merci, Au revoir")
                save_data_transac(data)
                break
            else:
                print("Veuillez entrer une action valide (1 à 5).")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

if __name__ == "__main__":
    big_programme()