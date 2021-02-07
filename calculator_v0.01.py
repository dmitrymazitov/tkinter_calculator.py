import tkinter as tk

class Calculator:
	def __init__(self):
		
		self.root = tk.Tk()
		
		self.entry = tk.Entry(self.root, width=15, bd=1, font=('Arial', 20), justify=tk.RIGHT)
		self.entry.grid(row=0, column=0, columnspan=3, stick='wens')
		self.entry.insert(0, '0')
		
		self.digit = 0
		self.list_buttons = []
		self.d_buttons = ['=', '+', '-' , '*', '/']
		
		for r in range(1, 4):
			for col in range(3):
				self.digit+=1
				self.list_buttons.append(tk.Button(self.root, text=f'{self.digit}', bg='grey', bd=2, font=('Arial', 15), command = lambda x=self.digit-1: self.click_button(x)))
				self.list_buttons[self.digit-1].grid(row=r, column=col, stick='wens')
		
		self.list_buttons.append(tk.Button(self.root, text='0', font=('Arial', 15), command = lambda x=0: self.click_button(x-1)))
		self.list_buttons[-1].grid(row=4, column=1, stick='wens')
		
		self.clean_button = tk.Button(self.root, text='C', font=('Arial', 15), command=self.clean_win)
		self.clean_button.grid(row=4, column=2, stick='wens')
		
		self.back_button = tk.Button(self.root, text='#', font=('Arial', 15), command=self.back_mean)
		self.back_button.grid(row=4, column=0, stick='wens')
		
		
		for d in range(len(self.d_buttons)):
				self.button = tk.Button(self.root, text=f'{self.d_buttons[d]}', font=('Arial', 15), command=lambda x=d: self.d_handler(x))
				self.button.grid(row=d, column=3, stick='wens')
		
		for x in range(4):
			self.root.grid_columnconfigure(x, minsize=60)
			self.root.grid_rowconfigure(x, minsize=60)
		
		tk.mainloop()
			
	def d_handler(self, x):
		self.value = self.entry.get() + self.d_buttons[x]
		self.entry.delete(0, tk.END)
		if self.value[0] =='0' and len(self.value) > 1:
			self.entry.insert(0, self.value[1:])
		else:
			self.entry.insert(0, self.value)
		
	def click_button(self, x):
		self.value = self.entry.get() + str(self.list_buttons[x]['text'])
		self.entry.delete(0, tk.END)
		if self.value[0] == '0' and len(self.value) > 1:
			self.entry.insert(0, self.value[1:])
		else:
			self.entry.insert(0, self.value)
		
	def clean_win(self):
		self.entry.delete(0, tk.END)
		self.entry.insert(0, '0')
		
	def back_mean(self):
		self.value = self.entry.get()[:-1]
		self.entry.delete(0, tk.END)
		self.entry.insert(0, self.value)
		if len(self.value) == 0:
			self.entry.insert(0, '0') 

if __name__ == '__main__':	
	app = Calculator()
	
