import tkinter as tk

class Product:
	"""A Class for each new section in the window"""
	def __init__(self, label, color, master_row, column):
		"""Initialize the variables and call the __makeBox() function"""
		self.label = label
		self.color = color
		self.master_row = master_row
		self.column = column
		self.amount=0
		self.__makeBox(self.label, self.color, self.master_row, self.column, self.amount)

	def __makeBox(self, label, color, master_row, column, amount):
		"""Creates each component of the box and places them inside"""
		box = tk.Frame(master=self.master_row, borderwidth=1, padx=5, pady=5, bg=self.color)
		box.rowconfigure(0, minsize=60, weight=1)
		box.columnconfigure([0,1,2], minsize=60, weight=1)
		label = tk.Label(master=box, text=self.label, bg=self.color, fg="white")
		counter = tk.Label(master=box, text=self.amount, bg=self.color, fg="white")
		entryZone = tk.Entry(master=box, width=5, justify="center")
		def __plus():
			"""Function for the button to add to the current value"""
			entry = entryZone.get()
			if len(entry) == 0:
				self.amount+=1
				value = int(counter["text"])
				counter["text"] = f"{value + 1}"
			elif int(entry) >= 1:
				self.amount+=int(entry)
				value = int(counter["text"])
				counter["text"] = f"{value + int(entry)}"
			entryZone.delete(first=0, last=100)
		plusButton = tk.Button(master=box, text="+", height=1, width=5, command=__plus, bg=self.color, fg="white")
		def __minus():
			"""Function for the button to subtract from the current value"""
			entry = entryZone.get()
			if len(entry) == 0:
				self.amount-=1
				value = int(counter["text"])
				counter["text"] = f"{value - 1}"
			elif int(entry) >= 1:
				self.amount-=int(entry)
				value = int(counter["text"])
				counter["text"] = f"{value - int(entry)}"
			entryZone.delete(first=0, last=100)
		minusButton = tk.Button(master=box, text="-", height=1, width=5, command=__minus, bg=self.color, fg="white")

		label.grid(row=0, column=1, sticky="nsew")
		minusButton.grid(row=1, column=0, sticky="nsew")
		counter.grid(row=1, column=1, sticky="nsew")
		plusButton.grid(row=1, column=2, sticky="nsew")
		entryZone.grid(row=2, columnspan=3, sticky="nsew")
		box.grid(row=0, column=self.column)	