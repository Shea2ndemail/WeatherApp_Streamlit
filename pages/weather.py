import streamlit as st
#from sqlalchemy import create_engine
import pandas as pd
#from datetime import datetime, timedelta
#import plotly.express as px

#now = datetime.now()
#cutoff_dt = now - timedelta(hours=24)

#engine = create_engine('postgresql://postgres:12345@192.168.1.201:5432/test')

#df = pd.read_sql_query("select * from weather_station",con=engine)
#df = df.iloc[:15]

#fig = px.line( x = df['datetime'] ,
#              y = [df['temperature'], df['ground_temp'], df['humidity']],
#              title = 'Weather')

#newnames = {'wide_variable_0':'Temp', 'wide_variable_1':'Ground Temp', 'wide_variable_2':'Humidity'}
#fig.for_each_trace(lambda t: t.update(name = newnames[t.name],
#                                      legendgroup = newnames[t.name],
#                                      hovertemplate = t.hovertemplate.replace(t.name, newnames[t.name])
#                                     )
#                  )

#fig.update_layout(legend=dict(
#    yanchor="top",
#    y=0.99,
#    xanchor="left",
#    x=0.25,
#    title_text='',
#    font_size = 10,
#    orientation="h"))

#st.plotly_chart(fig, use_container_width=True)

test_df = pd.DataFrame({'a':[1,2,3], 'b':[34,5,6]})

st.write(test_df)