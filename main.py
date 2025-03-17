import streamlit as st
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


st.title("Risk Prediction for Atrial Fibrilation")

st.write("Development of an _AI-driven application_ that predicts a person's AF risk based on health data, enabling individuals and healthcare providers to take _proactive measure for better cardiovascular health_.")

st.divider()
pressed_1 = st.button("New Patient")
pressed_2 = st.button("Existing Patient")
print("First:", pressed_1, "Second:", pressed_2)

form_values  =  {
    "patientid" : None,
    "gender" : None,
    "age" : None,
    "heartrate" : None,
    "hypertension" : None,
    "diabetes" : None,
    "vmedications" : None
}

#Form for interactive element 
with st.form(key = "user_history"):
    form_values["patientid"] = st.text_input("Enter the Patient ID")

    form_values["gender"] = st.selectbox("Select the gender",['Male','Female','Other'])

    form_values["age"] = st.number_input("Enter the age")

    form_values["heartrate"] = st.select_slider("Select a hearbeat range", options= np.arange(60,120,1).tolist())

    form_values["hypertension"] = st.radio("Hypertension",['Yes','No'])

    form_values["diabetes"] = st.radio("Diabetes",['Yes','No'])

    form_values["medications"] = st.multiselect("List of medications currently undertaking", ['Anti-arrhythmic','ACE/ARB/Entresto','Beta blocker','Heart failure','Calcium channel blocker','Digoxin','Myosin inhibitors / negative inotropes','Amyloid therapeutics'])

    submit_button = st.form_submit_button(label = "Submit")
    if submit_button:
        if not all(fom_values.values()):
            st.warning("Please fill in all of the fields")
        else:
            st.write("Values successfully entered")




st.image(os.path.join(os.getcwd(), "streamlit", "bg.jfif"))


data = {
    'Tracking': ['000XpPEDHZ', '0089QvLYpD', '009OdzZUzb', '00AkCj8EF2', '00CBjJ6vTV',
                 '00CILYM7QO', '00Gq4umBKd', '00KcspgCzd', '00Qxfoo9Z9'],
    'Age': [51, 64, 61, 46, 75, 69, 42, 53, 36],
    'Sex': [2, 1, 1, 1, 2, 1, 2, 1, 1],
    'Hypertension': [0, 0, 0, 0, 0, 0, 0, 0, 0],
    'Diabetes': [0, 0, 0, 0, 0, 0, 0, 1, 0],
    'Dyslipidemia': [1, 1, 1, 1, 0, 0, 0, 1, 1],
    'Dilated_cardiomyopathy': [0, 0, 0, 0, 0, 0, 0, 0, 0],
    'Hypertrophic_cardiomyopathy': [0, 0, 0, 0, 0, 0, 0, 0, 0],
    'Arrhythmogenic_cardiomyopathy': [0, 0, 0, 0, 0, 0, 0, 0, 0]
}

chart_data = pd.DataFrame(data)

st.dataframe(chart_data)
editable_df = st.data_editor(chart_data)

st.line_chart(chart_data['Age'])
st.bar_chart(chart_data['Age'])

fig, ax = plt.subplots()
ax.plot(chart_data['Age'])
ax.set_title("Pyplot line chart")
st.pyplot(fig)