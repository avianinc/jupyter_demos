import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import requests

class GUI:

    def __init__(self, root):

        # Create the main window
        self.root = root
        self.root.geometry("800x600")
        self.root.title("GUI with Python tkinter")

        # Create a menu bar
        menubar = tk.Menu(self.root)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Save", command=self.save_data)
        filemenu.add_command(label="Load", command=self.load_data)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.root.destroy)
        menubar.add_cascade(label="File", menu=filemenu)

        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Documentation", command=self.show_documentation)
        helpmenu.add_command(label="About", command=self.show_about)
        menubar.add_cascade(label="Help", menu=helpmenu)

        self.root.config(menu=menubar)

        # Create the main frame
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill="both", expand=True)

        # Create the server info frame
        server_info_frame = tk.LabelFrame(self.main_frame, text="Server Info")
        server_info_frame.pack(side="left", padx=10, pady=10, fill="y")

        # Create the server info widgets
        server_ip_label = tk.Label(server_info_frame, text="Server IP:")
        server_ip_label.pack(anchor="w", padx=5, pady=2)
        self.server_ip_entry = tk.Entry(server_info_frame)
        self.server_ip_entry.pack(fill="x", padx=5, pady=2)

        server_port_label = tk.Label(server_info_frame, text="Server Port:")
        server_port_label.pack(anchor="w", padx=5, pady=2)
        self.server_port_entry = tk.Entry(server_info_frame)
        self.server_port_entry.pack(fill="x", padx=5, pady=2)

        auth_key_label = tk.Label(server_info_frame, text="Auth Key:")
        auth_key_label.pack(anchor="w", padx=5, pady=2)
        self.auth_key_entry = tk.Entry(server_info_frame)
        self.auth_key_entry.pack(fill="x", padx=5, pady=2)

        # Create the instance info frame
        instance_info_frame = tk.LabelFrame(self.main_frame, text="Instance Info")
        instance_info_frame.pack(side="right", padx=10, pady=10, fill="y")

        # Create the instance info widgets
        workspace_label = tk.Label(instance_info_frame, text="Workspace:")
        workspace_label.pack(anchor="w", padx=5, pady=2)
        self.workspace_combo = ttk.Combobox(instance_info_frame, state="readonly")
        self.workspace_combo.pack(fill="x", padx=5, pady=2)

        model_label = tk.Label(instance_info_frame, text="Model:")
        model_label.pack(anchor="w", padx=5, pady=2)
        self.model_combo = ttk.Combobox(instance_info_frame, state="readonly")
        self.model_combo.pack(fill="x", padx=5, pady=2)

        instance_label = tk.Label(instance_info_frame, text="Instance:")
        instance_label.pack(anchor="w", padx=5, pady=2)
        self.instance_combo = ttk.Combobox(instance_info_frame, state="readonly")
        self.instance_combo.pack(fill="x", padx=5, pady=2)

        # Create the instance tree frame
        instance_tree_frame = tk.LabelFrame(self.main_frame, text="Instance Tree")
        instance_tree_frame.pack(side="bottom", padx=10, pady=10, fill="both", expand=True)
    
        # Create the instance tree widget
        self.instance_tree = ttk.Treeview(instance_tree_frame)
        self.instance_tree.pack(fill="both", expand=True)
    
        # Create the data frame
        data_frame = tk.LabelFrame(self.main_frame, text="Data")
        data_frame.pack(side="bottom", padx=10, pady=10, fill="both", expand=True)
    
        # Create the data widget
        self.data_text = tk.Text(data_frame)
        self.data_text.pack(fill="both", expand=True)
    
        # Create the connect button
        connect_button = tk.Button(server_info_frame, text="Connect", command=self.connect)
        connect_button.pack(side="bottom", padx=5, pady=10)
    
        # Create the status light
        self.status_light = tk.Label(server_info_frame, text="", width=2)
        self.status_light.pack(side="right", padx=5)
    
        # Initialize the instance tree columns
        self.instance_tree["columns"] = ("Model", "Instance")
        self.instance_tree.column("#0", width=150, minwidth=150, stretch=tk.YES)
        self.instance_tree.column("Model", width=150, minwidth=150, stretch=tk.YES)
        self.instance_tree.column("Instance", width=150, minwidth=150, stretch=tk.YES)
        self.instance_tree.heading("#0", text="Workspace")
        self.instance_tree.heading("Model", text="Model")
        self.instance_tree.heading("Instance", text="Instance")
    
        # Set default values
        self.server_ip_entry.insert(0, "localhost")
        self.server_port_entry.insert(0, "443")
        self.auth_key_entry.insert(0, "abc123")
    
        self.workspace_combo["values"] = ["Workspace 1", "Workspace 2", "Workspace 3"]
        self.workspace_combo.current(0)
    
        self.model_combo["values"] = ["Model 1", "Model 2", "Model 3"]
        self.model_combo.current(0)
    
        self.instance_combo["values"] = ["Instance 1", "Instance 2", "Instance 3"]
        self.instance_combo.current(0)
    
    def save_data(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            with open(file_path, "w") as f:
                f.write(f"Server IP: {self.server_ip_entry.get()}\n")
                f.write(f"Server Port: {self.server_port_entry.get()}\n")
                f.write(f"Auth Key: {self.auth_key_entry.get()}\n")
                f.write(f"Workspace: {self.workspace_combo.get()}\n")
                f.write(f"Model: {self.model_combo.get()}\n")
                f.write(f"Instance: {self.instance_combo.get()}\n")
            messagebox.showinfo("Save Data", "Data saved successfully.")
    
    def load_data(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt")
        if file_path:
            with open(file_path, "r") as f:
                data = f.read()
                lines = data.split("\n")
                self.server_ip_entry.delete(0, tk.END)
                self.server_ip_entry.insert(0, lines[0].split(": ")[1])
                self.server_port_entry.delete(0, tk.END)
                self.server_port_entry.insert(0, lines[1].split(": ")[1])
                self.auth_key_entry.delete(0, tk.END)
                self.auth_key_entry.insert(0, lines[2].split(": ")[1])
                self.workspace_combo.set(lines[3].split(": ")[1])
                self.model_combo.set(lines[4].split(": ")[1])
                self.instance_combo.set(lines[5].split(": ")[1])
                messagebox.showinfo("Load Data", "Data loaded successfully.")

    def show_documentation(self):
        try:
            with open("docs.txt", "r") as f:
                self.data_text.delete("1.0", tk.END)
                self.data_text.insert(tk.END, f.read())
        except FileNotFoundError:
            messagebox.showerror("Documentation", "The documentation file is missing.")

    def show_about(self):
        messagebox.showinfo("About", "This is a sample GUI created with Python tkinter.")
    
    def connect(self):
        self.status_light.configure(bg="yellow")
        self.root.update()
    
        server_ip = self.server_ip_entry.get()
        server_port = self.server_port_entry.get()
        auth_key = self.auth_key_entry.get()
    
        call_string = "/osmc/workspaces?includeBody=True"
        url = f"https://{server_ip}:{server_port}{call_string}"
        headers = {"accept": "application/ld+json", "authorization": f"Basic {auth_key}"}
        resp_ws = requests.get(url, headers=headers, verify=False)
        if resp_ws.status_code == 200:
            workspaces = resp_ws.json()
    
            workspace_dict = {}
            for i in range(len(workspaces["ldp:contains"])):
                workspace_dict[workspaces["ldp:contains"][i][1]["dcterms:title"]] = workspaces["ldp:contains"][i][0]["@id"]
    
            self.workspace_combo["values"] = list(workspace_dict.keys())
            self.workspace_combo.current(0)
    
            self.status_light.configure(bg="green")
        else:
            messagebox.showerror("Connection Error", "Unable to connect to the server.")
            
if __name__ == "__main__":
    root = tk.Tk()
    gui = GUI(root)
    root.mainloop()
