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

    def start(self):
        self.matrix = [[0]*4 for _ in range(4)]
        r = random.randint(0,3)
        c = random.randint(0,3)
        self.matrix[r][c] = 2
        self.arr[r][c]['frame'].configure(bg=c.CELL_COLORS[2])
        self.arr[r][c]['number'].configure(bg=c.CELL_COLORS[2], fg=c.CELL_NUMBER_COLORS[2], font=c.CELL_NUMBER_FONTS[2], text='2')
        self.score = 0

    def stack(self):
        temp = [[0]*4 for _ in range(4)]
        for i in range(4):
            idx = 0
            for j in range(4):
                if self.matrix[i][j] != 0:
                    temp[i][idx] = self.matrix[i][j]
                    idx += 1
        self.matrix = temp
    def merge(self):
        for i in range(4):
            for j in range(3):
                if self.matrix == self.matrix[i][j+1] and self.matrix[i][j] != 0:
                    self.matrix[i][j] *=2
                    self.matrix[i][j+1] = 0
                    self.score += self.matrix[i][j]
    def backwards(self):
        temp = []
        for i in range(4):
            temp.append([])
            for j in range(4):
                temp[i].append(self.matrix[i][3-j])
        self.matrix = temp


def main():
    gamePlan()


if __name__ == "__main__":
    main()