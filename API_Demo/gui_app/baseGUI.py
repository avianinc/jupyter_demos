import tkinter as tk
from tkinter import ttk, filedialog, messagebox

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("GUI with Comboboxes, Treeview, and Textarea")

        # Add menu bar with commands
        menubar = tk.Menu(master)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Save", command=self.save_data)
        filemenu.add_command(label="Load", command=self.load_data)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=master.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Documentation", command=self.show_docs)
        helpmenu.add_command(label="About", command=self.show_about)
        menubar.add_cascade(label="Help", menu=helpmenu)
        loginmenu = tk.Menu(menubar, tearoff=0)
        loginmenu.add_command(label="Login", command=self.show_login)
        menubar.add_cascade(label="Login", menu=loginmenu)
        master.config(menu=menubar)

        # Add top area with comboboxes
        top_frame = tk.Frame(master)
        top_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        tk.Label(top_frame, text="Project").grid(row=0, column=0, padx=10, pady=2)
        self.project_cb = ttk.Combobox(top_frame, state="readonly", values=["Project1", "Project2", "Project3"])
        self.project_cb.current(0)
        self.project_cb.grid(row=0, column=1, padx=10, pady=2)
        tk.Label(top_frame, text="Model").grid(row=1, column=0, padx=10, pady=2)
        self.model_cb = ttk.Combobox(top_frame, state="readonly", values=["Model1", "Model2", "Model3"])
        self.model_cb.current(0)
        self.model_cb.grid(row=1, column=1, padx=10, pady=2)
        tk.Label(top_frame, text="Instance").grid(row=2, column=0, padx=10, pady=2)
        self.instance_cb = ttk.Combobox(top_frame, state="readonly", values=["Instance1", "Instance2", "Instance3"])
        self.instance_cb.current(0)
        self.instance_cb.grid(row=2, column=1, padx=10, pady=2)

        # Add lower left area with empty treeview
        self.treeview = ttk.Treeview(master)
        self.treeview.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Add lower right area with empty textarea
        self.textarea = tk.Text(master)
        self.textarea.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    def save_data(self):
        filename = filedialog.asksaveasfilename(title="Save data", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if filename:
            with open(filename, "w") as f:
                f.write(f"{self.project_cb.get()}\n")
                f.write(f"{self.model_cb.get()}\n")
                f.write(f"{self.instance_cb.get()}\n")
                f.write(f"{self.server_ip}\n")
                f.write(f"{self.auth_key}\n")

    def load_data(self):
        filename = filedialog.askopenfilename(title="Load data", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if filename:
            with open(filename, "r") as f:
                self.project_cb.set(f.readline().strip())
                self.model_cb.set(f.readline().strip())
                self.instance_cb.set(f.readline().strip())
                self.server_ip = f.readline().strip()
                self.auth_key = f.readline().strip()
            self.update_textarea()

    def show_docs(self):
        try:
            with open("docs.txt", "r") as f:
                self.textarea.delete("1.0", tk.END)
                self.textarea.insert(tk.END, f.read())
        except FileNotFoundError:
            tk.messagebox.showerror("Error", "Documentation file not found")

    def show_about(self):
        tk.messagebox.showinfo("About", "This is a GUI created by ChatGPT")

    def show_login(self):
        self.login_window = tk.Toplevel(self.master)
        self.login_window.title("Login")
        tk.Label(self.login_window, text="Server IP").grid(row=0, column=0, padx=10, pady=10)
        self.server_ip_entry = tk.Entry(self.login_window)
        self.server_ip_entry.grid(row=0, column=1, padx=10, pady=10)
        tk.Label(self.login_window, text="Auth Key").grid(row=1, column=0, padx=10, pady=10)
        self.auth_key_entry = tk.Entry(self.login_window)
        self.auth_key_entry.grid(row=1, column=1, padx=10, pady=10)
        tk.Button(self.login_window, text="Login", command=self.login).grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def login(self):
        self.server_ip = self.server_ip_entry.get()
        self.auth_key = self.auth_key_entry.get()
        self.login_window.destroy()
        self.update_textarea()

    def update_textarea(self):
        self.textarea.delete("1.0", tk.END)
        self.textarea.insert(tk.END, f"Project: {self.project_cb.get()}\n")
        self.textarea.insert(tk.END, f"Model: {self.model_cb.get()}\n")
        self.textarea.insert(tk.END, f"Instance: {self.instance_cb.get()}\n")
        self.textarea.insert(tk.END, f"Server IP: {self.server_ip}\n")
        self.textarea.insert(tk.END, f"Auth Key: {self.auth_key}\n")

root = tk.Tk()
app = App(root)
root.mainloop()
