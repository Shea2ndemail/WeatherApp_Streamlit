import streamlit as st
import pandas as pd

df = pd.DataFrame({'a':[1,2,3,4], 'b': [23423,343243,34234,44444444444]}, index = [0])

st.title('Evans Home Weather')
st.write(df)
