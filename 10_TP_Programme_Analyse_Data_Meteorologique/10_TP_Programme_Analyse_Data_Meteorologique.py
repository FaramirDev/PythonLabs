import random as rd
import statistics as stat

## Objectif : CREATION DATA & ANALYSE AUTO 

## DATA BASE 
data_meteo = {}

data_stat = {
    "temperature moyenne" : 0,
    "date temperature max" : 0,
    "total précipiation" : 0,
    "jours de pluie" : 0,
}

## == FONCTION == ## 
## Generé une data random 
def creation_date():
    year_random = rd.randint(2020,2025)
    month_random = rd.randint(1,12)
    day_random = rd.randint(1,30)
    date = f"{year_random}-{month_random:02d}-{day_random:02d}"

    return date

def creation_id():
    id_random = rd.randint(1000,9999)
    id = 'Id_' + str(id_random)

    return id

def creation_temperature():
    temp_random = rd.randint(-5,30)

    return temp_random

def creation_precipitation():
    precipitation_random = rd.randint(0,200)

    return precipitation_random

def creation_humidite():
    humidite_random = rd.randint(1,100)

    return humidite_random
                      
def creation_programme_data(data):
    nombre_de_data = rd.randint(5,200)

    init_nb = 1

    while init_nb != nombre_de_data:
        id_data = {
        "date mesure" : 0,
        "temperature" : 0,
        "humidite" : 0,
        "precipitation" : 0}

        id = creation_id()
        
        date = creation_date()
        id_data["date mesure"] = date

        temp = creation_temperature()
        id_data["temperature"] = temp

        precipitation = creation_precipitation()
        id_data["precipitation"] = precipitation

        humidite =creation_humidite()
        id_data["humidite"] = humidite

        data[id] = id_data

        init_nb +=1


    return data


## Calcul de Data Stat
def stat_temperature_moyen(data, data_stat):
    list_valeur = []
    quantite_valeur = 0

    for id in data:
        list_valeur.append(data[id]["temperature"])
        quantite_valeur += 1
       
    moyenne = stat.mean(list_valeur)

    data_stat["temperature moyenne"] = moyenne
    print(f"La moyenne des Temperature est de {moyenne} °C sur {quantite_valeur} échantillons.")

    return data_stat
            
def most_temperature_high(data, data_stat):
    most_temperature = 0
    most_date = "init"

    for id in data:
        if data[id]["temperature"] >= most_temperature:
            most_temperature = data[id]["temperature"]
            most_date = data[id]["date mesure"]
        else:
            continue

    data_stat["date temperature max"] = most_date
    data_stat["Temperature max"] = most_temperature

    print(f"La temperature la plus élève est de {most_temperature} °C, qui a été enregistré le {most_date}")

    return data_stat

def calcul_total_precipitation(data, data_stat):
    valeur_precipitation = 0
    for id in data:
        recup_precipitation = data[id]["precipitation"]
        valeur_precipitation += recup_precipitation

    data_stat["total précipiation"] = valeur_precipitation

    print(f"La valeur Total des précipitations sur l'ensemble des données, et de {valeur_precipitation} mm.")

    return data_stat

def afficher_mesure_date(data):
    recup_date = input("Entrez la date dont vous souhaitez afficher les mesures. \n La valeur doit etre de type XXXX-MM-DAY. \nTappez ici -->")
    for id in data:
        if data[id]["date mesure"] == recup_date:
            print("Pour cette dates les valeurs sont de :")
            recup_temperature = data[id]["temperature"]
            recup_humidite = data[id]["humidite"]
            recup_precipitation = data[id]["precipitation"]
            print(f"La temperature a été de {recup_temperature} °C")
            print(f"Le Taux d'humidité a été {recup_humidite} %")
            print(f"Le Taux de précipitation enregistré a été {recup_precipitation} mm.")

        else:
            continue
    
def calcul_jours_pluie(data, data_stat):
    jours_de_pluie = 0
    recup_day = 0

    for id in data:
        recup_value = data[id]["precipitation"]
        recup_day += 1 

        if recup_value > 0:
            jours_de_pluie += 1
        else:
            continue
    data_stat["jours de pluie"] = jours_de_pluie

    print(f"Le nombre de Jours de pluie dans l'ensemble des donnée récolté est de {jours_de_pluie} Jours, sur un ensemble de {recup_day} Jours.")

    return data_stat

def affiche_data(data):
    for id in data:
        print(data[id])     
        print("----")

def afficher_data_stat(data_stat):
    print(data_stat)

## == ACTION PROGRAMME == ##
action_1 = "\n Pour Générer une Nouvelle Data de Vente. Tapez 1"
action_2 = "\n Pour Caculer la température moyenne sur l'ensemble des données. TAPEZ 2"
action_3 =  "\n Pour Déterminer la date avec la température la plus élevée. TAPEZ 3"
action_4 =  "\n Pour Calculer le total des précipitations sur l'ensemble des données. TAPEZ 4"
action_5 =  "\n Pour Afficher les mesures pour une date donnée. TAPEZ 5"
action_6 =  "\n Pour Afficher le nombre de jours où il a plus. TAPEZ 6"
action_7 =  "\n Pour Afficher Toutes les donnée. TAPEZ 7"
action_8 =  "\n Pour Afficher Toutes les Statistiques. TAPEZ 8"
action_9 =  "\n Pour Quitter le programme. TAPEZ 9"

## == PROGRAMME == ## 
def programme_data(data, data_stat):
    data = creation_programme_data(data)

    print("Bonjour, Bienvenu sur notre service de Data Analyse aux Donnée Météorologique.")
    while True:
        try:
            print("Que voulez-vous faire ?")
            print(action_1, action_2, action_3, action_4, action_5, action_6, action_7, action_8, action_9)
            recup_choix = int(input("Entrez ici --->"))
            if recup_choix == 1:
                data = creation_programme_data(data)
                
            elif recup_choix == 2:
                data_stat = stat_temperature_moyen(data, data_stat)

            elif recup_choix == 3:
                data_stat = most_temperature_high(data, data_stat)

            elif recup_choix == 4:
                data_stat = calcul_total_precipitation(data, data_stat)

            elif recup_choix == 5:
                data_stat = calcul_jours_pluie(data, data_stat)

            elif recup_choix == 6:
                afficher_mesure_date(data)

            elif recup_choix == 7:
                affiche_data(data)

            elif recup_choix == 8:
                data_stat = stat_temperature_moyen(data, data_stat)
                data_stat = most_temperature_high(data, data_stat)
                data_stat = calcul_total_precipitation(data, data_stat)
                data_stat = calcul_jours_pluie(data, data_stat)

                afficher_data_stat(data_stat)

            elif recup_choix == 9:
                print("Vous quittez le programme. Aurevoir")
                break
        except ValueError:
            print("Entrez un nombre valide.")

    return data, data_stat

## == START == ## 
data_meteo, data_stat = programme_data(data_meteo, data_stat)

