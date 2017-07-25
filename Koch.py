import turtle

def koch(t, order, size):
    if order == 0:          # The base case is just a straight line
        t.forward(size)
    else:
        koch(t, order-1, size/3)   # Go 1/3 of the way
        t.left(60)
        koch(t, order-1, size/3)
        t.right(120)
        koch(t, order-1, size/3)
        t.left(60)
        koch(t, order-1, size/3)
        
if __name__ == '__main__':
    t = turtle.Turtle()
    myWin = t.screen
    t.speed(1)
    koch(t, 3, 300)
    myWin.exitonclick()