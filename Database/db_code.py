#library and connexion to database
import sqlite3
import pandas as pd 
conn = sqlite3.connect('JORDANS.db')
 
# define the table and columns
table_name = 'INSTRUCTOR'
attribute_list = ['ID', 'FNAME' , 'LNAME' ,'CITY','CCODE' ]

#reading the CSV file 
file_path = '/home/jordans/Database/INSTRUCTOR.csv'
df = pd.read_csv(file_path, names = attribute_list)

#loading the select data to our table
df.to_sql(table_name, conn, if_exists = 'replace', index = 'false')
print('Table is ready') 

#viewing all the data in table
query_statement = f"SELECT * FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output) 

#viewing only column FNAME
query_statement = f"SELECT FNAME FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

#viewing the total number of entriwes in the in table
query_statement = f"SELECT COUNT(*) FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# close the connexion to JORDANS.db 
conn.close() 
