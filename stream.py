import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Simple Data Dashboard")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    st.write("File uploaded...")
    
    df = pd.read_csv(uploaded_file)
    
    st.subheader("Data Preview")
    st.write(df.head())
    
    st.subheader("Data Summary")
    st.write(df.describe())
    
    st.subheader("Filter Data")
    columns = df.columns.to_list()
    selected_column = st.selectbox("Select Column to Filter by", columns)
    uniqe_values = df[selected_column].unique()
    selected_value = st.selectbox("select values", uniqe_values)
    
    filtered_df = df[df[selected_column]==selected_value]
    st.write(filtered_df)
    
    st.subheader("Plot Data")
    x_column = st.selectbox("Select X-axis Column", columns)
    y_column = st.selectbox("Select Y-axis Column", columns)
    
    if st.button("Generate Plot"):
        st.line_chart(filtered_df.set_index(x_column)[y_column])
        
else:
    st.write("Waiting on file upload...")      