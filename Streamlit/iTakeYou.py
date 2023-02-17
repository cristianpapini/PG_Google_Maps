import streamlit as st
import pandas as pd
from PIL import Image

df_lugares = pd.read_csv ('sitios_FL_New.csv')

st.sidebar.markdown ('# **iTakeYou**')
st.sidebar.markdown ('### La web para encontrar los mejores lugares para comer!')
st.sidebar.markdown ('***')

imagen = Image.open('ITakeU_Logo_1.jpg')
st.image(imagen, width=400)

st.markdown ('***')

ciudad = st.selectbox ('**Seleccione la Ciudad**', (df_lugares['City'].unique()))
df_ciudad = df_lugares [df_lugares ['City'] == ciudad]
categoria = st.selectbox ('**Seleccione la Categoría**', (df_ciudad['category'].unique()))
df_categoria = df_ciudad [df_ciudad ['category'] == categoria]

col1, col2 = st.columns (2)

with col1:
    st.map (df_categoria)

with col2:
    st.markdown("<h2 style='text-align: center; color: red;'>Top 10 </h2>", unsafe_allow_html=True)
    df_top_10 = df_categoria[['Nombre', 'Zip','Reviews','Rating']].sort_values('Rating', ascending=False).head(10)
    hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """
    st.markdown (hide_table_row_index, unsafe_allow_html=True)
    st.table (df_top_10)

st.markdown ('***')

nombre = st.selectbox('Seleccione un Lugar', (df_categoria['Nombre'].unique()))
df_nombre = df_categoria[df_categoria['Nombre'] == nombre]

zip = st.selectbox('Seleccione el Código Zip', (df_nombre['Zip']))
df_zip = df_nombre[df_nombre['Zip'] == zip]

st.markdown ('***')

st.markdown("<h3 style='text-align: center; color: red;'>Información de Interés </h3>", unsafe_allow_html=True)
st.write('**Nombre:**', nombre)
st.write('**Rango de Precio:**', df_zip['price'].iloc[0])
st.write('**Descripción:**', df_zip['description'].iloc[0])
st.write('**Categoría:**', df_zip['category'].iloc[0])
st.write('**Horario:**', df_zip['horario'].iloc[0])
st.write('**Dirección:**', df_zip['address'].iloc[0])
st.write('**Ubicación en Google Maps:**',df_zip['url'].iloc[0])
st.write('**Rating:**', df_zip['Rating'].iloc[0])