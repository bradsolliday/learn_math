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



# Returns the root frame of the list of profile buttons
def profile_list(master):
	from dataManager import profile_list

	profiles = profile_list()

	root = tk.Frame(master=master, relief=tk.RIDGE, bg="yellow", borderwidth=5)
	root.columnconfigure(0, weight=1, minsize=80)

	for row, profile_name in enumerate(profiles):
		button = profile_button(root, profile_name)
		button.grid(row=row, column=0, stick=tk.E+tk.W, padx=3, pady=3)

	return root

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

	profiles = profile_list(root)
	profiles.grid(row=2, column=1, sticky=tk.E+tk.W)

	create_profile_button = tk.Button(
		master=root,
		text="Create New Profile",
		command=lambda: load_create_profile_page(master))
	create_profile_button.grid(row=3, column=1, sticky=tk.W+tk.E)

	return root