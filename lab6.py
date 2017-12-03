from turtle import *
import random
import math
class Ball(Turtle):
	def __init__(self,radius,color,speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius)
		self.color(color)
		self.speed(speed)


a=Ball(5,"green",1)
a.pu()
a.goto(-100,100)
a.pd()
b=Ball(3,"yellow",1)
b.pu()
b.goto(-100,100)
b.pd()



ball1_x = a.xcor()
ball1_y = a.ycor()
ball2_x = b.xcor()
ball2_y = b.ycor()


def check_collision(ball1,ball2):
	if (ball1.shapesize()[0]+ball2.shapesize()[0])>math.sqrt(math.pow(ball1_x-ball2_x,2)+math.pow(ball1_y-ball2_y,2)):
		ball1.color("red")
		ball2.color("blue")	

check_collision(a,b)