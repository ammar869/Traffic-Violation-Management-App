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
