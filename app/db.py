import mysql.connector

class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='*Aa1131318#',
            database='traffic_violation_system'  
        )
        self.cursor = self.conn.cursor(dictionary=True)

    def fetch_user_by_username(self, username):
        query = 'SELECT * FROM users WHERE username = %s'
        self.cursor.execute(query, (username,))
        return self.cursor.fetchone()

    def create_user(self, username, password, email, full_name, role, phone=None, address=None, license_number=None):
        query = """
        INSERT INTO users (username, password, email, full_name, role, phone, address, license_number)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        self.cursor.execute(query, (username, password, email, full_name, role, phone, address, license_number))
        self.conn.commit()
        return self.cursor.lastrowid

    def update_user(self, user_id, **kwargs):
        if not kwargs:
            return  # nothing to update
        fields = ', '.join(f"{key} = %s" for key in kwargs.keys())
        values = list(kwargs.values()) + [user_id]
        query = f"UPDATE users SET {fields} WHERE user_id = %s"
        self.cursor.execute(query, values)
        self.conn.commit()

    def delete_user(self, user_id):
        query = "DELETE FROM users WHERE user_id = %s"
        self.cursor.execute(query, (user_id,))
        self.conn.commit()

    # Admin statistics methods
    def fetch_users_count(self):
        self.cursor.execute("SELECT COUNT(*) AS total FROM users WHERE is_active = 1")
        return self.cursor.fetchone()['total']

    def fetch_officers_count(self):
        self.cursor.execute("SELECT COUNT(*) AS total FROM officers WHERE is_active = 1")
        return self.cursor.fetchone()['total']

    def fetch_violations_count(self):
        self.cursor.execute("SELECT COUNT(*) AS total FROM violations")
        return self.cursor.fetchone()['total']

    def fetch_total_fines(self):
        self.cursor.execute("SELECT SUM(penalty_amount) AS total_fines FROM violations WHERE status = 'paid'")
        result = self.cursor.fetchone()['total_fines']
        return result if result else 0

    def fetch_all_users(self):
        self.cursor.execute("SELECT * FROM users")
        return self.cursor.fetchall()

    def fetch_officer_by_badge(self, badge_number):
        query = "SELECT * FROM officers WHERE badge_number = %s"
        self.cursor.execute(query, (badge_number,))
        return self.cursor.fetchone()

    def fetch_violations_by_vehicle(self, vehicle_id):
        query = "SELECT * FROM violations WHERE vehicle_id = %s"
        self.cursor.execute(query, (vehicle_id,))
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.conn.close()
