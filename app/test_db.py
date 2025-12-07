import sys
import os

# Add the project root (one level up from current file) to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.db import Database

def test_fetch_user(username):
    db = Database()
    user = db.fetch_user_by_username(username)
    db.close()

    if user:
        print("User found:", user)
    else:
        print("No user found with username:", username)

if __name__ == "__main__":
    username = input("Enter username to test: ")
    test_fetch_user(username)
