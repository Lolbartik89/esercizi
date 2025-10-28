# ==============================================
# Progetto 4 — Analizzatore di Dati CSV
# Versione sicura per qualsiasi CSV simile
# ==============================================

import pandas as pd
import matplotlib.pyplot as plt

# 1️Carichiamo il file CSV
url = "https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv"
dati = pd.read_csv(url)

# 2️ Puliamo i nomi delle colonne (rimuove spazi e virgolette)
dati.columns = dati.columns.str.strip().str.replace('"', '').str.replace(' ', '')
print("Nomi delle colonne dopo pulizia:")
print(dati.columns)

# 3️ Determiniamo i nomi corretti delle colonne
if 'Height(Inches)' in dati.columns:
    col_altezza = 'Height(Inches)'
    col_peso = 'Weight(Pounds)'
elif 'HeightInches' in dati.columns:
    col_altezza = 'HeightInches'
    col_peso = 'WeightPounds'
else:
    raise KeyError("Non trovo le colonne di altezza/peso! Controlla l'output sopra.")

# 4️⃣ Calcoliamo statistiche di base
media_altezza = dati[col_altezza].mean()
massimo_altezza = dati[col_altezza].max()
minimo_altezza = dati[col_altezza].min()

media_peso = dati[col_peso].mean()
massimo_peso = dati[col_peso].max()
minimo_peso = dati[col_peso].min()

# 5️⃣ Stampiamo i risultati
print("\n Statistiche - Altezza (in pollici):")
print(f"Media: {media_altezza:.2f}, Massimo: {massimo_altezza}, Minimo: {minimo_altezza}")

print("\nStatistiche - Peso (in libbre):")
print(f"Media: {media_peso:.2f}, Massimo: {massimo_peso}, Minimo: {minimo_peso}")

# 6️Mostriamo e salviamo il grafico della distribuzione dell’altezza
plt.figure(figsize=(8, 5))
plt.hist(dati[col_altezza], bins=20, color='skyblue', edgecolor='black')
plt.title("Distribuzione dell'Altezza (in pollici)")
plt.xlabel("Altezza (inches)")
plt.ylabel("Frequenza")
plt.grid(True, linestyle='--', alpha=0.6)
plt.savefig("grafico_altezza.png")  # сохранение графика
plt.show()

# 7 Mostriamo e salviamo il grafico della distribuzione del peso
plt.figure(figsize=(8, 5))
plt.hist(dati[col_peso], bins=20, color='lightcoral', edgecolor='black')
plt.title("Distribuzione del Peso (in libbre)")
plt.xlabel("Peso (pounds)")
plt.ylabel("Frequenza")
plt.grid(True, linestyle='--', alpha=0.6)
plt.savefig("grafico_peso.png")  # сохранение графика
plt.show()

print("\n Analisi completata con successo! I grafici sono salvati nella cartella del progetto.")

