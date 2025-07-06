# Empruntator 

Empruntator est une mini‑application  ecrite en Python 3 / Tkinter 
---

# Objectif : 

    - Calculer votre capacité maximale d’emprunt à partir d’un salaire brut (mensuel ou annuel)
    - Générer automatiquement un tableau d’amortissement mensuel
    - Exporter ce tableau au format CSV.

---

## Sommaire 

    - 1. Fonctionnement Général
    - 2. Installation
    - 3. Lancement de l'Application
    - 4. Utilisation de l’interface
    - 5. Détails des formules financières
    - 6. Organisation du code & fonctions clés
    - 7. Export CSV
    - 8. Capture d'Ecran
    - 9. Licence

---

## Fonctionnement général

- Après avoir renseigné vos données (salaire brut, durée du prêt, apport et taux d’intérêt)

    - 1. Convertit le salaire brut en salaire net mensuel (18 % de Charges).
    - 2. Fixe le plafond d’endettement mensuel à 35 % du net mensuel.
    - 3. Calcule le capital total finançable (prêt + apport) via les formules des emprunts à mensualité constante.
    - 4. Établit un tableau d’amortissement détaillant, mois par mois : intérêts, principal et capital restant dû.
    - 5. Permet un export du tableau CSV.

---

## Installation 
-  Aucun package externe requis mise a part Python. >= 3.8 conseillé.
---

## Lancement de l'Appliaction
    python empruntator .py

Une fenêtre “Empruntator” s’ouvre (540 × 640 px).

---

## Utilisation de l’interface 

- 1. Salaire Brut - Montant brut (en €). 
- 2. Year Emprunt - Durée du Pret en Années
- 3. Apport - Votre Apport personnel en €
- 4. Taux Intéret - Taux Nominal annuel ( ex : 3.2 pour 3.5% )
- 5. Menu Month / Year, le type de Salaire Saisi
- 6. Calculer - Lance tous les Calculs et Affiche les Résultats et les 10 premières lignes du Tableau d'Amortissement. 
- 7. Export CSV - Save le Talbeau d'Amoortissement en CSV

---

## Détails des Formules Financière 

- Salaire Net Mensuel : Net = Brut * ( 1 - 0.18 )
- Plafond d'Endettement Mensuel : Cap = 0.35 * net
- Taux Mensuel : t = Tannuel / 12*100
- Capital Financable : (C = Cap * (1-1+t)**-n )/ t
- Mensualité Réel : M = (Ct)/(1-(1+t)**-n)
- Intéret Mois : Ii = R(i-1) * t
- Princiapl Mois = Pi = M - Ii
- Nouveau Reste = Ri = R(i-1) - Pi


---

## Organisation du code & Fonction cles

- salaire_net_month()
- salaire_net_year()
- calcul_capacite_emprunt()
- calcul_mensualite()
- setup_data()
- exporter_csv()

---

## Export CSV

Le fichier comporte 5 Catégories : 
    - mois, mensualite, interet, principal, reste
    - puis une ligne par mois jusqu'à échéance final. 

---

## Capture d'Ecran

![Fenêtre principale](images/ouverture.png)
![Exemple de résultat](images/calcul_resultat.png)
![Export CSV](images/export_csv.png)

---

LicenceDistribué sous licence MIT (voir LICENSE).
© 2025 — Empruntator project.
