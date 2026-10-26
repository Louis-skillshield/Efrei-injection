"""
Démo d'injection SQL avec Streamlit : rechercher un abonné par son nom.

Deux versions de la même recherche :
  - vulnérable : le texte saisi est collé dans la requête (f-string) ;
  - sécurisée : le texte saisi est envoyé à part, avec %s.

Lancer :
    uv run streamlit run main.py

Saisies à essayer (en version vulnérable, puis sécurisée) :
    Martin
    ' OR '1'='1
    ' UNION SELECT abonne_id, titulaire, iban FROM moyen_paiement --
"""

import pandas as pd
import psycopg
import streamlit as st

from src.database import get_connection


def get_abonne_list_vulnerable(nom):
    """DANGER : le texte saisi devient du code SQL."""
    query = f"SELECT id, nom, prenom FROM abonne WHERE nom = '{nom}';"
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(query)
            column_list = [column.name for column in cursor.description]
            return query, pd.DataFrame(cursor.fetchall(), columns=column_list)


def get_abonne_list_securise(nom):
    """Le texte saisi est envoyé séparément : il reste une simple valeur."""
    query = "SELECT id, nom, prenom FROM abonne WHERE nom = %s;"
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(query, (nom,))
            column_list = [column.name for column in cursor.description]
            return query, pd.DataFrame(cursor.fetchall(), columns=column_list)


st.title("Vélib' · rechercher un abonné")

version = st.radio(
    "Version", ["Vulnérable (f-string)", "Sécurisée (%s)"], horizontal=True
)
nom = st.text_input("Nom de l'abonné", value="Martin")

if nom:
    try:
        if version.startswith("Vulnérable"):
            query, abonne_df = get_abonne_list_vulnerable(nom)
        else:
            query, abonne_df = get_abonne_list_securise(nom)
    except psycopg.Error as error:
        st.error(f"Erreur PostgreSQL : {error}")
    else:
        st.caption("Requête envoyée à PostgreSQL :")
        st.code(query, language="sql")
        st.write(f"**{len(abonne_df)}** ligne(s) trouvée(s)")
        st.dataframe(abonne_df, hide_index=True)
