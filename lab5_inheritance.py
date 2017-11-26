import turtle
from turtle import *
import random
turtle.tracer(1,0)
colormode(255)

red=random.randint(0,255)
blue=random.randint(0,255)
green=random.randint(0,255)


class Rectangle(Turtle):
	def __init__(self,width,height):
		Turtle.__init__(self)
		self.width=width
		self.height=height
		turtle.register_shape("rectangle", ((height,0),(height,width),(0,width),(0,0)))	
		turtle.shape("rectangle")
		self.setheading(90)

class Square(Rectangle):
	def __init__(self, size):
		Turtle.__init__(self)
		Rectangle.__init__(self,size,size)
		self.shape("square")
		self.shapesize(size)
		self.color(red,green,blue)
	def random_color(self):
		
		print(red,green,blue)
class Hexagon(Turtle):
	def __init__(self, side_len):
		Turtle.__init__(self)
		self.begin_poly()
		for i in range(6):
			self.pu()
			self.fd(side_len)
			self.right(60)
			self.pd()
		self.end_poly()

		setheading(90)
		hex = self.get_poly()
		register_shape("hexagon",hex)
		self.shape("hexagon")
lol=Hexagon(60)










#square1=Square(7)
#square1.random_color()