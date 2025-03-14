import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="127.0.0.1",  # XAMPP MySQL host
        port=3308,
        user="root",        # Default user
        password="",        # No password in XAMPP
        database="moviesrec"
    )
