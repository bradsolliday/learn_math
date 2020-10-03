import tkinter as tk
from enum import Enum

class Operation(Enum):
	ADDITION = 1
	MULTIPLICATION = 3

OP_SYMBOL = {Operation.ADDITION: "+", Operation.MULTIPLICATION: "X"}

class OverviewTable(tk.Frame):

	def __init__(self, profile, operation, *args, **kwargs):
		tk.Frame.__init__(self, *args, **kwargs)

		def label_template(text):
			return tk.Label(
						master=self,
						text=text,
						width=6,
						height=3,
						relief=tk.GROOVE,
						borderwidth=2)

		op_label = label_template(OP_SYMBOL[operation])
		op_label.configure(relief=tk.FLAT)
		op_label.grid(row=0, column=0)

		for i in range(1, 13):
			column_label = label_template(i)
			column_label.configure(relief=tk.RAISED)
			row_label = label_template(i)
			row_label.configure(relief=tk.RAISED)
			column_label.grid(row=i, column=0)
			row_label.grid(row=0, column=i)
		
		op_func = {Operation.ADDITION: lambda a,b: a + b,
				   Operation.MULTIPLICATION: lambda a,b: a * b}

		for operand1 in range(1, 13):
			for operand2 in range(1, 13):
				label = label_template(op_func[operation](operand1, operand2))
				label.grid(row=operand1, column=operand2)


class SelectOperationButtons(tk.Frame):

	def __init__(self, display_table, *args, **kwargs):
		tk.Frame.__init__(self, *args, **kwargs)

		for n,op in enumerate(Operation):

			op_button = tk.Button(
							master=self,
							text=OP_SYMBOL[op],
							command=lambda op: lambda: display_table(op))
			op_button.grid(row=0, column=n)


def select_operation_buttons(master, current_operation, profile):
	from windowController import load_page
	root = tk.Frame(master=master)

	def load_overview_page_for(op):
		return lambda: load_page(
							master,
							lambda master: overview_page(
											master,
											profile,
											operation=op))

	# Something that caught me off guard here:
	# In Python, closures only capture the name and scope of a variable.
	# If the lambda returned by load_overview_page_for were used directly,
	# since the commmands for the buttons are defined in the same scope and
	# the loop variable op has the same name when both lambda's are defined,
	# only the last value of op is used, i.e., op will be the same Operation
	# for both buttons.
	# By instead defining the lambda in the scope of load_overview_page_for and
	# then returning it, the scopes are different, and thus the desired value
	# of op is used.
	for n,op in enumerate(Operation):

		op_button = tk.Button(
					master=root,
					text=OP_SYMBOL[op],
					command=load_overview_page_for(op))
		
		if op == current_operation:
			op_button.configure(relief=tk.SUNKEN, command=lambda: None)

		op_button.grid(row=0, column=n)

	return root


class OverviewPage(tk.Frame):

	def __init__(self, profile, operation=Operation.ADDITION, *args, **kwargs):
		from windowController import load_profile_page

		tk.Frame.__init__(self, *args, **kwargs)

		back_button = tk.Button(
							master=self,
							text="Go Back",
							command=lambda: load_profile_page(master))
		back_button.grid(row=0, column=0)

		self.tables = {}
		for op in Operation:
			self.tables[op] = OverviewTable(profile, op, master=self)

		self.active_table = self.tables[operation]
		self.active_table.grid(row=1, column=1)

		op_select_frame = SelectOperationButtons(lambda op: self.display_table(op), master=self)
		op_select_frame.grid(row=0, column=1)

	def display_table(self, operation):
		self.active_table.grid_forget()
		self.active_table = self.tables[operation]
		self.active_table.grid(row=1, column=1)




# operation is of class Operation
# returns frame containing the overview page
def overview_page(master, profile, operation=Operation.ADDITION):
	return OverviewPage(profile, operation, master=master)