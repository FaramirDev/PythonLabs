## == DATA ==
tache_list = []

## == FONCTIONS ==
def add_tache():
    tache_add = input("Quelle tâche voulez-vous ajouter ? ")
    tache_list.append(tache_add)
    print(f"Merci, votre nouvelle tâche '{tache_add}' a bien été ajoutée.")

def del_tache():
    tache_del = input("Quelle tâche voulez-vous supprimer ? ")
    if tache_del in tache_list:
        tache_list.remove(tache_del)
        print(f"Votre tâche '{tache_del}' a bien été supprimée.")
    else:
        print(f"Votre tâche '{tache_del}' n'est pas dans votre liste.")

def tache_done():
    tache_done = input("Quelle tâche voulez-vous marquer comme terminée ? ")
    if tache_done in tache_list:
        index_tache = tache_list.index(tache_done)
        tache_list[index_tache] = tache_done + " *"
        print(f"Votre tâche '{tache_done}' a bien été mise à jour sur DONE.")
    else:
        print(f"Votre tâche '{tache_done}' n'est pas présente dans votre liste, merci de réessayer.")

def all_tache():
    if len(tache_list) == 0:
        print("Votre liste est actuellement vide, ajoutez quelque chose !")
    else:
        print("Votre liste de tâches est actuellement composée de :")
        for index, tache in enumerate(tache_list, start=1):
            print(f"{index}. {tache}")

def quit_programme():
    print("Merci, à bientôt !")

## == ACTIONS PROGRAMME ==
action_1 = "\nPour ajouter une tâche, tapez 1"
action_2 = "\nPour supprimer une tâche, tapez 2"
action_3 = "\nPour marquer une tâche comme terminée, tapez 3"
action_4 = "\nPour afficher toutes les tâches, tapez 4"
action_5 = "\nPour quitter le programme, tapez 5"
action_6 = "\nTapez ici s'il vous plaît --->"

## == PROGRAMME ==
def programme_tache():
    while True:
        try:
            user_input = int(input(f"Que voulez-vous faire ?\n{action_1}\n{action_2}\n{action_3}\n{action_4}\n{action_5}\n{action_6} "))
            if user_input == 1:
                add_tache()
            elif user_input == 2:
                del_tache()
            elif user_input == 3:
                tache_done()
            elif user_input == 4:
                all_tache()
            elif user_input == 5:
                quit_programme()
                break
            else:
                print("Veuillez entrer un nombre entre 1 et 5.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

## == START ==
programme_tache()
