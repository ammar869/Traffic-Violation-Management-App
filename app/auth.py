from app.db import Database
import hashlib

class Auth:
    def __init__(self):
        self.db = Database()

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def login(self, username, password, role):
        hashed_password = self.hash_password(password)

        sql = """
        SELECT * FROM users
        WHERE username = %s AND password = %s AND role = %s AND is_active = TRUE
        """

        self.db.cursor.execute(sql, (username, hashed_password, role))
        return self.db.cursor.fetchone()

    def close(self):
        self.db.close()
