"""
this is the main module where you set your initial sessions states
and navigate your page with respect to `selected_page` session state
"""

import streamlit as st
from src.pages import HomePage


# page config
st.set_page_config(page_title="My Project", layout="centered", initial_sidebar_state="collapsed")


# set session states
if 'selected_page' not in st.session_state:
    st.session_state['selected_page'] = 'home'

if 'input' not in st.session_state:
    st.session_state['input'] = ''

if 'input_list' not in st.session_state:
    st.session_state['input_list'] = []

if 'recommend' not in st.session_state:
    st.session_state['recommend'] = False

if 'omdb_responses' not in st.session_state:
    st.session_state['omdb_responses'] = ''

if 'openai_response' not in st.session_state:
    st.session_state['openai_responses'] = {}


# page navigation
match st.session_state['selected_page']:
    case 'home':
        HomePage.load_home_page()
