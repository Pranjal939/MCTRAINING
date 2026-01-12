import pandas as pd
import streamlit as st
data = pd.read_csv('products.csv')
data.head()
data.info()
st.write(data['Price'])
st.title('upload your data in csv format')
file = st.file_uploader('choose a file',type='csv')
if file is not None:
    df = pd.read_csv(file)
    st.dataframe(df)
    c = st.selectbox('select column for static',df.columns)
    st.line_chart(df[c])
else:
    st.error('please upload a csv file')