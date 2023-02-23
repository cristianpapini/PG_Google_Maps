# <h2 align=center> Pronósticos del Estado de Florida, EE.UU.
  
  Dentro de la plataforma **AWS**, se ha utilizado la herramienta **Amazon Forecast** para elaborar distintos pronósticos del Estado de la Florida en EE.UU., entre ellos:
  - Nacimientos
  - Muertes
  - Migración Internacional
  - Migración Local
  
  Para esto, se ha utilizado el dataset "Florida Population Change", el cual cuenta con datos desde 1990 a 2020 y cuenta con datos anuales de cada variable.
  A través de la herramienta antes mencionada, se pudo hacer un pronóstico de 7 años (hasta 2027). Estos se muestran a continuación y se anexan métricas que serán de gran aporte en la lectura de las gráficas.
  Métricas a mostrar:
  - WAPE (Weighted Absolute Percentage Error) - Error Absoluto Ponderado Porcentual
  - MASE (Mean Absolute Scaled Error) - Error Absoluto Medio Escalado
  - RMSE (Root Mean Squared Error) - Raiz del Error Cuadrático Medio
  - MAPE (Mean Absolute Percentage Error) - Error Absoluto Medio Porcentual
  
  Como se verá a continuación, las gráficas se pueden dividir en dos partes. 
  A la izquierda, en gris, se puede observar los datos verídicos de 2014 a 20220. 
  Por otro lado, a la derecha se va desde 2021 a 2027 y hay 3 líneas a considerar, P10, P50 y P90.
  Estos últimos, son términos estadísticos que se refieren a percentiles en un conjunto de datos, es decir, el conjunto de valores predecidos para todo ese rango de tiempo. Los percentiles dividen un conjunto de datos en 100 partes iguales, por lo que P10, P50 y P90 se refieren a los valores por debajo de los cuales caen el 10%, 50% y 90% de los datos, respectivamente.

- P10: Este es el valor por debajo del cual cae el 10% de los datos. En otras palabras, el 10% de los datos es más pequeño que este valor y el 90% de los datos es más grande que este valor.

- P50: Este es el valor por debajo del cual cae el 50% de los datos. También se conoce como la mediana, y representa el valor medio en un conjunto de datos.

- P90: Este es el valor por debajo del cual cae el 90% de los datos. En otras palabras, el 90% de los datos es más pequeño que este valor y solo el 10% de los datos es más grande que este valor.

Estos percentiles son útiles para comprender la distribución de datos en un conjunto de datos y pueden ayudar a identificar valores atípicos o extremos. Por ejemplo, si el valor de P90 es mucho más grande que el valor de P50, puede indicar que hay algunos valores muy grandes en el conjunto de datos que están sesgando la distribución general.
  
  <h3 align=center> Nacimientos
    
  
<a align=center href="https://ibb.co/7RnTKH1"><img src="https://i.ibb.co/3Mp8cwC/Births-Forecast-blanco.png" alt="Births-Forecast-blanco" border="0"></a>

    WAPE = 0.1020
    MASE = 8.9432
      RMSE = 22833.96
    MAPE = 0.1019

    Los nacimientos se mantendrán relativamente constante en el tiempo
    
  <h3 align=center> Muertes
  
<a align=center href="https://ibb.co/0ZCm7Sw"><img src="https://i.ibb.co/QnPpgR5/Deaths-Forecast-blanco.png" alt="Deaths-Forecast-blanco" border="0"></a>  

    WAPE = 0.2320
    MASE = 5.6947
      RMSE = 48647.28
    MAPE = 0.2286
    
    Las muertes empezarán a declinar, muy probablemente por el aumento en la calidad de vida de las personas
    
  <h3 align=center>Migraciones Internacionales
  
<a align=center href="https://ibb.co/xqMDwFy"><img src="https://i.ibb.co/TMHkJWZ/Int-Migration-Forecast-blanco.png" alt="Int-Migration-Forecast-blanco" border="0"></a>

    WAPE = 0.2286
    MASE = 1.7204
      RMSE = 43892.32
    MAPE = 0.2755
    
    Si bien las migraciones internacionales tenderán a subir, la velocidad irá en aumento con el correr de los años
    
  <h3 align=center>Migraciones Locales
  
<a align=center href="https://ibb.co/yg5cNTq"><img src="https://i.ibb.co/GCk4dwR/Local-Migration-Forecast-blanco.png" alt="Local-Migration-Forecast-blanco" border="0"></a>
 
    WAPE = 0.3318
    MASE = 1.6092
      RMSE = 60941.08
     MAPE = 0.3155
    
    Las migraciones se mantendrán relativamente constante en el tiempo, con fluctuaciones temporales
   
