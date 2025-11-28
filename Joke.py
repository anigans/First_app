# File: app.py
# Purpose: A tiny Streamlit app that makes kid-friendly jokes.
# How to run: streamlit run app.py

import random
import streamlit as st

# ----- 1) PAGE SETUP -----
st.set_page_config(page_title="Kid Joke Generator", page_icon="🎈", layout="centered")
st.title("🤣 Kid-Friendly Joke Generator")
st.caption("Type a topic or pick a category, then press the button for a silly, clean joke!")

# Keep favorites in memory while the app runs
if "favorites" not in st.session_state:
    st.session_state.favorites = []

# ----- 2) SIMPLE WORD BANKS (used to fill in joke templates) -----
CATEGORIES = {
    "Animals": ["cat", "dog", "elephant", "monkey", "cow", "penguin", "lion"],
    "School": ["teacher", "homework", "backpack", "pencil", "class", "principal", "bus"],
    "Space": ["rocket", "moon", "astronaut", "planet", "star", "meteor", "spaceship"],
    "Food": ["pizza", "banana", "broccoli", "cookie", "sandwich", "pancake", "carrot"],
    "Sports": ["soccer", "basketball", "tennis", "baseball", "skateboard", "swimming", "running"]
}

EMOJIS = ["😂", "😄", "🤪", "🤣", "😹", "🎉", "🌟", "🚀", "🍕", "🐒"]

# Joke templates: we’ll fill {thing} or {thing2} with words from the lists
TEMPLATES_QA = [
    "Q: Why did the {thing} cross the road?\nA: To prove it wasn’t chicken!",
    "Q: What do you call a {thing} that tells jokes?\nA: A pun-dit!",
    "Q: Why did the {thing} go to school?\nA: To get a little brighter!",
    "Q: What do you call a {thing} on a {thing2}?\nA: Fast and curious!"
]

TEMPLATES_ONELINER = [
    "My {thing} told me a secret… but it was too cheesy 🧀",
    "I tried to high-five a {thing}, but it only gave me a low-two!",
    "Never trust a {thing} with your snacks… it always takes a bite first!",
    "That {thing} is so cool, even the {thing2} asked for an autograph!"
]

TEMPLATES_RIDDLE = [
    "Riddle: I’m round, I shine, and astronauts love me. What am I? (Hint: not a cookie!)",
    "Riddle: I have a ring but no finger. What am I? (Think… space!)",
    "Riddle: What gets wetter the more it dries? (Not a {thing}, but it’s in your bathroom!)",
    "Riddle: I’m full of holes but I still hold water. What am I? (A sponge, but don’t tell!)"
]

# ----- 3) SIDEBAR CONTROLS -----
st.sidebar.header("Make your joke")
category = st.sidebar.selectbox("Pick a category", list(CATEGORIES.keys()), index=0)
custom_topic = st.sidebar.text_input("Or type your own topic (optional)", placeholder="e.g., unicorns, robots, dinosaurs")
style = st.sidebar.radio("Joke style", ["Q&A", "One-liner", "Riddle"], index=0)
add_emoji = st.sidebar.checkbox("Add emojis", value=True)

# ----- 4) BUILD A JOKE -----
def make_joke(category_name: str, style_name: str, topic_override: str | None) -> str:
    """Pick a template and fill it with words from the chosen category or the custom topic."""
    # Choose the word source
    words = CATEGORIES.get(category_name, ["thing"])
    thing = (topic_override.strip().lower() if topic_override else random.choice(words))
    thing2 = random.choice(words)

    # Select a template list based on style
    if style_name == "Q&A":
        template = random.choice(TEMPLATES_QA)
    elif style_name == "One-liner":
        template = random.choice(TEMPLATES_ONELINER)
    else:
        template = random.choice(TEMPLATES_RIDDLE)

    # Fill placeholders
    joke = template.format(thing=thing, thing2=thing2)

    # Optionally sprinkle emojis
    if add_emoji:
        joke = f"{random.choice(EMOJIS)} {joke} {random.choice(EMOJIS)}"

    return joke

col1, col2 = st.columns(2)
with col1:
    if st.button("Tell me a joke! 🎉", use_container_width=True):
        joke = make_joke(category, style, custom_topic)
        st.success(joke)

        # Show a save button for the most recent joke
        st.session_state.last_joke = joke

with col2:
    # Save last joke to favorites
    if st.button("⭐ Save last joke", use_container_width=True):
        last = st.session_state.get("last_joke")
        if last:
            st.session_state.favorites.append(last)
            st.toast("Saved to favorites!", icon="⭐")
        else:
            st.warning("No joke yet. Press 'Tell me a joke!' first.")

# ----- 5) FAVORITES LIST -----
st.divider()
st.subheader("⭐ Favorites")
if st.session_state.favorites:
    for i, j in enumerate(st.session_state.favorites, start=1):
        st.markdown(f"**{i}.** {j}")
else:
    st.caption("No favorites yet. Save one you like!")
