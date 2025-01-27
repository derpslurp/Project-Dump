from tkinter import *
from time import *
from Ball import *
import time

def update():
    time_string = strftime('%I:%M:%S %p')
    time_label.config(text=time_string)

    time_label.after(1000,update)

window = Tk()

WIDTH = 500
HEIGHT = 500

time_label = Label(window,font=('Arial',50))
time_label.pack()
canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

volley_ball = Ball(canvas,0,0,100,3,1,'white')
tennis_ball = Ball(canvas,0,0,50,3,4,'green')
basket_ball = Ball(canvas,0,0,125,8,7,'orange')
base_ball = Ball(canvas,0,0,40,10,6,'black')
base_ball1 = Ball(canvas,0,0,200,6,10,'blue')


update()
while True:
    volley_ball.move()
    tennis_ball.move()
    basket_ball.move()
    base_ball.move()
    base_ball1.move()
    window.update()
    time.sleep(0.01)


window.mainloop()