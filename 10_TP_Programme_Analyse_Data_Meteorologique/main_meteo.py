import random as rd
import statistics as stat

## Objectif : Création de données et analyse automatique

## DATA BASE
data_meteo = {}
data_stat = {
    "temperature moyenne": 0,
    "date temperature max": "",
    "Temperature max": 0,
    "total precipitation": 0,
    "jours de pluie": 0,
}

## == FONCTIONS ==

def creation_date():
    year_random = rd.randint(2020, 2025)
    month_random = rd.randint(1, 12)
    day_random = rd.randint(1, 30)
    date = f"{year_random}-{month_random:02d}-{day_random:02d}"
    return date

def creation_id():
    id_random = rd.randint(1000, 9999)
    id = 'Id_' + str(id_random)
    return id

def creation_temperature():
    temp_random = rd.randint(-5, 30)
    return temp_random

def creation_precipitation():
    precipitation_random = rd.randint(0, 200)
    return precipitation_random

def creation_humidite():
    humidite_random = rd.randint(1, 100)
    return humidite_random

def creation_programme_data(data):
    nombre_de_data = rd.randint(5, 200)
    for _ in range(nombre_de_data):
        id_data = {
            "date mesure": 0,
            "temperature": 0,
            "humidite": 0,
            "precipitation": 0
        }
        id = creation_id()
        date = creation_date()
        id_data["date mesure"] = date
        temp = creation_temperature()
        id_data["temperature"] = temp
        precipitation = creation_precipitation()
        id_data["precipitation"] = precipitation
        humidite = creation_humidite()
        id_data["humidite"] = humidite
        data[id] = id_data
    return data

def stat_temperature_moyen(data, data_stat):
    list_valeur = [data[id]["temperature"] for id in data]
    moyenne = stat.mean(list_valeur)
    data_stat["temperature moyenne"] = moyenne
    print(f"La moyenne des températures est de {moyenne:.2f} °C sur {len(list_valeur)} échantillons.")
    return data_stat

def most_temperature_high(data, data_stat):
    most_temperature = max(data[id]["temperature"] for id in data)
    most_date = next(id for id in data if data[id]["temperature"] == most_temperature)
    most_date = data[most_date]["date mesure"]
    data_stat["date temperature max"] = most_date
    data_stat["Temperature max"] = most_temperature
    print(f"La température la plus élevée est de {most_temperature} °C, qui a été enregistrée le {most_date}.")
    return data_stat

def calcul_total_precipitation(data, data_stat):
    valeur_precipitation = sum(data[id]["precipitation"] for id in data)
    data_stat["total precipitation"] = valeur_precipitation
    print(f"La valeur totale des précipitations sur l'ensemble des données est de {valeur_precipitation} mm.")
    return data_stat

def afficher_mesure_date(data):
    recup_date = input("Entrez la date dont vous souhaitez afficher les mesures. \nLa valeur doit être de type YYYY-MM-DD. \nTapez ici --> ")
    for id in data:
        if data[id]["date mesure"] == recup_date:
            print("Pour cette date, les valeurs sont de :")
            recup_temperature = data[id]["temperature"]
            recup_humidite = data[id]["humidite"]
            recup_precipitation = data[id]["precipitation"]
            print(f"La température a été de {recup_temperature} °C")
            print(f"Le taux d'humidité a été de {recup_humidite} %")
            print(f"Le taux de précipitation enregistré a été de {recup_precipitation} mm.")
            return
    print("Aucune donnée trouvée pour cette date.")

def calcul_jours_pluie(data, data_stat):
    jours_de_pluie = sum(1 for id in data if data[id]["precipitation"] > 0)
    data_stat["jours de pluie"] = jours_de_pluie
    print(f"Le nombre de jours de pluie dans l'ensemble des données récoltées est de {jours_de_pluie} jours, sur un ensemble de {len(data)} jours.")
    return data_stat

def affiche_data(data):
    for id in data:
        print(data[id])
        print("----")

def afficher_data_stat(data_stat):
    print(data_stat)

## == ACTIONS PROGRAMME ==
action_1 = "\nPour générer une nouvelle donnée météorologique, tapez 1"
action_2 = "\nPour calculer la température moyenne sur l'ensemble des données, tapez 2"
action_3 = "\nPour déterminer la date avec la température la plus élevée, tapez 3"
action_4 = "\nPour calculer le total des précipitations sur l'ensemble des données, tapez 4"
action_5 = "\nPour afficher les mesures pour une date donnée, tapez 5"
action_6 = "\nPour afficher le nombre de jours où il a plu, tapez 6"
action_7 = "\nPour afficher toutes les données, tapez 7"
action_8 = "\nPour afficher toutes les statistiques, tapez 8"
action_9 = "\nPour quitter le programme, tapez 9"

## == PROGRAMME ==
def programme_data(data, data_stat):
    data = creation_programme_data(data)
    print("\nBonjour, bienvenue sur notre service de Data Analyse des Données Météorologiques.")
    while True:
        try:
            print("\nQue voulez-vous faire ?")
            print(action_1, action_2, action_3, action_4, action_5, action_6, action_7, action_8, action_9)
            recup_choix = int(input("Entrez ici ---> "))
            if recup_choix == 1:
                data = creation_programme_data(data)
            elif recup_choix == 2:
                data_stat = stat_temperature_moyen(data, data_stat)
            elif recup_choix == 3:
                data_stat = most_temperature_high(data, data_stat)
            elif recup_choix == 4:
                data_stat = calcul_total_precipitation(data, data_stat)
            elif recup_choix == 5:
                afficher_mesure_date(data)
            elif recup_choix == 6:
                data_stat = calcul_jours_pluie(data, data_stat)
            elif recup_choix == 7:
                affiche_data(data)
            elif recup_choix == 8:
                data_stat = stat_temperature_moyen(data, data_stat)
                data_stat = most_temperature_high(data, data_stat)
                data_stat = calcul_total_precipitation(data, data_stat)
                data_stat = calcul_jours_pluie(data, data_stat)
                afficher_data_stat(data_stat)
            elif recup_choix == 9:
                print("Vous quittez le programme. Au revoir")
                break
            else:
                print("Veuillez entrer un nombre entre 1 et 9.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

    return data, data_stat

## == START ==
data_meteo, data_stat = programme_data(data_meteo, data_stat)
