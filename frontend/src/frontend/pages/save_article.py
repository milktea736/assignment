import streamlit as st

from frontend.controller.save_controller import save_doc

SESSION_KEY = 'save_result'

if SESSION_KEY not in st.session_state:
    st.session_state[SESSION_KEY] = ''


def save_callback():
    st.session_state[SESSION_KEY] = save_doc(doc_title, doc_content)


st.title('Save articles')

doc_title = st.text_input('Doc title')
doc_content = st.text_area('Doc content', max_chars=2000)

placeholder = st.empty()
with placeholder:
    text = st.text_area('Output', key=SESSION_KEY)


st.button('Save', on_click=save_callback)
