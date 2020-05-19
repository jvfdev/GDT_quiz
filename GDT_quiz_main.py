from pathlib import Path
import os
from tkinter import *
from PIL import Image, ImageTk

# working_directory = Path.cwd()

# gdt_flatness = {'name':'flatness',
#                 'image_file_name': 'flatness.png',
#                 'Type_of_tolerance': 'Form',
#                 'datum_required': "No"}

# gdt_straightness = {'name':'straightness',
#                 'image_file_name': 'straightness.png',
#                 'Type_of_tolerance': 'Form',
#                 'datum_required': "No"}

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("GD&T Symbol Quiz")
        self.pack(fill=BOTH, expand=1)

        gdt_menu = Menu(self.master)
        self.master.config(menu=gdt_menu)

        file_menu = Menu(gdt_menu)
        file_menu.add_command(label="Exit", command=self.client_exit)
        gdt_menu.add_cascade(label="File", menu=file_menu)

    def client_exit(self):
        root.quit()

root = Tk()
root.geometry("800x600")
app = Window(root)
root.mainloop()