import os
from datetime import datetime

# Configuration
DATA_FILE = "08_TP_Gestionnaire_de_Reservation/data/reservation.csv"
SALLES_DISPONIBLES = {
    1: "Salle_A",
    2: "Salle_B",
    3: "Salle_C",
    4: "Salle_D"
}
HEURE_MIN = 6
HEURE_MAX = 23
ANNEE_MIN = 2024

def initialiser_fichier():
    """Crée le fichier de données s'il n'existe pas"""
    if not os.path.exists(DATA_FILE):
        os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
        with open(DATA_FILE, 'w') as f:
            f.write('')

def valider_annee(annee):
    """Valide que l'année est correcte"""
    return annee >= ANNEE_MIN

def valider_mois(mois):
    """Valide que le mois est correct"""
    return 1 <= mois <= 12

def valider_jour(annee, mois, jour):
    """Valide que le jour est correct pour le mois donné"""
    try:
        datetime(annee, mois, jour)
        return True
    except ValueError:
        return False

def saisir_date():
    """Demande à l'utilisateur de saisir une date valide"""
    print("\n-- Sélection de la date de réservation --")

    while True:
        try:
            annee = int(input("Entrez l'année (>= 2024) : "))
            if valider_annee(annee):
                break
            print("Veuillez entrer une année valide (>= 2024).")
        except ValueError:
            print("Veuillez entrer un nombre valide pour l'année.")

    while True:
        try:
            mois = int(input("Entrez le mois (1-12) : "))
            if valider_mois(mois):
                break
            print("Veuillez entrer un mois valide (1-12).")
        except ValueError:
            print("Veuillez entrer un nombre valide pour le mois.")

    while True:
        try:
            jour = int(input("Entrez le jour (1-31) : "))
            if valider_jour(annee, mois, jour):
                break
            print("Veuillez entrer un jour valide pour ce mois.")
        except ValueError:
            print("Veuillez entrer un nombre valide pour le jour.")

    return f"{annee}-{mois:02d}-{jour:02d}"

def saisir_heure():
    """Demande à l'utilisateur de saisir une heure valide"""
    print("\n-- Sélection de l'heure de réservation --")
    print(f"La tranche horaire disponible est de {HEURE_MIN}h à {HEURE_MAX}h")

    while True:
        try:
            heure = int(input(f"Sélectionnez l'heure ({HEURE_MIN}-{HEURE_MAX}) : "))
            if HEURE_MIN <= heure <= HEURE_MAX:
                break
            print(f"Veuillez entrer une heure entre {HEURE_MIN} et {HEURE_MAX}.")
        except ValueError:
            print("Veuillez entrer un nombre valide pour l'heure.")

    while True:
        try:
            minute = int(input("Sélectionnez les minutes (0-59) : "))
            if 0 <= minute < 60:
                break
            print("Veuillez entrer des minutes valides (0-59).")
        except ValueError:
            print("Veuillez entrer un nombre valide pour les minutes.")

    return f"{heure:02d}:{minute:02d}"

def selectionner_salle():
    """Demande à l'utilisateur de sélectionner une salle"""
    print("\n-- Sélection de la salle --")
    for num, salle in SALLES_DISPONIBLES.items():
        print(f"{salle} => Tapez {num}")

    while True:
        try:
            choix = int(input("Quelle salle souhaitez-vous réserver ? "))
            if choix in SALLES_DISPONIBLES:
                return SALLES_DISPONIBLES[choix]
            print(f"Veuillez entrer un numéro entre 1 et {len(SALLES_DISPONIBLES)}.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

def saisir_nom():
    """Demande à l'utilisateur de saisir un nom pour la réservation"""
    print("\n-- Nom de la réservation --")
    while True:
        nom = input("Entrez un nom pour confirmer la réservation : ").strip()
        if nom:
            return nom
        print("Veuillez entrer un nom valide.")

def creer_reservation():
    """Crée une nouvelle réservation"""
    salle = selectionner_salle()
    date = saisir_date()
    heure = saisir_heure()
    nom = saisir_nom()

    print("\n-- Récapitulatif de la réservation --")
    print(f"Salle : {salle}")
    print(f"Date : {date}")
    print(f"Heure : {heure}")
    print(f"Nom : {nom}")

    return f"{salle},{date},{heure},{nom}\n"

def charger_reservations():
    """Charge les réservations existantes depuis le fichier"""
    reservations = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            reservations = f.readlines()
    return reservations

def sauvegarder_reservations(reservations):
    """Sauvegarde les réservations dans le fichier"""
    with open(DATA_FILE, 'w') as f:
        f.writelines(reservations)

def afficher_reservations(reservations):
    """Affiche toutes les réservations"""
    if not reservations:
        print("\nAucune réservation en cours.")
        return

    print("\n-- Liste des réservations --")
    for i, resa in enumerate(reservations, 1):
        salle, date, heure, nom = resa.strip().split(',')
        print(f"{i}. Salle: {salle}, Date: {date}, Heure: {heure}, Nom: {nom}")

def rechercher_reservation(reservations):
    """Recherche une réservation spécifique"""
    terme = input("\nEntrez le nom de la réservation à rechercher : ").strip()
    trouvees = [resa for resa in reservations if terme.lower() in resa.lower()]

    if not trouvees:
        print("Aucune réservation trouvée avec ce terme.")
        return

    print("\n-- Réservations trouvées --")
    for i, resa in enumerate(trouvees, 1):
        salle, date, heure, nom = resa.strip().split(',')
        print(f"{i}. Salle: {salle}, Date: {date}, Heure: {heure}, Nom: {nom}")

def annuler_reservation(reservations):
    """Annule une réservation"""
    nom = input("\nEntrez le nom de la réservation à annuler : ").strip()
    initial_count = len(reservations)
    reservations = [resa for resa in reservations if nom.lower() not in resa.lower()]

    if len(reservations) == initial_count:
        print("Aucune réservation trouvée avec ce nom.")
    else:
        print(f"{initial_count - len(reservations)} réservation(s) annulée(s).")

    return reservations

def menu_principal():
    """Affiche le menu principal et gère les choix de l'utilisateur"""
    print("\n=== Gestionnaire de Réservations ===")
    print("1. Nouvelle réservation")
    print("2. Annuler une réservation")
    print("3. Afficher toutes les réservations")
    print("4. Rechercher une réservation")
    print("5. Quitter")

    while True:
        try:
            choix = int(input("\nEntrez votre choix (1-5) : "))
            if 1 <= choix <= 5:
                return choix
            print("Veuillez entrer un nombre entre 1 et 5.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

def main():
    """Fonction principale du programme"""
    initialiser_fichier()
    reservations = charger_reservations()

    print("Bonjour, bienvenue sur l'espace de réservation en ligne.")

    while True:
        choix = menu_principal()

        if choix == 1:
            reservations.append(creer_reservation())
        elif choix == 2:
            reservations = annuler_reservation(reservations)
        elif choix == 3:
            afficher_reservations(reservations)
        elif choix == 4:
            rechercher_reservation(reservations)
        elif choix == 5:
            sauvegarder_reservations(reservations)
            print("\nMerci, au revoir!")
            break

if __name__ == "__main__":
    main()
