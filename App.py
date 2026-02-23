import streamlit as st
import random

st.set_page_config(page_title="Number Guessing Game", page_icon="🎯")

st.title("🎯 Number Guessing Game")
st.write("Try to guess the secret number!")

# Difficulty selection
difficulty = st.selectbox(
    "Choose difficulty:",
    ["Easy (1-50)", "Medium (1-100)", "Hard (1-500)"]
)

# Set max range based on difficulty
if difficulty == "Easy (1-50)":
    max_number = 50
elif difficulty == "Medium (1-100)":
    max_number = 100
else:
    max_number = 500

# Initialize session state
if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, max_number)
    st.session_state.attempts = 0
    st.session_state.game_over = False

# If difficulty changes, reset game
if st.session_state.secret_number > max_number:
    st.session_state.secret_number = random.randint(1, max_number)
    st.session_state.attempts = 0
    st.session_state.game_over = False

# User input
guess = st.number_input("Enter your guess:", min_value=1, max_value=max_number, step=1)

if st.button("Submit Guess") and not st.session_state.game_over:
    st.session_state.attempts += 1

    if guess < st.session_state.secret_number:
        st.warning("Too low! 📉")
    elif guess > st.session_state.secret_number:
        st.warning("Too high! 📈")
    else:
        st.success(f"Correct! 🎉 You guessed it in {st.session_state.attempts} attempts.")
        st.session_state.game_over = True

# Restart button
if st.session_state.game_over:
    if st.button("Play Again"):
        st.session_state.secret_number = random.randint(1, max_number)
        st.session_state.attempts = 0
        st.session_state.game_over = False
        st.rerun()
