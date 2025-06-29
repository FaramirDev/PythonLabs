### APPLICATION RUNNING PREDICTION 

#===== DONNÉES ENTRÉES ====

# Temps (1h 24min 17s)
heure = 1
minutes = 24
secondes = 17 

# Distance (semi-marathon : 21 095 m)
distance_m = 21095


#=== CONVERSION ET CALCULS ===

def addition_all_temps(heures, minutes, secondes):
    total_minutes = heures * 60 + minutes + secondes / 60
    total_secondes = total_minutes * 60
    return total_minutes, total_secondes

def calcul_vitesse_kmh(distance_m, temps_secondes):
    vitesse_ms = distance_m / temps_secondes
    vitesse_kmh = vitesse_ms * 3.6
    return vitesse_kmh, vitesse_ms

def convert_time_pace(distance_km, vitesse_kmh):
    pace_brut = 60 / vitesse_kmh
    pace_min = int(pace_brut)
    pace_sec = round((pace_brut - pace_min) * 60)

    # Correction si on a 60 secondes
    if pace_sec == 60:
        pace_sec = 0
        pace_min += 1

    return pace_min, pace_sec

def afficher_info(distance, h, m, s, vitesse_kmh, pace_min, pace_sec):
    print(f"\nPour une distance de {distance} mètres parcourue en {h}h {m}min {s}sec :")
    print(f" - Vitesse moyenne : {round(vitesse_kmh, 2)} km/h")
    print(f" - Allure moyenne : {pace_min} min {pace_sec:02} sec par kilomètre\n")

def nb_1000_in_distance(distance):
    nb_de_1k = distance / 1000
    kilometres_complets = int(nb_de_1k)
    metres_restants = round((nb_de_1k - kilometres_complets) * 1000)
    return kilometres_complets, metres_restants

def afficher_temps_passage(nb_km, reste_metres, vitesse_kmh, vitesse_ms):
    print("== Temps de passage à chaque kilomètre :")
    for km in range(1, nb_km + 1):
        pace_brut = (60 / vitesse_kmh) * km
        heures = int(pace_brut // 60)
        minutes = int(pace_brut % 60)
        secondes = int(round((pace_brut - int(pace_brut)) * 60))

        # Corriger 60 secondes
        if secondes == 60:
            secondes = 0
            minutes += 1
            if minutes == 60:
                minutes = 0
                heures += 1

        if heures > 0:
            print(f"Kilomètre {km:2} : {heures}h {minutes:02}min {secondes:02}s")
        else:
            print(f"Kilomètre {km:2} : {minutes:02}min {secondes:02}s")

    if reste_metres > 0:
        temps_restant = reste_metres / vitesse_ms
        minutes = int(temps_restant // 60)
        secondes = int(round(temps_restant % 60))

        if secondes == 60:
            secondes = 0
            minutes += 1

        print(f"\nReste {reste_metres} m : {minutes}min {secondes:02}s")


#=== LANCEMENT DES CALCULS ===

all_min, all_sec = addition_all_temps(heure, minutes, secondes)
vitesse_kmh, vitesse_ms = calcul_vitesse_kmh(distance_m, all_sec)
pace_min, pace_sec = convert_time_pace(1, vitesse_kmh)

afficher_info(distance_m, heure, minutes, secondes, vitesse_kmh, pace_min, pace_sec)

nb_km, reste_m = nb_1000_in_distance(distance_m)
afficher_temps_passage(nb_km, reste_m, vitesse_kmh, vitesse_ms)
