import logging
import numpy as np
import pandas as pd

import streamlit as st
from src.utils.dataio import get_data
import streamlit.components.v1 as components
from sqlalchemy import inspect, create_engine

connection_string = 'sqlite:///./src/data/stw_data.db'
engine = create_engine(connection_string)
insp = inspect(engine)

cities_df = get_data("SELECT * FROM CITIES;")
# donors_df = get_data("SELECT * FROM DONORS;")
org_df = get_data("SELECT * FROM ORGANIZATIONS;")

def get_city_for_org(org_name): 
    city_name = org_df.loc[org_name, 'City']
    return city_name

def get_phone_for_org(org_name): 
    phone = org_df.loc[org_name, 'Phone number']
    #st.write(type(phone))
    if isinstance(phone, np.integer):
        phone = phone
    else:
        phone = phone[0]
    phone = str(phone)
    return phone

def get_cred_for_org(org_name): 
    cred = org_df.loc[org_name, 'Credibility rating(1-5)']
    if isinstance(cred, np.integer):
        cred = cred
    else:
        cred = cred[0]
    cred = str(cred)
    return cred


def main(df):
    #Header information 
    st.title("Organizations", anchor=None)
    # st.subheader("We work with a wide variety of NGOs providing access to funding resources.")
    # st.caption("Project 3 by Phoebe Gunter, Harry Oestreicher, Abhishek Banerjee, Gabriel Paganin, Gerald Cortright, Javier", unsafe_allow_html=False)
    # st.write(df)

    st.title("Explore Organizations")
    st.write("Available Organizations to Donate to")

    for i in org_df.index.drop_duplicates():
        col1, col2 = st.columns(2)
        with col1:
            city = get_city_for_org(i)
            st.subheader(i)
            if isinstance(city, str):
                st.write("City: " + city)
            else:
                st.dataframe(city)
            phone = get_phone_for_org(i)
            cred = get_cred_for_org(i)
            st.write("Phone Number: " + phone)
            st.write("Credibility Rating (out of 5): " + cred )

        with col2:
            # short_name = i.replace(" ", "")
            # url = "https://github.com/Saving-the-world-org/saving_the_world_app/blob/edcd26a335fe3c6e99f17cd194a5491f913be26d/images/" + short_name + ".png"
            # st.write(url)
            # st.image(url, caption = i)
            st.write("place holder for photos")



def load_data():
    query_str = "SELECT * FROM ORGANIZATIONS;"
    df = get_data(query_str)
    return df

if __name__ == '__main__':
    logging.basicConfig(level=logging.CRITICAL)
    df = load_data()
    main(df)
