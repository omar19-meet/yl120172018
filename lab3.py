import turtle
"""turtle.register_shape("heart.gif")
turtle.shape("heart.gif")"""

b=2
a=360/b
turtle.tracer(100000)
for i in range(int(a)):
	turtle.forward(200)
	turtle.right(45)
	turtle.forward(100)
	turtle.right(85)
	turtle.forward(50)
	turtle.penup()
	turtle.home()
	turtle.pendown()
	turtle.right(b)
	b=b+1
turtle.mainloop()

