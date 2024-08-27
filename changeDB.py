import tkinter as tk
from tkinter import ttk
from utils.managejobs import ManageJobs
from utils.database import Database
from utils.about import About

import subprocess
import os


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Notebook to manage jobs")
        self.geometry("400x400")
        self.resizable(True, True)

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        self.database = Database()

        self.about_frame = About(self)
        self.notebook.add(self.about_frame, text="About")

        self.manage_jobs_frame = ManageJobs(self)
        self.notebook.add(self.manage_jobs_frame, text="manage urls")


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))

    res = subprocess.run(['git', 'pull'], cwd=script_dir, capture_output=True, text=True)

    app = App()
    app.mainloop()

    res = subprocess.run(['git', 'add', '.'], cwd=script_dir, capture_output=True, text=True)
    res = subprocess.run(['git', 'commit', '-m', '"updates"'], cwd=script_dir, capture_output=True, text=True)
    res = subprocess.run(['git', 'push'], cwd=script_dir, capture_output=True, text=True)