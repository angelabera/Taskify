import tkinter as tk

root = tk.Tk()
root.title("To-Do List")
root.geometry("350x450")
root.resizable(False, False)

def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected[0])

title = tk.Label(
    root,
    text="My To-Do List",
    font=("Arial", 16, "bold")
)
title.pack(pady=10)

entry = tk.Entry(root, width=30, font=("Arial", 11))
entry.pack(pady=10)

listbox = tk.Listbox(
    root,
    width=35,
    height=10,
    font=("Arial", 11)
)
listbox.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

add_button = tk.Button(
    button_frame,
    text="Add Task",
    width=12,
    bg="#4CAF50",
    fg="white",
    command=add_task
)
add_button.pack(side="left", padx=5)

delete_button = tk.Button(
    button_frame,
    text="Delete Task",
    width=12,
    bg="#f44336",
    fg="white",
    command=delete_task
)
delete_button.pack(side="left", padx=5)

root.mainloop()
