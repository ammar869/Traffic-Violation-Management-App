1. Secure Login System

Implement password hashing (bcrypt or hashlib) to safely store & verify passwords.

Build a Tkinter login UI that checks credentials against your database securely.

2. Role-Based Navigation

After login, route users to different panels based on their role (admin, police, user).

Design separate UI frames for each panel with role-specific features.

3. Core Functionalities by Role

Admin: Manage users, officers, violation types, reports.

Police: Log violations, view assigned cases, update statuses.

User: View own violations, pay fines, appeal violations.

4. Modularize Codebase

Organize your code into clean modules: DB access, UI components, business logic.

Use classes and functions that you can reuse and maintain easily.

5. Incremental Testing

After each feature, test thoroughly with sample data.

Make sure DB reads/writes are accurate and UI responds correctly.

6. Polish & Extras

Add features like search, filters, notifications.

Improve UX with validation, error handling, and neat layouts.



| Role    | Username | Plain Password | Notes          |
| ------- | -------- | -------------- | -------------- |
| admin   | admin    | admin123       | SHA-256 hashed |
| officer | officer1 | officer123     | SHA-256 hashed |
| officer | officer2 | officer123     | SHA-256 hashed |
| user    | user1    | user123        | SHA-256 hashed |
| user    | user2    | user123        | SHA-256 hashed |


(DB project) PS C:\Users\Ammar\Documents\DB project> cd "C:\Users\Ammar\Documents\DB project"
>> python -u "app\login_gui.py"
>>

Correct

(DB project) PS C:\Users\Ammar\Documents\DB project> cd "C:\Users\Ammar\Documents\DB project"
>> python -m app.login_gui


previous code
import tkinter as tk
from tkinter import messagebox
from app.auth import Auth

class LoginGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Traffic Violation System - Login")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        # Title
        tk.Label(root, text="Traffic Violation System", font=("Arial", 18, "bold")).pack(pady=10)

        # Role selection
        tk.Label(root, text="Select Role", font=("Arial", 12)).pack()

        self.role_var = tk.StringVar(value="admin")

        role_frame = tk.Frame(root)
        role_frame.pack(pady=5)

        tk.Radiobutton(role_frame, text="Admin", variable=self.role_var, value="admin").pack(side="left", padx=5)
        tk.Radiobutton(role_frame, text="Officer", variable=self.role_var, value="police").pack(side="left", padx=5)
        tk.Radiobutton(role_frame, text="User", variable=self.role_var, value="user").pack(side="left", padx=5)

        # Username
        tk.Label(root, text="Username").pack(pady=(10, 0))
        self.username_entry = tk.Entry(root, width=30)
        self.username_entry.pack()

        # Password
        tk.Label(root, text="Password").pack(pady=(10, 0))
        self.password_entry = tk.Entry(root, width=30, show="*")
        self.password_entry.pack()

        # Login Button
        tk.Button(root, text="Login", width=20, command=self.login).pack(pady=20)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        role = self.role_var.get()

        if not username or not password:
            messagebox.showerror("Error", "Please fill all fields")
            return

        auth = Auth()
        user = auth.login(username, password, role)

        if user:
            messagebox.showinfo("Login Success", f"Welcome {user['full_name']}")
        else:
            messagebox.showerror("Login Failed", "Wrong username or password")


if __name__ == "__main__":
    root = tk.Tk()
    app = LoginGUI(root)
    root.mainloop()



Login Page 
