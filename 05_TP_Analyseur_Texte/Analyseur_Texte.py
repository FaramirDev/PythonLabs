## DATA 
list_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', "*"]


#### CALUCL DE STAT #### 
## 1 - Calcul nombre de Mot 
def calcul_mot(user_input):
    nb_mot = user_input.lower()
    nb_mot = user_input.split()
    nb_mot_len = len(nb_mot)
    return nb_mot_len

## 2 - Calcul lettre avec et sans  ESPACE
def calcul_lettre_espace_off(user_input):
    total_lettre= []
    nb_lettre = 0

    nb_mot = user_input.lower()
    nb_mot = user_input.split()

    for mot in nb_mot: 
        lettres = list(mot)
        total_lettre.append(lettres)
        for let in lettres:
            nb_lettre += 1
    
    
    return nb_lettre

def calcul_lettre_espace_on(user_input):
    remplace_espace = user_input.replace(" ","*")

    split_all_espacelettre = list(remplace_espace)
    nb_lettre_avec_espace = 0

    for lettre in split_all_espacelettre:
        nb_lettre_avec_espace += 1

    
    return nb_lettre_avec_espace

def calcul_frequence(user_input):
    nb_mot = user_input.lower()
    nb_mot = nb_mot.replace(" ","*")
    nb_mot = nb_mot.split()

    data_alphabet = {}

    list_mot = list(nb_mot)

    for mot in list_mot:
        for alphabet in list_alphabet:
            recup_count = mot.count(alphabet)
            if recup_count > 0 and alphabet!= "*":
                data_alphabet[alphabet] = recup_count

    return data_alphabet
                
## == PROGRAMME == ##       
def programe():
    data = {}
    
    texte = input("Veuillez entrez votre Texte ! Nous l'analyserons ! Ici --->")

    ## CALCUL 
    nb_mot_len = calcul_mot(texte)
    data["data_mot"] = nb_mot_len

    nb_lettre = calcul_lettre_espace_off(texte)
    data["data_lettre"] = nb_lettre

    nb_lettre_avec_espace = calcul_lettre_espace_on(texte)
    data["data_lettre_espace"] = nb_lettre_avec_espace

    data_alphabet = calcul_frequence(texte)
    data["data_alphabet_all"] = data_alphabet

    data_espace = nb_lettre_avec_espace - nb_lettre
    ## AFFICHAGE 
    print("--- ANALYSE ---")
    print(f" * -- Nombre de Mots : {nb_mot_len} ")
    print(f" * -- Nombre de Lettre : {nb_lettre} ")
    print(f" * -- Nombre d'Espace :{data_espace}")

    recup_list_alpha = data['data_alphabet_all']
    print(" ==> ANALYSE Lettres Detail :")
    for analyse in recup_list_alpha:
        nb = recup_list_alpha[analyse] 
        print(f"    - La Lettre {analyse} : {nb} fois")

    return data 

## START 
data = programe()






