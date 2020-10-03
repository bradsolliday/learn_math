import tkinter as tk

# Returns the root of a button which loads a profile when clicked
def profile_button(master, name):
    from windowController import load_overview_page

    return tk.Button(
                master=master,
                text=name,
                relief=tk.RAISED,
                borderwidth=4,
                command=lambda: load_overview_page(master, name))


class ProfileList(tk.Frame):
    
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        self.configure(relief=tk.RIDGE, bg="yellow", borderwidth=5)
        self.columnconfigure(0, weight=1, minsize=80)

        from dataManager import profile_list
        profile_names = profile_list()

        self.buttons = [None] * len(profile_names)

        for row, name in enumerate(profile_names):
            self.buttons[row] = profile_button(self, name)
            self.buttons[row].grid(
                                row=row,
                                column=0,
                                stick=tk.E+tk.W,
                                padx=3,
                                pady=3)

# Returns the root frame of the profile page
def profile_page(master):
    from windowController import load_create_profile_page

    root = tk.Frame(master=master)

    root.columnconfigure(0, weight=1, minsize=20)
    root.columnconfigure(1, weight=1, minsize=100)
    root.columnconfigure(2, weight=1, minsize=20)

    fastmath_label = tk.Label(master=root, text="Fast Math")
    fastmath_label.grid(row=0, column=1)

    select_profile_label = tk.Label(master=root, text="Select Profile")
    select_profile_label.grid(row=1, column=1, sticky=tk.W)

    profiles = ProfileList(master=root)
    profiles.grid(row=2, column=1, sticky=tk.E+tk.W)

    create_profile_button = tk.Button(
        master=root,
        text="Create New Profile",
        command=lambda: load_create_profile_page(master))
    create_profile_button.grid(row=3, column=1, sticky=tk.W+tk.E)

    return root
