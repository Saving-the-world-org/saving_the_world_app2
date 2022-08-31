import logging
import streamlit as st
from src.utils.dataio import get_data
import streamlit.components.v1 as components
from src.utils.dataio import init_data

# Begin Streamlit calls
st.set_page_config(layout="wide")

def main(df):
    #Header information 
    st.title("System Settings", anchor=None)
    st.subheader("Configure database, users, etc.")
    #st.write("coming soon")

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


def load_data():
    query_str = "SELECT * FROM CITIES;"
    df = get_data(query_str)
    return df

if __name__ == '__main__':
    logging.basicConfig(level=logging.CRITICAL)
    df = load_data()
    main(df)


# # @st.cache
# def load_data():
#     query_str = "SELECT * FROM DONATIONS;"
#     df = get_data(query_str)
#     return df

# if __name__ == '__main__':
#     logging.basicConfig(level=logging.CRITICAL)
#     df = load_data()
#     main(df)