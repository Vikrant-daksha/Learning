import tkinter as tk
from tkinter import ttk


task_to_do = []
task_done = []
#if these variable are kept unchecked it will take more space as the list of items keep increasing how do i solve it?

def delete():
    #to check whether the item is selected and resides in the lists

    if unfinished_task_list.curselection(): 
        unfinished_task_list.delete(unfinished_task_list.curselection())
        warn.config(text = "Task Deleted from Unfinished Tasks")
    elif finished_task_list.curselection():
        finished_task_list.delete(finished_task_list.curselection())
        warn.config(text = "Task Deleted from Finished Tasks") #to display information about the task being operated
    else:
        warn.config(text = "Select to Delete or Add to Finished Task") #to display information about the task being operated

def done():
    #same as above but for done button and also calling delete function to delete from unfinished tasks

    if unfinished_task_list.curselection():
        task_to_append = unfinished_task_list.get(unfinished_task_list.curselection())
        task_done.append(task_to_append)
        finished_task_list.insert(tk.END, task_done[len(task_done)- 1])
        delete()
        warn.config(text = "Task Added to Finished Task") #to display information about the task being operated
    elif finished_task_list.curselection():
        warn.config(text = "Task is Already Finished or You can Delete It") #to display information about the task being operated
    else:
        warn.config(text = "Select A Task to be Finished") #to display information about the task being operated

def add_to_list():
    #simply add to list of unfinished 
    task = input_task.get()
    task_to_do.append(task)
    unfinished_task_list.insert(tk.END, task_to_do[len(task_to_do) - 1])



root = tk.Tk()
root.title("To Do List")
root.geometry('450x300')

frame = ttk.Frame(root)
label = ttk.Label(frame, text = "Task List", font = "Arial, 18" )
label.pack(padx = 5)
frame.pack()

input_frame = ttk.Frame(root)
input_task = tk.StringVar()
task_entry = ttk.Entry(input_frame, textvariable = input_task)
task_entry.grid(row = 0, column = 1, padx = 5)
add_btn = ttk.Button(input_frame, text = "Add", command = add_to_list)
add_btn.grid(row = 0, column = 2, padx = 5)
input_frame.pack(pady = 5)

btn_frame = tk.Frame(root)
is_done = ttk.Button(btn_frame, text = "Done", command = done)
is_done.grid(row = 0, column = 1, padx= 10)
this_will_delete = ttk.Button(btn_frame, text = "Delete", command = delete)
this_will_delete.grid(row = 0, column = 2)
btn_frame.pack()

warn = ttk.Label(root, text = "Select Tasks to Delete or Add to Your Finished Task")
warn.pack()

output_frame = ttk.Frame(root)

unfinished_task_frame = ttk.Frame(output_frame)
label_task = ttk.Label(unfinished_task_frame, text = "Unfinished Task", font = "Arial, 12")
label_task.pack(pady = 5)
unfinished_task_list = tk.Listbox(unfinished_task_frame)
unfinished_task_list.pack()
unfinished_task_frame.grid(row=0, column=1, padx = 15)

finished_task_frame = ttk.Frame(output_frame)
label_task = ttk.Label(finished_task_frame, text = "Finished Task", font = "Arial, 12")
label_task.pack(pady = 5)
finished_task_list = tk.Listbox(finished_task_frame)
finished_task_list.pack()
finished_task_frame.grid(row=0, column=2, padx = 15)

output_frame.pack()


root.mainloop()
