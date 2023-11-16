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