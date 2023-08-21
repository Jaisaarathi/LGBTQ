import turtle
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()
t.hideturtle()
t.speed(1000)
turtle.bgcolor('black')
for x in range(360):
	t.pencolor(colors[x%6])
	t.forward(x)
	t.left(61)

t.done()