import random as rd

## OBJECTIF : CREATION DE DATA de Vente 

## == DATA BASE == ## 
produit_stock = {
    "Produit_01" : {
        "Objet" : "Velo",
        "Prix" : 155,
        "Quantité_init" : 50,
        "Quantité_vendu" : 0,
        "ID_Object" : "id_155",
        "All_ID_vente" : 0},

    "Produit_02" : {
        "Objet" : "Skate",
        "Prix" : 75,
        "Quantité_init" : 23,
        "Quantité_vendu" : 0,
        "ID_Object" : "id_654",
        "All_ID_vente" : 0},

    "Produit_03" : {
        "Objet" : "Paddle_Surf",
        "Prix" : 225,
        "Quantité_init" : 35,
        "Quantité_vendu" : 0,
        "ID_Object" : "id_702",
        "All_ID_vente" : 0},

}

### == FONCTION == ## 
def set_quantité_et_vente(data):
    quantité_all = 0
    vente_all = 0
    for user in data:
        quantité_object = data[user]["Quantité_init"]
        quantité_all += quantité_object
        quantité_vendu = data[user]["Quantité_vendu"]
        vente_all += quantité_vendu
        obj = data[user]["Objet"]
        print(f"La quantité pour le produit : {obj} et de {quantité_object}")
        print(f"Ce produit a été vendu : {quantité_vendu} fois.")
    print(f"La quantité des ventes Maxi Dispo est de {quantité_all}")
    print(f"La quantité Total de vente a été de {vente_all}")

    return quantité_all, quantité_vendu, vente_all

def set_vente(data):
    for produit in data:
        quantite_max = data[produit]["Quantité_init"]
        vente = rd.randint(1,quantite_max)
        data[produit]["Quantité_vendu"] = vente

    ## Créer Liste avec Toutes les ventes
    return vente, data
    
def dico_vente():
    rand_vente = rd.randint(1000,9999)
    id_vente = "ID_" + str(rand_vente)
    date = 2025
    month = rd.randint(1,12)
    day = rd.randint(1,30)
    id_date = str(date) + '-' + str(month) + '-' + str(day)

    return id_vente, id_date


def set_liste_vente(data):
    data_vente = {}
    init = 1
    for produit in data:
        quantité_vendu = data[produit]["Quantité_vendu"]
        while init != quantité_vendu:
            id_vente, id_date = dico_vente()
            asset = {
                "Article" : data[produit]["Objet"],
                " Prix " : data[produit]["Prix"] ,
                " Date_Vente": id_date,
                "Id_vente" : id_vente }
            
            data_vente[id_vente] = asset
            init += 1

        if init == quantité_vendu:
            print(f"Nous avons établis la liste de vente")
            data[produit]["All_ID_vente"] = data_vente
            ob = "Objet"
            print(f"La data de vente du produit {data[produit][ob]} est {data_vente}")
            print("\n \n" )

    print(data)
    return data


## == START == ## 
vente, produit_stock = set_vente(produit_stock)

quantité_all = set_quantité_et_vente(produit_stock)

produit_stock = set_liste_vente(produit_stock)

## == AFFICHAGE == ## 
produit_stock

print("Finito")


