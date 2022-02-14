
import mysql.connector

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="#####",
    database="testdb"
)

my_cursor = my_db.cursor()

def insert_concert_from_user_input():
    datum = input('Datum: ')
    land  = input('Land: ')
    stadt = input('Stadt: ')

    val = f'"{datum}", "{land}", "{stadt}"'
    sql = f'INSERT INTO konzerte VALUE ({val})'

    my_cursor.execute(sql)
    my_db.commit()

def show_all_data():
    my_cursor.execute("SELECT * FROM konzerte")
    result = my_cursor.fetchall()

    for _ in result:
        print(_)


insert_concert_from_user_input()

show_all_data()
