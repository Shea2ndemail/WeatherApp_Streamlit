import streamlit as st
from sqlalchemy import create_engine
import pandas as pd
from datetime import datetime, timedelta
import plotly.express as px

now = datetime.now()
cutoff_dt = now - timedelta(hours=24)

host = 'ec2-44-210-50-83.compute-1.amazonaws.com'
db = 'd1fp8mklv5sglk'
user = 'tmrjpxsyzlnbdg'
port = '5432'
pwd = 'bf5fa66390bf26d445af2bdfbb4ec899b119150825b6008781acd4abfd267e0b'

engine = create_engine('postgresql://{}:{}@{}:{}/{}'.format(user, pwd, host, port, db))

df = pd.read_sql_query("select * from weather_station",con=engine)
df = df[df['datetime']>cutoff_dt]

fig = px.line( x = df['datetime'] ,
              y = [df['temperature'], df['ground_temp'], df['humidity']],
              title = 'Weather')

newnames = {'wide_variable_0':'Temp', 'wide_variable_1':'Ground Temp', 'wide_variable_2':'Humidity'}
fig.for_each_trace(lambda t: t.update(name = newnames[t.name],
                                      legendgroup = newnames[t.name],
                                      hovertemplate = t.hovertemplate.replace(t.name, newnames[t.name])
                                     )
                  )

fig.update_layout(legend=dict(
    yanchor="top",
    y=0.99,
    xanchor="left",
    x=0.25,
    title_text='',
    font_size = 10,
    orientation="h"))

st.plotly_chart(fig, use_container_width=True)
