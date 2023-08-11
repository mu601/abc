import os
import json
from database.database import collect_ids, display_table

def save_list(filename, list):
    container = {filename:[]}

    with open(f'./data/{filename}.json', 'w') as f:

        for item in list:
            container[filename].append(item)
        json.dump(container, f)
    

def load_list (filename):

    list = []

    # Opening JSON file
    with open(f'./data/{filename}.json', 'r') as f:
  
        items = json.load(f)
  
        # Iterating through the json list
        for item in items[filename]:
            list.append(item)

    return list

def clear_terminal():
    os.system('cls')

def print_list(data):
    for index, product in enumerate(data):
        print(index, product)

def get_order_status():
    while True:
        order_status = input("Enter 'r' for ready or 'p' for preparing ")
        
        if order_status == 'r' or order_status == 'preparing':
            return 'ready'
        elif order_status == 'p':
            return 'preparing'
        else:
            print("Invalid input. Please enter either 'r' for ready or 'p' for preparing.")

def get_customer_info():
    customer_name = input('Enter your name ')
    customer_address = input('Enter your address ')
    customer_phone = input('Enter you phone number ')
    assigned_courier = assign_courier()
    order_status = get_order_status()

    display_table('products', ['product_id', 'product_name', 'product_price'] )
    
    items = input('Enter the id of product, if more then one then separate with commas ')

    return [customer_name, customer_address, customer_phone, assigned_courier, order_status, items]

def assign_courier():
    display_table('couriers', ['courier_id', 'courier_name', 'courier_phone'] )
    id = enter_id('couriers', 'courier_id', 'Enter the id of item you courier to update? ')
    return id

def enter_id(table, col_id, text = 'Enter id ' ): 
    ids = collect_ids(table, col_id)
    while True:
        try:
            id = int(input(text))
            if id not in ids:
                raise IndexError() 
            return id
        except IndexError as e:
            print(f'\nThe id {id} does not exist in this {table} table. {e}')
        except ValueError as e:
            print(f'\nIncorrect value entered. You need to enter a number. {e}')

def enter_index(container, type, text = 'Enter index value ' ): 
    while True:
        try:
            index = int(input(text))
            if index > len(container):
                raise IndexError() 
            return index
        except IndexError as e:
            print(f'\nThe index {index} does not exist in this {type} data structure. {e}')
        except ValueError as e:
            print(f'\nIncorrect value entered. You need to enter a number. {e}')


def update_message(message):
    print(f'\n{message}')

# Loading products list from text file
products_list = load_list("products")
# Loading orders list from text file
orders_list = load_list('orders')
# Loading orders list from text file
couriers_list = load_list("couriers")

