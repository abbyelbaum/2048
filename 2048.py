import tkinter as tk
import colors as c
import random

class gamePlan(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.master.title('2048')
        self.board = tk.Frame(self,bg= c.GRID_COLOR, bd = 3, width= 400, height= 400)
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
                f.grid(row = i, column = j, padx = 5, pady = 5)
                num = tk.Label(self.board, bg=c.EMPTY_CELL_COLOR)
                num.grid(row=i, column=j)
                data = {"frame": f, "number": num}
                temp.append(data)
            self.arr.append(temp)
        score = tk.Frame(self)
        score.place(relx=0.5, y=40, anchor="center")
        tk.Label(score, text = "Score", font = c.SCORE_LABEL_FONT).grid(row = 0)
        self.score_label = tk.Label(score, text="0", font=c.SCORE_FONT)
        self.score_label.grid(row=1)



def main():
    gamePlan()


if __name__ == "__main__":
    main()