import streamlit as st
import pandas as pd
from database import execute_query



def Query():
    query=st.text_input(label='',placeholder='Enter a Query to execute')
    
    if st.button("Execute"):
        data = execute_query(query)
        if data not in [0,1]:
            try:
                df = pd.DataFrame(data[0],columns=data[1])
                st.dataframe(df)
            except:
                st.write(data[0])