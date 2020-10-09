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

        op_scores = {Operation.ADDITION: profile.addition,
                     Operation.MULTIPLICATION: profile.multiplication}
        scores = op_scores[operation]

        for operand1 in range(1, 13):
            for operand2 in range(1, 13):
                label = label_template(op_func[operation](operand1, operand2))
                score = scores[operand1 - 1][operand2 - 1]
                if score < 25:
                    color = "red"
                elif score < 50:
                    color = "yellow"
                elif score < 75:
                    color = "green"
                else:
                    color = "cyan"
                label.configure(bg=color)
                label.grid(row=operand1, column=operand2)


class SelectOperationButtons(tk.Frame):

    def __init__(self, display_table, displayed_operation, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        self.displayed_op = displayed_operation

        self.buttons = {}
        def handle_click(op):
            if op != self.displayed_op:
                self.buttons[self.displayed_op].configure(relief=tk.RAISED)
                self.buttons[op].configure(relief=tk.SUNKEN)
                self.displayed_op = op
                display_table(op)

        for n,op in enumerate(Operation):

            self.buttons[op] = tk.Button(
                                master=self,
                                text=OP_SYMBOL[op],
                                command=
                                    (lambda x: lambda: handle_click(x))(op))
            # (lambda x: lambda: foo(x))(op), as opposed to lambda: foo(op),
            # is needed because python closures capture name and scope. Since
            # op has same name and scope each time command is set, all the
            # commands will have the same value of op (the last one). By
            # passing op in as a function argument, the scope is changed and
            # each command uses the right value of op. Kinda wierd.

            if op == self.displayed_op:
                self.buttons[op].configure(relief=tk.SUNKEN)

            self.buttons[op].grid(row=0, column=n)
            

class OverviewPage(tk.Frame):

    def __init__(self, profile, operation=Operation.ADDITION, *args, **kwargs):
        from windowController import load_profile_page

        tk.Frame.__init__(self, *args, **kwargs)

        back_button = tk.Button(
                            master=self,
                            text="Go Back",
                            command=lambda: load_profile_page(self))
        back_button.grid(row=0, column=0)

        self.tables = {}
        for op in Operation:
            self.tables[op] = OverviewTable(profile, op, master=self)

        self.active_table = self.tables[operation]
        self.active_table.grid(row=1, column=1)

        op_select_frame = SelectOperationButtons(
                            lambda op: self.display_table(op),
                            operation,
                            master=self)
        op_select_frame.grid(row=0, column=1)

    def display_table(self, operation):
        self.active_table.grid_forget()
        self.active_table = self.tables[operation]
        self.active_table.grid(row=1, column=1)




# operation is of class Operation
# returns frame containing the overview page
def overview_page(master, profile, operation=Operation.ADDITION):
    return OverviewPage(profile, operation, master=master)
