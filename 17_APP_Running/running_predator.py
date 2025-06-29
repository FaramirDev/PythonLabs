import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import csv
### AP RUNING PREDATOR ###
# Version : 4.0
# Calcul de Vitesse / Pace et Temps de Passage


# 1. La mise En place des Fonctions
# === FONCTIONS CALCUL ===
def addition_all_temps(heures, minutes, secondes):
    total_minutes = heures * 60 + minutes + secondes / 60
    total_secondes = total_minutes * 60
    return total_minutes, total_secondes

def calcul_vitesse_kmh(distance_m, temps_secondes):
    vitesse_ms = distance_m / temps_secondes
    vitesse_kmh = vitesse_ms * 3.6
    return vitesse_kmh, vitesse_ms

def convert_time_pace(distance_km, vitesse_kmh):
    pace_brut = 60 / vitesse_kmh
    pace_min = int(pace_brut)
    pace_sec = round((pace_brut - pace_min) * 60)
    if pace_sec == 60:
        pace_sec = 0
        pace_min += 1
    return pace_min, pace_sec

def nb_1000_in_distance(distance):
    nb_de_1k = distance / 1000
    kilometres_complets = int(nb_de_1k)
    metres_restants = round((nb_de_1k - kilometres_complets) * 1000)
    return kilometres_complets, metres_restants

def calcul_temps_passage(nb_km, reste_metres, vitesse_kmh, vitesse_ms):
    passages = []
    for km in range(1, nb_km + 1):
        pace_brut = (60 / vitesse_kmh) * km
        heures = int(pace_brut // 60)
        minutes = int(pace_brut % 60)
        secondes = int(round((pace_brut - int(pace_brut)) * 60))
        if secondes == 60:
            secondes = 0
            minutes += 1
            if minutes == 60:
                minutes = 0
                heures += 1
        passages.append((f"{km} km", heures, minutes, secondes))
    if reste_metres > 0:
        temps_restant = reste_metres / vitesse_ms
        minutes = int(temps_restant // 60)
        secondes = int(round(temps_restant % 60))
        if secondes == 60:
            secondes = 0
            minutes += 1
        passages.append((f"{reste_metres} m", 0, minutes, secondes))
    return passages

# 2. La Mise en Place de L'interface Tk
# === INTERACTIONS TKINTER ===
def lancer_calcul():
    try:
        h = int(entry_heure.get())
        m = int(entry_minute.get())
        s = int(entry_seconde.get())
        d = int(entry_distance.get())

        total_min, total_sec = addition_all_temps(h, m, s)
        vitesse_kmh, vitesse_ms = calcul_vitesse_kmh(d, total_sec)
        pace_min, pace_sec = convert_time_pace(1, vitesse_kmh)
        nb_km, reste_m = nb_1000_in_distance(d)
        passages = calcul_temps_passage(nb_km, reste_m, vitesse_kmh, vitesse_ms)

        result_text.config(state='normal')
        result_text.delete('1.0', tk.END)
        result_text.insert(tk.END, f"Vitesse moyenne : {round(vitesse_kmh, 2)} km/h\n", "green")
        result_text.insert(tk.END, f"Allure moyenne : {pace_min} min {pace_sec:02} sec/km\n\n", "green")
        result_text.insert(tk.END, "Temps de passage :\n\n", "header")

        for point, h, m, s in passages:
            if h > 0:
                result_text.insert(tk.END, f"{point:>7} : {h}h {m:02}min {s:02}s\n")
            else:
                result_text.insert(tk.END, f"{point:>7} : {m:02}min {s:02}s\n")

        result_text.config(state='disabled')
        global last_passages
        last_passages = passages

    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer des valeurs numériques valides.")

def export_csv():
    if not last_passages:
        messagebox.showwarning("Aucun calcul", "Veuillez d'abord lancer un calcul.")
        return
    
    filepath = filedialog.asksaveasfilename(defaultextension=".csv",filetypes=[("CSV files", "*.csv")])

    if filepath:
        with open(filepath, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Kilometres", "Heures", "Minutes", "Secondes"])
            for row in last_passages:
                writer.writerow(row)

        messagebox.showinfo("Export terminé", f"Fichier sauvegardé : {filepath}")


## ===== TKINTER ======= ##
# === INTERFACE TKINTER ===
root = tk.Tk()
root.title("Running Predictor")
root.geometry("540x640")
root.configure(bg="#2c2f33")

style = ttk.Style()
style.theme_use("default")

# Styles Base
style.configure("TFrame", background="#2c2f33")
style.configure("TLabel", background="#2c2f33", foreground="white", font=("Segoe UI", 10))
style.configure("TButton", background="#7289da", foreground="white", font=("Segoe UI", 10), padding=6)
style.map("TButton", background=[("active", "#5b6eae")])

# Styles pour LabelFrame + titres
style.configure("Custom.TLabelframe", background="#2c2f33", borderwidth=1)
style.configure("Custom.TLabelframe.Label", background="#2c2f33", foreground="white", font=("Segoe UI", 11, "bold"))

# ==== Saisie ====
frame_inputs = ttk.LabelFrame(root, text="Données d'entrée", style="Custom.TLabelframe")
frame_inputs.pack(padx=15, pady=15, fill="x")

def create_entry_label(text, row, column):
    ttk.Label(frame_inputs, text=text).grid(row=row, column=column, padx=5, pady=8)
    entry = tk.Entry(frame_inputs, width=6, bg="#99aab5", fg="black", font=("Segoe UI", 10), justify="center")
    entry.grid(row=row, column=column + 1)
    return entry

entry_heure = create_entry_label("Heures", 0, 0)
entry_minute = create_entry_label("Minutes", 0, 2)
entry_seconde = create_entry_label("Secondes", 0, 4)
entry_distance = create_entry_label("Distance (m)", 1, 0)

# ==== Boutons ====
frame_buttons = ttk.Frame(root)
frame_buttons.pack(pady=10)

btn_calcul = ttk.Button(frame_buttons, text="Calculer", command=lancer_calcul)
btn_calcul.grid(row=0, column=0, padx=10)

btn_export = ttk.Button(frame_buttons, text="Exporter CSV", command=export_csv)
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

root.mainloop()
