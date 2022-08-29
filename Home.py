import os
import logging
import streamlit as st
from src.utils.dataio import init_data, get_data
import streamlit.components.v1 as components
from web3 import Web3
from dotenv import load_dotenv
load_dotenv()

contract_address = os.getenv("SMART_CONTRACT_ADDRESS")
contract_abi = os.getenv("ABI_PATH")
# st.write(f"Contract Address: {contract_address}")
# st.write(f"Contract ABI: {contract_abi}")

def main(df):
    # Page Header information
    st.title("Humanitarian Aid Supply Chain Tracker Tool", anchor=None)
    st.subheader("This app enabled you to safetly track donating and receiving aid products on a blockchain. ")
    st.caption("Project 3 by Phoebe Gunter, Harry Oestreicher, Abhishek Banerjee, Gabriel Paganin, Gerald Cortright, Javier", unsafe_allow_html=False)
    st.write(df)
    # st.table(df)

    # with st.sidebar.form(key ='Form1'):
        # user_word = st.text_input("Enter a keyword", "habs")    
        # select_language = st.radio('Tweet language', ('All', 'English', 'French'))
        # include_retweets = st.checkbox('Include retweets in data')
        # num_of_tweets = st.number_input('Maximum number of tweets', 100)
        # submitted1 = st.form_submit_button(label = 'Search Twitter 🔎')
        
    hvar = """
            <script>
                var elements = window.parent.document.querySelectorAll('.css-1q8dd3e')
                elements[0].innerText = 'reloaded';
                elements[0].disabled = true;
            </script>
            """
    btn =  st.button("Reload Database")
    if btn:
        init_data()
        components.html(hvar, height=0, width=0)

    return

# @st.cache
def load_data():
    query_str = "SELECT * FROM DONATIONS;"
    df = get_data(query_str)
    return df

if __name__ == '__main__':
    logging.basicConfig(level=logging.CRITICAL)
    df = load_data()
    main(df)