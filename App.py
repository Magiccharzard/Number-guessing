import streamlit as st
import random

st.set_page_config(page_title="Number Guessing Game", page_icon="🎯")

st.title("🎯 Number Guessing Game")

# -------------------------
# Difficulty Selection
# -------------------------
difficulty = st.selectbox(
    "Select Difficulty",
    ["Easy (1-50)", "Medium (1-100)", "Hard (1-500)"]
)

if difficulty == "Easy (1-50)":
    max_number = 50
elif difficulty == "Medium (1-100)":
    max_number = 100
else:
    max_number = 500

st.write(f"Guess a number between **1 and {max_number}**")

# -------------------------
# Initialize Game State
# -------------------------
if "game_started" not in st.session_state:
    st.session_state.game_started = False

if "secret_number" not in st.session_state:
    st.session_state.secret_number = None

if "attempts" not in st.session_state:
    st.session_state.attempts = 0

if "game_over" not in st.session_state:
    st.session_state.game_over = False


# -------------------------
# Start Game Button
# -------------------------
if not st.session_state.game_started:
    if st.button("Start Game"):
        st.session_state.secret_number = random.randint(1, max_number)
        st.session_state.attempts = 0
        st.session_state.game_over = False
        st.session_state.game_started = True
        st.rerun()


# -------------------------
# Game Logic
# -------------------------
if st.session_state.game_started and not st.session_state.game_over:

    guess = st.number_input(
        "Enter your guess:",
        min_value=1,
        max_value=max_number,
        step=1
    )

    if st.button("Submit Guess"):
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


# -------------------------
# Restart Game
# -------------------------
if st.session_state.game_over:
    if st.button("Play Again"):
        st.session_state.game_started = False
        st.session_state.secret_number = None
        st.session_state.attempts = 0
        st.session_state.game_over = False
        st.rerun()
