import logging
import streamlit as st
from src.utils.dataio import get_data
import streamlit.components.v1 as components

def main(df):
    #Header information 
    st.title("Organizations", anchor=None)
    st.subheader("We work with a wide variety of NGOs providing access to funding resources.")
    st.caption("Project 3 by Phoebe Gunter, Harry Oestreicher, Abhishek Banerjee, Gabriel Paganin, Gerald Cortright, Javier", unsafe_allow_html=False)
    st.write(df)


def load_data():
    query_str = "SELECT * FROM ORGANIZATIONS;"
    df = get_data(query_str)
    return df

if __name__ == '__main__':
    logging.basicConfig(level=logging.CRITICAL)
    df = load_data()
    main(df)
