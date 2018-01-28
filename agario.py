import turtle
import time
import random
import math
from ball import *



tracer(0)
turtle.hideturtle()
colormode(255)

RUNNING=True
SLEEP=0.0077
SCREEN_WIDTH=turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT=turtle.getcanvas().winfo_height()/2



NUMBER_OF_BALLS=5
MINIMUM_BALL_RADIUS=10
MAXIMUM_BALL_RADIUS=50
MINIMUM_BALL_DX=-2
MINIMUM_e_BALL_DX=-1
MAXIMUM_e_BALL_DX=1
MAXIMUM_BALL_DX=2
MINIMUM_BALL_DY=-2
MINIMUM_e_BALL_DY=-1
MAXIMUM_e_BALL_DY=1
MAXIMUM_BALL_DY=2

BALLS=[]
e_BALLS=[]

for i in range(4):
	x=random.randint(int(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS),int(SCREEN_WIDTH-MAXIMUM_BALL_RADIUS))
	y=random.randint(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS)
	dx=random.randint(MINIMUM_e_BALL_DX,MAXIMUM_e_BALL_DX)
	if dx==0:
		dx+=1
	dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
	if dy==0:
		dy+=1
	r=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
	color=(random.randint(0,255), random.randint(0,255), random.randint(0,255))


	ball = Ball(x,y,dx,dy,r,"green")
	e_BALLS.append(ball)


for i in range(4):
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
		i.move(SCREEN_WIDTH,SCREEN_HEIGHT)

def move_e_balls():
	for i in e_BALLS:
		i.move(SCREEN_WIDTH,SCREEN_HEIGHT)

def collide(ball_a,ball_b):
	if ball_a==ball_b:
		return False
	if (ball_a.r+ball_b.r)>=math.sqrt(math.pow(ball_a.xcor()-ball_b.xcor(),2)+math.pow(ball_a.ycor()-ball_b.ycor(),2)):
		return True
	else:
		return False

def check_all_balls_collision():
	for ball_a in BALLS:
		for ball_b in BALLS:
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
			if collide(ball_a,ball_b)==True:

				radius_a=ball_a.r
				radius_b=ball_b.r
				if radius_a<radius_b:
					ball_a.goto(x,y)
					ball_a.dx=dx
					ball_a.dy=dy
					ball_a.r=r
					ball_a.color=color
					ball_b.r+=1
					ball_b.shapesize(ball_b.r/10)
				elif radius_a>radius_b:
					ball_b.goto(x,y)
					ball_b.dx=dx
					ball_b.dy=dy
					ball_b.r=r
					ball_b.color=color
					ball_a.r+=1
					ball_a.shapesize(ball_a.r/10)


def check_my_e_balls_collision():
	for ball in e_BALLS:
		if collide(MY_BALL,ball)==True:
			print("lol")
			MY_BALL.r-=2
			MY_BALL.shapesize(MY_BALL.r/10)
			x=random.randint(int(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS),int(SCREEN_WIDTH-MAXIMUM_BALL_RADIUS))
			y=random.randint(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS)
			ball.goto(x,y)


def check_e_balls_collision():
	for ball_a in BALLS:
		for ball_b in e_BALLS:
			if collide(ball_a,ball_b)==True:
				print("Collided")
				ball_a.r-=2
				ball_a.shapesize(ball_a.r/10)
				x=random.randint(int(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS),int(SCREEN_WIDTH-MAXIMUM_BALL_RADIUS))
				y=random.randint(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS)
				ball_b.goto(x,y)




def check_my_ball_collision():
	for ball in BALLS:
		if collide(MY_BALL,ball)==True:

			radius_my_ball=MY_BALL.r
			radius_my_ball=ball.r
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
			if MY_BALL.r<ball.r:
				MY_BALL.goto(x,y)
				MY_BALL.dx=dx
				MY_BALL.dy=dy
				MY_BALL.r=r
				MY_BALL.color=color
				ball.r+=1
				ball.shapesize(ball.r/10)
			if MY_BALL.r>ball.r:
				
				ball.goto(x,y)
				ball.dx=dx
				ball.dy=dy
				ball.r=r
				ball.color=color
				MY_BALL.r+=1
				MY_BALL.shapesize(MY_BALL.r/10)


def movearound(event):
	MY_BALL.goto(event.x-SCREEN_WIDTH,SCREEN_HEIGHT-event.y)
turtle.getcanvas().bind("<Motion>", movearound)
turtle.listen()




while True:
	move_e_balls()
	check_my_e_balls_collision()
	check_e_balls_collision()
	move_all_balls()
	check_all_balls_collision()
	check_my_ball_collision()
	getscreen().update()
	time.sleep(SLEEP)



