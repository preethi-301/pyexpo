import streamlit as st
import random

# Title of the app
st.title('Number Guessing Game')

# Game instructions
st.write("""
    Welcome to the Number Guessing Game!
    I am thinking of a number between 1 and 100.
    Try to guess it!
""")

# Generate a random number
if 'secret_number' not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.guesses = 0
    st.session_state.game_over = False

# Handle guesses
if not st.session_state.game_over:
    guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

    if st.button("Submit Guess"):
        st.session_state.guesses += 1

        if guess < st.session_state.secret_number:
            st.write("Too low! Try again.")
        elif guess > st.session_state.secret_number:
            st.write("Too high! Try again.")
        else:
            st.write(f"Congratulations! You guessed the number {st.session_state.secret_number} in {st.session_state.guesses} attempts.")
            st.session_state.game_over = True

# Button to restart the game
if st.session_state.game_over:
    if st.button("Play Again"):
        st.session_state.secret_number = random.randint(1, 100)
        st.session_state.guesses = 0
        st.session_state.game_over = False
        st.write("The game has been reset! Try again.")
        

