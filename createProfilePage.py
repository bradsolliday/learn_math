import tkinter as tk

class CreateProfilePage(tk.Frame):

    def __init__(self, *args, **kwargs):
        from dataManager import create_profile
        from windowController import load_profile_page

        tk.Frame.__init__(self, *args, **kwargs)
        
        instructions_label = tk.Label(
            master=self,
            text="Enter the name of your new profile")
        instructions_label.pack()

        entry = tk.Entry(master=self, width=40)
        entry.pack()

        button_frame = tk.Frame(master=self)
        button_frame.pack()

        def handle_create_click():
            new_profile_name = entry.get()
            if new_profile_name != "":
                create_profile(new_profile_name)
                load_profile_page(self.master)

        create_button = tk.Button(
            master=button_frame,
            text="Create Profile",
            command=handle_create_click)
        create_button.grid(row=0, column=0)

        cancel_button = tk.Button(
            master=button_frame,
            text="Cancel",
            command=lambda: load_profile_page(self.master))
        cancel_button.grid(row=0, column=1)

def create_profile_page(master):
    return CreateProfilePage(master=master)
