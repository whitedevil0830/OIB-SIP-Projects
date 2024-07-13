import numpy as np, streamlit as st
from Prediction import pred

st.title("Car Price Prediction")
col1, col2 = st.columns(2)
with col1:
    yr = st.selectbox("Year", options=[2003, 2004, 2005, 2006, 2007, 2008, 2009, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018])
    pp = st.select_slider("Present Price (in lakhs)", options= np.arange(start=0.3, stop=23, step=0.01))
    dkms = st.select_slider("Driven kms", options= np.arange(start=500, stop=100000, step=0.1))
    ft = st.selectbox("Fuel Type", options=['Petrol', 'Diesel', 'CNG'])
with col2:
    St = st.selectbox("Selling Type", options=["Dealer", "Indivisual"])
    tran = st.selectbox("Transmission", options=['Manual', 'Automatic'])
    Owner = st.selectbox("Number of Previous Owners", options=[0, 1, 3])

if ft == "Petrol":
    ft = 0
elif ft == "Diesel":
    ft = 1
else:
    ft = 2
    
St = 0 if St == "Dealer" else 1

tran = 0 if tran == "Manual" else 1

Selling_Price = pred(yr, pp, dkms, ft, St, tran, Owner)
st.write("")
st.write("")
st.write("")
cont = st.container(border=True, )
with cont:
    st.write("Selling Price (in Lakhs):", Selling_Price)