from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry

class Traffic:
    def __init__(self, root):
        self.root = root
        self.root.title("Traffic Violation System")
        self.root.geometry("1540x800+0+0")
        self.root.configure(bg="#CBCBCB")

        # Title
        lbltitle = Label(self.root, bd=15, relief=RIDGE,
                         text="Traffic Violation System",
                         fg="white", bg="#1B3C53",
                         font=("Times New Roman", 36, "bold"))
        lbltitle.pack(side=TOP, fill=X)

        # Main frame
        dataframe = Frame(self.root, bd=15, relief=RIDGE, bg="white")
        dataframe.place(x=10, y=130, width=1520, height=400)

        # Left frame
        dataframe_left = LabelFrame(
            dataframe, bd=10, relief=RIDGE, padx=10, pady=10,
            font=("Calibri", 14, "bold"), text="Violation Information",
            fg="white", bg="#234C6A"
        )
        dataframe_left.place(x=0, y=5, width=980, height=380)

        # Labels + Fields
        self.create_label_entry(dataframe_left, "Violation ID", 0)
        self.create_label_entry(dataframe_left, "Vehicle ID", 1)
        self.create_label_entry(dataframe_left, "Violation Type ID", 2)

        # Seatbelt
        self.create_combobox(dataframe_left, "Seatbelt", 3)

        # Personal Injury
        self.create_label_entry(dataframe_left, "Personal Injury", 4)

        # Property Damage
        self.create_combobox(dataframe_left, "Property Damage", 5)

        # Accident
        self.create_combobox(dataframe_left, "Contributed To Accident", 6)

        # State
        self.create_label_entry(dataframe_left, "State", 7)

        # Date Picker
        Label(dataframe_left, font=("Arial", 12, "bold"),
              text="Violation Date", bg="#234C6A", fg="white")\
              .grid(row=8, column=0, sticky=W)

        self.dateViolation = DateEntry(
            dataframe_left,
            font=("Arial", 12, "bold"),
            width=33,
            background='#234C6A',
            foreground='white',
            borderwidth=2,
            date_pattern='yyyy-mm-dd'
        )
        self.dateViolation.grid(row=8, column=1)

    # Helper methods
    def create_label_entry(self, parent, text, row):
        Label(parent, font=("Arial", 12, "bold"),
              text=text, bg="#234C6A", fg="white")\
              .grid(row=row, column=0, sticky=W)

        Entry(parent, font=("Arial", 13, "bold"), width=35)\
            .grid(row=row, column=1)

    def create_combobox(self, parent, text, row):
        Label(parent, font=("Arial", 12, "bold"),
              text=text, bg="#234C6A", fg="white")\
              .grid(row=row, column=0, sticky=W)

        combo = ttk.Combobox(
            parent, state="readonly",
            values=("Yes", "No"),
            font=("Arial", 12, "bold"),
            width=33
        )
        combo.current(0)
        combo.grid(row=row, column=1)


# Safe venv runner
if __name__ == "__main__":
    root = Tk()
    app = Traffic(root)
    root.mainloop()
