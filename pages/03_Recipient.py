import logging
import streamlit as st
from src.utils.dataio import get_data
import streamlit.components.v1 as components

def main(df):
    #Header information 
    st.title("Recipients", anchor=None)
    st.subheader("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")
    st.caption("work in progress ", unsafe_allow_html=False)
    st.write(df)

def load_data():
    query_str = "SELECT * FROM RECIPIENTS;"
    df = get_data(query_str)
    return df

if __name__ == '__main__':
    logging.basicConfig(level=logging.CRITICAL)
    df = load_data()
    main(df)
