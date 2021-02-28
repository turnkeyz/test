import mysql.connector

from mysql.connector import Error

# write function that handles creation of connection
def create_connection(host_name, user_name, user_password, db_name):
    connector = None
    # wrap the following into a try except statement
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name)
        if connection.is_connected():
            db_inf = connection.get_server_info()
            print("connected to mysql server", db_inf)
            cursor = connection.cursor()
            cursor.execute("select database();")
            contactRecord = cursor.fetchone()
            print("you're connected to: ", contactRecord)
            contactData.print_menu()
    except Error as e:
        print("Error while connecting to mysql", e)
    return connection

#creation of contactData Class
class contactData():
    #sample function defined for usage
    def print_menu(self, menu_option):
        for i in menu_option:
            if menu_option == 'q':
                self.quit()
                break
            if menu_option == 'a':
                self.add_contact()
            elif menu_option == 'd':
                self.remove_contact()
            elif menu_option == 'u':
                self.update_contact()
            elif menu_option == 'b':
                self.alpha()
            elif menu_option == 'c':
                self.byDate()
            elif menu_option == 'o':
                print(self.allContacts())
    def add_contact(self):
        sql_insert_query = """Insert into Contact """
        return sql_insert_query
    def remove_contact(self, col):
        sql_remove_query = """Delete from Contact where id = col"""
        return sql_remove_query
    def update_contact(self, col, newInfo):
        sql_update_query = """Update Contact set Name = newInfo where id = col"""
        cursor.execute(sql_update_query)
        connection.commit()
        print('Record updated successfully')
        return sql_update_query
    def alpha(self):
        cursor = connection.cursor()
        sql = "SELECT * FROM contacts ORDER BY contactDetails"
        return sql
    def byDate(self):
        cursor = connection.cursor()
        sql = "SELECT * FROM contacts ORDER BY creationDate"
        return sql
    def allContacts(self):
        cursor = connection.cursor()
        sql = "SELECT * FROM contacts"
        return sql
    def quit(self):
        print('goodbye')
        pass
# open up connection
# this would use the mysql.connector directly, not inside a function
# connection = mysql.connector.connect(
#         host="cis3368-db.crr2rtz45qld.us-east-1.rds.amazonaws.com",
#         user=user_name,
#         passwd=user_password,
#         database=db_name
#     )
# call function to open connection
connection = create_connection("cis3368-db.c7y64olw7ex3.us-east-1.rds.amazonaws.com", "kdtelge", "Turnkey1999", "testdb")

# execute a read query on the DB - to get every row from the users table
# we need a query
query = "SELECT * FROM users"
# place to store results
result = None
# cursor to operate
cursor = connection.cursor()

cursor.execute(query)
result = cursor.fetchall()
#contactData.print_menu()
