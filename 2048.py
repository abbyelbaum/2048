import tkinter as tk
import colors as color
import random

class gamePlan(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.master.title('2048')
        self.board = tk.Frame(self,bg= color.GRID_COLOR, bd = 3, width= 400, height= 400)
        self.board.grid(pady=(80,0))
        self.create_graphics()
        self.start()
        self.master.bind("<Left>",self.left)
        self.master.bind("<Right>",self.right)
        self.master.bind("<Up>",self.up)
        self.master.bind("<Down>",self.down)
        self.mainloop()
    def create_graphics(self):
        self.arr = []
        for i in range(4):
            temp = []
            for j in range(4):
                f = tk.Frame(self.board,bg = color.EMPTY_CELL_COLOR, width = 100, height= 100)
                f.grid(row = i, column = j, padx = 5, pady = 5)
                num = tk.Label(self.board, bg=color.EMPTY_CELL_COLOR)
                num.grid(row=i, column=j)
                data = {"frame": f, "number": num}
                temp.append(data)
            self.arr.append(temp)
        score = tk.Frame(self)
        score.place(relx=0.5, y=40, anchor="center")
        tk.Label(score, text = "Score", font = color.SCORE_LABEL_FONT).grid(row = 0)
        self.score_label = tk.Label(score, text="0", font=color.SCORE_FONT)
        self.score_label.grid(row=1)
    def start(self):
        self.matrix = [[0]*4 for _ in range(4)]
        r = random.randint(0,3)
        c = random.randint(0,3)
        self.matrix[r][c] = 2
        self.arr[r][c]['frame'].configure(bg=color.CELL_COLORS[2])
        self.arr[r][c]['number'].configure(bg=color.CELL_COLORS[2], fg=color.CELL_NUMBER_COLORS[2], font=color.CELL_NUMBER_FONTS[2], text='2')
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
                if self.matrix[i][j] != 0 and self.matrix[i][j] == self.matrix[i][j + 1]:
                    self.matrix[i][j] *= 2
                    self.matrix[i][j + 1] = 0
                    self.score += self.matrix[i][j]
    def backwards(self):
        temp = []
        for i in range(4):
            temp.append([])
            for j in range(4):
                temp[i].append(self.matrix[i][3-j])
        self.matrix = temp
    def translate(self):
        temp = [[0] * 4 for _ in range(4)]
        for i in range(4):
            for j in range(4):
                temp[i][j] = self.matrix[j][i]
        self.matrix = temp
    def add(self):
        r = random.randint(0,3)
        c = random.randint(0,3)
        while self.matrix[r][c]!=0:
            r = random.randint(0,3)
            c = random.randint(0,3)
        self.matrix[r][c] = random.choice([2,4])
    def update_graphics(self):
        for i in range(4):
            for j in range(4):
                val = self.matrix[i][j]
                if val == 0:
                    self.arr[i][j]['frame'].configure(bg=color.EMPTY_CELL_COLOR)
                    self.arr[i][j]['number'].configure(bg = color.EMPTY_CELL_COLOR,text='')
                else:
                    self.arr[i][j]['frame'].configure(bg=color.CELL_COLORS[val])
                    self.arr[i][j]['number'].configure(bg=color.CELL_COLORS[val],fg=color.CELL_NUMBER_COLORS[val],font= color.CELL_NUMBER_FONTS[val], text=str(val))
        self.score_label.configure(text = self.score)
        self.update_idletasks()
    def left(self,event):
        self.stack()
        self.merge()
        self.stack()
        self.add()
        self.update_graphics()
        self.end()
    def right(self,event):
        self.backwards()
        self.stack()
        self.merge()
        self.stack()
        self.backwards()
        self.add()
        self.update_graphics()
        self.end()
    def up(self,event):
        self.translate()
        self.stack()
        self.merge()
        self.stack()
        self.translate()
        self.add()
        self.update_graphics()
        self.end()
    def down(self,event):
        self.translate()
        self.backwards()
        self.stack()
        self.merge()
        self.stack()
        self.backwards()
        self.translate()
        self.add()
        self.update_graphics()
        self.end()
    def h_real(self):
        for i in range(4):
            for j in range(3):
                if self.matrix[i][j] == self.matrix[i][j+1]:
                    return True
        return False
    def v_real(self):
        for i in range(3):
            for j in range(4):
                if self.matrix[i][j] == self.matrix[i+1][j]:
                    return True
        return False
    def end(self):
        if any(2048 in row for row in self.matrix):
            end_frame = tk.Frame(self.board,borderwidth=2)
            end_frame.place(relx=0.5,rely=0.5,anchor='center')
            tk.Label(end_frame,text='Winner!!',bg=color.WINNER_BG,fg=color.GAME_OVER_FONT_COLOR,font=color.GAME_OVER_FONT).pack()
        elif not any(0 in row for row in self.matrix) and not self.h_real() and not self.v_real():
            end_frame = tk.Frame(self.board,borderwidth=2)
            end_frame.place(relx=0.5,rely=0.5, anchor='center')
            tk.Label(end_frame,text='Game Over :(', bg = color.LOSER_BG, fg=color.GAME_OVER_FONT_COLOR, font=color.GAME_OVER_FONT).pack()
            

def main():
    gamePlan()


if __name__ == "__main__":
    main()