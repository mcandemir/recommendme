"""
this is where you define your callbacks
"""


import streamlit as st


def set_page_home():
    """
    example callback that will set the selected page to 'home'
    """
    st.session_state['selected_page'] = 'home'


def set_state_recommend():
    st.session_state['recommend'] = True


def add_input_item_to_list():
    st.session_state['input_list'].append(st.session_state['input'])


def clear_input_list():
    try:
        st.session_state['input_list'].pop()
    except IndexError:
        st.info('Your list is empty!')

    
    








