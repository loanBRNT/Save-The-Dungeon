import time, sys, pygame
from random import *
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((685,521))
blfB= pygame.image.load("items/boule de feuB.png")
blfD= pygame.image.load("items/boule de feuD.png")
blfH= pygame.image.load("items/boule de feuH.png")
blfG= pygame.image.load("items/boule de feuG.png")
map0 = pygame.image.load("map/map15.png")
pygame.key.set_repeat(400,30)
enigme=[]
clock = pygame.time.Clock()

def actualiser():
	pygame.display.update()




violetactive=False
bleuactive=False
grisactive=False
jauneactive=False
Fin=False
while not Fin:
	screen.blit(map0,(0,0))
	clock.tick(20)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
		if event.type == KEYDOWN:
			if event.key == K_LEFT:
				if not 3 in enigme:
					enigme.append(3)
					violetactive=True
			if event.key == K_UP:
				if not 2 in enigme:
					enigme.append(2)
					bleuactive=True
			if event.key == K_DOWN:
				if not 1 in enigme:
					enigme.append(1)
					grisactive=True
			if event.key == K_RIGHT:
				if not 4 in enigme:
					enigme.append(4)
					jauneactive=True
	if jauneactive==True and grisactive==True and violetactive==True and bleuactive==True :
		if enigme==[1,2,3,4]:
			pygame.quit()
			quit()
		else:
			violetactive=False
			bleuactive=False
			grisactive=False
			jauneactive=False
			enigme=[]
	actualiser()
pygame.quit()
quit()


