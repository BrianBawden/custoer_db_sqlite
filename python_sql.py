# Import pandas and sqlite3 to help interact with the database
import pandas as pd
import sqlite3 as db

# Set the variable 'conn' to the sqlite database with db
conn = db.connect('sqlite.db')
# Set the variable 'cur' to use as the cursor which will allow me to execute SQL commands in Python.
cur = conn.cursor()


def create_table(table_name):

    """ 
    table_name = str

    This function will create a new table based on the name passed to the function when it is called.
    """

    cur.execute(f"CREATE TABLE IF NOT EXISTS {table_name}")


def alter_table(table_name, column_name, datatype):
    
    """
    table_name = str
    column_name = str
    datatype = str

    The alter_table function is how new columns are added to a table and takes three parameters: 
    """

    cur.execute(f"ALTER TABLE {table_name} ADD {column_name} {datatype}")


def add_customer(cu_id, first_name, last_name, phone_num, address):

    """
    cu_id = integer
    first_name = NVARCHAR(50)
    first_name = NVARCHAR(50)
    p_number = NVARCHAR(50)
    address = NVARCHAR(50)
    date = TEXT 

    Add new customer to the customers database.
    """
    
    cur.execute(f"INSERT INTO customers(rowid, first_name, last_name, p_number, address) VALUES('{cu_id}', '{first_name}', '{last_name}', '{phone_num}', '{address}')")


def update_customer(cu_id, column_name, new_info):

    """
    cu_id = int
    column_name = str
    new_info = str

    update_customer is used to edit information of a customer and takes three arguments.
    """
    
    cur.execute(f"UPDATE customers SET {column_name} = '{new_info}' WHERE customer_id = {cu_id}")

def show_table():

    """
    prints out all the data in the table. 
    """
    
    cur.execute("SELECT * FROM customers")
    for row in cur.fetchall():
        print(row)

def commit():
    print("Commit")
    conn.commit()

def view_table_names():
    data = pd.read_sql_query('SELECT name FROM sqlite_master WHERE type="table";', conn)
    print(data.head())

def view_column_name(table_name):
    cur.execute(f"PRAGMA table_info({table_name});")
    for col in  cur.fetchall():
        print(col)
