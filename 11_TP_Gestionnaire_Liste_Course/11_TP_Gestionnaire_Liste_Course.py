## EXERCICE Gestion Liste COURSE

## == DATA == ## 
liste_de_course = []

## == ACTION PROGRAMME == ## 
act_1 = "\n \nVoulez vous-vous Ajouter un Article ? Tapez 1 !"
act_2 = "\nVoulez vous-vous Enlever un Article ? Tapez 2 !"
act_3 = "\nVoulez vous-vous Afficher la liste ? Tapez 3 !"
act_4 = "\nVoulez vous-vous Quitter le Programme ? Tapez 4 !"


##F == FONCTION == ## 
def add_item_list(liste):
    article = input("\n Quelle article voulez-vous ajouter ?")
    liste.append(article)
    print(f"Merci, votre article {article} à bien été ajouté !")

def remove_item_list(liste):
    article = input("\n Quelle article voulez-vous Supprimer ?")
    if article in liste:
        liste.remove(article)
        print(f"Merci, votre article {article} à bien été supprimé !")
    else:
        print(f"Mince, nous n'avons pas trouvé votre article {article} dans votre liste, veuillez réessayé !")

def print_all_list(liste):
    if len(liste) != 0:
        print("Votre liste est actuellement composé de :")
        print(liste)
    else:
        print("Votre liste est vide !")

def choix(action,liste):
    if action == 1:
        add_item_list(liste)
    elif action == 2:
        remove_item_list(liste)
    elif action == 3:
        print_all_list(liste)
    else: 
        print("Ce n'est pas dans mon champs d'action, reessayé !")

## == PROGRAMME == ##
def prog_article():
    input_u = int(input(f"Quelle Action voulez-vous faire ? {act_1} {act_2} {act_3} {act_4}  \n ---> Entrez votre Action ->"))
    list = liste_de_course

    while input_u != 4:
         choix(input_u,list)
         input_u = int(input(f"\n Chouette, que voulez-vous faire maintenant ? {act_1} {act_2} {act_3} {act_4} \n ---> Entrez votre Action ->"))
    if input_u == 4:
        print("Merci ! A bientot !")

## == START == ##          
prog_article() 



    



