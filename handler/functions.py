#*-------------------------------------------------*#

import mysql.connector
import say

#*-------------------------------------------------*#

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

def TableIfNone(cursor):
    try:
        cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(30), password VARCHAR(50))")
        say.say("Table created", "success")
    except mysql.connector.Error as err:
        say.say(f"Error creating table: {err}", "error")

#*-------------------------------------------------*#