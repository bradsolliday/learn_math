import tkinter as tk

def create_profile_page(master):

	from dataManager import create_profile
	from windowController import load_profile_page
	
	root = tk.Frame(master=master)

	instructions_label = tk.Label(
		master=root,
		text="Enter the name of your new profile")
	instructions_label.pack()

	entry = tk.Entry(master=root, width=40)
	entry.pack()

	button_frame = tk.Frame(master=root)
	button_frame.pack()

	def handle_create_click():
		new_profile_name = entry.get()
		if new_profile_name == "":
			# TODO - Handle empty input
			print("empty input handling not implemented")
		create_profile(new_profile_name)
		load_profile_page(master)

	create_button = tk.Button(
		master=button_frame,
		text="Create Profile",
		command=handle_create_click)
	create_button.grid(row=0, column=0)

	cancel_button = tk.Button(
		master=button_frame,
		text="Cancel",
		command=lambda: load_profile_page(master))
	cancel_button.grid(row=0, column=1)

	return root