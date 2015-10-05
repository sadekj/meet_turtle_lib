import meet
user_cell = {'radius': 14, 'x':20, 'y':3, 'dx': 1, 'dy':1 ,'color':'red', 'shape':'square'}

cell1 = {'radius': 13, 'x':100, 'y':0, 'dx': 2, 'dy':1 ,'color':'black'}
cell2 = {'radius': 15, 'x':-100, 'y':0, 'dx': -2.5, 'dy':-2.5, 'color':'black'}

food1 = {'radius': 5, 'x':2, 'y':5, 'dx': 0, 'dy':0,'color':'yellow'}
food2 = {'radius': 5, 'x':15, 'y':12, 'dx': 0, 'dy':0,'color':'green'}
food3 = {'radius': 5, 'x':15, 'y':12, 'dx': 0, 'dy':0,'color':'blue'}
food4 = {'radius': 5, 'x':15, 'y':12, 'dx': 0, 'dy':0,'color':'black'}
food5 = {'radius': 5, 'x':15, 'y':12, 'dx': 0, 'dy':0,'color':'green'}
food6 = {'radius': 5, 'x':15, 'y':12, 'dx': 0, 'dy':0,'color':'green'}


cells = []
foods = []

running = True
food_eaten = False

user_cell = meet.create_cell(user_cell)
cells.append(user_cell)

cell = meet.create_cell(cell1)
cells.append(cell)
cell = meet.create_cell(cell2)
cells.append(cell)

food = meet.create_cell(food1)
cells.append(food)
food = meet.create_cell(food2)
cells.append(food)
food = meet.create_cell(food3)
cells.append(food)
food = meet.create_cell(food4)
cells.append(food)
food = meet.create_cell(food5)
cells.append(food)
food = meet.create_cell(food6)
cells.append(food)

food = meet.create_cell(food6)
cells.append(food)
food = meet.create_cell(food6)
cells.append(food)
food = meet.create_cell(food6)
cells.append(food)
food = meet.create_cell(food6)
cells.append(food)
food = meet.create_cell(food6)
cells.append(food)
food = meet.create_cell(food6)
cells.append(food)
food = meet.create_cell(food6)
cells.append(food)
food = meet.create_cell(food6)
cells.append(food)
food = meet.create_cell(food6)
cells.append(food)



###########
def check_walls(cells):
	for cell in cells:
		#print (str(cell.xcor()) + ", " +str(cell.ycor()) + " " + str(meet.get_screen_width()) + " " + str(meet.get_screen_height()))
		# if(cell != user_cell):
		if(cell.xcor()+cell.get_radius() > meet.get_screen_width() or cell.xcor()-cell.get_radius() < -meet.get_screen_width()):
			cell.set_dx(-cell.get_dx())

		if(cell.ycor()+cell.get_radius() > meet.get_screen_height() or cell.ycor()-cell.get_radius() < -meet.get_screen_height()):
			cell.set_dy(-cell.get_dy())

def collide(cell1,cell2):
	delta_x = cell2.xcor() - cell1.xcor()
	delta_y = cell2.ycor() - cell1.ycor()
	double_delta_x = delta_x**2
	double_delta_y = delta_y**2
	distance = (double_delta_x+double_delta_y)**0.5
	two_radiuses = cell1.get_radius() + cell2.get_radius()
	if (distance <= two_radiuses):
		return True
	else:
		return False

def check_collision(cells):
	global running
	for c1 in cells:
		for c2 in cells:
			if (c1 != c2 and collide(c1, c2)):
				print("collided")
				if(c1.get_radius()>c2.get_radius()):
					c2.goto(meet.get_random_x(),meet.get_random_y())
					c1.set_radius(c1.get_radius()+c2.get_radius()*0.1)
					if(c2 == user_cell):
						running = False
				elif(c1.get_radius()<c2.get_radius()):
					c1.goto(meet.get_random_x(),meet.get_random_y())
					c2.set_radius(c2.get_radius()+c1.get_radius()*0.1)
					if(c1 == user_cell):
						running = False

def move_user_cell(user_cell):
	xdir,ydir = meet.get_user_direction(user_cell)
	user_cell.set_dy(ydir)
	user_cell.set_dx(xdir)
	#user_cell.goto(user_cell.xcor()+xdir,user_cell.ycor()+ydir)

############



while(running):
	check_walls(cells)
	move_user_cell(user_cell)
	meet.move_cells(cells)
	if(food_eaten):
		meet.move_cells(foods)
	check_collision(cells)
	#print ("------------------------")