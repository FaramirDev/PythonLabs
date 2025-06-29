import random as rd

## Creation d'un mini jeu de devinette 

def jeux_dev():
    min = 1
    max = 100
    essais = 1
    nb_pc = rd.randint(min,max)
    input_user = float(input(f"Devinez mon nombre compris enre {min} et {max} ! Bonne change !!! \n Tape ici ---->"))

    while input_user != nb_pc: 
        if input_user > nb_pc:
            print("Arf ! dommage, le nombre secret est plus petit ! Ressais ! ")
            input_user = float(input("Mince Réessais ici --->"))
            essais += 1
        elif input_user < nb_pc:
            print("Arf ! dommage, le nombre secret est plus Grand ! Réessais ! ")
            input_user = float(input("Mince Réessais ici --->"))
            essais += 1

    if input_user == nb_pc:
        print(f"Ouiiii Bravooooo !! Comment tu gères ! Tu as trouvé le bon nombre, et oui c'était bien {nb_pc} !!")
        print(f"Tu as réussi en {essais} Essais !!")

## == START == ## 
jeux_dev()


 