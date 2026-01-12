import pandas as pd
import streamlit as st
data = pd.read_csv('products.csv')
data.head()
data.info()
st.write(data['Price'])
st.title('upload your data in')

