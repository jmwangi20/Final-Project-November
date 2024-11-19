import streamlit as st
import pandas as pd
import numpy as np
import pickle
import zipfile

# Path to your zipped model file
zipped_file_path = 'Final_Project_model.zip'

# Open the zipped file and load the model
with zipfile.ZipFile(zipped_file_path, 'r') as zip_ref:
    # Locate the specific file within the zip
    with zip_ref.open('random_forest_model.pkl') as f:
        loaded_rf_model = pickle.load(f)
# model=joblib.load(open('Final_Project_model.zip','rb'))

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

    prediction=int(loaded_rf_model.predict(pd.DataFrame(columns=["Model","Make","YOM","Used","Transmission","Mileage","Location","Age","Fuel_Type"],
                             data=np.array([Model,Make,YOM,Used,Transmission,Mileage,Location,Age,Fuel_Type]).reshape(1,9))))
    print("Hello world")
    st.title("The car price ranges between " +
             str(prediction - 20000) + " Ksh " + " - " + str(prediction +20000) + " Ksh " )








