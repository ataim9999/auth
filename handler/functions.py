#*-------------------------------------------------*#

import mysql.connector
import say

import hashlib

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
        cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(30), password VARCHAR(50), role VARCHAR(10))")
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
def addUser(connection, name, hashPass):
    try:
        role = "user"
        cursor = connection.cursor()
        cursor.execute("INSERT INTO users (name, password, role) VALUES (%s, %s, %s)", (name, hashPass, role))
        connection.commit()
        cursor.close()
        say.say("Registration successful", "success")
    except mysql.connector.Error as err:
        say.say(f"Error adding user: {err}", "error")
    
#*-------------------------------------------------*#
        
# function to login user
def login(connection, name, password):
    try:
        cursor = connection.cursor()
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        cursor.execute("SELECT * FROM users WHERE name = %s", (name,))
        user = cursor.fetchone()
        cursor.close()

        if name == user[1] and hashed_password == user[2]:
            return True
        else:
            return False
    except mysql.connector.Error as err:
        say.say(f"Error logging in: {err}", "error")


#*-------------------------------------------------*#

# function to add user to admin
def addAdmin(connection, name, role):
    try:
        cursor = connection.cursor()
        cursor.execute("UPDATE users SET role = %s WHERE name = %s", (role, name))
        connection.commit()
        cursor.close()
        say.say("Set admin successfully", "success")
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

