import time, sys, pygame
from random import *
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((685,521))
bg = pygame.image.load("map/map03.png")
stand =pygame.image.load("perso/perso 1/1.D.png")
walkleft = [pygame.image.load("perso/perso 1/1.G1.png"), pygame.image.load("perso/perso 1/1.G2.png"), pygame.image.load("perso/perso 1/1.G3.png"), pygame.image.load("perso/perso 1/1.G4.png")]
walkRight = [pygame.image.load("perso/perso 1/1.D1.png"), pygame.image.load("perso/perso 1/1.D2.png"), pygame.image.load("perso/perso 1/1.D3.png"), pygame.image.load("perso/perso 1/1.D4.png")]
clock = pygame.time.Clock()




def actualiser():
	pygame.display.update()


run = True
walkCount=0
x=200
y=300
while run:
	screen.blit(bg,(0,0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	clock.tick(20)

	if event.type == KEYDOWN:
		if event.key == K_RIGHT :
			screen.blit(walkRight[walkCount//3],(x,y))
			x=x+5
			walkCount=walkCount+1
		if event.key == K_LEFT :
			screen.blit(walkleft[walkCount//3],(x,y))
			x=x-5
			walkCount=walkCount+1
	else :
		screen.blit(stand,(x,y))
	if walkCount >=10 :
		walkCount =0

	actualiser()
pygame.quit()