# Youtube website used: https://www.youtube.com/watch?v=xY54Emo8rQM

from turtle import onclick
import pandas as pd
import sqlite3 as db

conn = db.connect('sqlite.db')
cur = conn.cursor()


def create_table(table_name):
    cur.execute(f"CREATE TABLE IF NOT EXISTS {table_name}")

def alter_table(table_name, column_name, datatype):
    cur.execute(f"ALTER TABLE {table_name} ADD {column_name} {datatype}")

def add_customer(cu_id, first_name, last_name, phone_num, address):
    cur.execute(f"INSERT INTO customers(rowid, first_name, last_name, p_number, address) VALUES('{cu_id}', '{first_name}', '{last_name}', '{phone_num}', '{address}')")

def update_last_name(cu_id, new_name):
    cur.execute(f"UPDATE customers SET last_name = '{new_name}' WHERE customer_id = {cu_id}")

def show_table():
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
    column_name = cur.execute(f"PRAGMA table_info({table_name});")
    column_name = cur.fetchall()
    print(column_name)