import streamlit as st

from frontend.controller.get_doc_title_controller import get_title

SESSION_KEY = 'title_result'

if SESSION_KEY not in st.session_state:
    st.session_state[SESSION_KEY] = ''


def list_title_callback():
    st.session_state[SESSION_KEY] = get_title()


st.title('List doc titles')

placeholder = st.empty()
with placeholder:
    text = st.text_area('Output', key=SESSION_KEY)


st.button('List doc titles', on_click=list_title_callback)
