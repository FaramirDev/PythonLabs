## == DATA == ## 
tache_list = []

## == FONCTION == ## 
def add_tache():
    tache_add = input("Que voulez-vous ajouter ?")
    tache_list.append(tache_add)
    print(f"Merci votre nouvelle tache {tache_add} à bien été ajouter.")

def del_tache():
    tache_del= input("Que voulez-vous ajouter ?")
    if tache_del in tache_list:
        tache_list.remove(tache_del)
        print(f"Votre Tache {tache_del} à bien été supprimer.")
    else:
        print("Votre Taches n'est pas dans votre liste.")

def tache_done():
    tache_done = input("Quelle Tache voulez-vous marqué comme Terminé ?")
    if tache_done in tache_list:
        for tache in tache_list:
            index_tache = tache_list.index(tache)

            tache_list[index_tache] = tache + "*"


        print(f"Votre Taches {tache_done} à bien été mis a jours sur DONE.")
    else: 
        print(f"Votre {tache_done} n'est pas présente dans votre Liste, merci de rééessayer.")

def all_tache():
    if len(tache_list) == 0:
        print("Votre Liste est Actuellement Vide, ajoutez quelques chose !")
    else:
        print("Votre Liste de Taches est actuellement composé de :")
        print(tache_list)

def quit_programme():
    print("Merci, a bientot !") 
        
## == ACTION PROGRAMME == ##        
action_1 = "\n Pour Ajouter une Taches. TAPEZ 1"
action_2 = "\n Pour Supprimer une TAches. TAPEZ 2"
action_3 =  "\n Pour Marquer une Taches Terminer. TAPEZ 3"
action_4 = "\n Pour Afficher toutes les Taches. TAPEZ 4"
action_5 =  "\n Pour Qutter le Programme. Tappez 5"
action_6 = "\n TAPEZ ICI s'il vous plait --->"

## == PROGRAMME == ## 
def programme_tache():
    while True:
        try:
            user_input = int(input(f"Que voulez-vous faire ? \n {action_1} {action_2} {action_3} {action_4} {action_5} {action_6}"))

            if user_input == 1:
                add_tache()
            elif user_input == 2:
                del_tache()
            elif user_input == 3:
                tache_done()
            elif user_input == 4:
                all_tache()
            elif user_input == 5:
                print("Merci, a bientot !")
                break
        except ValueError:
            print("Veuiller entrer un nombre valide")

## == START == ## 
programme_tache()


