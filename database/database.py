import pymysql
import os
from dotenv import load_dotenv

load_dotenv()
host_name = os.environ.get("mysql_host")
database_name = os.environ.get("mysql_db")
user_name = os.environ.get("mysql_user")
user_password = os.environ.get("mysql_pass")

mydb = None

def get_connection():
    mydb = pymysql.connect(
    host = host_name, database = database_name, 
    user = user_name, password = user_password 
    )
    return mydb

try:
    print('\nOPENING CONNECTION...\n')

    mydb = get_connection()

except Exception as e:
    print('Unable to establish connection', e)
    

if mydb != None:
    mydb = get_connection()

def convert_to_sql_string(array_of_cols):
    sql_col = ''
    
    for i in array_of_cols:
        if i == array_of_cols[-1]:
            sql_col += i
        else:
            sql_col += i + ', '
    return sql_col


def display_table(table, array_of_cols):

    cursor = mydb.cursor()

    sql_col = convert_to_sql_string(array_of_cols)

    cursor.execute(f'SELECT {sql_col} FROM {table}')
    # Fetch all the rows into memory
    rows = cursor.fetchall()
    
    # y=[]

    print(rows)

    for row in rows:
        # y.append((array_of_cols[0], array_of_cols[1]))
        print(row)
        if len(rows):
            print(f'id: {row[0]}    [ {array_of_cols[1]}: {str(row[1])}, {array_of_cols[2]}: {row[2]} ]')
        else:
            print(f'id: {row[0]}   [{array_of_cols[1]}: {row[1]}, {array_of_cols[2]}: {row[2]}, {array_of_cols[3]}: {row[3]}, {array_of_cols[4]}: {row[4]}, {array_of_cols[5]}: {row[5]}, {array_of_cols[6]}: {row[6]}]')            


    # print(y)
    

def display_order_table(table, array_of_cols):
    
    cursor = mydb.cursor()
    print(cursor)

    sql_col = convert_to_sql_string(array_of_cols)

    cursor.execute(f'SELECT {sql_col} FROM {table}')
    # Fetch all the rows into memory
    rows = cursor.fetchall()
    
    for row in rows:
        # print(row)
        print(f'id: {row[0]}   [{array_of_cols[1]}: {row[1]}, {array_of_cols[2]}: {row[2]}, {array_of_cols[3]}: {row[3]}, {array_of_cols[4]}: {row[4]}, {array_of_cols[5]}: {row[5]}, {array_of_cols[6]}: {row[6]}]')       

def collect_ids(table, col_id ):

    cursor = mydb.cursor()

    cursor.execute(f'SELECT {col_id} FROM {table}')
    # Fetch all the rows into memory
    rows = cursor.fetchall()

    list = [] 
    for row in rows:
        list.append(row[0])

    return list

def update_item(id, name, price, table, array_of_cols):

    cursor = mydb.cursor()

    # delete record
    sql = f'update {table} set {array_of_cols[1]} = %s, {array_of_cols[2]} = %s WHERE {array_of_cols[0]} = %s'
    cursor.execute(sql, (name, price, id))
    mydb.commit()
    cursor.close()

def update_order(id, name, address, phone, courier, status, items, table, array_of_cols):
    
    cursor = mydb.cursor()

    # delete record
    sql = f'update {table} set {array_of_cols[1]} = %s, {array_of_cols[2]} = %s, {array_of_cols[3]} = %s, {array_of_cols[4]} = %s, {array_of_cols[5]} = %s, {array_of_cols[6]} = %s  WHERE {array_of_cols[0]} = %s'
    cursor.execute(sql, (name, address, phone, courier, status, items, id))
    mydb.commit()
    cursor.close()

def update_order_status(id, order_status ):
    
    cursor = mydb.cursor()

    # delete record
    sql = f'update orders set status = %s  WHERE order_id = %s'
    cursor.execute(sql, (order_status, id))
    mydb.commit()
    cursor.close()

def add_item( name, price, table, array_of_cols ):
    
    cursor = mydb.cursor()
    # Insert a new record
    sql = f'INSERT INTO {table} ({array_of_cols[1]}, {array_of_cols[2]}) VALUES (%s, %s)'
    cursor.execute(sql, (name, price))
    # Commit the record
    mydb.commit()

    cursor.close()   


def add_item_to_order(name, address, phone, courier_id, status, items, table, array_of_cols ):
    
    cursor = mydb.cursor()

    # Insert a new record
    sql = f'INSERT INTO {table} ({array_of_cols[1]}, {array_of_cols[2]}, {array_of_cols[3]}, {array_of_cols[4]}, {array_of_cols[5]}, {array_of_cols[6]}) VALUES (%s, %s, %s, %s, %s, %s)'
    cursor.execute(sql, (name, address, phone, courier_id, status, items))
    # Commit the record
    mydb.commit()
    cursor.close()

def add_item( name, price, table, array_of_cols ):
    
    cursor = mydb.cursor()
    # Insert a new record
    sql = f'INSERT INTO {table} ({array_of_cols[1]}, {array_of_cols[2]}) VALUES (%s, %s)'
    cursor.execute(sql, (name, price))
    # Commit the record
    mydb.commit()

    cursor.close()    

def delete_item(id, table, array_of_cols):

    cursor = mydb.cursor()
    # delete record
    sql = f'DELETE FROM {table} WHERE {array_of_cols[0]} = %s'
    cursor.execute(sql, id)
    mydb.commit()

    cursor.close()

def search_record(table, col_id, user_input):
    cursor = mydb.cursor()

    cursor.execute(f'SELECT * FROM {table} WHERE {col_id} = {user_input}')
    # Fetch all the rows into memory
    rows = cursor.fetchall()
    # print('hello there', len(rows[0]))

    list = []
    for i in range(len(rows[0])):
        list.append(rows[0][i])

    # print(list)
    return list    

def close_connection():
    mydb.close()
