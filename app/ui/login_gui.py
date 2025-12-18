import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.ui.admin.admin_dashboard import TVMSApp



import customtkinter as ctk
from tkinter import messagebox
from app.auth import Auth

# ===================== COLOR PALETTE =====================
DARK_BLUE = "#1E293B"
LIGHT_BG = "#F8FAFC"
BUTTON_BLUE = "#3B82F6"
WARNING_RED = "#EF4444"
SUCCESS_GREEN = "#22C55E"
MAIN_TEXT = "#0F172A"
SECONDARY_TEXT = "#64748B"


ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

class LoginGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Traffic Violation System")
        self.root.geometry("420x520")
        self.root.resizable(False, False)

        # Window background
        self.root.configure(bg=LIGHT_BG)

        # Outer Shadow Frame (for depth)
        self.shadow = ctk.CTkFrame(
            root,
            fg_color="#E5E7EB",
            corner_radius=25
        )
        self.shadow.pack(padx=15, pady=15, fill="both", expand=True)

        # Main Glass Card
        self.frame = ctk.CTkFrame(
            self.shadow,
            fg_color="white",
            corner_radius=25,
            border_width=1,
            border_color="#E2E8F0"
        )
        self.frame.pack(padx=10, pady=10, fill="both", expand=True)

        # App Title
        ctk.CTkLabel(
            self.frame,
            text="Traffic Violation System",
            font=("Poppins", 22, "bold"),
            text_color=DARK_BLUE
        ).pack(pady=(30, 10))

        # Subtitle
        ctk.CTkLabel(
            self.frame,
            text="Secure Access Portal",
            font=("Arial", 12),
            text_color=SECONDARY_TEXT
        ).pack(pady=(0, 25))

        # Role
        ctk.CTkLabel(
            self.frame,
            text="Login as",
            font=("Arial", 12, "bold"),
            text_color=MAIN_TEXT
        ).pack()

        self.role_var = ctk.StringVar(value="admin")

        self.role_frame = ctk.CTkFrame(self.frame, fg_color="transparent")
        self.role_frame.pack(pady=10)

        for text, val in [("Admin", "admin"), ("Officer", "police"), ("User", "user")]:
            ctk.CTkRadioButton(
                self.role_frame,
                text=text,
                variable=self.role_var,
                value=val,
                fg_color=BUTTON_BLUE,
                text_color=MAIN_TEXT
            ).pack(side="left", padx=8)

        # Username Field
        ctk.CTkLabel(
            self.frame,
            text="Username",
            text_color=SECONDARY_TEXT
        ).pack(anchor="w", padx=60, pady=(20, 5))

        self.username_entry = ctk.CTkEntry(
            self.frame,
            width=280,
            height=38,
            corner_radius=10,
            fg_color="#F9FAFB",
            border_color="#CBD5F5",
            text_color=MAIN_TEXT
        )
        self.username_entry.pack()

        # Password Field
        ctk.CTkLabel(
            self.frame,
            text="Password",
            text_color=SECONDARY_TEXT
        ).pack(anchor="w", padx=60, pady=(20, 5))

        self.password_entry = ctk.CTkEntry(
            self.frame,
            width=280,
            height=38,
            corner_radius=10,
            fg_color="#F9FAFB",
            border_color="#CBD5F5",
            text_color=MAIN_TEXT,
            show="*"
        )
        self.password_entry.pack()

        # Premium Login Button
        self.login_btn = ctk.CTkButton(
            self.frame,
            text="Login",
            width=280,
            height=42,
            corner_radius=12,
            fg_color=BUTTON_BLUE,
            hover_color=DARK_BLUE,
            font=("Arial", 14, "bold")
        )
        self.login_btn.pack(pady=(35, 15))
        self.login_btn.configure(command=self.login)  # Correct binding here

        # Footer
        ctk.CTkLabel(
            self.frame,
            text="Protected System Interface",
            font=("Arial", 10),
            text_color=SECONDARY_TEXT
        ).pack(pady=10)

    def login(self):  # <-- moved inside the class
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

            self.root.destroy()  # Close login window

            if role == "admin":
                app = TVMSApp(user)  # Open admin dashboard
                app.mainloop()

            # Add handling for other roles here if needed

        else:
            messagebox.showerror("Login Failed", "Wrong username or password")


if __name__ == "__main__":
    root = ctk.CTk()
    app = LoginGUI(root)
    root.mainloop()


