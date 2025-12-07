from app.db import Database
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.db import Database
def test_fetch_user(username):
    db = Database()
    user = db.fetch_user_by_username(username)
    db.close()

    if user:
        print("User found:")
        print(user)
    else:
        print("No user found with username:", username)

if __name__ == "__main__":
    test_username = input("Enter username to fetch: ")
    test_fetch_user(test_username)
