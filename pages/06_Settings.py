import logging
import streamlit as st
from src.utils.dataio import get_data
import streamlit.components.v1 as components

def main(df):
    #Header information 
    st.title("System Settings", anchor=None)
    st.subheader("Configure database, users, etc.")
    st.write("coming soon")


def load_data():
    query_str = "SELECT * FROM CITIES;"
    df = get_data(query_str)
    return df

if __name__ == '__main__':
    logging.basicConfig(level=logging.CRITICAL)
    df = load_data()
    main(df)
