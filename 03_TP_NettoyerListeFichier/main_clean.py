import csv
import os
from pathlib import Path

# Extensions valides
EXTENSIONS_VALIDES = {'.txt', '.csv'}

def nettoyer_nom_fichier(nom):
    """Nettoie un nom de fichier en vérifiant son extension"""
    if not nom.strip():
        return None

    extension = os.path.splitext(nom)[1].lower()
    if extension not in EXTENSIONS_VALIDES:
        return None

    return nom.strip()

def lire_fichier_csv(fichier_entree):
    """Lit un fichier CSV et retourne une liste nettoyée des noms de fichiers"""
    if not os.path.exists(fichier_entree):
        raise FileNotFoundError(f"Le fichier {fichier_entree} n'existe pas.")

    with open(fichier_entree, mode='r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        # Supposons que les noms de fichiers sont dans la première colonne
        fichiers = [row[0] for row in reader if row]
    return fichiers

def nettoyer_liste_fichiers(fichiers):
    """Nettoie une liste de fichiers en supprimant les doublons et les entrées invalides"""
    fichiers_clean = []
    fichiers_vus = set()

    for fichier in fichiers:
        fichier_nettoye = nettoyer_nom_fichier(fichier)
        if fichier_nettoye and fichier_nettoye not in fichiers_vus:
            fichiers_vus.add(fichier_nettoye)
            fichiers_clean.append(fichier_nettoye)

    return fichiers_clean

def ecrire_fichier_csv(fichier_sortie, fichiers_clean):
    """Écrit la liste nettoyée dans un fichier CSV"""
    # Créer le dossier de sortie s'il n'existe pas
    Path(os.path.dirname(fichier_sortie)).mkdir(parents=True, exist_ok=True)

    with open(fichier_sortie, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Nom du fichier'])  # En-tête
        for fichier in fichiers_clean:
            writer.writerow([fichier])

def afficher_resultats(fichiers_originaux, fichiers_clean):
    """Affiche les résultats du nettoyage"""
    print("\n=== RÉSULTATS DU NETTOYAGE ===")
    print(f"Fichiers originaux: {len(fichiers_originaux)}")
    print(f"Fichiers après nettoyage: {len(fichiers_clean)}")
    print(f"Fichiers supprimés: {len(fichiers_originaux) - len(fichiers_clean)}")

    print("\nListe des fichiers conservés:")
    for i, fichier in enumerate(fichiers_clean, 1):
        print(f"{i}. {fichier}")

def main():
    print("=== NETTOYAGE DE FICHIER CSV ===")

    # Configuration
    fichier_entree = "03_TP_NettoyerListeFichier/data/fichiers_bruts.csv"
    fichier_sortie = "03_TP_NettoyerListeFichier/data/fichiers_nettoyes.csv"

    try:
        # Lecture du fichier CSV
        print(f"\nLecture du fichier {fichier_entree}...")
        fichiers = lire_fichier_csv(fichier_entree)

        # Nettoyage des données
        print("Nettoyage des données...")
        fichiers_clean = nettoyer_liste_fichiers(fichiers)

        # Affichage des résultats
        afficher_resultats(fichiers, fichiers_clean)

        # Écriture du fichier CSV nettoyé
        print(f"\nÉcriture du fichier nettoyé {fichier_sortie}...")
        ecrire_fichier_csv(fichier_sortie, fichiers_clean)

        print("\nNettoyage terminé avec succès!")

    except FileNotFoundError as e:
        print(f"Erreur: {e}")
        print("Veuillez créer un fichier 'fichiers_bruts.csv' avec vos données.")
    except Exception as e:
        print(f"Une erreur inattendue est survenue: {e}")

if __name__ == "__main__":
    main()
