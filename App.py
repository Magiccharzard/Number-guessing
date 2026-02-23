import streamlit as st
import random

st.set_page_config(page_title="Number Guessing Game", page_icon="🎯")

st.title("🎯 Number Guessing Game")
st.write("Try to guess the secret number!")

# -----------------------
# Difficulty Selection
# -----------------------
difficulty = st.selectbox(
    "Choose difficulty:",
    ["Easy", "Medium", "Hard"]
)

# Set max range
if difficulty == "Easy":
    max_number = 50
elif difficulty == "Medium":
    max_number = 100
else:
    max_number = 500

st.write(f"Guess a number between **1 and {max_number}**")

# -----------------------
# Initialize session state
# -----------------------
if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, max_number)
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.session_state.current_difficulty = difficulty

# Reset game if difficulty changes
if st.session_state.current_difficulty != difficulty:
    st.session_state.secret_number = random.randint(1, max_number)
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.session_state.current_difficulty = difficulty

# -----------------------
# Game Logic
# -----------------------
guess = st.number_input(
    "Enter your guess:",
    min_value=1,
    max_value=max_number,
    step=1
)

if st.button("Submit Guess") and not st.session_state.game_over:
    st.session_state.attempts += 1

    if guess < st.session_state.secret_number:
        st.warning("Too low! 📉")
    elif guess > st.session_state.secret_number:
        st.warning("Too high! 📈")
    else:
        st.success(
            f"Correct! 🎉 You guessed it in {st.session_state.attempts} attempts."
        )
        st.session_state.game_over = True

# -----------------------
# Restart Button
# -----------------------
if st.session_state.game_over:
    if st.button("Play Again"):
        st.session_state.secret_number = random.randint(1, max_number)
        st.session_state.attempts = 0
        st.session_state.game_over = False
        st.rerun()
