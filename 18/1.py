import tkinter as tk

window = tk.Tk()
window.title('My first window')
# Записываем экземпляр класса Label(надпись) в переменную ozon_label
ozon_label = tk.Label(window, text = 'Ozon')
ozon_label.pack()
# Записываем экземпляр класса Button(надпись) в переменную ozon_button
ozon_button = tk.Button(window, text = 'Ozon Button')
ozon_button.pack()
# Записываем экземпляр класса Entry(поле для ввода) в переменную ozon_entry
ozon_entry = tk.Entry(window, width=30)
ozon_entry.pack()
window.mainloop()