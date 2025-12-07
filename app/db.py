import mysql.connector

class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost',       # Your MySQL host
            user='root',       # Your MySQL username
            password='*Aa1131318#',   # Your MySQL password
            database='traffic_violation_system '      # Your MySQL database name
        )
        self.cursor = self.conn.cursor(dictionary=True)

    def fetch_user_by_username(self, username):
        query = 'SELECT * FROM users WHERE username = %s'
        self.cursor.execute(query, (username,))
        return self.cursor.fetchone()

    def close(self):
        self.cursor.close()
        self.conn.close()
