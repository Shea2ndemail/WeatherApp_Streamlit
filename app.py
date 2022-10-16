import streamlit as st
from sqlalchemy import create_engine
import pandas as pd

host = 'ec2-44-209-24-62.compute-1.amazonaws.com'
db = 'deqji7h232uoc8'
user = 'lexcwuwkjlbzok'
port = '5432'
pwd = 'de7a0a0d25bd3a889553353eee682f3742c7fc67890d97b5db9a51f89a7091f8'

engine = create_engine('postgresql://{}:{}@{}:{}/{}'.format(user, pwd, host, port, db))

df = pd.read_sql_query("select * from weather_station",con=engine)
df = df.iloc[:5]

st.title("Weather Station")
st.write(df)
