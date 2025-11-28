import streamlit as st
import random
from datetime import datetime   # 👈 to get the current time

# --- PAGE SETUP ---
st.set_page_config(page_title="Anitha's App", page_icon="😊")   # 👈 changed rocket to smiley

# --- TITLE & INTRO ---
st.title("😊 Anitha's App")   # 👈 changed rocket to smiley
st.write("Built by me with Python!")

# --- USER INPUT ---
name = st.text_input("What's your name?")

# --- BUTTON 1: Say Hello ---
if st.button("Say Hello"):
    if name:
        st.success(f"Hello {name}! Welcome to your app!")
    else:
        st.warning("Please enter your name first")

# --- NEW BUTTON: Show Current Time ---
if st.button("🕒 Show Current Time"):
    current_time = datetime.now().strftime("%I:%M:%S %p")
    st.info(f"⏰ The current time is: **{current_time}**")

# --- SPACER LINE ---
st.divider()

# --- THOUGHT FOR THE DAY SECTION ---
st.subheader("🌤️ Thought for the Day")

THOUGHTS = [
    "Start with gratitude; it changes what comes next.",
    "Tiny steps, taken daily, move mountains.",
    "Be the reason someone smiles today.",
    "Do the next right small thing.",
    "Fall, breathe, rise—this is resilience.",
    "Progress beats perfection—show up once more.",
    "Attention is your superpower—aim it well."
]

if "last_thought" not in st.session_state:
    st.session_state.last_thought = None

if st.button("✨ New Thought for the Day"):
    choices = THOUGHTS.copy()
    if st.session_state.last_thought in choices:
        choices.remove(st.session_state.last_thought)
    thought = random.choice(choices)
    st.session_state.last_thought = thought
    st.success(thought)
else:
    st.info("Click the button to get your Thought for the Day!")

# --- FOOTER MESSAGE ---
st.divider()
st.info("Keep building and improving this app!")
