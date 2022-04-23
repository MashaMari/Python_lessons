from logging import root
import tkinter as tk

class MainApp(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent

        self.label = tk.Label(parent, text='Hello!')
        self.label.pack()
        self.button1 = tk.Button(parent, text='Hello!', command=self.label.pack_forget)
        self.button1.pack()
        self.button2 = tk.Button(parent, text='Add!', command=self.new_window)
        self.button2.pack()
        self.button3 = tk.Button(parent, text='Delete!', command=self.delete_all_windows)
        self.button3.pack()

        self.windows = []
        self.windows_counter = 0

    def new_window(self):
        self.windows.append(tk.Tk())
        if self.windows_counter % 2 == 0:
            tk.Label(self.windows[self.windows_counter], text=f'{self.windows_counter}').pack()
            tk.Button(self.windows[self.windows_counter], text='destoroy', command=self.windows[self.windows_counter].destroy).pack()

        self.windows_counter += 1    

    def delete_all_windows(self):
        for window in self.windows:
            try:
                window.destroy()
            except:  
                pass

root = tk.Tk(screenName='AAA')
ma = MainApp(root)
ma.pack()
root.mainloop()        