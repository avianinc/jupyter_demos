import tkinter as tk
from tkinter import ttk

# Create a window object
window = tk.Tk()

# Set the window title
window.title("GUI Example")

# Create a menu bar
menu_bar = tk.Menu(window)

# Add a "File" menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.destroy)
menu_bar.add_cascade(label="File", menu=file_menu)

# Add an "Edit" menu
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Add the menu bar to the window
window.config(menu=menu_bar)

# Create a frame for the top section
top_frame = ttk.Frame(window)
top_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

# Add labels for the textboxes
serverip_label = ttk.Label(top_frame, text="Server IP:")
serverip_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

authkey_label = ttk.Label(top_frame, text="Auth Key:")
authkey_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

# Add textboxes for entering data
serverip_entry = ttk.Entry(top_frame)
serverip_entry.grid(row=0, column=1, padx=5, pady=5)

authkey_entry = ttk.Entry(top_frame)
authkey_entry.grid(row=1, column=1, padx=5, pady=5)

# Add labels for the dropdown boxes
project_label = ttk.Label(top_frame, text="Project:")
project_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)

model_label = ttk.Label(top_frame, text="Model:")
model_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)

instance_label = ttk.Label(top_frame, text="Instance:")
instance_label.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)

# Add dropdown boxes
project_options = ["Project 1", "Project 2", "Project 3"]
project_dropdown = ttk.Combobox(top_frame, values=project_options)
project_dropdown.grid(row=2, column=1, padx=5, pady=5)

model_options = ["Model 1", "Model 2", "Model 3"]
model_dropdown = ttk.Combobox(top_frame, values=model_options)
model_dropdown.grid(row=3, column=1, padx=5, pady=5)

instance_options = ["Instance 1", "Instance 2", "Instance 3"]
instance_dropdown = ttk.Combobox(top_frame, values=instance_options)
instance_dropdown.grid(row=4, column=1, padx=5, pady=5)

# Create a frame for the lower section
bottom_frame = ttk.Frame(window)
bottom_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True, padx=10, pady=10)

# Add a treeview to the lower left section
treeview = ttk.Treeview(bottom_frame)
treeview.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Add a textarea to the lower right section
textarea = tk.Text(bottom_frame)
textarea.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

window.mainloop()
