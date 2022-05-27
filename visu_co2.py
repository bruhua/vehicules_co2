import streamlit as st
from math import pi
import matplotlib.pyplot as plt
import os



# Page de visualisation des données
def app(df, data_path):
    st.title("Visualisation des données")
    st.markdown("""
    Cette page présente quelques visualisations choisies du jeu de données afin de mieux appréhender le lien 
    entre les variables, et plus particulièrement entre la variable cible et quelques variables importantes.
    """)

    st.subheader('Le jeu de données')

    st.markdown("""
    Les données proviennent de l’ADEME (Agence De l'Environnement et de la Maîtrise de l'Énergie) et sont 
    disponibles [ici](https://www.data.gouv.fr/fr/datasets/emissions-de-co2-et-de-polluants-des-vehicules-commercialises-en-france/#_).
    \nElles recensent tous les véhicules commercialisés en France au cours de l’année 2014 et contiennent leurs principales 
    caractéristiques techniques ainsi que les consommations de carburant, les émissions de CO2 et les émissions de polluants dans l’air
    \nLe jeu de données contient 55 001 lignes et 14 colonnes après nettoyage. Chaque ligne représente un modèle de véhicule homologué, 
    chaque colonne contient une caractéristique technique ou une mesure. 
    \nVoici un aperçu des premières lignes de données :
    """)
    st.dataframe(df.head(8))

    st.subheader('Corrélations entre les variables')

    st.markdown("Voici la heatmap des corrélations :")

    graph_correlation = plt.imread(os.path.join(data_path, "graph_correlation.PNG"))
    st.image(graph_correlation)




    st.markdown("""
    On remarque que la variable cible est très corrélée avec les variables de consommations. Elle est également corrélée, 
    dans une moindre mesure, avec les variables de masses et de puissances du véhicule.
    """)

    st.subheader("Corrélations avec la variable cible")

    st.write("Relation entre la puissance maximale et l'émission de CO2 :")

    croisement_puissance_co2 = plt.imread(os.path.join(data_path, "croisement_puissance_co2.PNG"))
    st.image(croisement_puissance_co2)



    st.write("Relation entre la consommation extra-urbaine et l'émission de CO2 :")

    croisement_conso_co2 = plt.imread(os.path.join(data_path, "croisement_conso_co2.PNG"))
    st.image(croisement_conso_co2)



    st.write("Relation entre la masse à vide et l'émission de CO2 :")

    croisement_masse_co2 = plt.imread(os.path.join(data_path, "croisement_masse_co2.PNG"))
    st.image(croisement_masse_co2)

    st.write("Relation entre la gamme et l'émission de CO2 :")

    croisement_gamme_co2 = plt.imread(os.path.join(data_path, "croisement_gamme_co2.PNG"))
    st.image(croisement_gamme_co2)

