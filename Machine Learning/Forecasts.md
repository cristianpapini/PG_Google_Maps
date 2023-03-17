# <h2 align=center> Forecasts for the State of Florida, USA
  
Within the **AWS** platform, the **Amazon Forecast** tool has been used to prepare different forecasts for the State of Florida in the US, including:
  - Births
  - Deaths
  - International Migration
  - Local Migration
  
For this, the "Florida Population Change" dataset has been used, which has data from 1990 to 2020 and has annual data for each variable.
Through the aforementioned tool, a 7-year forecast (until 2027) could be made. These are shown below and metrics are attached that will be of great contribution in reading the graphs.
Metrics to display:
  - WAPE: Weighted Absolute Percentage Error
  - MASE: Mean Absolute Scaled Error
  - RMSE: Root Mean Squared Error
  - MAPE: Mean Absolute Percentage Error
  
  As will be seen below, the graphs can be divided into two parts.
  On the left, in grey, you can see the true data from 2014 to 20220.
  On the other hand, on the right it goes from 2021 to 2027 and there are 3 lines to consider, P10, P50 and P90.
  The latter are statistical terms that refer to percentiles in a data set, that is, the set of predicted values for that entire time range. Percentiles divide a data set into 100 equal parts, so P10, P50, and P90 refer to the values below which 10%, 50%, and 90% of the data fall, respectively.
- P10: This is the value below which 10% of the data falls. In other words, 10% of the data is smaller than this value and 90% of the data is larger than this value.

- P50: This is the value below which 50% of the data falls. Also known as the median, it represents the middle value in a data set.

- P90: This is the value below which 90% of the data falls. In other words, 90% of the data is smaller than this value and only 10% of the data is larger than this value.

These percentiles are useful for understanding the distribution of data in a data set and can help identify outliers or extreme values. For example, if the value of P90 is much larger than the value of P50, it may indicate that there are some very large values ​​in the data set that are skewing the overall distribution.
  
  <h3 align=center> Births
    
  
<a align=center href="https://ibb.co/7RnTKH1"><img src="https://i.ibb.co/3Mp8cwC/Births-Forecast-blanco.png" alt="Births-Forecast-blanco" border="0"></a>

    WAPE = 0.1020
    MASE = 8.9432
      RMSE = 22833.96
    MAPE = 0.1019

    Births will remain relatively constant over time
    
  <h3 align=center> Deaths
  
<a align=center href="https://ibb.co/0ZCm7Sw"><img src="https://i.ibb.co/QnPpgR5/Deaths-Forecast-blanco.png" alt="Deaths-Forecast-blanco" border="0"></a>  

    WAPE = 0.2320
    MASE = 5.6947
      RMSE = 48647.28
    MAPE = 0.2286
    
    Deaths will begin to decline, most likely due to the increase in people's quality of life
    
  <h3 align=center>International Migrations
  
<a align=center href="https://ibb.co/xqMDwFy"><img src="https://i.ibb.co/TMHkJWZ/Int-Migration-Forecast-blanco.png" alt="Int-Migration-Forecast-blanco" border="0"></a>

    WAPE = 0.2286
    MASE = 1.7204
      RMSE = 43892.32
    MAPE = 0.2755
    
    Although international migration will tend to rise, the speed will increase over the years
    
  <h3 align=center>Local Migrations
  
<a align=center href="https://ibb.co/yg5cNTq"><img src="https://i.ibb.co/GCk4dwR/Local-Migration-Forecast-blanco.png" alt="Local-Migration-Forecast-blanco" border="0"></a>
 
    WAPE = 0.3318
    MASE = 1.6092
      RMSE = 60941.08
     MAPE = 0.3155
    
    Migrations will remain relatively constant over time, with temporary fluctuations
   
