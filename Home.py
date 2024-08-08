import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')
df = pd.read_csv('data.csv')

st.title("The Best Company")
content= "Laboris mollit quis sunt quis consectetur exercitation voluptate laborum.Laboris mollit quis sunt quis consectetur exercitation voluptate laborum.Laboris mollit quis sunt quis consectetur exercitation voluptate laborum.Laboris mollit quis sunt quis consectetur exercitation voluptate laborum.Laboris mollit quis sunt quis consectetur exercitation voluptate laborum."
st.write(content)
col1, col2, col3 = st.columns(3)

with col1:
    for index, item in df[:4].iterrows():
        st.header(f"{item['first name'].title()} {item['last name'].title()} ")
        st.write(item['role'])
        st.image("images/"+item['image'])
with col2:
    for index, item in df[4:8].iterrows():
        st.header(f"{item['first name'].title()} {item['last name'].title()} ")
        st.write(item['role'])
        st.image("images/"+item['image'])
with col3:
    for index, item in df[8:].iterrows():
        st.header(f"{item['first name'].title()} {item['last name'].title()} ",)
        st.write(item['role'])
        st.image("images/"+item['image'])