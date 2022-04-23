import tkinter as tk
from tkinter import font as tkFont

class Menu(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super(Menu, self).__init__(*args, **kwargs)
        self.helv36 = tkFont.Font(family='Helvetica', size=15, weight='bold')
        self.parent = parent
        self.score = tk.Label(self, text=0)
        self.score.pack(side='left')

        self.condition = tk.Label(self, text='╳  turn')
        self.condition.pack(side='left', padx=40)

        self.refresh_button = tk.Button(self, text='🔁', width=5, font=self.helv36)
        self.refresh_button.pack(side='right')

    def update_score(self, score):
        self.score.config(text=str(score))

    def update_condition(self, condition: str):
        """
        Функция ``update_condition`` меняет значение строки состояния на ``condition``
        """
        self.condition.config(text=condition)   

    def set_game(self, game):
        self.game = game
        self.refresh_button.config(command=self.game.refresh)        

# Класс Game
class Game(tk.Frame):
    def __init__(self, parent, menu: Menu, *args, **kwargs):
        super(Game,self).__init__(*args, **kwargs)
        self.parent = parent
        self.menu = menu
        self.buttons = [[0,0,0],[0,0,0],[0,0,0]]
        self.count_moves = 0
        
        # Поле для игры в виде кнопок
        for i in range(3):
            for j in range(3):
                self.buttons[i] [j] = tk.Button(self, width=9, height=4, command= lambda i=i, j=j: self.buttonclicked(i, j))
                self.buttons[i] [j].grid(row = i, column = j, padx = 5, pady=5)

    # Функция, которая при нажатии на кнопку ставит крестик или нолик, и блокирует эту кнопку
    def buttonclicked(self, i, j):
        self.count_moves += 1
        self.menu.update_score(self.count_moves)
        if self.count_moves % 2 == 1:
            self.buttons[i] [j].config(text='╳', bg='orange', state='disabled')
            self.menu.update_condition('⭕  turn')
        else:
             self.buttons[i] [j].config(text='⭕', bg='lightblue', state='disabled')
             self.menu.update_condition('╳  turn') 
        self.check_row(i)
        self.check_col(j)
        self.check_diags()
        # Условие, которое проверяет ничью
        if self.count_moves == 9:
            self.menu.update_condition('Draw')

    # Функция, которая проверяет выигрыш строки
    def check_row(self, row):
        row_values = [x.cget('text') for x in self.buttons[row]]
        row_button = [x for x in self.buttons[row]]
        if row_values[0] == row_values[1] and row_values[1]==row_values[2] and row_values[0] != "":
            self.menu.update_condition(f'{row_values[0]}  is win')
            self.deactivate_buttons()

    # Функция, которая проверяет выигрыш колонны
    def check_col(self, col):
        col_values = [self.buttons[x] [col].cget('text') for x in range(3)]                  
        if col_values[0] == col_values[1] and col_values[1]==col_values[2] and col_values[0] != "":
            self.menu.update_condition(f'{col_values[0]}  is win')
            self.deactivate_buttons()

    # Функция, которая проверяет выигрыш диагонали
    def check_diags(self):
        main_diags_values = [self.buttons[x][x].cget('text') for x in range(3)]
        side_diags_values = [self.buttons[x][2 - x].cget('text') for x in range(3)]
        if main_diags_values[0] == main_diags_values[1] and main_diags_values[2] == main_diags_values[1] and main_diags_values[0] !='':
            self.menu.update_condition(f'{main_diags_values[0]}  is win')
        elif side_diags_values[0] == side_diags_values[1] and side_diags_values[2] == side_diags_values[1] and side_diags_values[0] !='':
            self.menu.update_condition(f'{side_diags_values[0]}  is win')
            self.deactivate_buttons()

    def deactivate_buttons(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(state='disabled')

    def refresh(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text='', state='active', bg="lightgray")
                self.buttons[i][j].update_idletasks()
        self.menu.update_condition('╳  turn')
        self.count_moves = 0
        self.menu.update_score(0)

root = tk.Tk()
m = Menu(root)
g = Game(root, m)
m.set_game(g)
g.pack(side='top', fill='both', expand=True)
m.pack(side='top', fill='both', expand=True, padx=10, pady=10)
root.mainloop()