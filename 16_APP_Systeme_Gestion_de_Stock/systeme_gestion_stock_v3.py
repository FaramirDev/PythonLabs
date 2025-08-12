from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from datetime import datetime
import calendar
import os

## == DATA BASE == ## 
all_data_stock = {}

path_save_data = "16_APP_Systeme_Gestion_de_Stock/data/in/data_stock.txt"
path_save = path_save_data
list_path_data = [path_save_data]

nom_fichier = "data_stock.txt"

couleur_fond = '#1d1f20'
couleur_clair = "#dae0f0"
couleur_entree = "#d5d4d8"
couleur_bouton = "#237cbf"

elements = []

tree = None

## == FONCTION == ## 
def charge_data(path):
    with open(path, 'r') as f:
        recup_data = f.readlines()

    for data in recup_data:
        data_stock = data.split(',')

        id = int(data_stock[0].strip())
        nom = data_stock[1].strip()
        quantite = data_stock[2].strip()
        prix = data_stock[3].strip()
        date_expiration = data_stock[4].strip()

        article_data = [id,nom, quantite, prix, date_expiration]

        elements.append(article_data)
 
def ajoute_article():
    recup_id = str(len(elements) + 1)
    recup_nom = entry1_ajout.get().lower()
    recup_quantite = entry2_ajout.get().lower()
    recup_date = entry3_ajout.get().lower()

    new_article = [recup_id, recup_nom,recup_quantite,recup_date]


    elements.append(new_article)
    affiche_all()

def supp_article():
    recup_id_supp = entry2_supp.get()
    id = int(recup_id_supp) - 1

    print(id)
    for data in elements:
        recup_index = elements.index(data)
        if recup_index == id:
            elements.remove(data)

    init_id = 1
    for data in elements:
        data[0] = init_id   
        init_id += 1   

    affiche_all()
    
def modif_article():
    article_modif = "Paddle"
    new_quantite = 21

    for article in elements:
        if article[1] == article_modif:
            article[2] = str(new_quantite)
        
    affiche_all()         

def affiche_all():
    global tree

    # Vérifier si tree existe déjà
    if tree not in globals():
        # Créer un nouveau Treeview s'il n'existe pas
        tree = ttk.Treeview(root, columns=("ID", "Article", "Quantité", "Prix", "Date Expriration"), show="headings")

        # Définir les en-têtes de colonne
        tree.heading("ID", text="ID")
        tree.heading("Article", text="Article")
        tree.heading("Quantité", text="Quantité")
        tree.heading("Prix", text="Prix")
        tree.heading("Date Expriration", text="Date Expriration")

        # Définir la largeur des colonnes
        tree.column("ID", width=12)
        tree.column("Article", width=12)
        tree.column("Quantité", width=8)
        tree.column("Prix", width=10)
        tree.column("Date Expriration", width=10)

        # Ajouter le Treeview à la grille
        tree.grid(row=10, column=0, columnspan=3, sticky=NSEW, padx=10, pady=0)
    else:
        # Nettoyer le Treeview existant
        for item in tree.get_children():
            tree.delete(item)

    # Ajouter les éléments au Treeview
    for element in elements:
        date = element[4]
        date_seperate = date.split('-')
        annee_solo = int(date_seperate[0])
        month_solo = int(date_seperate[1])
        day_solo =  int(date_seperate[2])

        aujourdhui = datetime.today()
        annee = aujourdhui.year
        mois = aujourdhui.month

        date_aujourdhui_str = aujourdhui.strftime("%Y-%m-%d")
        date_aujourdui_split = date_aujourdhui_str.split('-')
        jours_actuel = int(date_aujourdui_split[2])

        validation_date = False
        if annee_solo == annee and month_solo == mois and day_solo > jours_actuel:
            validation_date = True
        elif annee_solo > annee:
            validation_date = True
        elif annee_solo >= annee and month_solo >= mois:
            validation_date = True
        else:
            validation_date = False

        item = tree.insert("", END, values=element)

        if element[4] and validation_date == False:
            tree.tag_configure('date_off', foreground="#ef382f")
            tree.item(item, tags=('date_off',))

        elif element[4] and validation_date == True:
            tree.tag_configure('date_on', foreground="#4bad2e")
            tree.item(item, tags=('date_on', ))
        
        else:
            tree.tag_configure('normal', foreground="#0b0c0b")
            tree.item(item, tags=('normal', ))

def si_path_no_exist():
    if not os.path.exists(path_save_data):
            with open(path_save_data, 'w') as f:
                f.write("")

def save_data():
    print(list_path_data)
    new_path = list_path_data[0]

    with open(new_path, 'w') as f:
        for stock in elements:
            recup_id = stock[0]
            recup_nom = stock[1].strip()
            recup_quantite = stock[2].strip()
            prix = stock[3].strip()
            recup_date = stock[4].strip()
            stock_save = f'{recup_id},{recup_nom},{recup_quantite},{prix},{recup_date}\n'

            f.write(stock_save)

def rechercher():
    texte_recherche = entry_recherche.get().lower()

    for item in tree.get_children():
        tree.delete(item)
    
    for element in elements:
        if texte_recherche in element[1].lower() or texte_recherche in element[3]:
            tree.insert("", END, values=element)

def affiche_entre_ajout():
    cacher_champs()
    label_nom.grid(row=4,column=0, sticky=NSEW, padx=2, pady=4,)
    label_quantite.grid(row=4,column=1, sticky=NSEW, padx=2, pady=4)
    label_date.grid(row=4,column=2, sticky=NSEW, padx=2, pady=4)

    entry1_ajout.grid(row=5,column=0, sticky=NSEW, padx=10, pady=2)
    entry2_ajout.grid(row=5,column=1, sticky=NSEW, padx=10, pady=2)
    entry3_ajout.grid(row=5,column=2, sticky=NSEW, padx=10, pady=2)

    button_ok.grid(row=6,column=1, sticky=NSEW, padx=10, pady=20)

    entry1_ajout.delete(0, END)
    entry2_ajout.delete(0, END)
    entry3_ajout.delete(0, END)

def cacher_champs():
    entry1_ajout.grid_forget()
    entry2_ajout.grid_forget()
    entry3_ajout.grid_forget()
    label_nom.grid_forget()
    label_supp_id.grid_forget()
    label_quantite.grid_forget()
    label_date.grid_forget()
    button_ok.grid_forget()
    button_sur.grid_forget()
    entry2_supp.grid_forget()

def affiche_entre_sup():
    cacher_champs()
    label_supp_id.grid(row=4,column=1, sticky=NSEW, padx=2, pady=4,)
    entry2_supp.grid(row=5,column=1, sticky=NSEW, padx=10, pady=2)
    button_sur.grid(row=6,column=1, sticky=NSEW, padx=10, pady=20)

    entry2_supp.delete(0, END)

def ouvrir_fenetre_choix_modify():
    fenetre_modify_choix = Toplevel(root)
    fenetre_modify_choix.title("Fenetre Modify")
    fenetre_modify_choix.geometry("400x600")
    fenetre_modify_choix.configure(bg=couleur_fond)
    fenetre_modify_choix.resizable(False, False)


    ## Titre : 
    label_titre_modif = Label(fenetre_modify_choix,text= "Modifier Article",fg=couleur_clair,bg = couleur_fond,font=('Arial', 13, 'bold'), )
    label_titre_modif.grid(row=0,column=1, sticky=NSEW, pady=15)

    ## Variable pour les stocker les choix
    choix1_titre = IntVar()
    choix2_quantite = IntVar()
    choix3_prix = IntVar()
    choix4_date = IntVar()
    

    ### Entré l'ID
    label_id = Label(fenetre_modify_choix,text= "Entré ID ( obligatoire )",fg=couleur_clair,bg = couleur_fond,font=('Arial', 8), )
    label_id.grid(row=1, column=0, sticky=NSEW, pady=10)

    entry_id_modify = Entry(fenetre_modify_choix, width=20, bg= couleur_entree, validate="key", validatecommand=(vcmd, '%P'))
    entry_id_modify.grid(row=1,column=1, sticky=NSEW, pady=10)

    ## Ajouter les boutons selection
    label_new_value = Label(fenetre_modify_choix,text= "Nouvelle Valeur",fg=couleur_clair,bg = couleur_fond,font=('Arial', 8), )
    label_new_value.grid(row=2, column=2, sticky=NSEW, pady=10)

    checkbutton_choix_titre = Checkbutton(fenetre_modify_choix, text="Modifé Nom :", variable=choix1_titre, bg=couleur_fond, fg=couleur_clair, selectcolor=couleur_fond,)
    checkbutton_choix_titre.grid(row=3,column=1, sticky=W, pady=5)

    entry_new_nom = Entry(fenetre_modify_choix, width=20, bg= couleur_entree)
    entry_new_nom.grid(row=3,column=2, sticky=NSEW, pady=5)

    checkbutton_choix_quantite = Checkbutton(fenetre_modify_choix, text="Modifé Quantite :", variable=choix2_quantite, bg=couleur_fond, fg=couleur_clair, selectcolor=couleur_fond, justify=LEFT)
    checkbutton_choix_quantite.grid(row=4,column=1, sticky=W, pady=5)

    entry_new_quantite = Entry(fenetre_modify_choix, width=20, bg= couleur_entree, validate="key", validatecommand=(vcmd, '%P'))
    entry_new_quantite.grid(row=4,column=2, sticky=NSEW, pady=5)

    entry_new_prix= Entry(fenetre_modify_choix, width=20, bg= couleur_entree, validate="key", validatecommand=(vcmd, '%P'))
    entry_new_prix.grid(row=5,column=2, sticky=NSEW, pady=5)

    checkbutton_choix_prix = Checkbutton(fenetre_modify_choix, text="Modifé Prix :", variable=choix3_prix, bg=couleur_fond, fg=couleur_clair, selectcolor=couleur_fond, justify=LEFT)
    checkbutton_choix_prix.grid(row=5,column=1, sticky=W, pady=5)

    checkbutton_choix_date = Checkbutton(fenetre_modify_choix, text="Modifé Date :", variable=choix4_date, bg=couleur_fond, fg=couleur_clair, selectcolor=couleur_fond, justify=LEFT)
    checkbutton_choix_date.grid(row=6,column=1, sticky=W, pady=5)


    def afficher_date():
        date = cal.get_date()
        label_date.config(text=date)


    def modifier_article(choix1_titre,choix2_quantite, choix3_prix, choix4_date, id, nom, quantite, prix, date):
        ## Ajouter les nom
        list_nom = []
        for item in elements:
            list_nom.append(item[1])

        ## date
        date_seperate = date.split('-')
        annee_solo = int(date_seperate[0])
        month_solo = int(date_seperate[1])
        day_solo =  int(date_seperate[2])

        aujourdhui = datetime.today()
        annee = aujourdhui.year
        mois = aujourdhui.month

        date_aujourdhui_str = aujourdhui.strftime("%Y-%m-%d")
        date_aujourdui_split = date_aujourdhui_str.split('-')
        jours_actuel = int(date_aujourdui_split[2])

        validation = False

        if annee_solo >= annee and month_solo >= mois and day_solo >= jours_actuel:
            validation = True

        elif annee_solo >= annee and month_solo > mois:
            validation = True
        
        elif annee_solo > annee:
            validation = True
        
        else:
            validation = False
             

        id = int(id) - 1

        if quantite == "":
            quantite = 0

        if prix == "":
            prix = 0

        tweak_quantite = int(quantite)
        tweak_prix = int(prix)


        for data in elements:
            recup_index = elements.index(data)
            if recup_index == id and validation == True:  
                if choix1_titre and nom not in list_nom and nom != "":               
                    new_nom = str(nom)
                    data[1] = new_nom

                if choix2_quantite and tweak_quantite > 0:                
                    new_quantite = str(quantite)
                    data[2] = new_quantite

                if choix3_prix and tweak_prix > 0:           
                    new_prix = str(prix)
                    data[3] = new_prix

                if choix4_date and validation == True:           
                    new_date = str(date)
                    data[4] = new_date 
                
                affiche_all()
                label_error_mod.config(text="Modification Réussi", fg="#2fef3e")

            elif nom in list_nom and nom != "":
                label_error_mod.config(text="Error : Nom utilisé ou non reconnu", fg = "#ef2f2f")

            elif nom == "" and choix2_quantite == False and choix4_date == False and choix3_prix == False:
                label_error_mod.config(text="Error : Veuillez Entrer un Nom", fg = "#ef2f2f")

            elif choix4_date == True and validation == False:
                label_error_mod.config(text="Date Non Valide.", fg = "#ef2f2f")

            elif tweak_quantite == 0 and choix4_date == False and choix3_prix == False and choix1_titre == False:
                label_error_mod.config(text="Entrez une Quantite valide.", fg = "#ef2f2f")

            elif tweak_prix == 0 and choix4_date == False and choix2_quantite == False and choix1_titre == False:
             label_error_mod.config(text="Entrez un Prix valide.", fg = "#ef2f2f")


    cal = Calendar(fenetre_modify_choix, selectmode="day", date_pattern="yyyy-mm-dd")
    cal.place(x=110, y=285)

    bouton_valider_date = Button(fenetre_modify_choix, text="Select Date", command=afficher_date, bg= "#4c4f4a", fg = couleur_clair)
    bouton_valider_date.place(x=110, y=475)

    label_date = Label(fenetre_modify_choix, text="", bg= "#4c4f4a", fg = couleur_clair)
    label_date.grid(row=6,column=2, sticky=NSEW, pady=5)

    label_error_mod = Label(fenetre_modify_choix, text="", bg= couleur_fond, fg = "#ef2f2f")
    label_error_mod.place(x=10, y=575)

    ## Bouton Valide Choix
    bouton_valider = Button(fenetre_modify_choix, text="Validé Modification", command=lambda: modifier_article(
        choix1_titre.get(), 
        choix2_quantite.get(), 
        choix3_prix.get(), 
        choix4_date.get(), 
        entry_id_modify.get(),
        entry_new_nom.get(),
        entry_new_quantite.get(),
        entry_new_prix.get(),
        cal.get_date(),), bg= "#46b143", fg=couleur_clair, font=('Arial', 11))
    
    bouton_valider.place(x=225, y=500)

def ouvrir_fenetre_ajout():
    fenetre_ajout_article = Toplevel(root)
    fenetre_ajout_article.title("Fenetre Ajout")
    fenetre_ajout_article.geometry("500x400")
    fenetre_ajout_article.configure(bg=couleur_fond)
    fenetre_ajout_article.resizable(False, False)

    ## Titre : 
    label_titre_modif = Label(fenetre_ajout_article,text= "Nouveau Article",fg=couleur_clair,bg = couleur_fond,font=('Arial', 13, 'bold'), )
    label_titre_modif.grid(row=0,column=2, sticky=NSEW, pady=10)

    label_nom = Label(fenetre_ajout_article,text= "Nom :",fg=couleur_clair,bg = couleur_fond,font=('Arial', 8), )
    label_nom.grid(row=2,column=1, sticky=W, pady=5, padx= 10)

    entry_nom = Entry(fenetre_ajout_article, width=20, bg= couleur_entree)
    entry_nom.grid(row=2,column=2, sticky=NSEW, pady=5)

    label_quantite = Label(fenetre_ajout_article,text= "Quantite :",fg=couleur_clair,bg = couleur_fond,font=('Arial', 8), )
    label_quantite.grid(row=3,column=1, sticky=W, pady=5, padx= 10)

    entry_quantite = Entry(fenetre_ajout_article, width=20, bg= couleur_entree, validate="key", validatecommand=(vcmd, '%P'))
    entry_quantite.grid(row=3,column=2, sticky=NSEW, pady=5)

    label_prix = Label(fenetre_ajout_article,text= "Prix :",fg=couleur_clair,bg = couleur_fond,font=('Arial', 8), )
    label_prix.grid(row=4,column=1, sticky=W, pady=5, padx= 10)

    entry_prix = Entry(fenetre_ajout_article, width=20, bg= couleur_entree, validate="key", validatecommand=(vcmd, '%P'))
    entry_prix.grid(row=4,column=2, sticky=NSEW, pady=5)

    def afficher_date():
        date = cal.get_date()
        label_date.config(text=date)


    def valider_ajout(nom, quantite, prix, date):
        list_nom = []
        for item in elements:
            list_nom.append(item[1])

        ## date
        date_seperate = date.split('-')
        annee_solo = int(date_seperate[0])
        month_solo = int(date_seperate[1])
        day_solo =  int(date_seperate[2])

        aujourdhui = datetime.today()
        annee = aujourdhui.year
        mois = aujourdhui.month

        date_aujourdhui_str = aujourdhui.strftime("%Y-%m-%d")
        date_aujourdui_split = date_aujourdhui_str.split('-')
        jours_actuel = int(date_aujourdui_split[2])

        validation = False

        if quantite == "":
            quantite = 0 
            
        if prix == "" :
            prix = 0


        tweak_quantite = int(quantite)
        tweak_prix = float(prix)

        if annee_solo >= annee and month_solo >= mois and day_solo >= jours_actuel:
            validation = True

        elif annee_solo >= annee and month_solo > mois:
            validation = True
        
        elif annee_solo > annee:
            validation = True
        
        else:
            validation = False
        

        if nom not in list_nom and nom != "" and validation == True and tweak_quantite > 0 and tweak_prix > 0: 
            recup_id = str(len(elements) + 1)
            new_article = [recup_id, nom,quantite, prix, date]
            elements.append(new_article)
            affiche_all()
            label_error.config(text="Ajout réussi", fg="#2fef3e")

        elif nom in list_nom and validation == True:
            label_error.config(text="Error : Nom utilisé ou non reconnu", fg = "#ef2f2f")

        elif nom == "" and validation == True:
            label_error.config(text="Error : Veuillez Entrer un Nom", fg = "#ef2f2f")

        elif validation == False:
            label_error.config(text="Error : Date Invalide", fg = "#ef2f2f")

        elif tweak_quantite <= 0 or tweak_prix <= 0:
            label_error.config(text="Error : Entrez une quantite ou prix valide" , fg = "#ef2f2f")


    cal = Calendar(fenetre_ajout_article, selectmode="day", date_pattern="yyyy-mm-dd")
    cal.place(x=220, y=45)

    bouton_valider_date = Button(fenetre_ajout_article, text="Select Date", command=afficher_date, bg= "#4c4f4a", fg = couleur_clair)
    bouton_valider_date.place(x=220, y=235)

    label_date_titre = Label(fenetre_ajout_article,text= "Date :",fg=couleur_clair,bg = couleur_fond,font=('Arial', 8), )
    label_date_titre.grid(row=5,column=1, sticky=W, pady=5, padx= 10)

    label_date = Label(fenetre_ajout_article, text="", bg= "#4c4f4a", fg = couleur_clair)
    label_date.grid(row=5,column=2, sticky=NSEW, pady=5,)

    label_error = Label(fenetre_ajout_article, text="", bg= couleur_fond, fg = "#ef2f2f")
    label_error.place(x=10, y=375)

    ## Bouton Valide Choix
    bouton_valider = Button(fenetre_ajout_article, text="Ajouter Article", command=lambda: valider_ajout( 
        entry_nom.get(),
        entry_quantite.get(), entry_prix.get(),
        cal.get_date(),), bg= "#46b143", fg=couleur_clair, font=('Arial', 10))
    
    bouton_valider.place(x=320, y=325, width= 150 )

def afficher_choix(choix1_titre, choix2_quantite, choix3_date, id, nom, quantite, date):
    # Afficher les choix sélectionnés
    id = int(id) - 1

    for data in elements:
        recup_index = elements.index(data)
        if recup_index == id:        
            if choix1_titre:               
                new_nom = str(nom)
                data[1] = new_nom

            if choix2_quantite:                
                new_quantite = str(quantite)
                data[2] = new_quantite

            if choix3_date:           
                new_date = str(date)
                data[3] = new_date
                

    print(elements) 

    affiche_all()

def charger_fichier(): 
    fichier_path = filedialog.askopenfilename(
        title="Selectionne un fichier",
        filetypes=(("Fichiers texte", "*.txt"), ("Tous les fichiers", "*.*"))
    )
    
    if fichier_path:
        clear_elements()

        charge_data(fichier_path)
    
        label_path.config(text=f"{fichier_path}")
        label_data_charge.config(text="New Data OK")

        list_path_data.clear()
        list_path_data.append(fichier_path)

        nom_fichier = os.path.basename(fichier_path)
        label_nom_fichier.config(text=f"Work on : {nom_fichier}")


        

        print(list_path_data)
        print(path_save)

        affiche_all()
        
def save_as_data():
    fichier_path = filedialog.asksaveasfilename(
        title="Sauvegarder un fichier",
        defaultextension=".txt",
        filetypes=(("Fichiers texte", "*.txt"), ("Tous les fichiers", "*.*"))
    )

    

    if fichier_path:
        with open(fichier_path, 'w') as f:
            for stock in elements:
                recup_id = stock[0]
                recup_nom = stock[1].strip()
                recup_quantite = stock[2].strip()
                prix = stock[3].strip()
                recup_date = stock[4].strip()
                stock_save = f'{recup_id},{recup_nom},{recup_quantite},{prix},{recup_date}\n'

                f.write(stock_save)
 
def clean_tableau():
    for item in tree.get_children():
        tree.delete(item)

def clear_elements():
    elements.clear()
 
def validate_input(new_value):
    if new_value == "":
        return True
    try : 
        int(new_value)
        return True
    
    except ValueError:
        return False

## == INTERFACE TK == ##
## FENETRE
root = Tk()
root.title("Gestion de Stock")
root.configure(bg=couleur_fond)

vcmd = root.register(validate_input)

## Def taille
root.geometry("630x600")
root.resizable(False, False)

si_path_no_exist()
charge_data(path_save_data)

## Labelle pour le Titre => pour image ou texte
label_titre = Label(root,text= "Gestion de Sotck",fg=couleur_clair,bg = couleur_fond,font=('Arial', 13, 'bold'), )
label_titre.grid(row=0,column=1, sticky=NSEW, pady=25)


## Bouton Ajout article
button_ajout = Button(root,text="Ajoute",command=ouvrir_fenetre_ajout,bg = couleur_bouton,fg = couleur_clair,font=('Arial', 8, 'bold'),width=20,height=1,state=NORMAL,)
button_ajout.grid(row=1,column=0, sticky=NSEW, padx=10, pady=10)

## Bouton Supprime article
button_supp = Button(root,text="Supprime",command=affiche_entre_sup,bg = couleur_bouton,fg = couleur_clair,font=('Arial', 8, 'bold'),width=20,height=1,state=NORMAL,)
button_supp.grid(row=1,column=1, sticky=NSEW, padx=10, pady=10)

## Bouton Modifierarticle
button_modify = Button(root,text="Modifier",command=ouvrir_fenetre_choix_modify,bg = couleur_bouton,fg = couleur_clair,font=('Arial', 8, 'bold'),width=20,height=1,state=NORMAL,)
button_modify.grid(row=1,column=2, sticky=NSEW, padx=10, pady=10)

## Button Affiche all data
button_affiche = Button(root,text="Affiche Sotck",command=affiche_all,bg = "#7155b0",fg = couleur_clair,font=('Arial', 8, 'bold'),width=20,height=1,state=NORMAL,)
button_affiche.grid(row=9,column=0, sticky=NSEW, padx=10, pady=0)

## Grid Tree

## Button Save & Quitte  all data
button_save = Button(root,text="Save",command=save_data,bg = "#7155b0",fg = couleur_clair,font=('Arial', 8, 'bold'),width=20,height=1,state=NORMAL,)
button_save.grid(row=11,column=2, sticky=NSEW, padx=10, pady=0)

## Barre de Recherche
entry_recherche = Entry(root, width=30, bg= couleur_entree)
entry_recherche.grid(row=9,column=1, sticky=NSEW, padx=10, pady=0)

button_ok = Button(root,text="Validé Ajout",command=ajoute_article,bg = "#5bb054",fg = couleur_clair,font=('Arial', 8, 'bold'),width=20,height=1,state=NORMAL,)
button_sur = Button(root,text="Validé Suppresion",command=supp_article,bg = "#c82c11",fg = couleur_clair,font=('Arial', 8, 'bold'),width=20,height=1,state=NORMAL,)

## Champ d'ajout 
label_nom = Label(root,text= "Nom Article :",fg=couleur_clair,bg = couleur_fond,font=('Arial', 8, 'bold'), )
label_quantite = Label(root,text= "Quantite :",fg=couleur_clair,bg = couleur_fond,font=('Arial', 8, 'bold'), )
label_date = Label(root,text= "Date :",fg=couleur_clair,bg = couleur_fond,font=('Arial', 8, 'bold'), )

label_supp_id = Label(root,text= "Entrez Valeur ID :",fg=couleur_clair,bg = couleur_fond,font=('Arial', 8, 'bold'), )

entry1_ajout = Entry(root, width=10,bg= couleur_entree)
entry2_ajout = Entry(root, width=10,bg= couleur_entree)
entry3_ajout = Entry(root, width=10,bg= couleur_entree)
entry2_supp = Entry(root, width=10,bg= couleur_entree, validate="key", validatecommand=(vcmd, '%P'))

entry1_ajout.grid_forget()
entry2_ajout.grid_forget()
entry3_ajout.grid_forget()
entry2_supp.grid_forget()
button_ok.grid_forget()
button_sur.grid_forget()

button_rechercher = Button(root,text="Rechercher",command=rechercher,bg = "#7155b0",fg = couleur_clair,font=('Arial', 8, 'bold'),width=20,height=1,state=NORMAL,)
button_rechercher.grid(row=9,column=2, sticky=NSEW, padx=10, pady=0)

label_nom_fichier = Label(root, text=f'Work on : {nom_fichier}', bg="#1f201f", fg="#696c66")
label_nom_fichier.place(x=10, y=500)

label_data_charge = Label(root, text="Data Chargé OK", bg="#26a93a", fg=couleur_clair)
label_data_charge.place(x=10, y=550)

label_path = Label(root, text=f'Data : {path_save_data}', bg="#1f201f", fg="#696c66")
label_path.place(x=10, y=570)

bouton_charger = Button(root, command=charger_fichier, text="Charger new Data..", bg="#2f302e", fg= "#a3a89f", font=('Arial', 8))
bouton_charger.place(x=10, y=10)

bouton_save_as = Button(root, command=save_as_data, text="Save as..", bg="#2f302e", fg= "#a3a89f", font=('Arial', 8))
bouton_save_as.place(x=10, y=40)

bouton_clear = Button(root, command=clear_elements, text="Clear data..", bg="#2f302e", fg= "#a3a89f", font=('Arial', 8))
bouton_clear.place(x=475, y=10)

## START 
root.mainloop()

