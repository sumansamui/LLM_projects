import json
import requests
import streamlit as st
from streamlit_lottie import st_lottie

# Import your custom modules
from text_to_text import translate
from Medi_talk_ollama import get_answer

# Constants
LOTTIE_URL = 'https://lottie.host/97b3731e-68ac-4429-83d0-d2b5fc3d145e/DpFQUzOmYL.json'

language_codes = {
    "English": "en",
    "Hindi": "hi",
    "Bengali": "bn",
    "Spanish": "es",
    "Chinese (Simplified)": "zh-CN",
    "Russian": "ru",
    "Japanese": "ja",
    "Korean": "ko",
    "German": "de",
    "French": "fr",
    "Tamil": "ta",
    "Telugu": "te",
    "Kannada": "kn",
    "Gujarati": "gu",
    "Punjabi": "pa"
}

def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return
    return r.json()

# Page setup
lottie_anim = load_lottie(LOTTIE_URL)
st.set_page_config(page_title="MediTalk - Medical Assistant Chatbot", page_icon='', layout='centered')

# Initialize session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

if 'user_lang' not in st.session_state:
    st.session_state.user_lang = 'en'

# Sidebar: Language selection and clear button
st.sidebar.subheader("Select User Language")
st.session_state.user_lang = st.sidebar.selectbox("Choose Language", list(language_codes.keys()))

if st.sidebar.button("🧹 Clear Chat History"):
    st.session_state.chat_history = []

# UI Header and Animation
with st.container():
    left, right = st.columns([2, 3])
    with left:
        st_lottie(lottie_anim, height=300, key='coding')
    with right:
        st.subheader('Hi, I am MediTalk - Medical Assistant Chatbot!')
        st.write("Type your health-related question below and click 'Submit'.")

# Text prompt input (no key used to avoid session_state write conflicts)
prompt_input = st.text_area("Your Question:", height=100)
submit = st.button("Submit")

# Handle user submission
if submit and prompt_input.strip():
    submitted_prompt = prompt_input.strip()

    # Translate to English if needed
    tran_prompt_text = translate(submitted_prompt, "English") if st.session_state.user_lang != "English" else submitted_prompt

    # Get response from Ollama model
    response = get_answer(tran_prompt_text)
    json.dump({"response": response}, open('response.json', 'wt'))

    # Translate response back to user language if necessary
    tran_response = translate(response, st.session_state.user_lang) if st.session_state.user_lang != "English" else response

    # Save to history
    st.session_state.chat_history.append((submitted_prompt, tran_response))

# Display chat history
with st.container():
    st.write('---')
    st.markdown("### 💬 Chat History")

    for i, (q, r) in enumerate(st.session_state.chat_history):
        st.markdown(f"**You:** {q}")
        lines = r.split('.')
        for line in lines:
            if line.strip():
                st.markdown(f"- {line.strip()}")
        st.write("")  # Add spacing between entries
