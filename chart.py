import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




st.markdown("## Bar Chart")
chart_data = pd.DataFrame(
    np.random.randn(10,3),
    columns=["a","b","c"]
)

st.markdown("## Line Chart")
st.line_chart(chart_data)


st.markdown("## Area Chart")
st.area_chart(chart_data)


st.markdown("## Bar Chart")
st.bar_chart(chart_data)




import plotly.figure_factory as ff
# Histogram Data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

hist_data = [x1, x2, x3]
group_labels = ['Group 1', 'Group 2', 'Group 3']

fig = ff.create_distplot(
    hist_data,
    group_labels,
    bin_size=[0.1, 0.5, 0.2]
)

st.subheader("Distribution Plot")
st.plotly_chart(fig, use_container_width=True)




st.subheader("Pydeck Chart")
import pydeck as pdk

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.pydeck_chart(pdk.Deck(
     map_style='mapbox://styles/mapbox/light-v9',
     initial_view_state=pdk.ViewState(
         latitude=37.76,
         longitude=-122.4,
         zoom=11,
         pitch=50,
     ),
     layers=[
         pdk.Layer(
            'HexagonLayer',
            data=df,
            get_position='[lon, lat]',
            radius=200,
            elevation_scale=4,
            elevation_range=[0, 1000],
            pickable=True,
            extruded=True,
         ),
         pdk.Layer(
             'ScatterplotLayer',
             data=df,
             get_position='[lon, lat]',
             get_color='[200, 30, 0, 160]',
             get_radius=200,
         ),
     ],
 ))




st.subheader("GraphViz Chart")

import graphviz as graphviz
st.graphviz_chart('''
    digraph {
        run -> intr
        intr -> runbl
        runbl -> run
        run -> kernel
        kernel -> zombie
        kernel -> sleep
        kernel -> runmem
        sleep -> swap
        swap -> runswap
        runswap -> new
        runswap -> runmem
        new -> runmem
        sleep -> runmem
    }
''')




st.subheader("MAP : Dhaka, Bangladesh")

df = pd.DataFrame(
     np.random.randn(1000, 2) / [50, 50] + [23.8103, 90.4125],
     columns=['lat', 'lon'])

st.map(df)