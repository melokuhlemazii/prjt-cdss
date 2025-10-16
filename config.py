import streamlit as st
import pandas as pd
import numpy as np


total_patients=125

stock_data = pd.DataFrame({
    'Item' : ['Bandages','Syringes','gloves','Masks'],
    'Current_Stock' : [200,150,300,500],
    'Threshold' : [50,30,100,150]
})


active_cases=pd.DataFrame({
    'Patient ID' : [102,103,104,105],
    'Name' : ['John Doe','John Doe','Jane Smith','Bob Lee'],
    'Status' : ['Under Treatment','Under Treatment','Discharched','nder Treatment'],
})


treatment_recommendations=pd.DataFrame({
    'Patient ID' : [102,103,104,105],
    'Recommendation' : ['Increase Medication','Regular Monitoring','Discharge Soon','Discharge']    
})

st.title("Clinical Opeaaritions Dashboard")

st.header("Total Patients")
st.metric("Patients", total_patients)


st.header("Stock Alerts")
low_stock=stock_data[stock_data['Current_Stock'] < stock_data['Threshold']]
if not low_stock.empty:
    st.dataframe(low_stock)
else:
    st.write("No low stock alerts.")



st.header("Active Cases")
active_treatment=active_cases[active_cases['Status'] == 'Under Treatment']
st.dataframe(active_treatment)


st.header("Treatment Recommendations")
st.dataframe(treatment_recommendations)
