import turtle
col=('red','yellow','green','cyan','pink','white')
t=turtle.Turtle()
screen=turtle.Screen()
screen.bgcolor('black')
t.speed()
for i in range(150):

    t.color(col[i%6])
    t.forward(i*1.5)
    t.left(59)
    t.width(3)