import mysql.connector

# Connect to MySQL server (no database specified yet)
conn = mysql.connector.connect(
    host='localhost',port=3306,
    user='root',
    password='*Aa1131318#' ,
    #database='TrafficDB'
)
print(conn) 
cursor = conn.cursor()
# Create a new database
cursor.execute("USE TrafficVoilationSystem")
cursor.execute("show tables")
tables = cursor.fetchall()  # Fetch all rows from the executed query

for table in tables:
    print(tables)  # table is a tuple like ('table_name',), so we print the first element

cursor.close()
conn.close()
