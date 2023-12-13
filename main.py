from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title("TO-DO LIST")
window.config(padx=10, pady=10, bg=BACKGROUND_COLOR)
canvas = Canvas(width=370, height=600)


def delete_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)


def add_task():
    task = tasks_entry.get()
    if task:
        listbox.insert(END, task)
        tasks_entry.delete(0, END)


Heading = canvas.create_text(180, 40, text="TO-DO LIST", font=("Arial", 20))
canvas.grid(row=0, column=0)

tasks_label = Label(window, text="Write your tasks:", font=("Arial", 10))
canvas.create_window(60, 100, window=tasks_label)

tasks_entry = Entry(width=32)
canvas.create_window(210, 100, window=tasks_entry)
tasks_entry.focus()

add_button = Button(text="ADD", width=5, command=add_task)
canvas.create_window(340, 100, window=add_button)

listbox = Listbox(selectmode="SINGLE", width=40, height=20)
canvas.create_window(190, 320, window=listbox)

delete_button = Button(text="DELETE TASK", command=delete_task)
canvas.create_window(185, 550, window=delete_button)

window.mainloop()
