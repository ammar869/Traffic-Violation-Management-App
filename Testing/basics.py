from tkinter import *

from tkinter import filedialog

window = Tk()
# mylabel = Label(root , text= "Hello World")
# mylabel.pack()

window.geometry("400x400")
window.title("Traffic Voilation System")

#icon = PhotoImage(file="Gemini_Generated_Image_9uh4l89uh4l89uh4.png")
#rwindow.iconphoto(True, icon)




# Label

label = Label(window, text="Welcome to Traffic Voilation System", font=("Arial", 16), )
label.pack(pady=20)


# Button
def on_button_click():
    print("Button clicked!")
button = Button(window, text="Click Me", command=on_button_click, font=("Arial", 14), bg="black", fg="white")
button.pack(pady=10)

# Checkbutton
def on_check():
    print("Checkbutton toggled:", var.get())
var = IntVar()
checkbutton = Checkbutton(window, text="I agree to the terms", variable=var, command=on_check, font=("Arial", 14))
checkbutton.pack(pady=10)
# Entry
entry = Entry(window, font=("Arial", 14))
entry.pack(pady=10)

button2 = Button(window, text="Submit", command=lambda: print("Submitted:", entry.get()), font=("Arial", 14), bg="blue", fg="white")
button2.pack(pady=10)



# List Button 
listbox=Listbox(window, font=("Arial", 14), background="lightgray")
listbox.pack(pady=10)
listbox.insert(END, "Option 1")
listbox.insert(END, "Option 2")
listbox.insert(END, "Option 3")

button1 = Button(window, text="Show Selected", command=lambda: print("Selected:", listbox.get(ACTIVE)), font=("Arial", 14), bg="green", fg="white")




# File Dialog 

def openfile():
    file = filedialog.askopenfilename()
    file = open(file, 'r')
    print(file.read())
    file.close()
button3 = Button(window, text = "open File ", command  = openfile)

button3.pack(pady=10)







# Menu 


def new_file():
    print("New File Selected")

def open_file():
    print("Open File Selected")

def save_file():
    print("Save File Selected")

def exit_app():
    window.quit()



menu_bar = Menu(window)

# File Menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)

menu_bar.add_cascade(label="File", menu=file_menu)

# Edit Menu
edit_menu = Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut", command=lambda: print("Cut"))
edit_menu.add_command(label="Copy", command=lambda: print("Copy"))
edit_menu.add_command(label="Paste", command=lambda: print("Paste"))

menu_bar.add_cascade(label="Edit", menu=edit_menu)

window.config(menu=menu_bar)

window.mainloop()
window.mainloop()

