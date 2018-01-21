import turtle
import time
import random
from ball import *


#turtle.tracer(0)
turtle.hideturtle()
colormode(255)

RUNNING=True
SLEEP=0.0077
SCREEN_WIDTH=turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT=turtle.getcanvas().winfo_height()/2



NUMBER_OF_BALLS=5
MINIMUM_BALL_RADIUS=10
MAXIMUM_BALL_RADIUS=100
MINIMUM_BALL_DX=-5
MAXIMUM_BALL_DX=5
MINIMUM_BALL_DY=-5
MAXIMUM_BALL_DY=5

BALLS=[]


for i in range(NUMBER_OF_BALLS):
	x=random.randint(int(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS),int(SCREEN_WIDTH-MAXIMUM_BALL_RADIUS))
	y=random.randint(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS)
	dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
	if dx==0:
		dx+=1
	dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
	if dy==0:
		dy+=1
	r=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
	color=(random.randint(0,255), random.randint(0,255), random.randint(0,255))


	ball = Ball(x,y,dx,dy,r,color)
	BALLS.append(ball)

def move_all_balls():
	for i in BALLS:
		self.move(SCREEN_WIDTH,SCREEN_HEIGHT)

def collide(ball_a,ball_b):
	if ball_a==ball_b:
		return False
	if (ball_a.r+ball_b.r)>=math.sqrt(math.pow(ball_a.x-ball_b_x,2)+math.pow(ball_a.y-ball_b.y,2)):
		return True
	else:
		return False

def check_all_balls_collision():
	for ball_a in BALLS:
		for ball_b in BALLS:
			if collide(ball_a,ball_b)==True:
				radius_a=ball_a.r
				radius_b=ball_b.r
				if radius_a<radius_b:
					x=random.randint(int(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS),int(SCREEN_WIDTH-MAXIMUM_BALL_RADIUS))
					y=random.randint(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS)
					dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
					if dx==0:
						dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
					dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
					if dy==0:
						dx=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
					r=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
					color=(random.random(), random.random(), random.random())
					ball_a=Ball(x,y,dx,dy,r,color)
					ball_b.r+=1
				if radius_a>radius_b:
					x=random.randint(int(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS),int(SCREEN_WIDTH-MAXIMUM_BALL_RADIUS))
					y=random.randint(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS)
					dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
					if dx==0:
						dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
					dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
					if dy==0:
						dx=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
					r=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
					color=(random.random(), random.random(), random.random())
					ball_b=Ball(x,y,dx,dy,r,color)
					ball_a.r+=1


"""def check_my_ball_collision():
	for i in BALLS:"""