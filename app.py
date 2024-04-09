import streamlit as st
import pandas as pd
import numpy as np
import geopandas as gpd
import json


with open('redes_camineras.geojson', "r") as read_file:
    data = json.load(read_file)

st.title("Redes Camineras Medellín 2022")

st.write('Las redes camineras son espacios públicos seguros para el peatón, logrados a través de urbanismo táctico, que además pretenden la organización de los flujos viales, reducir los conflictos entre actores viales (peatón, moto, vehículo, transporte público, entre otros), acortar la distancia para cruzar la vía, eliminar el estacionamiento irregular y mejorar la accesibilidad para personas con movilidad reducida.)'
         )
st.subheader('Sistema de consulta de redes camineras de Medellín')

longitud_km = data['features'][0]['properties']['LONGITUD_KM']

print("Longitud en kilómetros:", longitud_km)
