import streamlit as st
from sqlalchemy import create_engine

host = 'ec2-44-210-50-83.compute-1.amazonaws.com'
db = 'd1fp8mklv5sglk'
user = 'tmrjpxsyzlnbdg'
port = '5432'
pwd = 'bf5fa66390bf26d445af2bdfbb4ec899b119150825b6008781acd4abfd267e0b'

engine = create_engine('postgresql://{}:{}@{}:{}/{}'.format(user, pwd, host, port, db))

table_name = 'todo_list'

def insert_item(item):
    insert_sql_string = """INSERT INTO todo_list VALUES(2, 'sdfdf');"""
    engine.execute(insert_sql_string)