import os
import random as rd
from datetime import datetime, timedelta

# == OBJECTIF : GESTION BIBLIOTHÈQUE AVEC EMPRUNTS ==

# == CHEMINS DES FICHIERS ==
DATA_DIR = "14_TP_Gestionnaire_bibliotheque_avance/data"
BOOKS_FILE = os.path.join(DATA_DIR, "livres.csv")
LOANS_FILE = os.path.join(DATA_DIR, "emprunts.csv")

# == FONCTIONS D'INITIALISATION ==
def init_data_dir():
    """Create dossier s'il n'existe pas encore"""
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    if not os.path.exists(BOOKS_FILE):
        with open(BOOKS_FILE, 'w') as f:
            pass
    if not os.path.exists(LOANS_FILE):
        with open(LOANS_FILE, 'w') as f:
            pass

# == FONCTIONS DE LECTURE/ÉCRITURE ==
def read_books():
    """Lit et retourne les données des livres depuis le fichier"""
    books = {}
    with open(BOOKS_FILE, 'r') as f:
        for line in f:
            if line.strip():
                id_book, title, author, year, available = line.strip().split(',')
                books[int(id_book)] = {
                    "titre": title,
                    "auteur": author,
                    "annee": year,
                    "disponibilite": available
                }
    return books

def write_books(books):
    """Écrit les données des livres dans le fichier"""
    with open(BOOKS_FILE, 'w') as f:
        for id_book, book in books.items():
            line = f"{id_book},{book['titre']},{book['auteur']},{book['annee']},{book['disponibilite']}\n"
            f.write(line)

def read_loans():
    """Lit et retourne les données des emprunts depuis le fichier"""
    loans = {}
    with open(LOANS_FILE, 'r') as f:
        for line in f:
            if line.strip():
                loan_id, book_id, title, borrower, start_date, end_date = line.strip().split(',')
                loans[loan_id] = {
                    "id_livre": book_id,
                    "titre": title,
                    "lecteur": borrower,
                    "date_emprunt": start_date,
                    "date_retour": end_date
                }
    return loans

def write_loans(loans):
    """Écrit les données des emprunts dans le fichier"""
    with open(LOANS_FILE, 'w') as f:
        for loan_id, loan in loans.items():
            line = f"{loan_id},{loan['id_livre']},{loan['titre']},{loan['lecteur']},{loan['date_emprunt']},{loan['date_retour']}\n"
            f.write(line)

# == FONCTIONS DE GESTION ==
def add_book(books):
    """Ajoute un nouveau livre à la bibliothèque"""
    print("\n--- Ajout d'un nouveau livre ---")
    title = input("Titre du livre: ")
    author = input("Auteur: ")
    while True:
        try:
            year = int(input("Année de publication: "))
            if 500 <= year <= datetime.now().year:
                break
            print("Veuillez entrer une année valide (entre 500 et l'année actuelle).")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

    new_id = max(books.keys()) + 1 if books else 1
    books[new_id] = {
        "titre": title,
        "auteur": author,
        "annee": str(year),
        "disponibilite": "Disponible"
    }
    print(f"\nLivre ajouté avec succès (ID: {new_id})")
    return books

def remove_book(books):
    """Supprime un livre de la bibliothèque"""
    print("\n--- Suppression d'un livre ---")
    title = input("Titre du livre à supprimer: ")
    found = False
    for id_book, book in list(books.items()):
        if book["titre"].lower() == title.lower():
            del books[id_book]
            print(f"Livre '{title}' supprimé avec succès.")
            found = True
            break
    if not found:
        print(f"Livre '{title}' non trouvé dans la bibliothèque.")
    return books

def borrow_book(books, loans):
    """Emprunte un livre disponible"""
    print("\n--- Emprunt d'un livre ---")
    title = input("Titre du livre à emprunter: ")
    borrower = input("Nom de l'emprunteur: ")

    # Recherche du livre
    book_id = None
    for id_book, book in books.items():
        if book["titre"].lower() == title.lower() and book["disponibilite"] == "Disponible":
            book_id = id_book
            break

    if not book_id:
        print(f"Livre '{title}' non disponible ou non trouvé.")
        return books, loans

    # Sélection des dates
    print("\nSélectionnez la date de début (format: AAAA-MM-JJ)")
    start_date = get_valid_date()
    print("\nSélectionnez la date de retour (format: AAAA-MM-JJ)")
    end_date = get_valid_date()

    if not is_valid_date_range(start_date, end_date):
        print("La date de retour doit être postérieure à la date de début.")
        return books, loans

    # Mise à jour des données
    books[book_id]["disponibilite"] = "Indisponible"
    loan_id = f"E{rd.randint(1000, 9999)}"
    loans[loan_id] = {
        "id_livre": str(book_id),
        "titre": title,
        "lecteur": borrower,
        "date_emprunt": start_date,
        "date_retour": end_date
    }

    print(f"\nLivre '{title}' emprunté avec succès par {borrower} (ID emprunt: {loan_id})")
    return books, loans

def return_book(books, loans):
    """Retourne un livre emprunté"""
    print("\n--- Retour d'un livre ---")
    loan_id = input("ID de l'emprunt: ")

    if loan_id not in loans:
        print("ID d'emprunt non trouvé.")
        return books, loans

    loan = loans[loan_id]
    book_id = int(loan["id_livre"])

    if book_id not in books:
        print("Livre associé non trouvé.")
        return books, loans

    books[book_id]["disponibilite"] = "Disponible"
    del loans[loan_id]
    print(f"Livre '{loan['titre']}' retourné avec succès.")
    return books, loans

def display_books(books):
    """Affiche tous les livres de la bibliothèque"""
    print("\n--- Liste des livres ---")
    if not books:
        print("Aucun livre dans la bibliothèque.")
        return

    for id_book, book in books.items():
        print(f"\nID: {id_book}")
        print(f"Titre: {book['titre']}")
        print(f"Auteur: {book['auteur']}")
        print(f"Année: {book['annee']}")
        print(f"Statut: {book['disponibilite']}")

def display_loans(loans):
    """Affiche tous les emprunts en cours"""
    print("\n--- Liste des emprunts ---")
    if not loans:
        print("Aucun emprunt en cours.")
        return

    for loan_id, loan in loans.items():
        print(f"\nID Emprunt: {loan_id}")
        print(f"Livre: {loan['titre']} (ID: {loan['id_livre']})")
        print(f"Emprunteur: {loan['lecteur']}")
        print(f"Date emprunt: {loan['date_emprunt']}")
        print(f"Date retour: {loan['date_retour']}")

# == FONCTIONS UTILITAIRES ==
def get_valid_date():
    """Demande et valide une date au format AAAA-MM-JJ"""
    while True:
        date_str = input("Date (AAAA-MM-JJ): ")
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return date_str
        except ValueError:
            print("Format de date invalide. Utilisez AAAA-MM-JJ.")

def is_valid_date_range(start_date, end_date):
    """Vérifie si la date de fin est postérieure à la date de début"""
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    return end > start

# == PROGRAMME PRINCIPAL ==
def main():
    init_data_dir()
    books = read_books()
    loans = read_loans()

    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Ajouter un livre")
        print("2. Supprimer un livre")
        print("3. Emprunter un livre")
        print("4. Retourner un livre")
        print("5. Afficher tous les livres")
        print("6. Afficher les emprunts en cours")
        print("7. Quitter")

        try:
            choice = int(input("\nVotre choix (1-7): "))
            if choice == 1:
                books = add_book(books)
            elif choice == 2:
                books = remove_book(books)
            elif choice == 3:
                books, loans = borrow_book(books, loans)
            elif choice == 4:
                books, loans = return_book(books, loans)
            elif choice == 5:
                display_books(books)
            elif choice == 6:
                display_loans(loans)
            elif choice == 7:
                write_books(books)
                write_loans(loans)
                print("\nDonnées sauvegardées. Au revoir!")
                break
            else:
                print("Choix invalide. Veuillez entrer un nombre entre 1 et 7.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

if __name__ == "__main__":
    main()
