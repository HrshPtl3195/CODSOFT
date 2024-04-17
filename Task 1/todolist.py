import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.scrolled import ScrolledFrame
import datetime as dt
from PIL import Image, ImageTk

def add_task():
    global input_box, tasks_pane, entries

    if len(input_box.get()) < 1:
        input_box.configure(bootstyle="danger")
    else:
        date = dt.datetime.now()
        entries.update({date: {"status": 0, "value": input_box.get()}})
        update_list_view(tasks_pane, entries)
        input_box.delete(0, tk.END)

def add_task_via_enter(event):
    add_task()

def reset_input_box(event):
    input_box.configure(bootstyle="default")

def delete_task(key):
    global entries, tasks_pane, completed_pane

    entries.pop(key)
    update_list_view(tasks_pane, entries)
    update_completed_view(completed_pane, entries)

def mark_as_done(key):
    global entries, tasks_pane, completed_pane

    obj = entries[key]
    obj["status"] = 1
    update_list_view(tasks_pane, entries)
    update_completed_view(completed_pane, entries)

def undo_mark(key):
    global entries, tasks_pane, completed_pane

    obj = entries[key]
    obj["status"] = 0
    update_list_view(tasks_pane, entries)
    update_completed_view(completed_pane, entries)

def update_completed_view(view, list):
    for widget in view.winfo_children():
        widget.destroy()

    count = 1
    if len(list) > 0:
        for key, content in list.items():
            if content["status"] == 0:
                continue

            create_task_widget(view, key, content, count)
            count += 1

def update_list_view(view, list):
    for widget in view.winfo_children():
        widget.destroy()

    count = 1
    if len(list) > 0:
        for key, content in list.items():
            if content["status"] == 1:
                continue

            create_task_widget(view, key, content, count)
            count += 1

def create_task_widget(view, key, content, count):
    date = dt.datetime.date(key)
    time = dt.datetime.time(key)
    year = int(date.strftime("%Y"))
    month = int(date.strftime("%m"))
    day = int(date.strftime("%d"))
    hour = int(time.strftime("%I"))
    minute = int(time.strftime("%M"))
    ampm = time.strftime("%p")
    date_str = f"{hour}:{minute} {ampm} {day}/{month}/{year} "

    task_frame = tk.Frame(view, border=2)
    task_frame.pack(fill=tk.X, expand=True, pady=5, ipadx=5, ipady=0)

    details_frame = tk.Frame(task_frame)
    details_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

    task_value = ttk.Label(details_frame, text=content["value"], font=('sans-serif', 16), justify=tk.LEFT)
    task_value.pack(side=tk.TOP, fill=tk.BOTH, padx=1, pady=(0, 1))

    task_date = ttk.Label(details_frame, text=date_str, font=('sans-serif', 8), justify=tk.LEFT)
    task_date.pack(side=tk.BOTTOM, fill=tk.BOTH, padx=1, pady=(1, 0))

    task_delete = ttk.Button(task_frame, text="Delete Task", bootstyle="danger", cursor="hand2", command=lambda:delete_task(key))
    task_delete.pack(side=tk.RIGHT, padx=20)
    if content["status"] == 0:
        task_mark = ttk.Button(task_frame, text="Mark as Done", bootstyle="success", cursor="hand2", command=lambda:mark_as_done(key))
    else:
        task_mark = ttk.Button(task_frame, text="Undo Mark", bootstyle="warning", cursor="hand2", command=lambda:undo_mark(key))
    task_mark.pack(side=tk.RIGHT, padx=(10, 4))

    if(count % 2 == 0):
        task_frame.configure(bg="#fff")
        details_frame.configure(bg="#fff")
        task_value.configure(background="#fff")
        task_date.configure(background="#fff")
    else:
        task_frame.configure(bg="#F8FCFA")
        details_frame.configure(bg="#F8FCFA")
        task_value.configure(background="#F8FCFA")
        task_date.configure(background="#F8FCFA")

def switch_to_tasklist():
    global completed_pane, tasks_pane, tasks_btn, completed_btn
    tasks_btn.config(bootstyle="dark")
    completed_btn.config(bootstyle="light")
    completed_pane.pack_forget()
    tasks_pane.pack(fill=tk.BOTH, expand=False)

def switch_to_completedlist():
    global completed_pane, tasks_pane, tasks_btn, completed_btn
    tasks_btn.config(bootstyle="light")
    completed_btn.config(bootstyle="dark")
    tasks_pane.pack_forget()
    completed_pane.pack(fill=tk.BOTH, expand=False)

root = ttk.Window(title="To-Do List")
ico = Image.open("C:\\Users\\harsh\\OneDrive\\Desktop\\codsoft\\Task 1\\to-do-list.png")
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)

entries = {}

frame1 = tk.Frame(root)
frame1.pack(side=tk.TOP, padx=20, pady=(10, 20), ipadx=20)

input_label = ttk.LabelFrame(frame1, text="Add Task")
input_label.pack(padx=10, ipadx=10)

input_box = ttk.Entry(input_label, width=50)
input_box.bind("<Key>", reset_input_box)
input_box.bind("<Return>", add_task_via_enter)
input_box.pack(side=tk.LEFT, padx=(20, 0), pady=10)

input_btn = ttk.Button(input_label, text="Add Task", bootstyle="primary", cursor="hand2", command=add_task)
input_btn.pack(side=tk.RIGHT, padx=(0, 20), pady=10)

switch_btn_frame = tk.Frame(root)
switch_btn_frame.pack(side=tk.TOP, fill=tk.X)

tasks_btn = ttk.Button(switch_btn_frame, text="Pending Tasks", cursor="hand2", command=switch_to_tasklist, bootstyle="dark")
tasks_btn.pack(side=tk.LEFT, padx=(10, 0), expand=False)
completed_btn = ttk.Button(switch_btn_frame, text="Completed Tasks", cursor="hand2", command=switch_to_completedlist, bootstyle="light")
completed_btn.pack(side=tk.LEFT, padx=(10, 0), expand=False)

view_frame = tk.Frame(root, width=50, height=400, bd=2)
view_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=False)

tasks_pane = ScrolledFrame(view_frame, autohide=True, height=400)
tasks_pane.pack(fill=tk.BOTH, expand=False)

completed_pane = ScrolledFrame(view_frame, autohide=True, height=400)

root.resizable(False, False)
root.mainloop()
