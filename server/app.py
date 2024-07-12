import streamlit as st
import util

# Load saved artifacts
util.load_saved_artifacts()

# Function to predict home price
def predict_home_price(location, sqft, bedrooms, bath):
    estimated_price = util.get_estimated_price(location, sqft, bedrooms, bath)
    return estimated_price

# Streamlit app
st.title("Home Price Prediction")

# Select location
locations = util.get_location_names()
location = st.selectbox("Select Location", locations)

# Input features
sqft = st.number_input("Square Feet", min_value=0, step=1)
bedrooms = st.number_input("Bedrooms", min_value=0, step=1)
bath = st.number_input("Bathrooms", min_value=0, step=1)

# Predict button
if st.button("Predict"):
    try:
        estimated_price = predict_home_price(location, sqft, bedrooms, bath)
        st.success(f"The estimated price is {estimated_price} lakh (INR)")
    except Exception as e:
        st.error(f"Error: {str(e)}")
