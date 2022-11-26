import streamlit as st
from database import add_data


def create():
    col1, col2 = st.columns(2)
    with col1:
        accessory_id = st.selectbox("Accessory ID",["Select","1","2","3","4","5","6","7","8"])
        model = st.selectbox("Model Name",["Select","Macbook pro ","Galaxy Tab S4","iPad Pro 11","Playstation 5","Xbox one","Galaxy Note 10 plus","A7 III","Powershot SX740"])
        brand = st.selectbox("Brand",["Select","Apple","Samsung","Apple","Mutterfly","Mutterfly","Samsung","Sony","Sony"])
    with col2:
        cur_location_id = st.selectbox("Current Location",["Select","1","2","3"])
        date = st.date_input("Select a date")
        

    if st.button("Add Item"):
        add_data(accessory_id, model, brand, cur_location_id, date)
        st.success("Successfully added: {}".format(model))