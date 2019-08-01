# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 10:26:26 2019

@author: STEM
"""
import pandas as pd
dir(pd)
import plotly
from plotly.offline import plot
import plotly.graph_objs as go

wodf= pd.read_excel("GISdata.xlsx",sheet_name= "womenOccupation")
wodf

#we read the data into a dataset or data frame called of
wodf = pd.read_excel("GISdata.xlsx", sheet_name = "womenOccupation")

#we use the Bar graph option of the graph_objs function from the plotly library
womenoccupation =go.Bar(x=wodf["occupation"], y=wodf["women"],marker = {"color":wodf["women"],
                        "colorscale": "Jet"})
                        
        

plot([womenoccupation])


titles= go.Layout(title = "Percentage of Women Employed by Occupation", xaxis=go.layout.XAxis(title=go.layout.xaxis.Title(text="Occupation")), yaxis=go.layout.YAxis(title=go.layout.yaxis.Title(text="Percentage",)))
fig = go.Figure(data=[womenoccupation], layout=titles)        
plot(fig)    
                                                        