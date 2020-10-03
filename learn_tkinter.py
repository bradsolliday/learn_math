import tkinter as tk

class Fields:

	# master is a tkinter object
	def __init__(self, master):
		self.frame = tk.Frame(master=master, relief=tk.SUNKEN, borderwidth=3)
		self.frame.columnconfigure(0, weight=0, minsize=50)
		self.frame.columnconfigure(1, weight=1, minsize=50)
		self.frame.pack(fill=tk.X)
		self.row = 0

	# text is a string
	def add_field(self, text):
		label = tk.Label(master=self.frame, text= text + ":")
		entry = tk.Entry(master=self.frame, width= 40)

		label.grid(row=self.row, column=0, sticky="e")
		entry.grid(row=self.row, column=1, sticky=tk.E+tk.W)

		self.row += 1

class Buttons:

	# master is a tkinter object
	def __init__(self, master):
		self.frame = tk.Frame(master=master, borderwidth=3)
		self.frame.pack(side=tk.RIGHT, anchor=tk.NW)
		self.columns=0

	# text is a string
	def add_button(self, text):
		spacing = tk.Frame(master=self.frame, borderwidth=3)
		button = tk.Button(master=spacing, text=text)
		handle_click = lambda event: print(f"The {text} button was clicked!")
		button.bind("<Button-1>", handle_click)
		button.pack()
		spacing.grid(row=0, column=self.columns)
		self.columns += 1

window = tk.Tk()
fields = Fields(window)
buttons = Buttons(window)

field_names = [
	"First Name",
	"Last Name",
	"Address Line 1",
	"Address Line 2",
	"City",
	"State/Province",
	"Postal Code",
	"Country"
	]

for name in field_names:
	fields.add_field(name)

buttons.add_button("Submit")
buttons.add_button("Clear")


window.mainloop()