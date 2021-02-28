import mysql.connector

from mysql.connector import Error

# write function that handles creation of connection
def create_connection(host_name, user_name, user_password, db_name):
    connector = None
    # wrap the following into a try except statement
    connection = mysql.connector.connect(
        host=host_name,
        user=user_name,
        passwd=user_password,
        database=db_name
    )

    print("Connection to Mysql DB successfull")

    return connection

#creation of contactData Class
class contactData():
    #sample function defined for usage
    def contactInfo(self):
        return 0
    def menuOption(self):
        return 0
    def add_contact(self):
        sql_insert_query = """Insert into Contact """
        return 0
    def remove_contact(self, col):
        sql_remove_query = """Delete from Contact where id = col"""
        return 0
    def update_contact(self, col, newInfo):
        sql_update_query = """Update Contact set Name = newInfo where id = col"""
        cursor.execute(sql_update_query)
        connection.commit()
        print('Record updated successfully')
        return 0
    def alpha(self):
        return 0
    def byDate(self):
        return 0
    def allContacts(self):
        return 0
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
    def print_menu(self, menu_option):
        for i in menu_option:
            if menu_option == 'q':
                break
            if menu_option == 'a':
                self.add_contact(self,contact)
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
contactData()
print_menu()
print(result)
