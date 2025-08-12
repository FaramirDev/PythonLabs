import random as rd

# OBJECTIF : CREATION DE DATA de Vente
# == DATA BASE ==
produit_stock = {
    "Produit_01": {
        "Objet": "Velo",
        "Prix": 155,
        "Quantité_init": 50,
        "Quantité_vendu": 0,
        "ID_Object": "id_155",
        "All_ID_vente": {}
    },
    "Produit_02": {
        "Objet": "Skate",
        "Prix": 75,
        "Quantité_init": 23,
        "Quantité_vendu": 0,
        "ID_Object": "id_654",
        "All_ID_vente": {}
    },
    "Produit_03": {
        "Objet": "Paddle_Surf",
        "Prix": 225,
        "Quantité_init": 35,
        "Quantité_vendu": 0,
        "ID_Object": "id_702",
        "All_ID_vente": {}
    },
}

# == FONCTIONS ==
def set_quantité_et_vente(data):
    quantité_all = 0
    vente_all = 0
    for user in data:
        quantité_object = data[user]["Quantité_init"]
        quantité_all += quantité_object
        quantité_vendu = data[user]["Quantité_vendu"]
        vente_all += quantité_vendu
        obj = data[user]["Objet"]
        print(f"\n- La quantité pour le produit : {obj} est de {quantité_object}")
        print(f"- Ce produit a été vendu : {quantité_vendu} fois.")
    print(f"\n- La quantité des ventes Maxi Dispo est de {quantité_all}")
    print(f"- La quantité totale de ventes a été de {vente_all}")
    return quantité_all, vente_all

def set_vente(data):
    for produit in data:
        quantite_max = data[produit]["Quantité_init"]
        vente = rd.randint(1, quantite_max)
        data[produit]["Quantité_vendu"] = vente
    return data

def dico_vente():
    rand_vente = rd.randint(1000, 9999)
    id_vente = "ID_" + str(rand_vente)
    date = 2025
    month = rd.randint(1, 12)
    day = rd.randint(1, 30)
    id_date = f"{date}-{month:02d}-{day:02d}"
    return id_vente, id_date

def set_liste_vente(data):
    for produit in data:
        quantité_vendu = data[produit]["Quantité_vendu"]
        data_vente = {}
        init = 1
        while init <= quantité_vendu:
            id_vente, id_date = dico_vente()
            asset = {
                "Article": data[produit]["Objet"],
                "Prix": data[produit]["Prix"],
                "Date_Vente": id_date,
                "Id_vente": id_vente
            }
            data_vente[id_vente] = asset
            init += 1
        data[produit]["All_ID_vente"] = data_vente
        print(f"\n- [OK] Nous avons établi la liste de vente pour {data[produit]['Objet']}")
        print(f"- La data de vente du produit : \n{data[produit]['Objet']} est {data_vente}\n")
    return data

# == START ==
produit_stock = set_vente(produit_stock)
quantité_all, vente_all = set_quantité_et_vente(produit_stock)
produit_stock = set_liste_vente(produit_stock)

# == AFFICHAGE ==
print("-Toute la Liste de Vente : ")
print(produit_stock)
