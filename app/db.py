import mysql.connector

class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',        # <-- Replace with your MySQL username
            password='*Aa1131318#',    # <-- Replace with your MySQL password
            database='traffic_voilation_system'       # <-- Replace with your database name
        )
        self.cursor = self.conn.cursor(dictionary=True)

    def fetch_user_by_username(self, username):
        query = "SELECT * FROM users WHERE username = %s"
        self.cursor.execute(query, (username,))
        return self.cursor.fetchone()

    def close(self):
        self.cursor.close()
        self.conn.close()
