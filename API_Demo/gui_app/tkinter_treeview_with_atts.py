import tkinter as tk
import json
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("JSON Viewer")

# Create the treeview widget
treeview = ttk.Treeview(root)
treeview.pack(side="left", fill="both", expand=True)

# Create the scrollbar widget
scrollbar = ttk.Scrollbar(root, orient="vertical", command=treeview.yview)
scrollbar.pack(side="right", fill="y")

# Configure the treeview to use the scrollbar
treeview.configure(yscrollcommand=scrollbar.set)

# Create the text widget
text = tk.Text(root, height=10, width=50)
text.pack(side="right", fill="both", expand=True)

# Function to populate the treeview
def populate_treeview(node, data):
    if type(data) == dict:
        for key in data:
            child = treeview.insert(node, "end", text=key)
            populate_treeview(child, data[key])
    elif type(data) == list:
        for i, item in enumerate(data):
            uuid = item["uuid"]
            name = item["name"]
            child = treeview.insert(node, "end", text="{} - {}".format(uuid, name))
            populate_treeview(child, item.get("ownedElements", {}))
    else:
        treeview.insert(node, "end", text=data)

# Function to display the attributes of a selected node
def show_attributes(event):
    # Get the selected node
    selected_item = treeview.focus()
    # Get the data associated with the selected node
    data = treeview.item(selected_item)["text"]
    # Clear the text widget
    text.delete("1.0", "end")
    # Display the data in the text widget
    text.insert("1.0", json.dumps(data, indent=4))

# Read the JSON data from a file
with open("data.json") as f:
    data = json.load(f)

# Populate the treeview
populate_treeview("", data)

# Bind the selection event to the show_attributes function
treeview.bind("<<TreeviewSelect>>", show_attributes)

# Start the main loop
root.mainloop()
