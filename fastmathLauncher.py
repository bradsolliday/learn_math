import tkinter as tk
from windowController import load_profile_page

window = tk.Tk()
window.title("Fast Math")
load_profile_page(window)
window.mainloop()