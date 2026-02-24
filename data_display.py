import streamlit as st
import pandas as pd
import numpy as np


st.markdown("## Display 10 rows and 5 columns of random data")
df=pd.DataFrame(
    
    np.random.randn(10, 5),
    columns=('col %d' % i for i in range(5))
)
st.table(df)



st.markdown("## Display Single Cart")
st.metric(label="Temparature", value="70 F" , delta="1.2 F")


st.markdown("## Display Cart Series ")
st.metric(label="Temparature", value="70 F" , delta="1.2 F")
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 F", "1.2 F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")
