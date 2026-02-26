import streamlit as st
import pandas as pd
import numpy as np


st.markdown("## Button")
st.button("Non Functional Button")

if st.button("Functioanl Button"):
    st.write("Before pressing button")
else:
    st.write("After pressing button")




st.markdown("## Check Box")
agree = st.checkbox(" i agree with the terms and conditions")

if agree:
    st.write("You have agreed with the terms and conditions")
else:
    st.write("You have not agreed with the terms and conditions")
 
 
 
st.markdown("## Radio Button")
genre = st.radio(
     "What's your favorite movie genre",
     ('Comedy', 'Drama', 'Documentary'))

if genre == 'Comedy':
     st.write('You selected comedy.')
if genre == 'Drama':
     st.write('You selected drama.')
if genre == 'Documentary':
     st.write('You selected documnetary.')          
# else:
#      st.write("You didn't select comedy.")



st.markdown("## Select Box")
option = st.selectbox(
     'How would you like to be contacted?',
     ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)
