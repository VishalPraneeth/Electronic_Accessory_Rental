import pandas as pd
import streamlit as st
from database import view_all_data, view_only_model_names, delete_data


def delete():
    result = view_all_data()
    df = pd.DataFrame(result, columns=['Accessory_id','Model','Brand' ,'Cur_location_id' ,'Date'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_models = [i[0] for i in view_only_model_names()]
    selected_model = st.selectbox("Model to Delete", list_of_models)
    st.warning("Do you want to delete ::{}".format(selected_model))
    if st.button("Delete model"):
        delete_data(selected_model)
        st.success("Model has been deleted successfully")
    new_result = view_all_data()
    df2 = pd.DataFrame(new_result, columns=['Accessory_id','Model','Brand' ,'Cur_location_id' ,'Date'])
    with st.expander("Updated data"):
        st.dataframe(df2)