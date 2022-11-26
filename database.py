import mysql.connector
import streamlit as st

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="elec_acc"
)
c = mydb.cursor()


def create_table():
    c.execute('create table if not exists customer(customer_id int not null auto increment, email varchar(45), mobile varchar(45), ssn int, name varchar(45), primary key (customer_id))')

    c.execute('create table if not exists E_Accessory(Accessory_id varchar(3) not null, model varchar(45), brand varchar(45), Cur_location_id varchar(3), date DATE, primary key (Accessory_id))')

    c.execute('create table if not exists reservation(reservation_id varchar(3), amount double, accessory_id varchar(3), customer_id int,pickup_date DATE, return_date DATE, primary key(reservation_id), foreign key (customer_id) references customer(customer_id)  , foreign key (accessory_id) references E_Accessory(Accessory_id))')

    c.execute('create table if not exists Accessory_type(type_id varchar(4) not null, type_label varchar(45), type_desc varchar(45),primary key (type_id))')

    c.execute('create table if not exists office(office_id int not null, phone int, address varchar(45),primary key (office_id))')


def add_data(accessory_id, model, brand, cur_location_id, date):
    c.execute('INSERT INTO E_Accessory (Accessory_id,model,brand ,Cur_location_id ,date) VALUES (%s,%s,%s,%s,%s)',
              (accessory_id, model, brand, cur_location_id, date))
    mydb.commit()



def view_all_data():
    c.execute('SELECT * FROM E_Accessory')
    data = c.fetchall()
    return data


def view_only_model_names():
    c.execute('SELECT Model FROM E_Accessory')
    data = c.fetchall()
    return data


def get_details(model):
    c.execute('SELECT * FROM E_Accessory WHERE Model="{}"'.format(model))
    data = c.fetchall()
    return data


def edit_details(n_accessory_id, n_model, n_brand, new_cur_location_id, new_date, accessory_id, model, brand, cur_location_id, date):
    c.execute("UPDATE E_Accessory SET Accessory_id=%s, Model=%s, Brand=%s, Cur_location_id=%s, Date=%s WHERE "
              "Accessory_id=%s  and Model=%s and Brand=%s and Cur_location_id=%s and Date=%s", (accessory_id, model, brand, new_cur_location_id, new_date, accessory_id, model, brand, cur_location_id, date))
    mydb.commit()
    data = c.fetchall()
    return data


def delete_data(model):
    c.execute('DELETE FROM E_Accessory WHERE Model="{}"'.format(model))
    mydb.commit()

def add_cust_data(customer_id,email,mobile,ssn,name):
    c.execute('Insert into Customer (customer_id,email,mobile,ssn,name) VALUES (%s,%s,%s,%s,%s);',(customer_id,email,mobile,ssn,name))
    mydb.commit()


def execute_query(query):
    try:
        c.execute(query)
        if query.split()[0].lower() not in ['select','show','desc']:
            mydb.commit()
        data = c.fetchall()
        return [data,c.column_names]
    except BaseException as e:
        if str(e)=='No result set to fetch from.':
            st.success('querry successful')
            return 1
        st.error(e)
        return 0    