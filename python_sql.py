# Youtube websie used: https://www.youtube.com/watch?v=xY54Emo8rQM

import pandas as pd
import sqlite3 as db

conn = db.connect('sqlite.db')
cur = conn.cursor()


def create_customer_table():
    cur.execute(f"CREATE TABLE IF NOT EXISTS customers (customer_id INTEGER PRIMARY KEY, first_name NVARCHAR(50), last_name NVARCHAR(50), p_number NVARCHAR(12), address NVARCHAR(50))")

def add_customer(cu_id, first_name, last_name, phone_num, address):
    cur.execute(f"INSERT INTO customers(rowid, first_name, last_name, p_number, address) VALUES('{cu_id}', '{first_name}', '{last_name}', '{phone_num}', '{address}')")

def update_last_name(cu_id, new_name):
    cur.execute(f"UPDATE customers SET last_name = '{new_name}' WHERE customer_id = {cu_id}")

def show_table():
    cur.execute("SELECT * FROM customers")
    for row in cur.fetchall():
        print(row)

def commit():
    print("Commiot")
    conn.commit()

create_customer_table()
show_table()
add_customer(1, 'brian', 'bawden', '7734492935', '123 abc street')
show_table()
commit()
