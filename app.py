import streamlit as st
import pandas as pd
import numpy as np
import pickle
import requests

# Download the model file from Google Drive
url = "https://drive.google.com/file/d/1ZJHXjhfpul0tq5u5fuA0am4t_-65VvjA/view?usp=drive_link"
# Google Drive file ID
file_id = "1ZJHXjhfpul0tq5u5fuA0am4t_-65VvjA"
url = f"https://drive.google.com/uc?export=download&id={file_id}"

# Download the file
response = requests.get(url)
with open("final_project_model.pkl", "wb") as f:
    f.write(response.content)

# Load the model
with open("final_project_model.pkl", "rb") as f:
    model = pickle.load(f)
# Your Streamlit app code here
data=pd.read_csv("finalProjectData.csv")

#Create a title for the website
st.title("Car Price Prediction Website:")

#Create a selection box for the model/company make type
Model=st.selectbox("Model",data["Model"].unique())

#Create a selection box for the company
filtered_make_options = data[data["Model"] == Model]["Make"].unique()
Make = st.selectbox("Select Make", filtered_make_options)

#Input the year the car was made
YOM=st.number_input("Year the car was made")

#Used=>Whether foreign used or brandnew or  locally used
Used=st.selectbox("Used",data["Used"].unique())

#Transmission of the car
Transmission=st.selectbox("Car Transmission",data["Transmission"].unique())

#Car mileage
Mileage=st.number_input("Enter the mileage of the car")

#Location where the car is used
Location=st.selectbox("Location",data["Location"].unique())

#input the age of the car
Age=st.number_input("Age of the Car")

#input the fuel type the car consumes
Fuel_Type=st.selectbox("Fuel_type",data["Fuel_Type"].unique())

#Create the predict button
if st.button('Predict Price'):
    # [Model, Make, YOM, Used, Transmission, Mileage, Location, Age, Fuel_Type]

    prediction=int(model.predict(pd.DataFrame(columns=["Model","Make","YOM","Used","Transmission","Mileage","Location","Age","Fuel_Type"],
                             data=np.array([Model,Make,YOM,Used,Transmission,Mileage,Location,Age,Fuel_Type]).reshape(1,9))))
    
    st.title("The car price ranges between " +
             str(prediction - 20000) + " Ksh " + " - " + str(prediction +20000) + " Ksh " )








