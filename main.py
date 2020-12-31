import ast
import json
import os
import sys
import tkinter as tk
from datetime import time, date
from pathlib import Path
from tkinter import messagebox
from cachetools import TTLCache

root = tk.Tk()
canvas1 = tk.Canvas(root, width=400, height=400)
canvas1.pack()
input_key = tk.Entry(root)
input_value = tk.Entry(root)
input_file = tk.Entry(root)
input_read = tk.Entry(root)
input_delete = tk.Entry(root)


# To create key,value pair
def create():
    content = {}
    bool_create = "true"
    key = input_key.get()
    value = input_value.get()
    file_name = input_file.get()
    if len(key) > 33 or len(key) == 0:
        bool_create = "false"
        messagebox.showinfo("information", "Please enter a valid key.Max length is 32.")
    try:
        value = json.loads(value)
        if sys.getsizeof(value) > 16000:
            bool_create = "false"
            messagebox.showinfo("information", "Please enter a valid value.Size should be less than 16KB .")
    except:
        bool_create = "false"
        messagebox.showinfo("information", "Please enter a valid value.Value should be a JSON.")

    try:
        if file_name:
            file_path = file_name
        else:
            file_path = os.getcwd() + '\Freshworks.txt'
        # To check Size Limit
        if Path(file_path).stat().st_size > 1000000:
            messagebox.showinfo("information", "File Size is exceed.Maximum limit is 1 GB")
            exit()

        f = open(file_path, 'a+')
        f.close()
        f = open(file_path, 'r')
        lines = f.read().split('\n')
        f.close()
        for l in lines:
            if l != '':
                res = ast.literal_eval(l)
                if key in res.keys():
                    print(key)
                    bool_create = "false"
                    messagebox.showinfo("information", "Key is already existing.Please enter a valid key.")

        f = open(file_path, 'a+')
        content[key] = value
        f.write(str(content))
        f.write("\n")
        f.close()
        if bool_create == "true":
            messagebox.showinfo("information", "Successfully inserted data.")
    except Exception as e:
        print(e)
        messagebox.showinfo("information", "Please provide a valid path.")


# To read data based on key value
def read():
    file_name = input_file.get()
    key = input_read.get()
    if file_name:
        file_path = file_name
    else:
        file_path = os.getcwd() + '\Freshworks.txt'
    f = open(file_path, 'r')
    lines = f.read().split('\n')
    f.close()
    bool_read = "false"
    for l in lines:
        if l != '':
            res = ast.literal_eval(l)
            if key in res.keys():
                bool_read = "true"
                messagebox.showinfo("information", "Value :" + str(res[key]))

    if bool_read == "false":
        messagebox.showinfo("information", "Please enter a valid key")


# To delete data based on key value
def delete():
    file_name = input_file.get()
    key = input_delete.get()
    if file_name:
        file_path = file_name
    else:
        file_path = os.getcwd() + '\Freshworks.txt'
    f = open(file_path, 'r')
    lines = f.read().split('\n')
    f.close()
    bool_delete = "false"
    f = open(file_path, 'w')
    for l in lines:
        if l != '':
            res = ast.literal_eval(l)
            if key in res.keys():
                bool_delete = "true"
                messagebox.showinfo("information", "Deleted Successfully")
            else:
                f.write(l)
                f.write("\n")
    f.close()
    if bool_delete == "false":
        messagebox.showinfo("information", "Please enter valid key")


def Start():
    File_Label = tk.Label(root, text="File_Path : ")
    Key_Label = tk.Label(root, text="Enter Key*: ")
    Value_Label = tk.Label(root, text="Enter Value *: ")
    Value_read = tk.Label(root, text="Enter key to read*: ")
    Value_delete = tk.Label(root, text="Enter key to delete*: ")

    canvas1.create_window(100, 10, window=File_Label)
    canvas1.create_window(250, 10, window=input_file)
    canvas1.create_window(100, 50, window=Key_Label)
    canvas1.create_window(250, 50, window=input_key)
    canvas1.create_window(100, 100, window=Value_Label)
    canvas1.create_window(250, 100, window=input_value)
    canvas1.create_window(100, 200, window=Value_read)
    canvas1.create_window(250, 200, window=input_read)
    canvas1.create_window(100, 300, window=Value_delete)
    canvas1.create_window(250, 300, window=input_delete)

    create_b = tk.Button(text='Create', command=create)
    read_b = tk.Button(text='Read', command=read)
    delete_b = tk.Button(text='Delete', command=delete)
    canvas1.create_window(150, 150, window=create_b)
    canvas1.create_window(150, 250, window=read_b)
    canvas1.create_window(150, 350, window=delete_b)
    root.mainloop()


if __name__ == '__main__':
    Start()
