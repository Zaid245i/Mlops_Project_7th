import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"  # Replace with the correct URL if needed

def signup():
    st.header("Signup")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Sign Up"):
        response = requests.post(f"{BASE_URL}/signup", json={"username": username, "password": password})
        if response.status_code == 200:
            st.success("User created successfully")
        else:
            st.error(response.json().get("detail"))

def login():
    st.header("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        response = requests.post(f"{BASE_URL}/login", json={"username": username, "password": password})
        if response.status_code == 200:
            st.success("Login successful")
            weather_app()
        else:
            st.error(response.json().get("detail"))

def weather_app():
    st.header("Weather Prediction")
    st.write("This is a simple weather prediction app that takes user input for weather parameters.")
    
    # Collect user inputs for the weather prediction
    location = st.text_input("Enter your location")
    temperature = st.number_input("Temperature (°C)", min_value=-50, max_value=50, value=25)
    humidity = st.slider("Humidity (%)", min_value=0, max_value=100, value=50)
    condition = st.selectbox("Weather Condition", ["Sunny", "Cloudy", "Rainy", "Snowy", "Windy"])

    if st.button("Predict Weather"):
        # Perform inference based on the inputs (using a hardcoded response here)
        st.write(f"Weather forecast for {location}:")
        st.write(f"Temperature: {temperature}°C")
        st.write(f"Humidity: {humidity}%")
        st.write(f"Condition: {condition}")
        st.success("Weather prediction complete!")

# Main logic
st.sidebar.title("Navigation")
app_mode = st.sidebar.selectbox("Choose the app mode", ["Login", "Signup"])

if app_mode == "Signup":
    signup()
elif app_mode == "Login":
    login()
