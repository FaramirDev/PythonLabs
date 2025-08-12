import csv
import os
from collections import defaultdict
from datetime import datetime

def lire_logs_csv(fichier):
    """Lit les logs depuis un fichier CSV et retourne une liste des connexions"""
    if not os.path.exists(fichier):
        raise FileNotFoundError(f"Le fichier {fichier} n'existe pas.")

    with open(fichier, mode='r', newline='') as f:
        reader = csv.reader(f)
        next(reader)  # Sauter l'entete présent
        logs = [row[0] for row in reader if row]  # Supposons que le nom d'utilisateur est dans la première colonne
    return logs

def analyser_logs(logs, seuil_activite=3):
    """Analyse les logs et retourne les statistiques d'accès"""
    comptes = defaultdict(int)
    for user in logs:
        comptes[user] += 1

    utilisateurs_actifs = {user: count for user, count in comptes.items() if count > seuil_activite}

    return dict(comptes), utilisateurs_actifs

def afficher_resultats(comptes, actifs):
    """Affiche les résultats de l'analyse"""
    print("\n===== STATISTIQUES D'ACCÈS =====\n")
    print("--- Tous les utilisateurs ---")
    print(f"{'Utilisateur':<15} | {'Accès':<6}")
    print("-" * 25)
    for user, count in sorted(comptes.items(), key=lambda x: x[1], reverse=True):
        print(f"{user:<15} | {count:<6}")

    print("\n--- Utilisateurs actifs (plus de 3 accès) ---")
    if actifs:
        print(f"{'Utilisateur':<15} | {'Accès':<6}")
        print("-" * 25)
        for user, count in sorted(actifs.items(), key=lambda x: x[1], reverse=True):
            print(f"{user:<15} | {count:<6}")
    else:
        print("Aucun utilisateur actif (plus de 3 accès)")

def sauvegarder_resultats_csv(comptes, actifs, fichier_sortie):
    """Sauvegarde les résultats dans un fichier CSV"""
    with open(fichier_sortie, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Statistiques d'accès aux logs"])
        writer.writerow([])  # Ligne vide
        writer.writerow(["Tous les utilisateurs"])
        writer.writerow(["Utilisateur", "Nombre d'accès"])
        for user, count in sorted(comptes.items(), key=lambda x: x[1], reverse=True):
            writer.writerow([user, count])

        writer.writerow([])  # Ligne vide
        writer.writerow(["Utilisateurs actifs (plus de 3 accès)"])
        writer.writerow(["Utilisateur", "Nombre d'accès"])
        if actifs:
            for user, count in sorted(actifs.items(), key=lambda x: x[1], reverse=True):
                writer.writerow([user, count])
        else:
            writer.writerow(["Aucun utilisateur actif"])

def main():
    print("=== ANALYSE DES LOGS D'UTILISATEURS (CSV) ===")

    # Configuration
    fichier_logs = "02_TP_AnalyseLogsUsers/data/user_logs.csv"
    fichier_sortie = f"02_TP_AnalyseLogsUsers/data/resultats_analyse_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    seuil = 3

    try:
        # Lecture et analyse
        logs = lire_logs_csv(fichier_logs)
        comptes, actifs = analyser_logs(logs, seuil)

        # Affichage et sauvegarde
        afficher_resultats(comptes, actifs)
        sauvegarder_resultats_csv(comptes, actifs, fichier_sortie)

        print(f"\nLes résultats ont été sauvegardés dans {fichier_sortie}")

    except FileNotFoundError as e:
        print(f"Erreur: {e}")
        print("Veuillez créer un fichier 'user_logs.csv' avec vos données.")
    except Exception as e:
        print(f"Une erreur inattendue est survenue: {e}")

if __name__ == "__main__":
    main()
