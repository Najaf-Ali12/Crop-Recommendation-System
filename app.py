import pickle
import streamlit as st

with open('Crop_Recommendation_model.pkl', 'rb') as Crop_Recommendation_classifier:
    Crop_Recommendator = pickle.load(Crop_Recommendation_classifier)

st.markdown("<h1 class=title>Crop Recommendation System</h1>",unsafe_allow_html=True)
st.image("Crop Recommendation system image.jpg")

st.markdown(
    """
    <style>
    html, body, [data-testid="stAppViewContainer"] {
        background-color: wheat;
    }
    </style>
    """,
    unsafe_allow_html=True
)
with st.form(key="form"):
    st.write("Please provide the following data to get a crop recommended")
    nitrogen=st.number_input("Ratio of Nitrogen content(kg/hector) in soil",key='N',min_value=0)
    Phosphorous=st.number_input("Ratio of Phosphorous content(kg/hector) in soil",key='P',min_value=0)
    Potassium=st.number_input("Ratio of Potassium content(kg/hector) in soil",key='K',min_value=0)
    humidity=st.number_input("Humidity in percentage",key='Humidity')
    temperature=st.number_input("Temperature in degree celsius",key='C')
    ph=st.number_input("PH value of the soil",key='ph')
    rainfall=st.number_input("Rainfall in mm",key='rainfall')
    submitted=st.form_submit_button("Submit Data")
    if submitted:
        if not nitrogen or not Phosphorous or not Potassium or not temperature or not humidity or not ph or not rainfall:
            st.warning("Please provide full information")
        else:
            recommended_crop=Crop_Recommendator.predict([[nitrogen,Phosphorous,Potassium,temperature,humidity,ph,rainfall]])
            st.info("Based on the data provided,You are suggested to grow",recommended_crop)