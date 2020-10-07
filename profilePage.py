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

class ProfileButton(tk.Button):

    def __init__(self, name, *args, **kwargs):
        tk.Button.__init__(self, *args, **kwargs)
        self.name = name
        self.become_normal()

    def become_normal(self):
        from windowController import load_overview_page
        self.configure(
            text=self.name,
            relief=tk.RAISED,
            bg="SystemButtonFace",
            borderwidth=4,
            command=lambda: load_overview_page(self.master, self.name))

    def become_delete(self):
        from windowController import load_profile_page
        from dataManager import delete_profile
        self.configure(
            text = "DELETE -- " + self.name,
            bg="red",
            command=lambda: (delete_profile(self.name),
                             load_profile_page(self.master)))


class ProfileList(tk.Frame):
  
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        self.configure(relief=tk.RIDGE, bg="yellow", borderwidth=5)
        self.columnconfigure(0, weight=1, minsize=80)

        from dataManager import profile_list
        profile_names = profile_list()

        self.buttons = [None] * len(profile_names)

        for row, name in enumerate(profile_names):
            self.buttons[row] = ProfileButton(name, master=self)
            self.buttons[row].grid(
                                row=row,
                                column=0,
                                stick=tk.E+tk.W,
                                padx=3,
                                pady=3)

    def to_normal(self):
        for button in self.buttons:
            button.become_normal()


    def to_delete(self):
        for button in self.buttons:
            button.become_delete()


class ProfilePage(tk.Frame):

    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        
        self.columnconfigure(0, weight=1, minsize=20)
        self.columnconfigure(1, weight=1, minsize=100)
        self.columnconfigure(2, weight=1, minsize=20)
        
        fastmath_label = tk.Label(master=self, text="Fast Math")
        fastmath_label.grid(row=0, column=1)

        select_profile_label = tk.Label(master=self, text="Select Profile")
        select_profile_label.grid(row=1, column=1, sticky=tk.W)

        profiles = ProfileList(master=self)
        profiles.grid(row=2, column=1, sticky=tk.E+tk.W)

        from windowController import load_create_profile_page
        create_profile_button = tk.Button(
            master=self,
            text="Create New Profile",
            command=lambda: load_create_profile_page(self.master))
        create_profile_button.grid(row=3, column=1, sticky=tk.W+tk.E)

        delete_profile_button = tk.Button(master=self)

        def handle_cancel_click():
            delete_profile_button.configure(
                    text="Delete Existing Profile",
                    bg="red",
                    command=handle_delete_click)
            profiles.to_normal()
        
        def handle_delete_click():
            delete_profile_button.configure(
                    text="Cancel",
                    bg="green",
                    command=handle_cancel_click)
            profiles.to_delete()
            
        handle_cancel_click()
        delete_profile_button.grid(row=4, column=1, sticky=tk.W+tk.E)

# Returns the root frame of the profile page
def profile_page(master):
    return ProfilePage(master=master)

