import streamlit as st
import random

# --- PAGE SETUP ---
st.set_page_config(page_title="My App", page_icon="🚀")

# --- TITLE & INTRO ---
st.title("🚀 My First Streamlit App")
st.write("Built by me with Python!")

# --- USER INPUT ---
name = st.text_input("What's your name?")

# --- BUTTON 1: Say Hello ---
if st.button("Say Hello"):
    if name:
        st.success(f"Hello {name}! Welcome to your app!")
    else:
        st.warning("Please enter your name first")

# --- SPACER LINE ---
st.divider()

# --- THOUGHT FOR THE DAY SECTION ---
st.subheader("🌤️ Thought for the Day")

# A few sample thoughts (you can add more anytime)
THOUGHTS = [
    "Start with gratitude; it changes what comes next.",
    "Tiny steps, taken daily, move mountains.",
    "Be the reason someone smiles today.",
    "Do the next right small thing.",
    "Fall, breathe, rise—this is resilience.",
    "Progress beats perfection—show up once more.",
    "Attention is your superpower—aim it well."
]

# Save the last thought in session state so a new one appears each click
if "last_thought" not in st.session_state:
    st.session_state.last_thought = None

# Button 2: Get new thought
if st.button("✨ New Thought for the Day"):
    # Choose a random thought different from the last one
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
