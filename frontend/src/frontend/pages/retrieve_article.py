import streamlit as st

from frontend.controller.retrieve_controller import retrive_doc

SESSION_KEY = 'retrieve_result'

if SESSION_KEY not in st.session_state:
    st.session_state[SESSION_KEY] = ''


def retrieve_callback():
    st.session_state[SESSION_KEY] = retrive_doc(doc_title)


st.title('Retrieve articles')

doc_title = st.text_input('Doc title')

placeholder = st.empty()
with placeholder:
    text = st.text_area('Output', key=SESSION_KEY)


st.button('Retrieve', on_click=retrieve_callback)
