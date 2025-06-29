### APPLICATION RUNNING PREDICTION 

## EXPRESSION Utilse v = distance / temps
## Distance en Metre et Temps en Seconde 
# Exemple 10km = 10000m
# Exemple 40min = 40*60 = 2400s 
# Result = 4.16m/s

# Pour avoir km/h
## 1h = 3600s et 1k = 1000m
# donc 4.16*3.6
# result = 15km/h


## DATA Entré TEMPS
heure = 1
min = 24
sec = 17 
##CONVERSION EN MINUTES PUIS EN SECONDE
all_minute = heure*60 + min + sec*0.01
all_seconde = all_minute*60


## DATA DISTANCE
distance_m = 21095

## CALCUL VITESSE EN M/S PUIS CONVERSION EN KM/h
calcul_vitesse_ms = distance_m / all_seconde
calcul_vitesse_kmh = calcul_vitesse_ms*3.6


## CALCUL PACE POUR 1km
# Expression calculer temps  
temps_1k_brut = 60/calcul_vitesse_kmh

## JUST CONVERTE TIME
recup_just_int = int(temps_1k_brut)
recup_just_float = temps_1k_brut - recup_just_int
float_minute = recup_just_float*60*0.01
temps_1k = recup_just_int + float_minute


print(f"Pour une Disance de {distance_m} Metres Parcourut en {heure}h {min}min {sec}sec")
print(f"La Vitesse sera de {round(calcul_vitesse_kmh,2)} Km/h")
print(f"Le Pace sera alors de {round(temps_1k, 2)} min au Kilomètres")


## DEF FONCTION CONVERTION TIME
def convert_time(nombre_kilo, vitesse_kmh):
    pace_1k_brut = 60/vitesse_kmh
    temps_boucle = nombre_kilo*pace_1k_brut
    # Calcul Temps juste
    recup_int = int(temps_boucle)
    recup_float = temps_boucle - recup_int
    recup_seconde = recup_float*60*0.01
    # Additionne Minutes + Floatante
    temps_clean = recup_int + recup_seconde

    return temps_clean


### AFFICHAGE TEMPS DE PASSAGE : 
# SAVOIR COMBIEN DE 1000m dans la DISTANCE 
nb_de_1k = distance_m/1000

recup_nombre_1k = int(nb_de_1k)
recup_metre_restant = round((nb_de_1k - recup_nombre_1k)* 1000)


print(f"Dans la Disance de {distance_m}")
print(f"Le Nombre de 1km est de {recup_nombre_1k}")
print(f"Le Dernier Tours est de {recup_metre_restant} mètres")


### affichage
init_boucle = 1

while init_boucle <= recup_nombre_1k:
    calcul_temps = init_boucle*temps_1k
    print(f"Kilometres : {init_boucle} km - Temps : {round(calcul_temps,2)}")
    init_boucle += 1

print(f"Metres Restant : {recup_metre_restant} m - Temps : {round(calcul_temps,2)} ")