## EXERCICE Gestion Liste de Course

## == DATA ==
liste_de_course = []

## == ACTIONS PROGRAMME ==
act_1 = "\nVoulez-vous ajouter un article ? Tapez 1 !"
act_2 = "\nVoulez-vous enlever un article ? Tapez 2 !"
act_3 = "\nVoulez-vous afficher la liste ? Tapez 3 !"
act_4 = "\nVoulez-vous quitter le programme ? Tapez 4 !"

## == FONCTIONS ==
def add_item_list(liste):
    article = input("\nQuel article voulez-vous ajouter ? ")
    liste.append(article)
    print(f"Merci, votre article '{article}' a bien été ajouté !")

def remove_item_list(liste):
    article = input("\nQuel article voulez-vous supprimer ? ")
    if article in liste:
        liste.remove(article)
        print(f"Merci, votre article '{article}' a bien été supprimé !")
    else:
        print(f"Mince, nous n'avons pas trouvé votre article '{article}' dans votre liste, veuillez réessayer !")

def print_all_list(liste):
    if len(liste) != 0:
        print("Votre liste est actuellement composée de :")
        for index, article in enumerate(liste, start=1):
            print(f"{index}. {article}")
    else:
        print("Votre liste est vide !")

def choix(action, liste):
    if action == 1:
        add_item_list(liste)
    elif action == 2:
        remove_item_list(liste)
    elif action == 3:
        print_all_list(liste)
    elif action == 4:
        print("Merci ! À bientôt !")
    else:
        print("Ce n'est pas dans mon champ d'action, réessayez !")

## == PROGRAMME ==
def prog_article():
    liste = liste_de_course
    input_u = int(input(f"Quelle action voulez-vous faire ? {act_1} {act_2} {act_3} {act_4} \n---> Entrez votre action : "))
    while input_u != 4:
        choix(input_u, liste)
        input_u = int(input(f"\nChouette, que voulez-vous faire maintenant ? {act_1} {act_2} {act_3} {act_4} \n---> Entrez votre action : "))
    print("Merci ! À bientôt !")

## == START ==
prog_article()
