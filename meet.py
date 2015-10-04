from turtle import *
import random

mouse = Turtle()
mouse.ht()
mouse.pu()

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
	def ycor(self):
		return super(Cell, self).ycor() + self.r
	def org_ycor(self):
		return super(Cell, self).ycor()



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
	y = c.org_ycor()
	dy = c.get_dy()
	r = c.get_radius()
	c.goto(x+dx,y+dy)
	c.begin_fill()
	c.pd()
	c.circle(c.get_radius())
	c.pu()
	c.end_fill()

def move_cells(cells):
	ht()
	for c in cells:
		c.clear()
		move_cell(c)
	getscreen().update()

def create_screen(width, height):
	getscreen().screensize(width,height)

def get_screen_width():
	return getscreen().screensize()[0]

def get_screen_height():
	return getscreen().screensize()[1]

def get_x_mouse():
	global mouse
	return mouse.xcor()

def get_y_mouse():
	global mouse
	return mouse.ycor()

def movearound(event):
	mouse.goto(event.x-336,387-event.y)

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

c=getcanvas()
c.bind("<Motion>", movearound)
getscreen().listen()