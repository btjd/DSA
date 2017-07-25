import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()

# def paint(myTurtle, line):
#     myTurtle.forward(line)
#     myTurtle.right(90)

def fib(n):
     a,b = 1,1
     for i in range(n-1):
        a,b = b,a+b
        myTurtle.forward(a)
        myTurtle.right(90)
    
fib(15)
myWin.exitonclick()