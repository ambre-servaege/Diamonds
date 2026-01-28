import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

print("⏳ Chargement des données...")
# Chargement du CSV
try:
    df = pd.read_csv('diamonds.csv')
    # Suppression de la colonne d'index si elle existe
    if "Unnamed: 0" in df.columns:
        df = df.drop("Unnamed: 0", axis=1)
except FileNotFoundError:
    print("❌ ERREUR : Le fichier 'diamonds.csv' est introuvable !")
    exit()

# --- PARTIE CRUCIALE : Encodage manuel identique à Prediction.py ---
# L'ordre des listes ci-dessous doit être STRICTEMENT le même que dans votre application
cut_opts = ["Fair", "Good", "Ideal", "Premium", "Very Good"]
color_opts = ["D", "E", "F", "G", "H", "I", "J"]
clarity_opts = ["I1", "IF", "SI1", "SI2", "VS1", "VS2", "VVS1", "VVS2"]

print("⚙️ Transformation des données...")

# On transforme les colonnes de texte en colonnes de 0 et 1
for opt in cut_opts:
    df[opt] = (df['cut'] == opt).astype(int)

for opt in color_opts:
    df[opt] = (df['color'] == opt).astype(int)

for opt in clarity_opts:
    df[opt] = (df['clarity'] == opt).astype(int)

# On sélectionne les colonnes finales dans l'ordre exact attendu par l'app
feature_cols = ['carat', 'depth', 'table', 'x', 'y', 'z'] + cut_opts + color_opts + clarity_opts

X = df[feature_cols]
y = df['price']

# --- ENTRAINEMENT ---
print("🚀 Entraînement du modèle (Random Forest)...")
model = RandomForestRegressor(n_estimators=20, max_depth=10, random_state=42)
model.fit(X, y)

# --- SAUVEGARDE ---
# On s'assure que le dossier resources existe
if not os.path.exists('resources'):
    os.makedirs('resources')

output_path = 'resources/best_model.pkl'
print(f"💾 Sauvegarde du modèle dans : {output_path}")
joblib.dump(model, output_path)

print("✅ SUCCÈS ! Le fichier best_model.pkl a été recréé.")