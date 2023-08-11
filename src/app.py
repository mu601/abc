# py -m src.app
from src.functions import *
from database.database import *

if __name__ == '__main__':

    if mydb != None:

        while True:

            print('#################### Main Menu ################################')

            response = int(input('\n Select option:\n\n\t 0 - EXIT app \n\t 1 - PRINT product menu options\n\t 2 - PRINT order menu options \n\t 3 - PRINT courier menu options ' ))
            clear_terminal()
            if response == 0:
                break
            elif response == 1:

                while True:

                    print('\n#################### Products Menu ################################')

                    response = int(input('\n Select option:\n\n\t 0 - RETURN to main menu \n\t 1 - PRINT products list \n\t 2 - CREATE new product \n\t 3 - UPDATE existing product \n\t 4 - DELETE product\n '))
                    
                    clear_terminal()

                    if response == 0:
                        # Return to main menu
                        break
                    elif response == 1:
                        print('\n')
                        display_table('products', ['product_id', 'product_name', 'product_price'] )
                    
                    elif response == 2:
                        # Create product
                        item = input('Enter name of product ')
                        price = input('Enter price of product ')
                        add_item(item, price, 'products', ['product_id', 'product_name', 'product_price'])

                    elif response == 3:
                        # update product
                        print('\n')
                        display_table('products', ['product_id', 'product_name', 'product_price'] )
                            
                        id = enter_id('products', 'product_id', 'Enter the id of product you want to update? ')

                        if id != None: 
                            update_name = input('Enter name to update item ')
                            update_price = input('Enter price to update item ')

                            current_record = search_record('products', 'product_id', id)

                            # if user inputs empty value then record stays the same
                            if update_name == '':
                                update_name = current_record[1]
                            if update_price == '':
                                update_price = float(current_record[2])

                            update_item(id, update_name, update_price, 'products', ['product_id', 'product_name', 'product_price'])
                            update_message('Item has now been updated ')

                    elif response == 4:
                        # delete product
                        print('\n')
                        display_table('products', ['product_id', 'product_name', 'product_price'] )

                        id = enter_id('products', 'product_id', 'Enter the id of item you want to delete? ')
                        if id != None: 
                            delete_item(id, 'products', ['product_id', 'product_name', 'product_price'] )
                            update_message('Item has now been deleted ')
                    
                    else: 
                        print('Enter one value from 0 to 4')

            elif response == 2:
                while True:

                    print('\n#################### Orders Menu ################################')

                    response = int(input('\n Select option:\n\n\t 0 - RETURN to main menu \n\t 1 - PRINT order dictionary \n\t 2 - GET customer inputs \n\t 3 - UPDATE existing status \n\t 4 - UPDATE existing order \n\t 5 - DELETE order \n\t '))

                    col_names = ['order_id', 'customer_name', 'customer_address', 'customer_phone', 'courier_id', 'status', 'product_items' ]
             

                    clear_terminal()

                    if response == 0:

                        # Back to main menu
                        break
                    elif response == 1:

                        # Print orders list
                        print('\n')
                        display_order_table('orders', col_names )
          
                    elif response == 2:

                        # Get customer inputs
                        customer_order = get_customer_info()

                        add_item_to_order(customer_order[0], customer_order[1], customer_order[2], customer_order[3], customer_order[4], customer_order[5], 'orders', col_names )
                        update_message('New order has now been added')

                    elif response == 3:

                        # Update order status
                        display_order_table('orders', col_names )
                        id = enter_id('orders', 'order_id', 'Enter id of the order status you want to change ')

                        if id != None:
                            order_status = get_order_status()
                            update_order_status(id, order_status)
                            update_message('Order status has been update ')

                    elif response == 4:

                        # Update order
                        display_order_table('orders', col_names )

                        id = enter_id('orders', 'order_id', 'Enter id of the order you want to update ')

                        if id != None:
                            customer_order = get_customer_info()
                            current_record = search_record('orders', 'order_id', id)
                                
                            if customer_order[0] != '':
                                updated_name = customer_order[0]
                            else:
                                updated_name = current_record[1]
                            if customer_order[1] != '':
                                updated_address = customer_order[1]
                            else:
                                updated_address = current_record[2]
                            if customer_order[2] != '':
                                updated_phone = customer_order[2]
                            else:
                                updated_phone = current_record[3]
                            if customer_order[3] != '':
                                updated_courier= customer_order[3]
                            else:
                                updated_courier = current_record[4]
                            if customer_order[4] == 'ready' or customer_order[4] == 'preparing':
                                updated_status = customer_order[4]                            
                            else:
                                updated_status = current_record[5]
                            if customer_order[5] != '':
                                updated_items = customer_order[5]
                            else:
                                updated_items = current_record[6]
                            
                            update_order(id, updated_name, updated_address, updated_phone, updated_courier, updated_status, updated_items, 'orders', col_names)
                            update_message('Changes has now been made to item')

                    elif response == 5:

                        # Delete order
                        print('\n')
                        display_order_table('orders', col_names )
                        id = enter_id('orders', 'order_id', 'Enter id of the order you want to delete ')

                        if id != None:
                            delete_item(id, 'orders', col_names )
                            update_message('Order has now been deleted')

                    else: 
                        print('Enter one value from 0 to 5')
            elif response == 3:

                while True:
            
                    print('\n#################### Courier Menu ################################')

                    response = int(input('\n Select option:\n\n\t 0 - RETURN to main menu \n\t 1 - PRINT courier list \n\t 2 - CREATE new courier \n\t 3 - UPDATE courier \n\t 4 - DELETE courier \n\t '))

                    clear_terminal()

                    if response == 0:

                        # Back to main menu
                        break
                    elif response == 1:

                        # Print couiers list
                        print('\n')
                        display_table('couriers', ['courier_id', 'courier_name', 'courier_phone'] )
                    elif response == 2:
                        name = input('Enter name of courier ')
                        phone = input('Enter phone of courier ')
                        add_item(name, phone, 'couriers', ['courier_id', 'courier_name', 'courier_phone'])

                    elif response == 3:

                        # Create existing courier
                        print('\n')
                        display_table('couriers', ['courier_id', 'courier_name', 'courier_phone'] )
                            
                        id = enter_id('couriers', 'courier_id', 'Enter the id of item you courier to update? ')

                        if id != None: 
                            update_name = input('Enter name to update courier ')
                            update_phone = input('Enter phone to update ')

                            current_record = search_record('couriers', 'courier_id', id)

                            # if user inputs empty value then record stays the same
                            if update_name == '':
                                update_name = current_record[1]
                            if update_phone == '':
                                update_phone = current_record[2]

                            update_item(id, update_name, update_phone, 'couriers', ['courier_id', 'courier_name', 'courier_phone'] )
                            update_message('Item has now been updated ')

                    elif response == 4:
                    
                        print('\n')
                        display_table('couriers', ['courier_id', 'courier_name', 'courier_phone'] )

                        id = enter_id('couriers', 'courier_id', 'Enter the id of courier you want to delete? ')

                        if id != None: 
                            delete_item(id, 'couriers', ['courier_id', 'courier_name', 'courier_phone'] )
                            update_message('Item has now been deleted ')
                    
                    else: 
                        print('Enter one value from 0 to 4')

            else:
                print('Enter one value from 0 to 3')

close_connection()
print('\nCONNECTION CLOSED\n')

