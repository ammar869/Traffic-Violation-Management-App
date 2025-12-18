import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# --- Configuration & Colors ---
c_bg_main = "#0F1116"       # Very dark background
c_card_bg = "#161B22"       # Card background
c_sidebar = "#0D1117"       # Sidebar background
c_accent = "#238636"        # Green accents
c_blue = "#2F81F7"          # Blue highlights
c_text_main = "#E6EDF3"     # Whiteish text
c_text_sec = "#8B949E"      # Gray text
c_danger = "#F85149"        # Red
c_warning = "#D29922"       # Orange

class TVMSApp(ctk.CTk):
    def __init__(self, user_data):
        super().__init__()
        self.user_data = user_data

        # Window Setup
        self.title("TVMS | Traffic Violation Management System")
        self.geometry("1300x800")
        ctk.set_appearance_mode("Dark")
        # Grid Layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # State tracking
        self.current_frame = "Dashboard"
        self.buttons = {} # Store sidebar buttons to toggle colors

        # --- 1. Sidebar ---
        self.sidebar_frame = ctk.CTkFrame(self, width=250, corner_radius=0, fg_color=c_sidebar)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self.create_sidebar()

        # --- 2. Main Content Container ---
        self.main_frame = ctk.CTkFrame(self, fg_color=c_bg_main, corner_radius=0)
        self.main_frame.grid(row=0, column=1, sticky="nsew")
        
        # Load Dashboard by default
        self.select_frame("Dashboard")

    def create_sidebar(self):
        # App Logo/Title
        title_lbl = ctk.CTkLabel(self.sidebar_frame, text="TVMS", font=("Roboto", 24, "bold"), text_color=c_text_main)
        title_lbl.pack(pady=30, padx=20, anchor="w")

        # Menu Items
        menu_items = [
            "Dashboard", "Users", "Officers",
            "Violations", "Cases", "Payments",
            "Reports", "Settings"
        ]

        for item in menu_items:
            btn = ctk.CTkButton(
                self.sidebar_frame, 
                text=f"  {item}", 
                height=40, 
                anchor="w", 
                fg_color="transparent", 
                text_color=c_text_sec,
                hover_color="#1F6FEB",
                font=("Roboto", 14),
                command=lambda name=item: self.select_frame(name)
            )
            btn.pack(fill="x", padx=10, pady=5)
            self.buttons[item] = btn

    def select_frame(self, name):
        # 1. Update Sidebar Visuals
        for btn_name, btn in self.buttons.items():
            if btn_name == name:
                btn.configure(fg_color=c_blue, text_color=c_text_main)
            else:
                btn.configure(fg_color="transparent", text_color=c_text_sec)

        # 2. Clear Main Frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # 3. Create Header (Common for all pages)
        self.create_header(name)

        # 4. Render Specific Content
        self.content_area = ctk.CTkScrollableFrame(self.main_frame, fg_color="transparent")
        self.content_area.pack(fill="both", expand=True, padx=20, pady=10)

        if name == "Dashboard":
            self.render_dashboard()
        else:
            self.render_empty_shell(name)

    def create_header(self, title_text):
        header_frame = ctk.CTkFrame(self.main_frame, height=60, fg_color="transparent")
        header_frame.pack(fill="x", padx=20, pady=10)

        title = ctk.CTkLabel(header_frame, text=title_text, font=("Roboto", 20, "bold"), text_color=c_text_main)
        title.pack(side="left")

        # Profile & Logout
        logout_btn = ctk.CTkButton(header_frame, text="Logout", width=80, fg_color=c_danger, hover_color="#B62324")
        logout_btn.pack(side="right", padx=10)
        
        user_lbl = ctk.CTkLabel(
        header_frame,
            text=f"{self.user_data['full_name']} 👤",
            font=("Roboto", 14),
            text_color=c_text_main
        )
        user_lbl.pack(side="right", padx=10)

    # ---------------------------------------------------------
    # RENDER METHODS
    # ---------------------------------------------------------

    def render_empty_shell(self, page_name):
        """Generic shell for non-dashboard pages"""
        
        # Placeholder Container
        container = ctk.CTkFrame(self.content_area, fg_color=c_card_bg, corner_radius=10, border_width=1, border_color="#30363d")
        container.pack(fill="both", expand=True, pady=10)

        # Placeholder Icon/Text
        icon_map = {
            "Users": "👥", "Officers": "👮", "Violations": "⚠️",
            "Cases": "⚖️", "Payments": "💳", "Reports": "📊", "Settings": "⚙️"
        }
        icon = icon_map.get(page_name, "📁")

        ctk.CTkLabel(container, text=icon, font=("Arial", 60)).pack(pady=(150, 20))
        ctk.CTkLabel(container, text=f"{page_name} Management Module", font=("Roboto", 24, "bold"), text_color=c_text_main).pack()
        ctk.CTkLabel(container, text="This module is under development.", font=("Roboto", 14), text_color=c_text_sec).pack(pady=10)
        
        # Example Action Button
        ctk.CTkButton(container, text=f"Add New {page_name[:-1]}", fg_color=c_accent, width=200).pack(pady=20)


    def render_dashboard(self):
        """Replicates the complex Dashboard UI"""
        
        # -- Stats Grid --
        stats_container = ctk.CTkFrame(self.content_area, fg_color="transparent")
        stats_container.pack(fill="x", pady=10)
        stats_container.grid_columnconfigure((0,1,2), weight=1)

        self.create_stat_card(stats_container, 0, 0, "Total Users", "124,500", "Registered Citizens", "👥", c_blue)
        self.create_stat_card(stats_container, 0, 1, "Total Officers", "1,250", "Active Duty", "👮", c_blue)
        self.create_stat_card(stats_container, 0, 2, "Total Violations", "8,920", "All Time Records", "⚠️", c_warning)
        self.create_stat_card(stats_container, 1, 0, "Fines Collected", "$15.2M", "Fiscal Year", "💵", c_accent)
        self.create_stat_card(stats_container, 1, 1, "Today's Violations", "145", "Last 24 Hours", "📅", c_blue)
        self.create_stat_card(stats_container, 1, 2, "Pending Cases", "2,340", "Action Required", "⏳", c_warning)

        # -- Bottom Section --
        bottom_frame = ctk.CTkFrame(self.content_area, fg_color="transparent")
        bottom_frame.pack(fill="both", expand=True, pady=10)
        bottom_frame.grid_columnconfigure(0, weight=2)
        bottom_frame.grid_columnconfigure(1, weight=1)

        # Table
        self.render_table(bottom_frame)
        # Chart
        self.render_chart(bottom_frame)

    def create_stat_card(self, parent, row, col, title, value, subtitle, icon, icon_color):
        card = ctk.CTkFrame(parent, fg_color=c_card_bg, corner_radius=10, border_width=1, border_color="#30363d")
        card.grid(row=row, column=col, sticky="ew", padx=10, pady=10, ipady=10)
        
        head_frame = ctk.CTkFrame(card, fg_color="transparent")
        head_frame.pack(fill="x", padx=15, pady=10)
        ctk.CTkLabel(head_frame, text=title, font=("Roboto", 12), text_color=c_text_sec).pack(side="left")
        ctk.CTkLabel(head_frame, text=icon, font=("Arial", 20), text_color=icon_color).pack(side="right")
        ctk.CTkLabel(card, text=value, font=("Roboto", 28, "bold"), text_color=c_text_main).pack(anchor="w", padx=15)
        ctk.CTkLabel(card, text=subtitle, font=("Roboto", 11), text_color=c_text_sec).pack(anchor="w", padx=15, pady=(0, 10))

    def render_table(self, parent):
        table_container = ctk.CTkFrame(parent, fg_color=c_card_bg, corner_radius=10, border_width=1, border_color="#30363d")
        table_container.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        ctk.CTkLabel(table_container, text="Recent Violations Overview", font=("Roboto", 16, "bold"), text_color=c_text_main).pack(anchor="w", padx=20, pady=15)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", background=c_card_bg, foreground=c_text_main, fieldbackground=c_card_bg, bordercolor=c_card_bg, rowheight=30)
        style.configure("Treeview.Heading", background=c_sidebar, foreground=c_text_sec, relief="flat", font=("Arial", 11, "bold"))
        style.map("Treeview", background=[('selected', c_blue)])

        columns = ("Date", "User", "Violation", "Amount", "Status")
        tree = ttk.Treeview(table_container, columns=columns, show="headings", height=8)
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=100)
        tree.pack(fill="both", expand=True, padx=15, pady=(0, 15))

        data = [
            ("Oct 24, 2023", "J. Smith", "Speeding > 20mph", "$250", "Paid"),
            ("Oct 24, 2023", "M. Doe", "Red Light Jump", "$150", "Pending"),
            ("Oct 24, 2023", "A. Khan", "Illegal Parking", "$500", "Unpaid"),
        ]
        for item in data:
            tree.insert("", "end", values=item)

    def render_chart(self, parent):
        chart_container = ctk.CTkFrame(parent, fg_color=c_card_bg, corner_radius=10, border_width=1, border_color="#30363d")
        chart_container.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        ctk.CTkLabel(chart_container, text="Violations Last 7 Days", font=("Roboto", 14, "bold"), text_color=c_text_main).pack(anchor="w", padx=20, pady=15)

        fig = Figure(figsize=(4, 3), dpi=100, facecolor=c_card_bg)
        ax = fig.add_subplot(111)
        ax.set_facecolor(c_card_bg)
        x, y = ["M", "T", "W", "T", "F", "S", "S"], [10, 25, 15, 40, 30, 70, 45]
        ax.plot(x, y, color=c_blue, linewidth=2, marker='o')
        ax.fill_between(x, y, color=c_blue, alpha=0.1)
        ax.spines['bottom'].set_color(c_text_sec)
        ax.spines['left'].set_color(c_text_sec)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.tick_params(axis='x', colors=c_text_sec)
        ax.tick_params(axis='y', colors=c_text_sec)

        canvas = FigureCanvasTkAgg(fig, master=chart_container)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True, padx=10, pady=10)


if __name__ == "__main__":
    # Dummy user data for testing purposes
    user_data = {"full_name": "Test Admin"}
    app = TVMSApp(user_data)
    app.mainloop()