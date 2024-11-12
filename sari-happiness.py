import streamlit as st
import random

# Define the function to calculate happiness probability
def happiness_probability(food, drink):
    """Predicts happiness probability based on food and drink choices."""
    # Assign happiness scores to food and drink options
    food_scores = {
        "Pizza": 0.8,
        "Salad": 0.6,
        "Burger": 0.7,
    }

    drink_scores = {
        "Water": 0.5,
        "Juice": 0.7,
        "Soda": 0.6,
    }

    # Get scores, defaulting to 0.5 if not found
    food_score = food_scores.get(food, 0.5)
    drink_score = drink_scores.get(drink, 0.5)

    # Calculate happiness with a random element
    happiness = (food_score + drink_score) / 2 + random.uniform(-0.1, 0.1)

    # Ensure happiness is within [0, 1]
    return max(0, min(1, happiness))

# Streamlit App Design
st.markdown("<h1 style='text-align: center; color: #FF4500;'>🍕 Happiness Predictor 🍹</h1>", unsafe_allow_html=True)
st.write("<h3 style='color: #4682B4;'>Choose your favorite food and drink, and we'll predict your happiness level!</h3>", unsafe_allow_html=True)

# Dropdowns for food and drink choices
food_choice = st.selectbox("Choose your food:", ["Pizza", "Salad", "Burger"])
drink_choice = st.selectbox("Choose your drink:", ["Water", "Juice", "Soda"])

# Button to calculate happiness probability
if st.button("Predict Happiness"):
    probability = happiness_probability(food_choice, drink_choice)
    st.markdown(f"<h2 style='color: #32CD32;'>😊 The probability of you being happy tomorrow is: {probability:.2f}</h2>", unsafe_allow_html=True)
