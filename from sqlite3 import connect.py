import mysql.connector
my_conn = mysql.connector.connect( user = "root", database = "bank_app", password= "Doubleg123@")
cursor = my_conn.cursor()
query = ("SELECT * FROM customers")
cursor.execute(query)
for row in cursor: 
    print(row)

