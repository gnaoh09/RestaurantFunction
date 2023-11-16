import mysql.connector as mysql
from datetime import datetime
from tabulate import tabulate

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "lehoanglehongphong",
    database = "hoangnguyen"
    )
current_time = datetime.now()
cursor = db.cursor()

def show_menu():
    print("1. Reservation ")
    print("2. Display ")
    print("3. Order ")
    print("4. Exit")

def handle_option():
    bool = False
    while bool == False:
        option = input()
        if option == "1":
            bool = True
            option1()
        elif option == "2":
            bool = True
            option2()
        elif option == "3":
            bool = True
            option3()
        elif option == "4":
            bool =True
            exit_program()
        else:
            print("Invalid option! Please input again!")

def option1():
    print("You selected Option 1")
    #user reserve table 
    date = current_time
    no_of_pax = input("number of passengers: ")
    insert = """
    insert into reservation( date_time, no_of_pax)
    values ( %s, %s)
    """
    values = (date, no_of_pax)
    cursor.execute(insert, values)

    db.commit()
def option2():
    print("You selected Option 2")
    # Define the SQL query to select all records from the table
    query = """SELECT
        t.*,
        w.waiter_name,
        tbl.location,
        om.menu_item_id,
        m.item_des,
        om.quantity,
        m.price,
        m.availability
  
        FROM
        table_order AS t
        join waiter as w on w.waiter_id = t.waiter_id
        join tbl as tbl on tbl.table_id = t.table_id
        JOIN order_menu_item AS om ON t.table_id = om.order_id
        JOIN menu_item AS m ON m.menu_item_id = om.menu_item_id;"""

        # Execute the query
    cursor.execute(query)

    # Fetch all the rows from the result set
    rows = cursor.fetchall()

    # Calculate the maximum width for each column
    columns = [desc[0] for desc in cursor.description]

    # Calculate the maximum width for each column
    column_widths = [max(len(str(value)) for value in column) for column in zip(columns, *rows)]
    # Print the table
    table_data = [columns] + list(rows)
    print(tabulate(table_data, headers="firstrow", colalign=("left",) * len(columns), tablefmt="plain"))

    # Close the cursor and connection
    cursor.close()
    db.close()
def option3():
    print("You selected Option 3")
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


def exit_program():
    print("Exiting the program")
    # Add any cleanup code or additional logic here
    quit()

# Main program loop

show_menu()
handle_option()