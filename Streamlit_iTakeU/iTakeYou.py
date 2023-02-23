import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from millify import millify


df_lugares = pd.read_csv ('sitios_FL_New.csv')
df_poblacion = pd.read_csv ('city_population.csv')

imagen = Image.open('ITakeU_Logo_1.jpg')
st.image(imagen, width=400)

st.sidebar.image (imagen, width=200)
st.sidebar.markdown ('# **iTakeYou**')
st.sidebar.markdown ('### La Web para encontrar los mejores lugares para Comer e Invertir!')
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
st.sidebar.markdown ('***')
cant_rest_ciudad = df_ciudad.shape[0]
st.sidebar.metric (label=f'**Total de Lugares en: {ciudad}**', value=cant_rest_ciudad)

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

col3, col4 = st.columns (2)

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

st.markdown ('***')

st.markdown("<h2 style='text-align: center; color: blue;'>Estadísticas </h2>", unsafe_allow_html=True)

# Gráficos

# Sitios Activos y Permanentemente Cerrados por Ciudad y Categoría. Gráfico de Barras
st.write(f"**<h5 style='text-align: center; '>Cantidad de Lugares Activos y Permanentemente Cerrados en {ciudad}, por la Categoría {categoria} </h5>**", unsafe_allow_html=True)
st.bar_chart (df_categoria['Condición_Establecimiento'].value_counts())

# Otro gráfico de barras
#df_condicion_sitios_categoria = df_categoria.groupby('Condición_Establecimiento').City.count()
#bar_fig = plt.figure(figsize=(8,7))
#bar_ax = bar_fig.add_subplot(111)
#df_condicion_sitios_categoria.plot.bar(alpha=0.8, ax=bar_ax)
#st.pyplot (bar_fig)

st.markdown ('***')

# Sitios Activos y Permanentemente Cerrados por Ciudad. Gráfico de Barras
st.write(f"**<h5 style='text-align: center; '>Cantidad de Lugares Activos y Permanentemente Cerrados en {ciudad}. Todas las Categorías </h5>**", unsafe_allow_html=True)
st.bar_chart (df_ciudad['Condición_Establecimiento'].value_counts())

st.markdown ('***')

# Porcentaje de Lugares Activos por Ciudad y todas sus Categorías. Gráfico de Pie
st.write(f"**<h5 style='text-align: center; '>Porcentaje de Lugares Activos en {ciudad}. Todas las Categorías </h5>**", unsafe_allow_html=True)
df_sitios_activo_ciudad_categoria = df_ciudad[df_ciudad['Condición_Establecimiento'] == 'Activo']

if df_sitios_activo_ciudad_categoria.shape[0] == 0:
    st.write (f'**No hay lugares activos en {ciudad}**')
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
   
# Porcentaje de Lugares Activos en el Estado de la Florida y todas sus Categorías. Gráfico de Pie
st.write(f"**<h5 style='text-align: center; '>Porcentaje de Lugares Activos en el Estado de la FLorida. Todas las Categorías </h5>**", unsafe_allow_html=True)
df_sitios_activo_estado = df_lugares[df_lugares['Condición_Establecimiento'] == 'Activo']
df_sitios_activo_estado = df_sitios_activo_estado.groupby('category').category.count()
labels_est = df_lugares['category'].unique()
sizes_est = df_sitios_activo_estado.reset_index(drop=True)
pie_fig_est, pie_ax_est = plt.subplots()
pie_ax_est.pie (sizes_est, explode=(0.1, 0.1, 0.1), labels=labels_est, autopct='%1.1f%%', shadow=True, startangle=90)
pie_ax_est.axis('auto')
st.pyplot (pie_fig_est)

st.markdown ('***')

st.write(f"**<h5 style='text-align: center; '>Ratings de los Lugares en {ciudad}. Todas las Categorías </h5>**", unsafe_allow_html=True)
df_rating_categoria = df_ciudad[['Rating','category']]
df_rating_categoria = df_rating_categoria.groupby(['Rating']).count()
st.bar_chart(df_rating_categoria)