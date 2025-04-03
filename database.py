import mysql.connector 
from mysql.connector import Error 

class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = self.database
            )

            print("MySQL connection is established")
            return self.connection

        except Error as e:
            print(f"Error conecting to Mysql: {e}")
            return None

    def closed(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("MySQL connection is closed")


# initialize a reusable collection object 

db = Database(
    host = 'localhost',
    user = 'root',
    password = 'Black99raiser%*',
    database = 'lms'
)
