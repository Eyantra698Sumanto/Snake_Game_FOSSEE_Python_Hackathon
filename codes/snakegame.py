# importing libraries
#https://www.geeksforgeeks.org/snake-game-in-python-using-pygame-module/
import pygame
import time
import random
import sys
snake_speed = 1 #deciding snake speed

# Initialising Window size
xaxis = 500
yaxis = 500

# defining colors
bgcolor = pygame.Color(random.randrange(1,255), random.randrange(1,255), random.randrange(1,255))
scorecolor = pygame.Color(255, 255, 255)
finalscorecolor = pygame.Color(255, 0, 0)
snakecolor = pygame.Color(random.randrange(1,255), random.randrange(1,255), random.randrange(1,255))
linecolor = pygame.Color(random.randrange(1,255), random.randrange(1,255), random.randrange(1,255))

# Initialising pygame
pygame.init()

# Initialise game window
pygame.display.set_caption('Snake Game by Sumanto')
gamewin = pygame.display.set_mode((xaxis, yaxis))

# FPS (frames per second) controller
fps = pygame.time.Clock()

# defining snake default position
snake_position = [100, 50]

# defining first 4 blocks of snake body
snake_body = [[100, 50],
			[90, 50],
			[80, 50],
			[70, 50]
			]
# fruit position
fruitpos = [random.randrange(1, (xaxis//10)) * 10,
				random.randrange(1, (yaxis//10)) * 10]

not_eaten= True

# setting default snake direction towards
# right
direction = 'RIGHT'
change_to = direction

# initial score
score = 0

# displaying Score function
def show_score(choice, color, font, size):

	# creating font object score_font
	score_font = pygame.font.SysFont(font, size)
	
	# create the display surface object
	# score_surface
	score_surface = score_font.render('Score : ' + str(score), True, color)
	
	# create a rectangular object for the text
	# surface object
	score_rect = score_surface.get_rect()
	
	# displaying text
	gamewin.blit(score_surface, score_rect)

# game over function
def game_over():

	# creating font object my_font
	my_font = pygame.font.SysFont('times new roman', 40)
	
	# creating a text surface on which text
	# will be drawn
	game_over_surface = my_font.render(
		'Game Over. Score: ' + str(score), True, finalscorecolor)
	
	# create a rectangular object for the text
	# surface object
	game_over_rect = game_over_surface.get_rect()
	
	# setting position of the text
	game_over_rect.midtop = (xaxis/2, yaxis/4)
	
	# blit will draw the text on screen
	gamewin.blit(game_over_surface, game_over_rect)
	pygame.display.flip()
	
	# after 2 seconds we will quit the program
	time.sleep(2)
	
	# deactivating pygame library
	pygame.quit()
	
	# quit the program
	quit()

bigfruit = random.randrange(1, 10) 
a=[]
b=[]
c=[]
d=[]
for i in range(random.randrange(4,10)):
	a.append(random.randrange(1,50)*10)
	b.append(random.randrange(1,50)*10)
	c.append(random.randrange(1,50)*10)
	d.append(random.randrange(1,50)*10)
e=random.randrange(1,20)

# Main Function
while True:
	
	fruitcolor = pygame.Color(random.randrange(1,255), random.randrange(1,255), random.randrange(1,255))
	# handling key events
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				change_to = 'UP'
			if event.key == pygame.K_DOWN:
				change_to = 'DOWN'
			if event.key == pygame.K_LEFT:
				change_to = 'LEFT'
			if event.key == pygame.K_RIGHT:
				change_to = 'RIGHT'
		if event.type == pygame.QUIT:
			sys.exit()

	# If two keys pressed simultaneously
	# we don't want snake to move into two
	# directions simultaneously
	if change_to == 'UP' :
		direction = 'UP'
	if change_to == 'DOWN' :
		direction = 'DOWN'
	if change_to == 'LEFT' :
		direction = 'LEFT'
	if change_to == 'RIGHT' :
		direction = 'RIGHT'

	# Moving the snake
	if direction == 'UP':
		snake_position[1] -= 10
	if direction == 'DOWN':
		snake_position[1] += 10
	if direction == 'LEFT':
		snake_position[0] -= 10
	if direction == 'RIGHT':
		snake_position[0] += 10

	# Snake body growing mechanism
	# if fruits and snakes collide then scores
	# will be incremented by 10
	#For big fruit the snake body will increase by 100
	
	snake_body.insert(0, list(snake_position))
	if snake_position[0] == fruitpos[0] and snake_position[1] == fruitpos[1]:
		if (score/10)%10==bigfruit:
			score +=90
			snake_speed +=14
			bigfruit = random.randrange(1, 10) 
		score += 10
		not_eaten= False
		snake_speed +=1
		
	else:
		snake_body.pop()
		
	if not not_eaten:
		fruitpos = [random.randrange(1, (xaxis//10)) * 10,
						random.randrange(1, (yaxis//10)) * 10]
		
	not_eaten= True
	gamewin.fill(bgcolor)
	for i in range(e):
		for j in range(len(a)):
			pygame.draw.rect(gamewin, linecolor,
							pygame.Rect(i*10+a[j], b[j], 10, 10))
			if snake_position[0] == i*10+a[j] and snake_position[1] == b[j]:
				game_over()
			if fruitpos[0] == i*10+a[j] and fruitpos[1] == b[j]:
				continue

		for j in range(len(c)):
			pygame.draw.rect(gamewin, linecolor,
							pygame.Rect(c[j], i*10+d[j], 10, 10))
			if snake_position[0] == c[j] and snake_position[1] == i*10+d[j]:
				game_over()
			if fruitpos[0] == c[j] and fruitpos[1] == i*10+d[j]:
				continue

	
	for pos in snake_body:
		pygame.draw.rect(gamewin, snakecolor,
						pygame.Rect(pos[0], pos[1], 10, 10))

	if (score/10)%10==bigfruit:
		pygame.draw.rect(gamewin, fruitcolor, pygame.Rect(
			fruitpos[0]-15, fruitpos[1]-15, 30, 30))
	else:
		pygame.draw.rect(gamewin, fruitcolor, pygame.Rect(
			fruitpos[0], fruitpos[1], 10, 10))


	# Defining the Game Over conditions
	if snake_position[0] < 0 or snake_position[0] > xaxis-10:
		game_over()
	if snake_position[1] < 0 or snake_position[1] > yaxis-10:
		game_over()

	# Touching the snake body
	for block in snake_body[1:]:
		if snake_position[0] == block[0] and snake_position[1] == block[1]:
			game_over()

	# displaying score countinuously
	show_score(1, scorecolor, 'times new roman', 20)

	# Refresh game screen
	pygame.display.update()

	# Frame Per Second /Refresh Rate
	fps.tick(snake_speed)
