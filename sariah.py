import streamlit as st

# Set a fun, colorful title
st.markdown("<h1 style='text-align: center; color: #FF69B4;'>🌈 Fun Adding App for Toddlers 🌈</h1>", unsafe_allow_html=True)
st.write("<h3 style='color: #FFA500;'>Let's add two numbers together!</h3>", unsafe_allow_html=True)

# Input fields with emojis for a playful feel
first_number = st.number_input("💙 Enter the first number:", step=1, min_value=0)
second_number = st.number_input("💚 Enter the second number:", step=1, min_value=0)

# Button to perform the addition
if st.button("✨ Add Numbers ✨"):
    # Calculate the sum
    result = first_number + second_number
    # Display the result with a celebratory message and vibrant color
    st.markdown(f"<h2 style='color: #32CD32;'>🎉 The sum is: {result} 🎉</h2>", unsafe_allow_html=True)
