import datetime

import pandas as pd
import streamlit as st
from database import view_all_data, view_only_model_names, get_details, edit_details


def update():
    result = view_all_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Accessory_id','Model','Brand' ,'Cur_location_id' ,'Date'])
    with st.expander("Current models"):
        st.dataframe(df)
    list_of_models = [i[0] for i in view_only_model_names()]
    selected_model = st.selectbox("Model to Edit", list_of_models)
    selected_result = get_details(selected_model)
    # st.write(selected_result)
    if selected_result:
        accessory_id = selected_result[0][0]
        model = selected_result[0][1]
        brand = selected_result[0][2]
        cur_location_id = selected_result[0][3]
        date = selected_result[0][4]
        

        # Layout of Create

        # col1, col2 = st.columns(2)
        # with col1:
        #     new_accessory_id = st.selectbox("Accessory ID",["Select","1","2","3","4","5","6","7","8"])
        #     new_model = st.selectbox("Model Name",["Select","Macbook pro ","Galaxy Tab S4","iPad Pro 11","Playstation 5","Xbox one","Galaxy Note 10 plus","A7 III","Powershot SX740"])
        # with col2:
            # new_brand = st.selectbox("Brand",["Select","Apple","Samsung","Apple","Mutterfly","Mutterfly","Samsung","Sony","Sony"])
        new_cur_location_id = st.selectbox("Current Location",["Select","1","2","3"])
        new_date = st.date_input("Select a date")
            

        if st.button("Update Item"):
            edit_details(accessory_id, model, brand, new_cur_location_id, new_date, accessory_id, model, brand, cur_location_id, date)
            st.success("Successfully updated:: {} to ::{}".format(model, model))

    result2 = view_all_data()
    df2 = pd.DataFrame(result2, columns=['Accessory_id','model','brand' ,'Cur_location_id' ,'date'])
    with st.expander("Updated data"):
        st.dataframe(df2)