import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import csv

## === FONCTIONS === ##
def salaire_net_month(salaire_brut_mensuel):
    taxe = 0.18
    return salaire_brut_mensuel * (1 - taxe)

def salaire_net_year(salaire_brut_annuel):
    taxe = 0.18
    return (salaire_brut_annuel * (1 - taxe)) / 12

def salaire_net(choix, salaire_brut):
    if choix == "Month":
        return salaire_net_month(salaire_brut)
    elif choix == "Year":
        return salaire_net_year(salaire_brut)
    else:
        return salaire_brut  # fallback

def calcul_capacité_emprunt(net_salaire_month, year, apport, taux_interet_ans):
    capacity_max = net_salaire_month * 0.35
    all_month = year * 12  
    taux_interet_ans_percent = taux_interet_ans / 100
    taux_interet_mensuel = taux_interet_ans_percent / 12

    if taux_interet_mensuel == 0:
        total_max = capacity_max * all_month
    else:
        total_max = capacity_max * ((1 - (1 + taux_interet_mensuel) ** -all_month) / taux_interet_mensuel)

    capacity_total = total_max + apport
    return capacity_max, capacity_total

def calcul_mensualite(capital, taux_annuel, duree_annees):
    taux_mensuel = (taux_annuel / 100) / 12
    n = duree_annees * 12
    if taux_mensuel == 0:
        return capital / n
    return capital * taux_mensuel / (1 - (1 + taux_mensuel) ** -n)

def setup_data(capital, taux_annuel, mensualite, nb_mois):
    data = []
    reste = capital
    data.append(["mois", "mensualite", "interet", "principal", "reste"])

    taux_mensuel = (taux_annuel / 100) / 12

    for mois in range(1, nb_mois + 1):
        interet = reste * taux_mensuel
        principal = mensualite - interet
        reste -= principal
        data.append([mois, round(mensualite, 2), round(interet, 2), round(principal, 2), round(max(reste, 0), 2)])

    return data

def validate_input(new_value):
    if new_value == "":
        return True
    try:
        float(new_value)
        return True
    except ValueError:
        return False

def exporter_csv():
    if not last_passages:
        messagebox.showinfo("Info", "Faites d'abord un calcul.")
        return
    
    filepath = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("Fichier CSV", "*.csv")])
    if not filepath:
        return
    
    with open(filepath, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(last_passages)
    messagebox.showinfo("Succès", "Fichier CSV exporté.")

## === INTERFACE TKINTER === ##
root = tk.Tk()
root.title("Empruntator")
root.geometry("540x640")
root.configure(bg="#2c2f33")

vcmd = root.register(validate_input)

style = ttk.Style()
style.theme_use("default")

style.configure("TFrame", background="#2c2f33")
style.configure("TLabel", background="#2c2f33", foreground="white", font=("Segoe UI", 10))
style.configure("TButton", background="#7289da", foreground="white", font=("Segoe UI", 10), padding=6)
style.map("TButton", background=[("active", "#5b6eae")])

style.configure("Custom.TLabelframe", background="#2c2f33", borderwidth=1)
style.configure("Custom.TLabelframe.Label", background="#2c2f33", foreground="white", font=("Segoe UI", 11, "bold"))
style.configure("Custom.TCombobox", fieldbackground="#2c2f33", background="#2c2f33")

# ==== Saisie ====
frame_inputs = ttk.LabelFrame(root, text="Données d'entrée", style="Custom.TLabelframe")
frame_inputs.pack(padx=15, pady=15, fill="x")

def create_entry_label(text, row, column):
    ttk.Label(frame_inputs, text=text).grid(row=row, column=column, padx=5, pady=8)
    entry = tk.Entry(frame_inputs, width=6, bg="#99aab5", fg="black", font=("Segoe UI", 10), justify="center", validate="key", validatecommand=(vcmd, '%P'))
    entry.grid(row=row, column=column + 1)
    return entry

entry_salaire_month = create_entry_label("Salaire Brut", 0, 0)
entry_years = create_entry_label("Years Emprunt", 1, 0)
entry_apport = create_entry_label("Apport", 1, 2)
entry_taux_interet = create_entry_label("Taux Interet", 1, 4)

# Menu déroulant
options = ["Month", "Year"]
combo = ttk.Combobox(frame_inputs, value=options, state="readonly", width=6, justify="center", style="Custom.TCombobox")
combo.set("Year")
combo.grid(row=0, column=2, padx=5, pady=8)

# ==== Boutons ====
frame_buttons = ttk.Frame(root)
frame_buttons.pack(pady=10)

btn_calcul = ttk.Button(frame_buttons, text="Calculer")
btn_calcul.grid(row=0, column=0, padx=10)

btn_export = ttk.Button(frame_buttons, text="Exporter CSV", command=exporter_csv)
btn_export.grid(row=0, column=1, padx=10)

# ==== Résultats ====
frame_result = ttk.LabelFrame(root, text="Résultats", style="Custom.TLabelframe")
frame_result.pack(padx=10, pady=10, fill="both", expand=True)

result_text = tk.Text(frame_result, height=20, wrap="word", bg="#23272a", fg="#ffffff", font=("Consolas", 11))
result_text.pack(padx=10, pady=10, fill="both", expand=True)
result_text.tag_config("green", foreground="#43b581")
result_text.tag_config("header", font=("Segoe UI", 11, "bold"))
result_text.config(state='disabled')

last_passages = []

def lancer_calcul():
    try:
        salaire_brut = float(entry_salaire_month.get())
        year = int(entry_years.get())
        month = year * 12
        apport = float(entry_apport.get())
        taux_interet = float(entry_taux_interet.get())
        choix = combo.get()

        salaire_calcul = salaire_net(choix, salaire_brut)
        endettement_max, capacity_max = calcul_capacité_emprunt(salaire_calcul, year, apport, taux_interet)
        mensualite = calcul_mensualite(capacity_max, taux_interet, year)
        data_csv = setup_data(capacity_max, taux_interet, mensualite, month)

        result_text.config(state='normal')
        result_text.delete('1.0', tk.END)

        result_text.insert(tk.END, f"Salaire Net (Mensuel) : {round(salaire_calcul)} €\n", "green")
        result_text.insert(tk.END, f"Apport : {apport} €\n", "green")
        result_text.insert(tk.END, f"Endettement Max Mensuel : {round(endettement_max)} €\n\n", "green")
        result_text.insert(tk.END, f"Capacité Totale d'Achat : {round(capacity_max)} €", "header")

        # Affichage des 10 premières lignes
        result_text.insert(tk.END, f"\n\n\n------ TABLEAU D'Amortissement ------", "green")
        result_text.insert(tk.END, f"\n\n{data_csv[0]}", "header")
        for i in range(1, min(11, len(data_csv))):
            result_text.insert(tk.END, f"\n{data_csv[i]}", "green")

        result_text.config(state='disabled')

        global last_passages
        last_passages = data_csv

    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer des valeurs numériques valides.")

btn_calcul.config(command=lancer_calcul)

root.mainloop()
