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

ball_list=[a,b]
def check_collision(ball1,ball2):
	if (ball1.shapesize()[0]+ball2.shapesize()[0])>=math.sqrt(math.pow(ball1_x-ball2_x,2)+math.pow(ball1_y-ball2_y,2)):
		ball1.color("red")
		ball2.color("blue")	
		if ball1.shapesize()[0]<ball2.shapesize()[0]:
			ball1.pu()
			ball1.goto(random.randint(-100,100),random.randint(-100,100))
		else:
			ball2.pu()
			ball2.goto(random.randint(-100,100),random.randint(-100,100))

f=0

def collision():
	for i in range(len((ball_list)+1)/2):
		check_collision(ball_list[0+f],ball_list[1+f])
		f=f+2
check_collision(a,b)
collision()