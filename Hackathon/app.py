import streamlit as st 
import pickle
import numpy as np

# import the model
model = pickle.load(open('resampled_model.pkl', 'rb'))

df = pickle.load(open('df.pkl', 'rb'))
st.subheader(f"New Change 'Fire_Occurrence_Yes' Predictor")
st.markdown("")

# User inputs
BuildingHeightm = st.number_input("Building_Height_(m)", value=44)
NumberofFloors = st.number_input("Number_of_Floors", value=12)
NumberofPeopleRescued = st.number_input("Number_of_People_Rescued", value=24)
NumberofFireExtinguishers = st.number_input("Number_of_Fire_Extinguishers", value=6)
NumberofEmergencyExits = st.number_input("Number_of_Emergency_Exits", value=14)
NumberofFireAlarms = st.number_input("Number_of_Fire_Alarms", value=7)
TemperatureC = st.number_input("Temperature_(_C)", value=27.72)
Humidity = st.number_input("Humidity_(%)", value=0.69)
WindSpeedms = st.number_input("Wind_Speed_(m_s)", value=4.73)
Precipitationmm = st.number_input("Precipitation_(mm)", value=66.15)
repair = st.number_input("repair", value=0.0)
BuildingTypeIndustrial = st.number_input("Building_Type_Industrial", value=0)
BuildingTypeResidential = st.number_input("Building_Type_Residential", value=1)
TypeofFireElectrical = st.number_input("Type_of_Fire_Electrical", value=0)
TypeofFireNegligence = st.number_input("Type_of_Fire_Negligence", value=0)
FireScaleMedium = st.number_input("Fire_Scale_Medium", value=0)
FireScaleSmall = st.number_input("Fire_Scale_Small", value=1)
SprinklerSystemPresentYes = st.number_input("Sprinkler_System_Present_Yes", value=1)
ElectricalEquipmentInspectionConductedYes = st.number_input("Electrical_Equipment_Inspection_Conducted_Yes", value=0)
GasEquipmentInspectionConductedYes = st.number_input("Gas_Equipment_Inspection_Conducted_Yes", value=0)
# Create a NumPy array with user inputs
user_inputs = np.array([BuildingHeightm, NumberofFloors, NumberofPeopleRescued, NumberofFireExtinguishers,
                       NumberofEmergencyExits, NumberofFireAlarms, TemperatureC, Humidity, WindSpeedms,
                       Precipitationmm, repair, BuildingTypeIndustrial, BuildingTypeResidential,
                       TypeofFireElectrical, TypeofFireNegligence, FireScaleMedium, FireScaleSmall,
                       SprinklerSystemPresentYes, ElectricalEquipmentInspectionConductedYes,
                       GasEquipmentInspectionConductedYes]).reshape(1, -1)

# Make prediction
prediction = model.predict(user_inputs)

# Display the prediction
st.subheader("Prediction:")
st.write("The predicted 'Fire_Occurrence_Yes' value is:", prediction[0])

    