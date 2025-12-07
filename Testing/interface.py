import tkinter as tk
from tkinter import messagebox
import json
import os

FILE = "tasks.json"

def load_tasks():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks():
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def add_task():
    task = entry.get().strip()
    if task:
        tasks.append(task)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Task cannot be empty.")

def delete_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        tasks.pop(index)
        listbox.delete(index)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Select a task to delete.")

def mark_done():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        task = tasks[index] + " ✔"
        tasks[index] = task
        listbox.delete(index)
        listbox.insert(index, task)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Select a task to mark done.")

# UI
root = tk.Tk()
root.title("Mini To-Do App")
root.geometry("300x400")

tasks = load_tasks()

entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

mark_button = tk.Button(root, text="Mark Done", command=mark_done)
mark_button.pack()

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack()

listbox = tk.Listbox(root, font=("Arial", 12))
listbox.pack(fill=tk.BOTH, expand=True, pady=10)

for t in tasks:
    listbox.insert(tk.END, t)

root.mainloop()
