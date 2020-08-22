import streamlit as st
import random

option = st.radio(
    'What would you like to be the limit',
    (2, 5, 10, 20, 50, 100, 500, 1000))

limit = st.number_input('Select your guess', min_value = 0, max_value = option, value= 0)
num = random.randint(0, option)

if st.button('Done'):
    if num == int(limit):
        st.success('Congrats, you got it correct!')
    else:
        st.error(f'Your Number was {limit}, but the Program guessed {num}')
