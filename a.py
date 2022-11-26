import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", password="Prateek@123")
c = mydb.cursor()
c.execute("CREATE DATABASE railway_system_lab_302")