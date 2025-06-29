### OBJECTIF : GESTION DE CLASSE 

## == DATA == ##
list_etudiant = {}

## == FONCTION == ##
def ajout_etudiant(data):
    recup_nom = input("Quel est le Nom de l'élève ?")
    recup_age = int(input("Quel age a t-il ?"))
    recup_moyenne = float(input("Quel est sa moyenne ?"))
    if recup_moyenne >= 0 and recup_moyenne  <= 20:
        data[recup_nom] = {
            "Nom" : recup_nom,
            "Age" : recup_age,
            "Moyenne" : recup_moyenne,
            }
    else:
        print("La moyenne doit etre comprise entre 0 et 20.")

    return data

def del_etudiant(data):
    recup_nom = input("Quel élèves voulez-vous supprimer ? \n Tappez ici -->")
    if recup_nom in data:
        del data[recup_nom]
        print(f"L'élèves {recup_nom}, a bien été supprimé")
    else:
        print("Mince nous n'avons pas trouvé cette élèves, veuillez rééssayer.")

    return data

def moyenne_eleve(data):
    recup_nom = input("Quel est le nom de l'élèves ? \n Tappez ici -->")
    old_moyenne = data[recup_nom]["Moyenne"]
    print(f"La moyenne de {recup_nom} est actuellement de {old_moyenne}.")
    recup_new_moyenne = float(input("Indiquez la nouvelle moyenne de l'élève s'il vous plait. \n Tappez ici -->"))
    if recup_new_moyenne >= 0 and recup_new_moyenne  <= 20:
        data[recup_nom]["Moyenne"] = recup_new_moyenne
        print(f"D'accord, nous avons bien mis a jours votre demande.\n La nouvelle moyenne de {recup_nom} et maintenant de {recup_new_moyenne}.")
    else: 
        print("La moyenne doit etre comprise entre 0 et 20")

    return data

def afficher_liste(data):
    for user in data:
        nom = "Nom"
        age = "Age"
        moyenne = "Moyenne"
        print(f"Le Nom de l'Etudiant est {data[user][nom]}")
        print(f"Son age est de {data[user][age]} ans")
        print(f"Sa Moyenne est de {data[user][moyenne]} \n")

def quit_programme():
    print("Merci, a bientot")

## == ACTION == ##    
action_1 = "\n Pour Ajouter un Nouvel Eleve. Tapez 1"
action_2 = "\n Pour Supprimer un Eleve existant. TAPEZ 2"
action_3 =  "\n Pour Modifier la Moyenne d'un Eleve. TAPEZ 3"
action_4 =  "\n Pour Afficher la Classe entière. TAPEZ 4"
action_5 =  "\n Pour Quitter le programme. TAPEZ 5"

## == PROGRAMME == ##
def programme_etudiant(data):
    print("Bonjour, bienvenue sur le servie de Classe en Ligne")
    while True:
        try:
            recup_choix = int(input(f"Que voulez-vous faire ? {action_1} {action_2} {action_3} {action_4} {action_5} \n Tapez ici -->"))
            if recup_choix == 1:
                data = ajout_etudiant(data)
            elif recup_choix == 2:
                data = del_etudiant(data)
            elif recup_choix == 3:
                data = moyenne_eleve(data)
            elif recup_choix == 4:
                afficher_liste(data)
            elif recup_choix == 5:
                quit_programme()
                break


        except ValueError:
            print("Veuillez entrer un nombre Valide s'il vous plait")

    return data
            
## == START == ##        
list_etudiant = programme_etudiant(list_etudiant)


