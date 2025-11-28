import streamlit as st
import random
from datetime import datetime   # 👈 to get the current time

# --- PAGE SETUP ---
st.set_page_config(page_title="Anitha's App", page_icon="😊")

# --- TITLE & INTRO ---
st.title("😊 Anitha's App")
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

# --- FAVORITE COLOR PICKER ---
st.subheader("🎨 Choose Your Favorite Color")
fav_color = st.color_picker("Pick a color you like:", "#00BFFF")  # Default is light blue
st.write(f"Your favorite color is: {fav_color}")

# --- SPACER LINE ---
st.divider()

# --- VEGETARIAN QUICK BREAKFAST RECIPE SECTION ---
st.subheader("🥣 Quick Vegetarian Breakfast Recipe")

RECIPES = [
    {
        "name": "Avocado Toast",
        "ingredients": "Whole-grain bread, ripe avocado, salt, pepper, lemon juice.",
        "instructions": "Toast bread, mash avocado, spread on toast, season, and enjoy!"
    },
    {
        "name": "Vegetable Upma",
        "ingredients": "Rava/semolina, onion, carrots, peas, mustard seeds, curry leaves.",
        "instructions": "Roast rava, sauté veggies, add water, cook until fluffy."
    },
    {
        "name": "Fruit Yogurt Parfait",
        "ingredients": "Greek yogurt, mixed fruits, honey, granola.",
        "instructions": "Layer yogurt, fruits, and granola; drizzle honey on top."
    },
    {
        "name": "Besan Chilla",
        "ingredients": "Chickpea flour, onion, tomato, coriander, spices.",
        "instructions": "Mix ingredients with water, pour on pan, cook like a pancake."
    },
    {
        "name": "Oats Porridge",
        "ingredients": "Rolled oats, milk, sugar or honey, nuts, and fruits.",
        "instructions": "Cook oats in milk, top with fruits and nuts."
    },
]

if "last_recipe" not in st.session_state:
    st.session_state.last_recipe = None

if st.button("🥗 Show Today's Recipe"):
    choices = RECIPES.copy()
    if st.session_state.last_recipe in choices:
        choices.remove(st.session_state.last_recipe)
    recipe = random.choice(choices)
    st.session_state.last_recipe = recipe

    # Styled box for recipe using user's favorite color
    st.markdown(
        f"""
        <div style="background-color:{fav_color}; padding:15px; border-radius:10px">
            <h4>🌿 {recipe['name']}</h4>
            <b>Ingredients:</b> {recipe['ingredients']}<br>
            <b>Instructions:</b> {recipe['instructions']}
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    st.info("Click the button to see a quick vegetarian breakfast recipe!")

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
