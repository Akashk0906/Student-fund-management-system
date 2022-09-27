import turtle
colors=["red","yellow","green","pink","sky blue"]
ak=turtle.Pen()
turtle.bgcolor("black")
for i in range(360):
    ak.pencolor(colors[i%5])
    ak.width(i/100+1)
    ak.forward(i)
    ak.left(80)