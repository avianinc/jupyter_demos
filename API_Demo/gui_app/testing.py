# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 16:55:08 2023

@author: jdehart
"""

import tkinter as tk
import tkinter.ttk as ttk
import json

def create_treeview(treeview, parent, data):
    if isinstance(data, dict):
        for key in data:
            if key == "ldp:contains":
                for item in data[key]:
                    node = treeview.insert(parent, 'end', text=item["@id"])
                    create_treeview(treeview, node, item)
            elif isinstance(data[key], dict):
                node = treeview.insert(parent, 'end', text=key)
                create_treeview(treeview, node, data[key])
            elif isinstance(data[key], list):
                node = treeview.insert(parent, 'end', text=key)
                for item in data[key]:
                    create_treeview(treeview, node, item)
            elif isinstance(data[key], str):
                value = data[key]
                treeview.insert(parent, 'end', text=f"{key}: {value}")
    elif isinstance(data, list):
        for item in data:
            create_treeview(treeview, parent, item)

# Load JSON data from file
with open('elementListData.json', 'r') as f:
    data = json.load(f)

# Create the main window
root = tk.Tk()
root.title("JSON Treeview")

# Create the combobox widget
keys = list(data.keys())
combo_var = tk.StringVar(value=keys[0])
combobox = ttk.Combobox(root, values=keys, textvariable=combo_var)
combobox.pack()

# Create the treeview widget
treeview = ttk.Treeview(root)
treeview.pack(fill=tk.BOTH, expand=True)

# Create the treeview from the JSON data
create_treeview(treeview, '', data[keys[0]])

# Function to update the treeview based on the selected key
def update_treeview(event):
    selected_key = combo_var.get()
    treeview.delete(*treeview.get_children())
    create_treeview(treeview, '', data[selected_key])

# Bind the combobox selected event to the update_treeview function
combobox.bind("<<ComboboxSelected>>", update_treeview)

# Start the main loop
root.mainloop()

