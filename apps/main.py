import streamlit as st
import pandas as pd
import numpy as np
import folium
from streamlit_folium import folium_static


map_data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50],
    columns=['lat', 'lon']
)
 
st.map(map_data)


x = 0

import time

if st.button("ダウンロード"):
    text = st.empty()
    bar = st.progress(0)

    for i in range(100):
        text.text(f"ダウンロード中 { i + 1}/100")
        bar.progress(i + 1)
        x = i
        time.sleep(0.01)

if st.checkbox("チェックボックス"):
    st.write("チェックボックスが入りました。")

selection = st.selectbox("セレクトボックス", ["1","2","3"])
st.write(f"{selection} を選択")

map_point=[35.4122,139.4130]

tooltip = "Liberty Bell"
m = folium.Map(location=map_point, zoom_start=15)
folium.Marker(
        map_point, popup="Liberty Bell", tooltip=tooltip
    ).add_to(m)
folium_static(m)
st.write(m.position())