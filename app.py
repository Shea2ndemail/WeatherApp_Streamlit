import streamlit as st
import pandas as pd
import numpy as np
from sqlalchemy import create_engine

#engine = create_engine('postgresql://postgres:12345@192.168.1.201:5432/test')

st.title('Evans Home Weather')

#df = pd.read_sql_query('select * from weather_station ORDER BY datetime DESC LIMIT 1',con=engine)

#st.write(df)

st.write(st.secrets["postgres"]["host"])
