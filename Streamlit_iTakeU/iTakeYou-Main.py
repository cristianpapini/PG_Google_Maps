import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


df_lugares = pd.read_csv ('sitios_FL_New.csv')
df_reviews = pd.read_csv ('review_FL.csv')

df_reviews.dropna(subset=['date'], inplace=True)
df_reviews.rename (columns={'name':'Nombre', 'text':'Reseña', 'date':'Fecha'}, inplace=True)

# Logo
col1, col2, col3 = st.columns(3)
with col1:
    st.write(' ')
with col2:
    imagen = Image.open('ITakeU_Logo_1.jpg')
    st.image(imagen, width=400)
with col3:
    st.write(' ')

# Información de la barra lateral izquierda
st.sidebar.image (imagen, width=200)
st.sidebar.markdown ('# **iTakeYou**')
st.sidebar.markdown ('### La Web para encontrar los mejores lugares para Comer!')
st.sidebar.markdown ('***')

st.markdown ('***')

# Seleccionar Ciudad y Categoría a consultar
ciudad = st.selectbox ('**Seleccione la Ciudad**', (df_lugares['City'].unique()))
df_ciudad = df_lugares [df_lugares ['City'] == ciudad]
categoria = st.selectbox ('**Seleccione la Categoría**', (df_ciudad['category'].unique()))
df_categoria = df_ciudad [df_ciudad ['category'] == categoria]

col1, col2 = st.columns (2)

# Mapa
with col1:
    st.map (df_categoria)

# Top 10
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

# Selección del Lugar y el Código Postal
nombre = st.selectbox('Seleccione un Lugar', (df_categoria['Nombre'].unique()))
df_nombre = df_categoria[df_categoria['Nombre'] == nombre]

zip = st.selectbox('Seleccione el Código Zip', (df_nombre['Zip']))
df_zip = df_nombre[df_nombre['Zip'] == zip]

st.markdown ('***')

st.markdown("<h3 style='text-align: center; color: red;'>Información de Interés </h3>", unsafe_allow_html=True)

col3, col4 = st.columns (2)

# Información más detallada del Lugar
with col3:
    st.write('**Nombre:**', nombre)
    st.write('**Rango de Precio:**', df_zip['price'].iloc[0])
    st.write('**Descripción:**', df_zip['description'].iloc[0])
    st.write('**Categoría:**', df_zip['category'].iloc[0])
    st.write('**Apertura:**', df_zip['open'].iloc[0])
    st.write('**Cierre:**', df_zip['close'].iloc[0])
    st.write('**Dirección:**', df_zip['address'].iloc[0])
    st.write('**Ubicación en Google Maps:**',df_zip['url'].iloc[0])
    st.write('**Rating:**', df_zip['Rating'].iloc[0])
    st.write('**Condición del Lugar:**', df_zip['Condición_Establecimiento'].iloc[0])

with col4:
    dicc_precio =  {'Símbolo Precio':['$', '$$', '$$$', '$$$$'],
                    'Significado':['Económico', 'Moderado', 'Caro', 'Lujoso'],
                    'Rango':['Entre 0 - 20$', 'Entre 20-40$', 'Entre 40-60$', 'Más de 60$']}
    df_precio = pd.DataFrame (dicc_precio)
    st.table (df_precio)

df_union = pd.merge (df_reviews, df_zip)

# Reviews de los usuarios
st.write('**Comentarios:**')
df_text = df_union[['Reseña', 'rating', 'Fecha']]
df_text.dropna (inplace=True)
df_text.drop_duplicates (inplace=True)
st.dataframe (df_text.sort_values('Fecha', ascending=False, ignore_index=True), 800)

st.markdown ('***')

# Gráficos

# Evolución de los Ratings por Años
if (df_union.shape[0] != 0):
    st.write(f"**<h5 style='text-align: center; '>Evolución de los Ratings en {nombre}, por Años </h5>**", unsafe_allow_html=True)
    df_rating_fecha = df_union [['rating', 'Fecha']]
    df_rating_fecha.dropna (inplace=True)
    df_rating_fecha.drop_duplicates (inplace=True)
    df_rating_fecha = df_rating_fecha.sort_values(by=['Fecha'], ignore_index=True)
    df_anio = df_rating_fecha['Fecha']
    df_anio= df_anio.str.split("-", n=1).str[0]
    x = df_anio
    y = df_rating_fecha ['rating'] 
    fig_line, ax_line = plt.subplots()
    ax_line.set_xlabel('Años')
    ax_line.set_ylabel('Ratings')
    ax_line.fill_between(x = x, y1 = y, color='purple')
    st.pyplot (fig_line)