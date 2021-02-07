import tkinter as tk

class Calculator:
	def __init__(self):
		
		self.root = tk.Tk()
		self.root.title('Калькулятор')
		self.root.geometry('300x350')
		self.root.resizable(False, False)
		
		#создание поля ввода
		self.entry = tk.Entry(self.root, width=15, bd=1, font=('Arial', 20), justify=tk.RIGHT)
		self.entry.grid(row=0, column=0, columnspan=3, stick='wens')
		self.entry.insert(0, '0')
		
		self.digit = 1
		self.digit_buttons = []
		self.d_buttons = ['=', '+', '-' , '*', '/']

		#создание кнопок цифр путем цикла и пакуем их в список		
		for r in range(1, 5):
			for col in range(3):
				self.digit_buttons.append(tk.Button(self.root, text=f'{self.digit}', bg='grey', bd=2, font=('Arial', 15), command=lambda x=self.digit: self.click_button(x-1)))
				self.digit_buttons[self.digit-1].grid(row=r, column=col, stick='wens', padx=1, pady=1)
				#заменяем "десятку" на "ноль" и завершаем цикл 
				if self.digit_buttons[self.digit-1]['text'] == '10':
					self.digit_buttons[self.digit-1]['text'] = '0'
					self.digit_buttons[self.digit-1].grid(row=4, column=1, stick='wens', padx=1, pady=1)
					break
				self.digit+=1
	
		#создание кнопки "очистить"
		self.clean_button = tk.Button(self.root, text='C', font=('Arial', 15), command=self.clean_win)
		self.clean_button.grid(row=4, column=2, stick='wens', padx=1, pady=1)
		
		#создание кнопки "отмена/назад"
		self.back_button = tk.Button(self.root, text='←', font=('Arial', 25), command=self.back_mean)
		self.back_button.grid(row=4, column=0, stick='wens', padx=1, pady=1)

		#создание кнопок "операции"
		for d in range(len(self.d_buttons)):
				self.button = tk.Button(self.root, text=f'{self.d_buttons[d]}', font=('Arial', 25), command=lambda x=d: self.operator_handler(x))
				self.button.grid(row=d, column=3, stick='wens', padx=1, pady=1)
		
		for x in range(5):
			self.root.grid_columnconfigure(x, minsize=70)
			self.root.grid_rowconfigure(x, minsize=70)
		
		tk.mainloop()
			
	#создание обработкича "знаков операций"	
	def operator_handler(self, x):
		self.value = self.entry.get()
		if self.d_buttons[x] == '=':
			self.sum = eval(self.value)
			self.entry.delete(0, tk.END)
			self.entry.insert(0, int(self.sum))
		else:
			self.value = self.entry.get() + self.d_buttons[x]
			self.entry.delete(0, tk.END)
			if self.value[0] =='0' and len(self.value) > 1:
				self.entry.insert(0, self.value[1:])
			else:
				self.entry.insert(0, self.value)

	#создание обработчика для "кнопок цифр"	
	def click_button(self, x):
		self.value = self.entry.get() + str(self.digit_buttons[x]['text'])
		self.entry.delete(0, tk.END)
		if self.value[0] == '0' and len(self.value) > 1:
			self.entry.insert(0, self.value[1:])
		else:
			self.entry.insert(0, self.value)
	
	#создание обработчик "очистить"	
	def clean_win(self):
		self.entry.delete(0, tk.END)
		self.entry.insert(0, '0')
	
	#создание обработчика "отмены/назад"	
	def back_mean(self):
		self.value = self.entry.get()[:-1]
		self.entry.delete(0, tk.END)
		self.entry.insert(0, self.value)
		if len(self.value) == 0:
			self.entry.insert(0, '0') 

if __name__ == '__main__':	
	app = Calculator()
	
