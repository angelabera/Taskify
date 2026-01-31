import tkinter as tk

root = tk.Tk()
root.title("To-Do List")
root.geometry("300x400")

def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected[0])

entry = tk.Entry(root, width=25)
entry.pack(pady=10)

listbox = tk.Listbox(root, width=30)
listbox.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

root.mainloop()
