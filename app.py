import streamlit as st
import pandas as pd
import numpy as np
from sqlalchemy import create_engine

engine = create_engine('postgresql://{}:{}@{}:{}/{}'.format(st.secrets["postgres"]["user"], st.secrets["postgres"]["password"], st.secrets["postgres"]["host"], st.secrets["postgres"]["port"], st.secrets["postgres"]["dbname"])

st.title('Evans Home Weather')

df = pd.read_sql_query('select * from weather_station ORDER BY datetime DESC LIMIT 1',con=engine)

st.write(df)
