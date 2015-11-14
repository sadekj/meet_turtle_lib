from turtle import *
import random

mouse = Turtle() # this line is making a turlte object that later will follow the mouse
mouse.hideturtle() # this line to hide the mouse turtle
mouse.penup() # this line tells mouse turtle to pen up so it will not draw line when the mouse move
canvas=getcanvas() # the canvas is the area that the turtle is moving (the white background)
CANVAS_WIDTH = canvas.winfo_width() # here we get canvas(screen) width
CANVAS_HEIGHT = canvas.winfo_height() # here we get the canvas(screen) height

## This is called a class we gave it the name Cell, this class inherit a turtle
## Class properties are self.dx, self.dy, self.radiusadius
class Cell(Turtle):
	# here is inside the class and the first thing we notice is __init__ function
	# this function is called everytime we create a new cell object
	def __init__(self,radius,x,y,dx,dy,color='black'):
		Turtle.__init__(self)
		self.penup()
		self.color("blue",color)
		self.goto(x,y)
		self.radius = radius # the radius of the circle
		self.dx = dx # the change in x (speed in x)
		self.dy = dy # the change in y (speed in y)
		self.shape("circle")
		self.hideturtle()
	# here ends the __init__ function
	# here starts the rest of the functions, these functions are only used for cell variables
	# get the radius of the cell
	def get_radius(self):
		return self.radius

	#get the change in x (speed in x)
	def get_dx(self):
		return self.dx
	
	#get the change in y (speed in y)
	def get_dy(self):
		return self.dy

	# this function cahnges the radius of the circle
	def set_radius(self,new_radius):
		self.radius = new_radius
	# this function changes the dx (speed in x)
	def set_dx(self,new_dx):
		self.dx = new_dx
	
	# this function changes the dy (speed in y)
	def set_dy(self,new_dy):
		self.dy = new_dy
	# this function calculates the speed factor of the cell that depends on the cell's size
	def get_speed(self):
		return 150 / (self.radius)
## here ends the class Cell
## and starts the defintion of normal functions

# this function takes a dictionary filled in with a cell's information
# and makes an object using the class we defined above,
# and returns a cell object with the dictionaries information
def create_cell(cell):
	getscreen().tracer(0)
	if ('color' in cell.keys()):
		c = Cell(cell['radius'],cell['x'],cell['y'],cell['dx'],cell['dy'],cell['color'])
	else:
		c = Cell(cell['radius'],cell['x'],cell['y'],cell['dx'],cell['dy'])
	return c

# this function takes a cell object and draws it on the screen
def move_cell(cell):
	x = cell.xcor()
	dx = cell.get_dx()
	y = cell.ycor()
	dy = cell.get_dy()
	r = cell.get_radius()
	cell.goto(x+dx,y+dy-r)
	cell.begin_fill()
	cell.pd()
	cell.circle(cell.get_radius())
	cell.penup()
	cell.end_fill()
	x = cell.xcor()
	dx = cell.get_dx()
	y = cell.ycor()
	dy = cell.get_dy()
	r = cell.get_radius()
	cell.goto(x+dx,y+dy+r)

# this function takes a list of rectangles and draws them on the screen
def move_cells(cells):
	hideturtle()
	for cell in cells:
		cell.clear()
		move_cell(cell)
	getscreen().update()


# This function returns the width of the screen
def get_screen_width():
	global CANVAS_WIDTH
	return int(CANVAS_WIDTH/2-10)

# This function returns the height of the screen
def get_screen_height():
	global CANVAS_HEIGHT
	return int(CANVAS_HEIGHT/2-5)

# This function returns the x location of the mouse on the screen
def get_x_mouse():
	global mouse
	return mouse.xcor()

# This function returns the y location of the mouse on the screen
def get_y_mouse():
	global mouse
	return mouse.ycor()

# this functio is called evertime the mouse moves on the screen
# and makes the mouse turtle goes and follows the mouse
# and updates the screen size if the screen size changed
def movearound(event):
	global CANVAS_WIDTH
	global CANVAS_HEIGHT
	mouse.goto(event.x-canvas.winfo_width()/2,canvas.winfo_height()/2-event.y)
	if(CANVAS_WIDTH != canvas.winfo_width() or CANVAS_HEIGHT != canvas.winfo_height()):
		getscreen().screensize(canvas.winfo_width()/2,canvas.winfo_height()/2)
		CANVAS_WIDTH = canvas.winfo_width()
		CANVAS_HEIGHT = canvas.winfo_height()

# This function calculates the new x speed(dx) and y speed(dy) depending on cell size and mouse location
# We use this function to make the user cell follows the mouse
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

# returns a random x on the screen
def get_random_x():
	return random.randint(-get_screen_width(), get_screen_width())

# return a random y on the screen
def get_random_y():
	return random.randint(-get_screen_height(), get_screen_height())

######################################################################
# Custom code goes here


######################################################################

canvas.bind("<Motion>", movearound) # this line tells turtle to call the function movearound (we defined above) everytime the mouse moves
getscreen().listen() # this line tells the screen in turtle to listen to the keyboard and the mouse, because we are using them