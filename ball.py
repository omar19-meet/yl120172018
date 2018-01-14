from turtle import *

class Ball(Turtle):
	def __init__(self,x,y,dx,dy,r,color):
		Turtle.__init__(self)
		self.pu()
		self.goto(x,y)
		self.dx=dx
		self.dy=dy
		self.r=r
		self.color=self.color
		self.shape('circle')
		self.shapesize(r/10)

	def move(self,screen_width,screen_height):
		current_x=self.xcor()
		new_x=self.xcor()+self.dx
		current_y=self.ycor()
		new_y=self.ycor()+self.dy
		right_side_ball=new_x+self.r
		left_side_ball=new_x-self.r
		top_side_ball=new_y+self.r
		bottom_side_ball=new_y-self.r
		self.goto(new_x,new_y)

		if right_side_ball>=(screen_width/2):
			new_x=self.xcor()-self.dx
		if left_side_ball<=(screen_width/2):
			new_x=self.xcor()+self.dx
		if top_side_ball>=(screen_height/2):
			new_y=self.ycor()-self.dy
		elif bottom_side_ball<=(screen_height/2):
			new_y=self.ycor()+self.dy



