import streamlit as st
import pickle
import numpy as np

# Set UI title
st.title("Diabetes Prediction")

psngr_class = [1,2,3]
# user input

preg = st.slider("Pregnancies",min_value=0,max_value=17)
glu = st.slider("Glucose",min_value=0,max_value=199)
bp = st.slider("BloodPressure",min_value=0,max_value=122)
skt = st.slider("SkinThickness",min_value=0,max_value=99)
bmi = st.number_input("BMI",min_value=0.00,max_value=67.10)
dpg = st.number_input("DiabetesPedigreeFunction",min_value=0.00,max_value=2.42)
age = st.slider("Age",min_value=0,max_value=81)
ins = st.slider("Insulin",min_value=0,max_value=846)

with open("db_log_model.pkl",'rb') as f:
    model = pickle.load(f)

# Predict

if st.button("Predict"):
    input_data = np.array([[preg,glu,bp,skt,bmi,dpg,age,ins]])
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][prediction]

    if prediction == 1:
        st.success(f"Survived and probability {probability:2f}")
    else:
        st.error(f"Not Survived and probability {probability:2f}")
