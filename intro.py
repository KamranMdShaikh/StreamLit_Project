# import necessay modules
import streamlit as st 
import pandas as pd 
import numpy as np


### Add title
st.title("Hello Welcome Title")

### Add header
st.header("Hello Welcome header")


### Add subheader
st.subheader("Hello Welcome sub-header")


### Data

Data ={
    "Student":["Mr.A","Mr.B","Mr.C","Mr.D","Mr.E"],
    "CGPA":[3.22,3.33,3.27,3.60,3.77],
    "Favourite Subject":["English","Physics","Botany","Mathematics","Statistics"]      
}


######### Play with markdown and data
st.markdown("# Play With Data")


st.markdown("### RAW Data")
st.write(Data)

st.markdown("### Converting to DataFrame")
st.write(pd.DataFrame(Data))