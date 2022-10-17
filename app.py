import streamlit as st
from sqlalchemy import create_engine
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

now = datetime.now()
cutoff_dt = now - timedelta(hours=24)

host = 'ec2-44-209-24-62.compute-1.amazonaws.com'
db = 'deqji7h232uoc8'
user = 'lexcwuwkjlbzok'
port = '5432'
pwd = 'de7a0a0d25bd3a889553353eee682f3742c7fc67890d97b5db9a51f89a7091f8'

engine = create_engine('postgresql://{}:{}@{}:{}/{}'.format(user, pwd, host, port, db))

df = pd.read_sql_query("select * from weather_station",con=engine)
df = df[df['datetime']>cutoff_dt]


fig, ax = plt.subplots()
ax.plot(df['datetime'], df['temperature'])
ax.xaxis.set_major_formatter(dates.DateFormatter('%H:%M'))
st.pyplot(fig)

df = df.iloc[-5:]
df = df[['datetime', 'ground_temp', 'temperature', 'humidity']]

st.write(df)
