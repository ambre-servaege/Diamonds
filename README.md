# [Diamonds]

## 📊 Description

Cette application permet de suivre le court du diamant et ainsi de pouvoir les revendre au meilleur prix. Vous pouvez rentrer vos données et faire fonctionner le modèle de prédiction

## 🎯 Parcours

- Projet Personnel sur le cout des diamants

## 📁 Dataset

- **Source** : (https://www.kaggle.com/datasets/shivam2503/diamonds/data)
- **Taille** : 53940 lignes, 10 colonnes
- **Variables principales** : price
price in US dollars (\$326--\$18,823)
carat
weight of the diamond (0.2--5.01)
cut
quality of the cut (Fair, Good, Very Good, Premium, Ideal)
color
diamond colour, from J (worst) to D (best)
clarity
a measurement of how clear the diamond is (I1 (worst), SI2, SI1, VS2, VS1, VVS2, VVS1, IF (best))
x
length in mm (0--10.74)
y
width in mm (0--58.9)
z
depth in mm (0--31.8)
depth
total depth percentage = z / mean(x, y) = 2 * z / (x + y) (43--79)
table
width of top of diamond relative to widest point (43--95)

## 🚀 Fonctionnalités

### Page 1 : Dataset
- description du data set et de ses principaux KPI

### Page 2 : Analyses
- selectionner les différentes formes d'analyses souhaitées

### Page 3 : Vizualization
- Choisissez vos visualisation selon les dimensions choisies, choisissez le type de visualisation que vous souhaitez

### Page 4 : Predictions
- Voyez les résultats de la prédiction en fonction des paramètres choisis

## 🛠️ Technologies Utilisées

- Python 3.13
- Streamlit
- Pandas
- Plotly Express
- layouts.footer
- layouts.header
- layouts.data
- sklearn.preprocessing
- sklearn.model_selection
- sklearn.linear_model
- sklearn.ensemble
- yellowbrick.regressor
- joblib
- matplotlib.pyplot
- numpy
- time


## 📦 Installation Locale
```bash
# Cloner le repository
git clone https://github.com/votre-username/votre-projet.git](https://github.com/ambre-servaege/Diamonds.git
cd votre-projet

# Installer les dépendances
pip install -r requirements.txt

# Lancer l'application
streamlit run app.py
```

## 🌐 Déploiement

Application déployée sur Streamlit Cloud :
👉 [Lien vers l'application](https://diamonds-k9f3cebauq7xg7rkjtmrne.streamlit.app/)](https://diamonds-bzmat6pb4xh2uqmiwluzou.streamlit.app/Prediction))

## 👥 Équipe

- **[Servaege Ambre]** 
- **[Lagaise Elliot]** 


## 📝 Notes

[Optionnel : Difficultés rencontrées, améliorations futures, etc.]# STREAMLIT APP WITH MACHINE LEARNING
Beaucoup d'installations n'avaient pas les versions utilisées sur VSCode 
