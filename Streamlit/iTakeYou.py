import streamlit as st
import pandas as pd
from PIL import Image

df_lugares = pd.read_parquet ('lugares.parquet')

st.sidebar.markdown ('# **iTakeYou**')
st.sidebar.markdown ('### La web para encontrar los mejores lugares para comer!')
st.sidebar.markdown ('***')

imagen = Image.open('ITakeU_Logo_1.jpg')
st.image(imagen)

st.markdown ('***')

ciudad = st.selectbox ('Seleccione la Ciudad', (df_lugares['City'].unique()))
categoria = st.selectbox ('Seleccione la Categoría', (df_lugares['category'].unique()))

col1, col2 = st.columns (2)

with col1:
    df_ciudad = df_lugares [df_lugares ['City'] == ciudad]
    st.map (df_ciudad)

with col2:
    st.markdown("<h2 style='text-align: center; color: red;'>Top 10 </h2>", unsafe_allow_html=True)
    df_top_10 = df_ciudad[['name','num_of_reviews','avg_rating']].sort_values('avg_rating', ascending=False).head(10)
    hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """
    st.markdown (hide_table_row_index, unsafe_allow_html=True)
    st.table (df_top_10)

st.markdown ('***')

nombre = st.selectbox ('Seleccione un Lugar', (df_ciudad['name'].unique()))

st.markdown ('***')

st.markdown("<h3 style='text-align: center; color: red;'>Información de Interés </h3>", unsafe_allow_html=True)
st.write('**Nombre:**', nombre)
st.write('**Precio:**')
st.write('**Descripción:**')
st.write('**Categoría:**')
st.write('**Horario:**')
st.write('**Dirección:**')
st.write('**Página Web:**')
st.write('**Bonus:**')
st.write('**Rating Promedio:**')