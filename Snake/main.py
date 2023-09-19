from tkinter import *
import tkinter as tk

window = Tk()
window.title("Snake")
window.minsize(1920, 1080)

canvas = tk.Canvas(window, width=1920, height=1080,)
canvas.configure(bg='black')
canvas.pack()

x1, y1, x2, y2 = 300, 300, 330, 330
direction = 3  # 0-up  1-down  2-left  3-right

def move_up(event):
    global direction
    direction = 0

def move_down(event):
    global direction
    direction = 1

def move_left(event):
    global direction
    direction = 2

def move_right(event):
    global direction
    direction = 3

player = canvas.create_rectangle(x1, y1, x2, y2, fill='green')

window.bind("<Up>", move_up)
window.bind("<Down>", move_down)
window.bind("<Left>", move_left)
window.bind("<Right>", move_right)

def game_loop():
    if direction == 0:
        canvas.move(player, 0, -30)
    elif direction == 1:
        canvas.move(player, 0, 30)
    elif direction == 2:
        canvas.move(player, -30, 0)
    elif direction == 3:
        canvas.move(player, 30, 0)
    
    window.after(500, game_loop)  # Schedule the game loop to run again after 1000ms (1 second)

# Start the game loop
game_loop()

window.mainloop()