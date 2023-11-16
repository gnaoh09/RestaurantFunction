import mysql.connector as mysql
from datetime import datetime

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "lehoanglehongphong",
    database = "hoangnguyen"
)
current_time = datetime.now()
cursor = db.cursor()
bool  = False

while bool == False:
        a = False
        #waiter input cus order
        order_id = input("order id: ")
        date_time = current_time
        table_id = input("table: ")
        waiter_id = input("waiter no: ")

        insert = """
        insert into table_order(order_id, date_time, table_id, waiter_id)
        values (%s, %s, %s, %s)
        """
        values =(order_id, date_time, table_id,waiter_id)
        cursor.execute(insert, values)

        #order from menu
        menu_item_id = input("item id: ")
        quantity = input("quantity: ")
        insert1 = """
        insert into order_menu_item (order_id, menu_item_id, quantity)
        values (%s, %s, %s)
        """
        values1 = (order_id, menu_item_id,quantity)
        cursor.execute(insert1,values1)
        db.commit()
        while a == False:
            user_input = input("Do you want to order more? (y or n): ")
            if user_input.lower() == "n":
                    a = True
                    bool = True
                    
            elif user_input.lower() == "y":
                    a = True
                    bool = False
            else:
                    a = False
                    print("Invalid input! Only y or n! Please input again!")

db.close()
