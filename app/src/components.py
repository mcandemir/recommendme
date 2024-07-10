"""
this is where you define your components
every component is a piece of row of your application
"""


import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
from src import callbacks
from src import utils


def component_home_button():
    st.button('Home', on_click=callbacks.set_page_home)


def component_say_hello():
    """
    example component with a home button and header
    """
    st.markdown('# Welcome to RecommendMe!')


def component_change_page():
    """
    example component with a page selection
    """
    st.markdown('##### RecommendMe is a tool that allows you to get movie recommendations based on your taste.')


def component_input_box():
        cols = st.columns([0.6, 0.2, 0.2])
        
        with cols[0]:
            st.write("")
            st.session_state['input'] = st.text_input('input', label_visibility='hidden')

        with cols[1]:
            st.write("#####")
            st.button('Add', use_container_width=True, on_click=callbacks.add_input_item_to_list)
        
        with cols[2]:
            st.write("#####")
            st.button('Remove', use_container_width=True, on_click=callbacks.clear_input_list)


def component_input_list():
    for i in st.session_state['input_list']:
        st.markdown(f"- {i}")


def component_vertical_space(n=1):
    for i in range(n):
        add_vertical_space()


def component_recommend_button():
    st.markdown(
        """
        <style>
        button {
            height: auto;
            margin-top: 1px !important;
            padding-top: 8px !important;
            padding-bottom: 8px !important;
            padding-left: 35px !important;
            padding-right: 35px !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


    cols = st.columns(3)
    with cols[1]:
        st.button('Get Recommendations', on_click=callbacks.set_state_recommend)


def component_recommendations():
    if st.session_state['recommend']:
        
        with st.status('Creating awesome-personalized recommendations.. Hold tight!', expanded=True):
            st.session_state['openai_responses'] = utils.fetch_openai_data()
            st.session_state['omdb_responses'] = utils.fetch_omdb_data()

        with st.container(height=1200):
            for i in range(10):

                # if st.session_state['omdb_responses'][i]['Response'] == 'False':
                #     st.warning(f'movie {st.session_state["input_list"][i]} not found')                

                with st.container():
                    st.image(st.session_state['omdb_responses'][i]['Poster'])
                    st.write(st.session_state['openai_responses'][i]['title'])
                    st.write(st.session_state['openai_responses'][i]['desc'])

                    
            st.session_state['recommend'] = False
    
    else:
        st.markdown('#### Waiting for your awesom-favorite movies..')

    

