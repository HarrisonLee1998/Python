import turtle
turtle.setup(width=1300, height=600, startx=100, starty=400)

x=5
d=300
sum=0
turtle.pencolor("pink")
turtle.forward(-600)
turtle.left(60)
while x>=0:
    turtle.dot(10)
    turtle.forward(d)
    turtle.right(120)
    turtle.dot(10)
    turtle.forward(d)
    turtle.left(120)
    sum=sum+d
    x=x-1
    d=d-50

turtle.begin_fill()
turtle.fillcolor("pink")
turtle.color("orange")
turtle.end_fill()
turtle.left(120)
turtle.forward(sum)


