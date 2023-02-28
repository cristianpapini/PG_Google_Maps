import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from millify import millify

df_lugares = pd.read_csv ('sitios_FL_New.csv')
df_poblacion = pd.read_csv ('city_population.csv')

# Logo
col1, col2, col3 = st.columns(3)
with col1:
    st.write(' ')
with col2:
    imagen = Image.open('ITakeU_Logo_1.jpg')
    st.image(imagen, width=400)
with col3:
    st.write(' ')

# Título
st.markdown("<h2 style='text-align: left; color: blue;'>Más Estadísticas </h2>", unsafe_allow_html=True)

st.markdown ('***')

# Información de la barra lateral izquierda
st.sidebar.image (imagen, width=200)
st.sidebar.markdown ('# **iTakeYou**')
st.sidebar.markdown ('### Invierte en las Mejores Zonas de la Florida!')
st.sidebar.markdown ('***')

# Seleccionar Ciudad y Categoría a consultar
ciudad = st.selectbox ('**Seleccione la Ciudad**', (df_lugares['City'].unique()))
df_ciudad = df_lugares [df_lugares ['City'] == ciudad]
categoria = st.selectbox ('**Seleccione la Categoría**', (df_ciudad['category'].unique()))
df_categoria = df_ciudad [df_ciudad ['category'] == categoria]

st.markdown ('***')

# Datos informativos en la barra lateral izquierda
poblacion = df_poblacion[df_poblacion['City'] == ciudad]
if (poblacion.shape[0] != 0):
    poblacion = poblacion.iloc[0][2]
    st.sidebar.metric (label=f'**Población en: {ciudad}**', value=millify(poblacion))
    st.sidebar.markdown ('***')
st.sidebar.write (f'**Categoría:** {categoria}')
cant_rest_categ = df_categoria.shape[0]
st.sidebar.metric (label='**Cantidad Lugares en esa Categoría:**', value=cant_rest_categ)
st.sidebar.markdown ('***')
cant_rest_ciudad = df_ciudad.shape[0]
st.sidebar.metric (label=f'**Total de Lugares en: {ciudad}**', value=cant_rest_ciudad)

# Lugares Activos y Permanentemente Cerrados por Ciudad y Categoría
st.write(f"**<h5 style='text-align: center; '>Cantidad de Lugares Activos y Permanentemente Cerrados en {ciudad}, por la Categoría {categoria} </h5>**", unsafe_allow_html=True)
df_condicion_sitios_categoria = df_categoria.groupby('Condición_Establecimiento').City.count()
barh_fig = plt.figure(figsize=(8,7))
barh_ax = barh_fig.add_subplot(111)
barh_ax.set_xlabel('Cantidad de Lugares')
barh_ax.set_ylabel('Condición del Lugar')
df_condicion_sitios_categoria.plot.barh(alpha=0.8, ax=barh_ax)
st.pyplot (barh_fig)

st.markdown ('***')

# Lugares Activos y Permanentemente Cerrados por Ciudad. Gráfico de Barras
st.write(f"**<h5 style='text-align: center; '>Cantidad de Lugares Activos y Permanentemente Cerrados en {ciudad}. Todas las Categorías </h5>**", unsafe_allow_html=True)
df_condicion_sitios_ciudad = df_ciudad['Condición_Establecimiento'].value_counts()
bar_fig = plt.figure(figsize=(8,7))
bar_ax = bar_fig.add_subplot(111)
bar_ax.set_xlabel('Fecha')
bar_ax.set_ylabel('Condición del Lugar')
df_condicion_sitios_ciudad.plot.barh(alpha=0.8, ax=bar_ax, color='orange')
st.pyplot (bar_fig)

st.markdown ('***')

# Ratings de los Lugares en una determinada Ciudad en todas las Categorías
st.write(f"**<h5 style='text-align: center; '>Ratings de los Lugares en {ciudad}. Todas las Categorías </h5>**", unsafe_allow_html=True)
df_rating_categoria = df_ciudad[['Rating','category']]
df_rating_categoria = df_rating_categoria.groupby(['Rating']).count()
bar_fig = plt.figure(figsize=(8,7))
bar_ax = bar_fig.add_subplot(111)
df_rating_categoria.plot.bar(alpha=0.8, ax=bar_ax, color='green')
st.pyplot (bar_fig)

st.markdown ('***')

# Porcentaje de Lugares Activos por Ciudad y todas sus Categorías
st.write(f"**<h5 style='text-align: center; '>Porcentaje de Lugares Activos en {ciudad}. Todas las Categorías </h5>**", unsafe_allow_html=True)
df_sitios_activo_ciudad_categoria = df_ciudad[df_ciudad['Condición_Establecimiento'] == 'Activo']

if df_sitios_activo_ciudad_categoria.shape[0] == 0:
    st.write (f"**<h5 style='text-align: center; color:red; '>No hay lugares Activos en {ciudad}</h5>**", unsafe_allow_html=True)
else:
    df_sitios_activo_ciudad_categoria = df_sitios_activo_ciudad_categoria.groupby('category').category.count()
    labels = df_ciudad['category'].unique()
    sizes = df_sitios_activo_ciudad_categoria.reset_index(drop=True)
    pie_fig, pie_ax = plt.subplots()

    if len(sizes) == 1:
        pie_ax.pie (df_sitios_activo_ciudad_categoria, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    elif sizes.shape[0] == 2:
        pie_ax.pie (sizes, explode=(0.1, 0.1), labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    else:
        pie_ax.pie (sizes, explode=(0.1, 0.1, 0.1), labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)

    pie_ax.axis('auto')
    st.pyplot (pie_fig)

st.markdown ('***')
   
# Porcentaje de Lugares Activos en el Estado de la Florida y todas sus Categorías
st.write(f"**<h5 style='text-align: center; '>Porcentaje de Lugares Activos en el Estado de la FLorida. Todas las Categorías </h5>**", unsafe_allow_html=True)
df_sitios_activo_estado = df_lugares[df_lugares['Condición_Establecimiento'] == 'Activo']
df_sitios_activo_estado = df_sitios_activo_estado.groupby('category').category.count()
labels_est = df_lugares['category'].unique()
sizes_est = df_sitios_activo_estado.reset_index(drop=True)
pie_fig_est, pie_ax_est = plt.subplots()
pie_ax_est.pie (sizes_est, explode=(0.1, 0.1, 0.1), labels=labels_est, autopct='%1.1f%%', shadow=True, startangle=90)
pie_ax_est.axis('auto')
st.pyplot (pie_fig_est)