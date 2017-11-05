import turtle
turtle.speed(1)


sidelength=100
angle=144

"""for i in range(3):
	for i in range(2):
		turtle.forward(sidelength)
		turtle.right(angle)
"""

'''for i in range(3):
	turtle.pencolor("red")
	turtle.forward(sidelength)
	turtle.right(angle)
	turtle.pencolor("yellow")
	turtle.forward(sidelength)
	turtle.right(angle)'''

turtle.register_shape("turtle_head1", ((100,0),(100,-100),(50,-200),(0,-100),(0,0)))
turtle.addshape("turtlehead.gif")
turtle.shape("turtle_head1/turtlehead.gif")
turtle.getshapes()

turtle.mainloop()

