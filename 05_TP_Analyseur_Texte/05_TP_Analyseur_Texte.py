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
                print(f"Dans ce Texte, il y a {recup_count} de {alphabet}")
                data_alphabet[alphabet] = recup_count

    return data_alphabet
                
## == PROGRAMME == ##       
def programe():
    data = {}
    
    texte = input("Veuillez entrez votre Texte ! Nous l'analyserons ! Ici --->")

    nb_mot_len = calcul_mot(texte)
    print(f"Dans ce texte, il y a {nb_mot_len} de Mots !")
    ## MAJ DATA Mot
    data["data_mot"] = nb_mot_len

    nb_lettre = calcul_lettre_espace_off(texte)
    print(f"Dans ce texte, il y a {nb_lettre} lettre SANS les ESPACES !")
    ## MAJ DATA lettre
    data["data_lettre"] = nb_lettre

    
    nb_lettre_avec_espace = calcul_lettre_espace_on(texte)
    print(f"Dans ce texte, il y a {nb_lettre_avec_espace} lettre AVEC les Espaces !")
    ## MAJ DATA Lettre avec Espace
    data["data_lettre_espace"] = nb_lettre_avec_espace

    data_alphabet = calcul_frequence(texte)
    data["data_alphabet_all"] = data_alphabet

    print(data)
    return data 

## START 
data = programe()

print(data["data_alphabet_all"])




