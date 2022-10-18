import streamlit as st
from sqlalchemy import create_engine
import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt, dates

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


fig, ax = plt.subplots()
ax.plot(df['datetime'], df['temperature'])
plt.tick_params(rotation=45)
ax.xaxis.set_major_formatter(dates.DateFormatter('%H:%M'))
st.pyplot(fig)

df = df.iloc[-5:]
df = df[['datetime', 'ground_temp', 'temperature', 'humidity']]

st.write(df)
