#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''This topic focuses on Visualisation process which involves the variation in Volume of each Ticker value'''
import pandas as pd
ticker=pd.read_csv("C:/Users/BHARATHWAJ T A/Desktop/AIDI Durham/20F/AIDI1100/Ticker.csv")  #Importing the ticker csv file
ticker.head(10)


# In[2]:


import plotly.express as px

Datetime=pd.Series(ticker["Date"].values) #Using this pandas.series function to display the date in ascending order

x=ticker["Date"]
y=ticker["Volume"]
z=ticker["Ticker"]

#Creating a Data Frame name "dateVolume" which contains Date, Volume and Ticker. 
dateVolume = {
    "Date": x,
    "Volume": y,
    "Ticker":z
}
df = pd.DataFrame(dateVolume)

#After that, we are using ploty express bar which contains Date as x- axis, Volume as y-axis. 

fig1 = px.bar(df, x="Date", y="Volume", title="Volume of each Ticker per day (excluding weekends) from Nov to Dec 2021", color = "Ticker")
# Ticker value is used as Color since the graph can display Volume of each ticker in different colors. 
# We can show/hide the specific Ticker value by pressing the square box situated at the top right corner. So this graph shows the Variation in Volume of each Ticker from Nov 2021 to Dec 2021
fig1.update_layout(barmode='group',xaxis={'categoryorder':'array','categoryarray':Datetime}) 
# We displayed in groups each color/Ticker and used Datetime as category array to display graph in orderwise pattern. 
# For example, we used csv that contains Volume variation from Nov to Dec 2021. If pd.series is not used for Date, it will shows first Dec 2021 values and then show Nov 2021. 


fig1.update_traces(texttemplate='%{y:.5s}', textposition='inside')    # To display numbers inside bar 
fig1.update_layout(uniformtext_minsize=2.3, uniformtext_mode='show')  # To show Volume values 
fig1.show()

