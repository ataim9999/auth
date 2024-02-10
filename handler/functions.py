import mysql.connector
import say

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
    


