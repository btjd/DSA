import turtle
from random import randint  

def tree(length, t):
    if length > 5:
        t.pensize(length * 0.3)
        t.forward(length)
        t.right(20)
        t.pensize(length * 0.2)
        tree(length - randint(5,15), t)
        t.left(40)
        t.pensize(length * 0.2)
        tree(length - randint(5,10), t)
        t.right(20)
        t.backward(length)

if __name__ == '__main__':
    length = 90
    t = turtle.Turtle()
    myWin = t.screen
    t.left(90)
    t.up()
    t.backward(150)
    t.down()
    t.color("black")
    t.speed(10)
    tree(length, t)
    myWin.exitonclick()