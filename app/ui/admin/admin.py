import customtkinter as ctk
import tkinter.ttk as ttk
from tkinter import messagebox

# Color palette
DARK_BLUE = "#1E293B"
LIGHT_BG = "#F8FAFC"
BUTTON_BLUE = "#3B82F6"
WARNING_RED = "#EF4444"
SUCCESS_GREEN = "#22C55E"
MAIN_TEXT = "#0F172A"
SECONDARY_TEXT = "#64748B"

class AdminPanel:
    def __init__(self, root):
        ctk.set_appearance_mode("light")  # or "dark"
        ctk.set_default_color_theme("blue")

        self.root = root
        self.root.title("Traffic Violation System - Admin Panel")
        self.root.geometry("700x600")
        self.root.configure(bg=LIGHT_BG)
        self.root.resizable(False, False)

        # Title
        title_label = ctk.CTkLabel(root, text="Traffic Violation System",
                                   font=("Arial", 20, "bold"),
                                   text_color=MAIN_TEXT, bg_color=LIGHT_BG)
        title_label.pack(pady=(10,0))

        sub_title_label = ctk.CTkLabel(root, text="ADMIN PANEL",
                                       font=("Arial", 16),
                                       text_color=SECONDARY_TEXT, bg_color=LIGHT_BG)
        sub_title_label.pack(pady=(0,20))

        # Dashboard Section
        dash_frame = ctk.CTkFrame(root, fg_color=LIGHT_BG, border_width=2, border_color=DARK_BLUE)
        dash_frame.pack(fill="x", padx=20)

        dash_label = ctk.CTkLabel(dash_frame, text="[ Dashboard ]", font=("Arial", 14, "bold"), text_color=MAIN_TEXT)
        dash_label.pack(anchor="w", pady=5)

        stats_frame = ctk.CTkFrame(dash_frame, fg_color=LIGHT_BG)
        stats_frame.pack(pady=10, fill="x")

        # Stats boxes
        self.create_stat_box(stats_frame, "TOTAL USERS", "1240").pack(side="left", expand=True, fill="both", padx=5)
        self.create_stat_box(stats_frame, "TOTAL OFFICERS", "45").pack(side="left", expand=True, fill="both", padx=5)
        self.create_stat_box(stats_frame, "VIOLATIONS", "320").pack(side="left", expand=True, fill="both", padx=5)

        fines_label = ctk.CTkLabel(dash_frame, text="TOTAL FINES COLLECTED : 450,000 PKR",
                                   font=("Arial", 12, "bold"), anchor="w", text_color=MAIN_TEXT)
        fines_label.pack(fill="x", pady=10)

        # Manage Users & Officers
        manage_frame = ctk.CTkFrame(root, fg_color=LIGHT_BG, border_width=2, border_color=DARK_BLUE)
        manage_frame.pack(fill="x", padx=20, pady=10)

        manage_label = ctk.CTkLabel(manage_frame, text="[ MANAGE USERS ]   [ MANAGE OFFICERS ]",
                                    font=("Arial", 14, "bold"), text_color=MAIN_TEXT)
        manage_label.pack(anchor="w", pady=5)

        manage_desc = ctk.CTkLabel(manage_frame, text="ADD / EDIT / DELETE USERS & OFFICERS", font=("Arial", 10), text_color=SECONDARY_TEXT)
        manage_desc.pack(anchor="w", pady=5)

        # Violation Management Table
        violation_frame = ctk.CTkFrame(root, fg_color=LIGHT_BG, border_width=2, border_color=DARK_BLUE)
        violation_frame.pack(fill="both", padx=20, pady=10, expand=True)

        violation_label = ctk.CTkLabel(violation_frame, text="[ VIOLATION MANAGEMENT ]", font=("Arial", 14, "bold"), text_color=MAIN_TEXT)
        violation_label.pack(anchor="w", pady=5)

        # Use ttk Treeview for table
        self.tree = ttk.Treeview(violation_frame, columns=("violation", "fine", "status"), show="headings", height=5)
        self.tree.heading("violation", text="Violation Name")
        self.tree.heading("fine", text="Fine Amount")
        self.tree.heading("status", text="Status")

        self.tree.column("violation", width=200)
        self.tree.column("fine", width=120)
        self.tree.column("status", width=100)
        self.tree.pack(fill="both", expand=True, pady=5)

        # Insert example data
        violations = [
            ("Speeding", "2000 PKR", "Active"),
            ("Red Light Jump", "3000 PKR", "Active")
        ]
        for v in violations:
            self.tree.insert("", "end", values=v)

        # Bottom buttons frame
        button_frame = ctk.CTkFrame(root, fg_color=LIGHT_BG)
        button_frame.pack(pady=20)

        btn_reports = ctk.CTkButton(button_frame, text="[ REPORTS & ANALYTICS ]", width=180, fg_color=BUTTON_BLUE, command=self.show_reports)
        btn_reports.grid(row=0, column=0, padx=5)

        btn_settings = ctk.CTkButton(button_frame, text="[ SYSTEM SETTINGS ]", width=140, fg_color=BUTTON_BLUE, command=self.show_settings)
        btn_settings.grid(row=0, column=1, padx=5)

        btn_audit = ctk.CTkButton(button_frame, text="[ AUDIT LOGS ]", width=110, fg_color=BUTTON_BLUE, command=self.show_audit_logs)
        btn_audit.grid(row=0, column=2, padx=5)

        btn_logout = ctk.CTkButton(button_frame, text="[ LOGOUT ]", width=90, fg_color=WARNING_RED, command=self.logout)
        btn_logout.grid(row=0, column=3, padx=5)

    def create_stat_box(self, parent, title, number):
        frame = ctk.CTkFrame(parent, fg_color=SUCCESS_GREEN, border_width=1, border_color=SUCCESS_GREEN)

        title_lbl = ctk.CTkLabel(frame, text=title, font=("Arial", 12, "bold"), text_color=MAIN_TEXT)
        title_lbl.pack(pady=(5,0))
        # Fix: Number text color must contrast bg
        num_lbl = ctk.CTkLabel(frame, text=number, font=("Arial", 20, "bold"), text_color="white")
        num_lbl.pack(pady=(0,5))
        return frame

    # Button callback placeholders - replace with real logic
    def show_reports(self):
        messagebox.showinfo("Reports & Analytics", "Reports & Analytics feature coming soon!")

    def show_settings(self):
        messagebox.showinfo("System Settings", "System Settings feature coming soon!")

    def show_audit_logs(self):
        messagebox.showinfo("Audit Logs", "Audit Logs feature coming soon!")

    def logout(self):
        confirm = messagebox.askyesno("Logout", "Are you sure you want to logout?")
        if confirm:
            self.root.destroy()

if __name__ == "__main__":
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    app = AdminPanel(root)
    root.mainloop()
