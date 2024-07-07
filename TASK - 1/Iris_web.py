import streamlit as st, numpy as np
from Prediction import pred

st.title("Flower Species Prediction")
st.write("")
c1, c2 = st.columns(2)

Range = np.arange(1, 10, 0.1)

with c1:
    st.subheader("Data for Sepal: ")
    st.write("")
    sl = st.select_slider("Enter the values of Sepal Length: ", options=Range)
    sw = st.select_slider("Enter the values of Sepal Width: ", options=Range)

with c2: 
    st.subheader("Data for Petal: ")
    st.write("")
    pl = st.select_slider("Enter the values of Petal Length: ", options=Range)
    pw = st.select_slider("Enter the values of Petal Width: ", options=Range)

st.subheader("Result: ")
st.markdown(f"SPECIES: {pred(sl, sw, pl, pw)}")