import os
from requests import Response
import streamlit as st
import requests
import datetime
import time
from openai import OpenAI


OMDB_API_KEY = os.environ['OMDB_API_KEY']
OPENAI_API_KEY = os.environ['OPENAI_API_KEY']


def fetch_omdb_data() -> list[dict]:
    omdb_responses = []
    progress_bar = st.progress(0, text='Fetching awesome posters..',)
    for i in range(len(st.session_state['openai_responses'])):
        title = st.session_state['openai_responses'][i]['title']
        title = title.replace(' ', '+')
        r = send_request_to_omdb_api(title)
        omdb_responses.append(r.json())
        progress_bar.progress(i * 10, text=f'Fetching awesome posters.. ({i}/{len(st.session_state["openai_responses"])})')
        time.sleep(1.2)
    progress_bar.empty()
    return omdb_responses


def send_request_to_omdb_api(omdb_api_title) -> Response:
    r = requests.request(
        method='GET',
        url=f'http://www.omdbapi.com/?t={omdb_api_title}&apikey={OMDB_API_KEY}'
    )
    return r


def fetch_openai_data() -> dict:
    client = OpenAI()
    content = "Recommend me 10 movies similar to following movies and tell me why you recommend them: "

    for item in st.session_state['input_list']:
        content += item

    completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": content,
            }
        ],
        model="gpt-3.5-turbo",
    )
    completion_text = completion.choices[0].message.content

    completion_texts = completion_text.split('\n')
    completion_texts = [i for i in completion_texts if i != ''] 

    openai_responses = {}
    for i, text in enumerate(completion_texts):
        desc = text[text.find('-') + 2:]
        title = text[:text.find('-') - 1]
        title = title[title.find(' ') + 1:]
        try:
            openai_responses[i] = {'title': title, 'desc': desc}
        except:
            st.warning('There was an error 🥺 Please make sure you give the right movie names..')

    with open('logs/favorite_movies.txt', 'a') as f:
        f.write(datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
        f.write('\n')
        f.writelines(st.session_state['input_list'])
        f.write('\n\n\n')

    with open('logs/openai_responses.txt', 'a') as f:
        f.write(datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
        f.write('\n')
        f.write(completion_text)
        f.write('\n\n\n')
    
    return openai_responses
