### OBJECTIF : GESTION DE CLASSE

## == DATA ==
list_etudiant = {}

## == FONCTIONS ==
def ajout_etudiant(data):
    recup_nom = input("Quel est le nom de l'élève ? ")
    recup_age = int(input("Quel âge a-t-il ? "))
    recup_moyenne = float(input("Quel est sa moyenne ? "))

    if 0 <= recup_moyenne <= 20:
        data[recup_nom] = {
            "Nom": recup_nom,
            "Age": recup_age,
            "Moyenne": recup_moyenne,
        }
    else:
        print("La moyenne doit être comprise entre 0 et 20.")

    return data

def del_etudiant(data):
    recup_nom = input("Quel élève voulez-vous supprimer ?\nTapez ici --> ")

    if recup_nom in data:
        del data[recup_nom]
        print(f"L'élève {recup_nom} a bien été supprimé.")
    else:
        print("Mince, nous n'avons pas trouvé cet élève. Veuillez réessayer.")

    return data

def moyenne_eleve(data):
    recup_nom = input("Quel est le nom de l'élève ?\nTapez ici --> ")

    if recup_nom in data:
        old_moyenne = data[recup_nom]["Moyenne"]
        print(f"La moyenne de {recup_nom} est actuellement de {old_moyenne}.")

        recup_new_moyenne = float(input("Indiquez la nouvelle moyenne de l'élève, s'il vous plaît.\nTapez ici --> "))

        if 0 <= recup_new_moyenne <= 20:
            data[recup_nom]["Moyenne"] = recup_new_moyenne
            print(f"D'accord, nous avons bien mis à jour votre demande.\nLa nouvelle moyenne de {recup_nom} est maintenant de {recup_new_moyenne}.")
        else:
            print("La moyenne doit être comprise entre 0 et 20.")
    else:
        print("L'élève n'a pas été trouvé.")

    return data

def afficher_liste(data):
    for etudiant in data.values():
        print(f"Le nom de l'étudiant est {etudiant['Nom']}")
        print(f"Son âge est de {etudiant['Age']} ans")
        print(f"Sa moyenne est de {etudiant['Moyenne']}\n")

def quit_programme():
    print("Merci, à bientôt.")

## == ACTIONS ==
action_1 = "\nPour ajouter un nouvel élève, tapez 1"
action_2 = "\nPour supprimer un élève existant, tapez 2"
action_3 = "\nPour modifier la moyenne d'un élève, tapez 3"
action_4 = "\nPour afficher la classe entière, tapez 4"
action_5 = "\nPour quitter le programme, tapez 5"

## == PROGRAMME ==
def programme_etudiant(data):
    print("---------------------")
    print("*** SYSTÈME DE CLASSE ***")
    print("\nBienvenue sur votre service de classe en ligne")

    while True:
        try:
            recup_choix = int(input(f"\nQue voulez-vous faire ?\n{action_1}{action_2}{action_3}{action_4}{action_5}\n\nTapez ici --> "))

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
            else:
                print("Veuillez entrer un nombre entre 1 et 5.")
        except ValueError:
            print("Veuillez entrer un nombre valide, s'il vous plaît.")

    return data

## == START ==
list_etudiant = programme_etudiant(list_etudiant)
