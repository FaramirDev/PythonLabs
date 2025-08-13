import string

# Liste des lettres de l'alphabet + espace
LIST_ALPHABET = list(string.ascii_lowercase) + ["*"]

def calcul_nombre_mots(texte):
    """Calcule le nombre de mots dans un texte"""
    return len(texte.split())

def calcul_lettres_sans_espaces(texte):
    """Calcule le nombre de lettres (sans compter les espaces)"""
    return sum(len(mot) for mot in texte.split())

def calcul_lettres_avec_espaces(texte):
    """Calcule le nombre total de caractères (lettres + espaces)"""
    return len(texte.replace(" ", "*"))

def calcul_frequence_lettres(texte):
    """Calcule la fréquence d'apparition de chaque lettre"""
    texte_normalise = texte.lower().replace(" ", "*")
    frequences = {lettre: 0 for lettre in LIST_ALPHABET}

    for lettre in texte_normalise:
        if lettre in frequences:
            frequences[lettre] += 1

    # Supprimer les lettres avec compte = 0
    return {k: v for k, v in frequences.items() if v > 0 and k != "*"}

def analyser_texte():
    """Programme principal d'analyse de texte"""
    print("=== ANALYSEUR DE TEXTE ===")
    texte = input("Veuillez entrer votre texte à analyser : ")

    # Calculs
    data = {
        "nombre_mots": calcul_nombre_mots(texte),
        "lettres_sans_espaces": calcul_lettres_sans_espaces(texte),
        "lettres_avec_espaces": calcul_lettres_avec_espaces(texte),
        "frequences_lettres": calcul_frequence_lettres(texte)
    }

    # Calcul du nombre d'espaces
    data["nombre_espaces"] = data["lettres_avec_espaces"] - data["lettres_sans_espaces"]

    # Affichage des résultats
    print("\n--- RÉSULTATS DE L'ANALYSE ---")
    print(f"Nombre de mots : {data['nombre_mots']}")
    print(f"Nombre de lettres (sans espaces) : {data['lettres_sans_espaces']}")
    print(f"Nombre d'espaces : {data['nombre_espaces']}")
    print(f"Nombre total de caractères : {data['lettres_avec_espaces']}")

    print("\nFréquence des lettres :")
    for lettre, count in sorted(data['frequences_lettres'].items()):
        print(f"  - '{lettre}' : {count} fois")

    return data

# Lancement du programme
if __name__ == "__main__":
    resultats = analyser_texte()
