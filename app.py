import streamlit as st
import mysql.connector

from create import create
from database import create_table
from delete import delete
from read import read
from update import update
from query import Query

def main():
    st.title("E-Accessory Rental")
    menu = ["Rent", "View Items", "Edit Info", "Delete","Query"]
    choice = st.sidebar.selectbox("Menu", menu)

    # create_table()
    if choice == "Rent":
        st.subheader("Enter Details:")
        create()

    elif choice == "View Items":
        st.subheader("View Details:")
        read()

    elif choice == "Edit Info":
        st.subheader("Edited Details:")
        update()

    elif choice == "Delete":
        st.subheader("Delete:")
        delete()

    elif choice == "Query":
        st.subheader("Execute a Query")
        Query()    



    # else:
    #     st.subheader("About Train")


if __name__ == '__main__':
    main()