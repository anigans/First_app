import streamlit as st

# Set up your app
st.set_page_config(page_title="My First App", page_icon="🚀")

# Title of your app
st.title("🚀 Masalaplate")
st.write("Built by Abhi, Ani and Ashok with Python!")

# Get input from user
name = st.text_input("What's your name kanna?")

# Do something when button is clicked
if st.button("Say Hello"):
    if name:
        st.success(f"Hello {name}! Welcome to your app!")
    else:
        st.warning("Please enter your name kanna")

# Show some info
st.info("Keep building and improving this app! Step by Step...")
