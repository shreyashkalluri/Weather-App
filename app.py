import requests
import streamlit as st   # to secure the API key we use/create .env file envirnoment file( hidden files are start with dot(.))
from dotenv import load_dotenv   # dont share .env file on github 
import os                     

load_dotenv()                         # step 1)to fetch the .env file intall ( pip install python-dotenv) in terminal
                                     # step 2) then this step from dotenv import load_dotenv 
                                     # step 3)load_dotenv()  it loads internally
                                     # step 4)os.getenv("paste api variable name here from .env file")

API_KEY = os.getenv("WEATHER_API_KEY")
# for title create thrugh streamlit
# how to run in terminal - streamlit run app.py 
st.set_page_config(
    page_title="Weather App",
    page_icon="⛅",

)


st.title("⛅Weather App")
st.write("Enter the city name and click the button to fetch the weather data")
city = st.text_input("Enter the city Name")

API_URL =f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"


# when ever button is clicked st.button will return true then we call API
if st.button("click to get data"):
    response = requests.get(API_URL) # used to get api
    if response.status_code == 200:
        st.success("Weather Data Fetched Successfully!")
        data = response.json() #fetching data

        
        name = data["name"]
        country = data["sys"]["country"]
        
        st.subheader(f"{name},{country}")

        temperature = data["main"]["temp"] # fetching data from the json on web page (nested dictionary indexing)
        speed = data["wind"]["speed"]
        weather = data["weather"][0]["main"]
        humidity = data["main"]["humidity"]


        col1,col2,col3,col4 = st.columns(4)
        col1.metric("Temperature",f"🌡️{temperature}°C")# 1st variable str is for display and variable
        col2.metric("Wind Speed",f"🍃{speed}m/s")          
        col3.metric("Weather",f"{weather}")   
        col4.metric("Humidity",f"💧{humidity}%")       
    else:
        st.error("Please enter a valid city name!")