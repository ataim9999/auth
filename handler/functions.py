#*-------------------------------------------------*#

import mysql.connector
import say

#*-------------------------------------------------*#

# function to connect to the mysql database
def connect():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="auth"
        )

        say.say("Connection successful", "success")

        return mydb
    except mysql.connector.Error as err:
        say.say(f"Error: {err}", "error")
        return None
    
#*-------------------------------------------------*#

# function to create a table if it doesn't exist
def TableIfNone(cursor):
    try:
        cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(30), password VARCHAR(50))")
        say.say("Table created", "success")
    except mysql.connector.Error as err:
        say.say(f"Error creating table: {err}", "error")

#*-------------------------------------------------*#

# return users from table
def getAllUsers(cursor):
    try:
        cursor.execute("SELECT * FROM users")
    except mysql.connector.Error as err:
        say.say(f"Error getting users: {err}", "error")

#*-------------------------------------------------*#
        
# function to hash password
def hash(password):
    import hashlib
    hashPass = hashlib.sha256(password.encode()).hexdigest()
    return hashPass

#*-------------------------------------------------*#

# function to add new user to db
# hash password
def addUser(connection, name, hashPass):
    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO users (name, password) VALUES (%s, %s)", (name, hashPass))
        connection.commit()
        cursor.close()
        say.say("Registration successful", "success")
    except mysql.connector.Error as err:
        say.say(f"Error adding user: {err}", "error")
    
#*-------------------------------------------------*#
        
#function to clear info in db
def clearDB(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM users")
        connection.commit()
        cursor.close()
        say.say("Database cleared", "success")
    except mysql.connector.Error as err:
        say.say(f"Error clearing database: {err}", "error")

#*-------------------------------------------------*#

