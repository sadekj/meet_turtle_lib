from turtle import *
import random

mouse = Turtle()
mouse.ht()
mouse.pu()
c=getcanvas()
CANVAS_WIDTH = c.winfo_width()
CANVAS_HEIGHT = c.winfo_height()

class Cell(Turtle):
	def __init__(self,r,x,y,dx,dy,color='black'):
		Turtle.__init__(self)
		self.penup()
		self.color("blue",color)
		self.goto(x,y)
		self.r = r
		self.dx = dx
		self.dy = dy
		self.shape("circle")
		self.ht()
	def get_radius(self):
		return self.r
	def get_dx(self):
		return self.dx
	def get_dy(self):
		return self.dy
	def set_radius(self,r):
		if(r<100):
			self.r = r
	def set_dx(self,dx):
		self.dx = dx
	def set_dy(self,dy):
		self.dy = dy
	def get_speed(self):
		return 150 / (self.r)



def create_cell(cell):
	getscreen().tracer(0)
	if ('color' in cell.keys()):
		c = Cell(cell['radius'],cell['x'],cell['y'],cell['dx'],cell['dy'],cell['color'])
	else:
		c = Cell(cell['radius'],cell['x'],cell['y'],cell['dx'],cell['dy'])
	return c

def move_cell(c):
	x = c.xcor()
	dx = c.get_dx()
	y = c.ycor()
	dy = c.get_dy()
	r = c.get_radius()
	c.goto(x+dx,y+dy-r)
	c.begin_fill()
	c.pd()
	c.circle(c.get_radius())
	c.pu()
	c.end_fill()
	x = c.xcor()
	dx = c.get_dx()
	y = c.ycor()
	dy = c.get_dy()
	r = c.get_radius()
	c.goto(x+dx,y+dy+r)

def move_cells(cells):
	ht()
	for c in cells:
		c.clear()
		move_cell(c)
	getscreen().update()

def create_screen(width, height):
	getscreen().screensize(width,height)

def get_screen_width():
	global CANVAS_WIDTH
	return CANVAS_WIDTH/2-10

def get_screen_height():
	global CANVAS_HEIGHT
	return CANVAS_HEIGHT/2-5

def get_x_mouse():
	global mouse
	return mouse.xcor()

def get_y_mouse():
	global mouse
	return mouse.ycor()

def movearound(event):
	global CANVAS_WIDTH
	global CANVAS_HEIGHT
	mouse.goto(event.x-c.winfo_width()/2,c.winfo_height()/2-event.y)
	if(CANVAS_WIDTH != c.winfo_width() or CANVAS_HEIGHT != c.winfo_height()):
		getscreen().screensize(c.winfo_width()/2,c.winfo_height()/2)
		CANVAS_WIDTH = c.winfo_width()
		CANVAS_HEIGHT = c.winfo_height()

def get_user_direction(cell):
	mouse_x = get_x_mouse()
	mouse_y = get_y_mouse()

	user_speed = cell.get_speed()
	distance = ((mouse_x - cell.xcor() )**2 + (mouse_y - cell.ycor())**2)**0.5

	if abs(mouse_x - cell.xcor()) < cell.get_radius():
		xdir = 0
	else:
		xdir = int(user_speed * (mouse_x - cell.xcor()) / distance)

	if abs(mouse_y - cell.ycor()) < cell.get_radius():
		ydir = 0
	else:
		ydir = int(user_speed * (mouse_y - cell.ycor()) / distance)

	return (xdir, ydir)

def get_random_x():
	return random.randint(-get_screen_width(), get_screen_width())
def get_random_y():
	return random.randint(-get_screen_height(), get_screen_height())

c.bind("<Motion>", movearound)
getscreen().listen()