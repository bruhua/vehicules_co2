import streamlit as st
import os
import pandas as pd
from joblib import dump, load
from typing_extensions import Required

import intro_co2
import visu_co2
import modeles_co2
import conclusion_co2
import demo_co2

# Variables globales
PAGES = {
    "Présentation du sujet": intro_co2,
    "Visualisation des données": visu_co2,
    "Modèles utilisés": modeles_co2,
    "Démonstration": demo_co2,
    "Conclusion et perspectives": conclusion_co2
}


# Gestion des chemins

# Récupération du dossier courant
#current_folder = os.path.dirname(__file__)
# Récupération du dossier der données (dataset, images, ...)
#data_path = os.path.join(current_folder, "Dataframe")


# Fonction pour charger les données
@st.cache
def load_data():
    df = pd.read_csv('https://raw.githubusercontent.com/bruhua/vehicules_co2/main/Dataframe/master_data_2014.csv', index_col = 0)
    return df
# Chargement des données
df = load_data()

# Chargement des modeles pour la partie demo
linear_reg = load('linear_reg.joblib')
linear_reg_EN = load('linear_reg_EN.joblib')
dt_reg = load('dt_reg.joblib')



# Affichage du menu sur le côté
st.sidebar.title('Emissions de CO2 des véhicules homologués')

# Choix de la page
selection = st.sidebar.radio("Menu ", (list(PAGES.keys())))
page = PAGES[selection]
page.app(df)

st.sidebar.markdown("""<hr style="height:2px;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)
st.sidebar.markdown("Auteurs :")
st.sidebar.markdown("[Jian Hu](https://www.linkedin.com/in/jian-hu-a7933687/)  \n[Bruno Huart](https://www.linkedin.com/in/bruno-huart-051459107/)  \n[Emilie Pottiez](https://www.linkedin.com/in/emilie-pottiez-776679216/)")
st.sidebar.markdown("""<hr style="height:2px;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)
st.sidebar.markdown("Projet DS  \nPromotion Juillet 2021")
