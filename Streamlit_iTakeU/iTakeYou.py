import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from millify import millify


df_lugares = pd.read_csv ('sitios_FL_New.csv')
df_poblacion = pd.read_csv ('city_population.csv')
df_reviews = pd.read_csv ('review_FL.csv')

df_reviews.rename (columns={'name':'Nombre', 'text':'Reseña', 'date':'Fecha'}, inplace=True)

imagen = Image.open('ITakeU_Logo_1.jpg')
st.image(imagen, width=400)

# Información de la barra lateral izquierda
st.sidebar.image (imagen, width=200)
st.sidebar.markdown ('# **iTakeYou**')
st.sidebar.markdown ('### La Web para encontrar los mejores lugares para Comer e Invertir!')
st.sidebar.markdown ('***')

st.markdown ('***')

# Seleccionar Ciudad y Categoría a consultar
ciudad = st.selectbox ('**Seleccione la Ciudad**', (df_lugares['City'].unique()))
df_ciudad = df_lugares [df_lugares ['City'] == ciudad]
categoria = st.selectbox ('**Seleccione la Categoría**', (df_ciudad['category'].unique()))
df_categoria = df_ciudad [df_ciudad ['category'] == categoria]

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
st.dataframe (df_text.sort_values('Fecha', ascending=False, ignore_index=True))

st.markdown ('***')

# Gráficos

# Evolución de los Ratings por Años
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

st.markdown ('***')

st.markdown("<h2 style='text-align: center; color: blue;'>Más Estadísticas </h2>", unsafe_allow_html=True)

# Lugares Activos y Permanentemente Cerrados por Ciudad y Categoría
st.write(f"**<h5 style='text-align: center; '>Cantidad de Lugares Activos y Permanentemente Cerrados en {ciudad}, por la Categoría {categoria} </h5>**", unsafe_allow_html=True)
df_condicion_sitios_categoria = df_categoria.groupby('Condición_Establecimiento').City.count()
barh_fig = plt.figure(figsize=(8,7))
barh_ax = barh_fig.add_subplot(111)
barh_ax.set_xlabel('Cantidad de lugares')
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

# Porcentaje de Lugares Activos por Ciudad y todas sus Categorías
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

st.markdown ('***')

# Ratings de los Lugares en una determinada Ciudad en todas las Categorías
st.write(f"**<h5 style='text-align: center; '>Ratings de los Lugares en {ciudad}. Todas las Categorías </h5>**", unsafe_allow_html=True)
df_rating_categoria = df_ciudad[['Rating','category']]
df_rating_categoria = df_rating_categoria.groupby(['Rating']).count()
bar_fig = plt.figure(figsize=(8,7))
bar_ax = bar_fig.add_subplot(111)
df_rating_categoria.plot.bar(alpha=0.8, ax=bar_ax, color='green')
st.pyplot (bar_fig)