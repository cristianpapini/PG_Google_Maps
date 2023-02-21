import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from millify import millify


df_lugares = pd.read_csv ('sitios_FL_New.csv')
df_poblacion = pd.read_csv ('city_population.csv')

imagen = Image.open('ITakeU_Logo_1.jpg')
st.image(imagen, width=400)

st.sidebar.image (imagen, width=200)
#st.sidebar.markdown ('# **iTakeYou**')
st.sidebar.markdown ('### La web para encontrar los mejores lugares para comer!')
st.sidebar.markdown ('***')

st.markdown ('***')

ciudad = st.selectbox ('**Seleccione la Ciudad**', (df_lugares['City'].unique()))
df_ciudad = df_lugares [df_lugares ['City'] == ciudad]
categoria = st.selectbox ('**Seleccione la Categoría**', (df_ciudad['category'].unique()))
df_categoria = df_ciudad [df_ciudad ['category'] == categoria]

poblacion = df_poblacion[df_poblacion['City'] == ciudad]
if (poblacion.shape[0] != 0):
    poblacion = poblacion.iloc[0][2]
    st.sidebar.metric (label=f'**Población en: {ciudad}**', value=millify(poblacion))
    st.sidebar.markdown ('***')
    st.sidebar.write (f'**Categoría:** {categoria}')
    cant_rest_categ = df_categoria.shape[0]
    st.sidebar.metric (label='**Cantidad Lugares en esa Categoría:**', value=cant_rest_categ)

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

st.markdown ('***')

st.markdown("<h2 style='text-align: center; color: blue;'>Estadísticas </h2>", unsafe_allow_html=True)

st.write(f"**<h5 style='text-align: center; '>Cantidad de Sitios Activos e Inactivos en {ciudad}, por la Categoría {categoria} </h5>**", unsafe_allow_html=True)
st.bar_chart (df_categoria['Condición_Establecimiento'].value_counts())

# Gráficos
# Sitios Activos e Inactivos por Ciudad y Categoría
df_condicion_sitios_categoria = df_categoria.groupby('Condición_Establecimiento').City.count()
bar_fig = plt.figure(figsize=(8,7))
bar_ax = bar_fig.add_subplot(111)
df_condicion_sitios_categoria.plot.bar(alpha=0.8, ax=bar_ax)

# Otro gráfico de barras
bar_fig

st.markdown ('***')

st.write(f"**<h5 style='text-align: center; '>Cantidad de Sitios Activos e Inactivos en {ciudad}. Todas las Categorías </h5>**", unsafe_allow_html=True)

# Sitios Activos e Inactivos por Ciudad
# df_condicion_sitios_ciudad = df_ciudad.groupby('Condición_Establecimiento').City.count()
st.bar_chart (df_ciudad['Condición_Establecimiento'].value_counts())

st.markdown ('***')

# Cantidad de Sitios por Ciudad y Categoría
df_sitios_ciudad_categoria = df_ciudad.groupby('category').value_counts()
pie_fig, ax = plt.subplots()
ax.pie (df_sitios_ciudad_categoria)
plt.show

