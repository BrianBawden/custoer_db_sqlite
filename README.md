# Overview

For this project I wanted to practice writing code that would allow me to work with a database through the use of functions. This would help reduce typing long repetitive commands by only having to call a function with a few parameters.

I started by writing a function called 'create_table' with the table name as a parameter. This function will create the table. Then to add columns to the table I wrote the 'alter_table' function to add columns. The table I am using is a customer database so I plan to add  customer information to the table with the 'add_customer' function. To demonstrate the ability to edit information in the table I wrote the 'update_customer' function which takes three arguments. 

In order to view information from the database I wrote functions: 'show_table', 'commit', 'view_table_names', and 'view_column_name.' The commit function is more to save the changes to the database as needed. If the commit function is not run the changes are not saved to the database. 


[Software Demo Video]([http://youtube.link.goes.here](https://youtu.be/1qaWrK4KWpc))

# Relational Database

For this database I created a table called 'customers' which has six columns: 

* customer_id, INTEGER
* first_name, NVARCHAR(50)
* last_name, NVARCHAR(50)
* p_number, NVARCHAR(50)
* address, NVARCHAR(50)
* date, TEXT

# Development Environment

The tools I used to develop my program were:

* VScode
* Python 3.10.4
* sqlite3
* pandas

# Useful Websites

* [Using SQL with Python](https://www.youtube.com/watch?v=xY54Emo8rQM)
* [Udemy SQL Bootcamp](https://www.udemy.com/course/the-complete-sql-bootcamp/learn/lecture/19242668?start=1#content)
* [Beginners Guide to SQLite](https://www.youtube.com/watch?v=5LpotBtmZZs)

# Future Work


* Second table with appointment information which can join with customers to keep track of when each customer was seen last.
* A function to show the user specific data from multiple tables.
* Change the customer_id and date data to automatically generate when a new row is created. 
