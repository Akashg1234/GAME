import pygame as pg
import random as ran
import os
# colors

white = (255,255,255)
red = (255,0,0)
blue = (65,79,205)
black = (0,0,0)

pg.mixer.init()
pg.init()

screen_width=600
screen_height=600
fps=100
clock=pg.time.Clock()
font=pg.font.SysFont('courier new',22,'bold')

# creating window
game_window = pg.display.set_mode((screen_width,screen_height))
pg.display.set_caption("snake game")
pg.display.update()
game_enter=False
#function
def welcome():
	exit_game=False
	
	while not exit_game :
		game_window.fill(black)
		text_screen("--PRESS ENTER TO PLAY--",white,screen_width/4,screen_height/2)
		text_screen("WELCOME TO THE SNAKE !..",white,screen_width/4,screen_height/2.5)
		
		for event in pg.event.get():
			pg.mixer.music.load("snake_background.mp3")
			pg.mixer.music.play()
			if event.type == pg.QUIT:
				exit_game=True

			if event.type == pg.KEYDOWN:
				if event.key==pg.K_RETURN:
					game_enter=True
					if game_enter==True:
						pg.mixer.music.stop()
						game_loop()
		pg.display.update()
		clock.tick(100)			
def text_screen(text,color,x,y):
	screen_text=font.render(text,True,color)
	game_window.blit(screen_text,[x,y])

def plot_snake(game_window,color,snk_list,snake_size):
	for x,y in snk_list:
		#print(snk_list)
		pg.draw.rect(game_window,color,[x,y,snake_size,snake_size])
#game lop

def game_loop():
	# game specific varible
	
	score=0
	exit_game=False
	game_over=False
	snake_x=10
	snake_y=20
	snake_size=15
	snk_list=[]
	snk_length=1
	velocity_x=0
	velocity_y=0
	food_x=ran.randint(5, screen_width)
	food_y=ran.randint(5,screen_height)

	if (not os.path.exists("high_score.txt")):
		with open("high_score.txt","w") as f:
			f.write(str(0))

	with open("high_score.txt","r") as f:
		high_score=f.read()
	while not exit_game:
		
		if game_over:
			game_window.fill(white)
			text_screen("Game over!... Your SCORE:" +str(score),red,screen_width/5,screen_height/2.5)
			with open("high_score.txt","w") as f:
				f.write(str(high_score))
			for event in pg.event.get():
				 
				if event.type == pg.QUIT:
					exit_game=True

				if event.type == pg.KEYDOWN:
					if event.key==pg.K_RETURN:
						game_loop()
		else:
			for event in pg.event.get():
				 
				if event.type == pg.QUIT:
					exit_game=True

				if event.type == pg.KEYDOWN:
					if event.key==pg.K_RIGHT:
						velocity_x =3
						velocity_y=0
						 
					if event.key==pg.K_LEFT:
						velocity_x -= 3
						velocity_y=0

					if event.key==pg.K_UP:
						velocity_y -= 3
						velocity_x=0

					if event.key==pg.K_DOWN:
						velocity_y = 3
						velocity_x=0

			snake_x+=velocity_x
			snake_y+=velocity_y

			if abs(snake_x-food_x)<15 and abs(snake_y-food_y)<15:
				score +=10
				#print("Score ",score*10 )
				pg.mixer.music.load("snake_sound.wav")
				pg.mixer.music.play()
				food_x=ran.randint(5, screen_width)
				food_y=ran.randint(5,screen_height)
				snk_length+=5
				if int(high_score)<score:
					high_score=score
			game_window.fill(white)

			text_screen("score :"+str(score)+"  high_score :"+str(high_score),blue,(screen_width/3-20),0)
			pg.draw.rect(game_window,black,[snake_x,snake_y,snake_size,snake_size])
			pg.draw.circle(game_window,red,[food_x,food_y],7)
			
			head=[]
			head.append(snake_x)
			head.append(snake_y)
			snk_list.append(head)

			if len(snk_list)>snk_length:
				del snk_list[0]

			if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
				game_over=True
				pg.mixer.music.load("ball_jump_sound.wav")
				pg.mixer.music.play()
			if head in snk_list[:-1]:
				game_over=True
				pg.mixer.music.load("ball_jump_sound.wav")
				pg.mixer.music.play()
			plot_snake(game_window,black,snk_list,snake_size)
		pg.display.update()
		clock.tick(fps)

	pg.quit()
	quit()

welcome()