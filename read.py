import pandas as pd
import streamlit as st
import plotly.express as px
from database import view_all_data


def read():
    result = view_all_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Accessory_id','Model','Brand' ,'Cur_location_id' ,'Date'])
    with st.expander("View all Bookings"):
        st.dataframe(df)
    # with st.expander("Train Details"):
    #     train_df = df['Availability'].value_counts().to_frame()
    #     train_df = train_df.reset_index()
    #     st.dataframe(train_df)
    #     p1 = px.pie(train_df, names='index', values='Availability')
    #     st.plotly_chart(p1)