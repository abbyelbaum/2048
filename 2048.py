import tkinter as tk
import colors as c
import random

class gamePlan(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.master.title('2048')
        self.board = tk.Frame(self,bg= 3, width= 400, height= 400)
        self.board.grid(pady=(80,0))
        self.create_graphics()
        self.start()
        self.master.bind("<Left>",self.left)
        self.master.bind("<Right>",self.right)
        self.master.bind("<Up>",self.up)
        self.master.bind("<Down>",self.down)
        self.main()
    def create_graphics(self):
        self.arr = []
        for i in range(4):
            temp = []
            for j in range(4):
                f = tk.Frame(self.board,bg = c.EMPTY_CELL_COLOR, width = 100, height= 100)