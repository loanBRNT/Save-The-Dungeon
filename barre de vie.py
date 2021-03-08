import time, sys, pygame
from random import *
from pygame.locals import *
from dialogue import*
pygame.init()


screen_size = (685,521)
screen = pygame.display.set_mode (screen_size)
Centrale = pygame.image.load("map/Centre.png")
MECH1G = pygame.image.load("perso/MECHANT1G.png")
P1D = pygame.image.load("perso/PLAYER1_STANDupD.png")
Fin = False
x1=500
y1=100
lonap=150
while not Fin :
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_LEFT:
				x1=x1-15
			elif event.key == K_RIGHT:
				x1=x1+15
			elif event.key == K_UP :
				y1=y1-15
			elif event.key == K_DOWN :
				y1=y1+15
				lonap=lonap-25
			elif event.key == K_p:
				Fin=True
			elif event.key == K_a:
				lonap=lonap-50
				print("a")
	screen.blit(Centrale,(0,0))
	screen.blit(MECH1G,(200,200))
	screen.blit(P1D,(x1,y1))
	pygame.draw.rect(screen,(255,0,0),(10,70,150,20))
	pygame.draw.rect(screen,(0,128,0),(10,70,lonap,20))
	pygame.display.flip()
pygame.quit()
quit()