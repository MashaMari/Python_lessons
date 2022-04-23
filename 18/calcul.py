import tkinter as tk

win = tk.Tk()

result_field = tk.Entry(state='disabled')
result_field.grid(row=0, column=0, columnspan=4)

for i in range(1,4):
    for j in range(0,3):
        button = tk.Button(win, text=f"{(i - 1) * 3 + j + 1}", command=lambda: result_field.config(text=result_field.cget("text")+str((i - 1) * 3 + j + 1)))
        button.grid(row=i+1, column=j)

nol_button = tk.Button(win, text='0')
nol_button.grid(row=5, column=1)
plus_button = tk.Button(win, text='+')
plus_button.grid(row=2, column=3)
minus_button = tk.Button(win, text='_')
minus_button.grid(row=3, column=3)
mult_button = tk.Button(win, text='*')
mult_button.grid(row=4, column=3)
div_button = tk.Button(win, text='/')
div_button.grid(row=5, column=3)
ravno_button = tk.Button(win, text='=', width=5)
ravno_button.grid(row=1, column=1)
zap_button = tk.Button(win, text=',')
zap_button.grid(row=5, column=2)
ster_button = tk.Button(win, text='⌫')
ster_button.grid(row=1, column=3)

win.mainloop()