import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from layouts.footer import footer
from layouts.header import header
from layouts.data import get_data
 
 
def main():
    header()
    st.subheader("Dataset brut")
    st.markdown("Ce projet permet de prédire le prix de vente du diamant, en fonction de ses caractéristiques. Voici le dataset utilisé :")
    st.dataframe(get_data())
    st.markdown("Ce dataset vient de Kaggle : [Diamonds Prices](https://www.kaggle.com/datasets/shivam2503/diamonds-prices). Il contient 10 colonnes et 53940 lignes.")
    st.markdown("Nous avons choisi ce projet car il vous permet de faire fructifier votre argent rapidement grace aux diamants")
    st.markdown("Voici les 3 KPI les plus intéressants du dataset : ")
    df = get_data()
    col1, col2, col3= st.columns(3)
    with col1:
        st.metric("Prix moyen", f"${df['price'].mean():.2f}")
    with col2:
        st.metric("Carat moyen", f"{df['carat'].mean():.2f} ct")
    with col3:
        st.metric("Profondeur moyenne d'extraction", f"{df['depth'].mean():.2f} %")
    st.markdown("voici la description des colonnes principales : ")
    st.markdown("- carat : poids du diamant (1 carat = 0.2 grammes)")
    st.markdown("- cut : qualité de la taille du diamant (Fair, Good, Very Good, Premium, Ideal)")
    st.markdown("- color : couleur du diamant (de D (meilleure) à J (pire))")
    st.markdown("- clarity : pureté du diamant (I1 (pire), SI2, SI1, VS2, VS1, VVS2, VVS1, IF (meilleure))")
    st.markdown("- depth : profondeur totale du diamant en pourcentage")
    st.markdown("- table : largeur de la table du diamant en pourcentage")
    st.markdown("- x : longueur en mm")
    st.markdown("- y : largeur en mm")
    st.markdown("- z : profondeur en mm")
    st.markdown("- price : prix en dollars américains")
    
if __name__ == "__main__":
    main()
 