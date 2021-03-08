import time, sys, pygame
from random import *
from pygame.locals import *
from variable import*
pygame.init()
#                                                                  UTILITAIRE                                                                      #
####################################################################################################################################################

def END(): 						 #Fermer la fenetre
	pygame.quit()
	quit()

def actualiser(): 				#actualiser la fenetre
	pygame.display.flip()

def transition(t, ttext):		#SOUS-affichage des transitations
	if t==1:
		t = t1
	elif t==2:
		t = t2
	else :
		t = t3
	screen.blit(t, (0,0))
	screen.blit(ttext, (0,0))
	actualiser()
	pygame.time.delay(5000)

def attentespace():			#attente d'un appuie sur la touche espace
	pygame.event.clear()
	FIN = False
	while not FIN:
		event = pygame.event.wait()
		if event.type == QUIT:
			END()
		if event.type == KEYDOWN :
			if event.key == K_SPACE :
				FIN = True

def attenteclic():			#attente d'un clic
	pygame.event.clear()
	FIN = False
	while not FIN:
		event = pygame.event.wait()
		if event.type == QUIT:
			END()
		if event.type == MOUSEBUTTONDOWN :
			FIN = True

def fermercarte():			#attente d'un appui sur la touche Q
	pygame.event.clear()
	FIN = False
	while not FIN:
		event = pygame.event.wait()
		if event.type == QUIT:
			FIN=True
		if event.type == KEYDOWN :
			if event.key == K_a :
				FIN = True

def minimapacl(posx,poxy): 			#Adaptation de la mini map
	screen.blit(minimap,(100,100))
	if not 5 in visiter:
		screen.blit(brouille,(257,238))			#Rendre sombre les salles non visiter
	if not 6 in visiter:
		screen.blit(brouille,(255,328))
	if not 8 in visiter:
		screen.blit(brouille,(306,238))
	if not 9 in visiter:
		screen.blit(brouille,(358,238))
	if not 10 in visiter:
		screen.blit(brouille,(408,238))
	if not 11 in visiter:
		screen.blit(brouille,(408,194))
	if not 12 in visiter:
		screen.blit(brouille,(357,283))
	if not 13 in visiter:
		screen.blit(brouille,(357,329))
	if not 14 in visiter:
		screen.blit(brouille,(307,329))
	if not 15 in visiter:
		screen.blit(brouille,(407,329))
	if not 16 in visiter:
		screen.blit(brouille,(407,283))
	if not 17 in visiter:
		screen.blit(brouille,(457,329))
	if not 18 in visiter:
		screen.blit(brouille,(504,329))
	if not 19 in visiter:
		screen.blit(brouille,(457,283))
	if not 20 in visiter:
		screen.blit(brouille,(457,237))
	if not 21 in visiter:
		screen.blit(brouille,(208,237))
	if not 22 in visiter:
		screen.blit(brouille,(208,191))
	if not 23 in visiter:
		screen.blit(brouille,(208,144))
	if not 24 in visiter:
		screen.blit(brouille,(163,144))
	screen.blit(point,(posx,poxy))

def VIE(vie):				#ffichage du nombre de vie
	xvie = 0
	for loop in range (vie):
		screen.blit(coeur, (xvie,5))
		xvie = xvie + 30

def tuto():					#ffichage des transitions et du tuto
	sonTrans.play()
	t = randint(1,3)
	transition(t,t1txt)
	screen.blit(ttuto, (0,0))
	actualiser()
	attenteclic()
	t = randint(1,3)
	transition(t,t2txt)


def lettreroi():			#la lettre du roi
	screen.blit(t1, (0,0))
	screen.blit(inventaire, (0,0))
	VIE(vie)
	screen.blit(parchemin, (75,5))
	actualiser()
	attenteclic()

def outil(valide,objet): 		#Gestion de l'objet équipe
	if valide == True :
		screen.blit(objet,(600,460))

def pts_scenario(scenario):			#les points scenario regulier
	sonTrans.stop()
	MSC1.play()
	screen.blit(scenario,(0,0))
	actualiser()

def sousGAMEPLAY(Orientation,CHmap,x1,y1,vie):			#affichage des composant primmaires	lors des animations
	screen.blit(CHmap, (0,0))
	screen.blit(Orientation,(x1,y1))

def Interface(valide,objet,vie,Sco):		#Affichage de l'interface general
	screen.blit(inventaire, (0,0))
	VIE(vie)
	outil(valide,objet)
	score(Sco)

def mort(Sco):								#Respawn apres la mort
	screen.blit(fen,(0,0))
	screen.blit(ecran_mort,(0,0))
	sonmort.play()
	actualiser()
	attenteclic()
	MSC1.stop()
	sonAilefeu.stop()
	MSC1.play()
	IntroGAMEPLAY(Orientation,mp_prison,30,400,5)
	salle3(Orientation,entree,valide,objet,vie,Sco)

def score(Sco):					#gestion du score
	if Sco==0 :
		screen.blit(s0,(0,0))
	if Sco==1 :
		screen.blit(s1, (0,0))
	if Sco==2 :
		screen.blit(s2,(0,0))
	if Sco==3 :
		screen.blit(s3, (0,0))
	if Sco==4 :
		screen.blit(s4,(0,0))
	if Sco==5 :
		screen.blit(s5, (0,0))

def choix(mapo,chaction):			#Affichage de l'interface de choix
	chx=0
	xh=100
	yh=300
	FIN = False
	while not FIN :
		for event in pygame.event.get():
			if event.type == pygame.QUIT :
				END()
		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT]:			#Choisir entre une des deux options
			xh=100
			chx=0
		elif keys[pygame.K_RIGHT]:
			xh=400
			chx=1
		elif keys[pygame.K_SPACE]:		#valider le choix
			FIN=True
		screen.blit(mapo,(0,0))
		screen.blit(fen,(0,0))
		screen.blit(chaction,(0,0))
		screen.blit(curseur,(xh,yh))
		actualiser()
	return chx

def dialogue(chaine,locuteur):												#gestion des dialogues
	font = pygame.font.SysFont("arial",24,bold=False,italic=False)
	fontl = pygame.font.SysFont("arial",15,bold=False,italic=True)			#police
	texte = font.render(chaine,1,(255,255,255))
	Ltxt = fontl.render(locuteur,1,(255,255,255))							# On met dans une variable la chaine de caractere
	screen.blit(BD,(0,0))
	screen.blit(texte,(100,460))											#on blite en bas de la fenetre
	screen.blit(Ltxt,(15,425))
	actualiser()

#                                                                  PROJECTILES                                                                     #
####################################################################################################################################################

class projectile(object):
	def __init__(self,x1,y1,facing):			#attribut des boule de feu
		self.x = x1
		self.y = y1
		self.facing = facing
		self.vel = 8 * facing

	def draw(self,screen,orientation):			#Changer l'orientation et direction des boules de feu
		if orientation == -1:
			screen.blit(blfG,(self.x +self.vel,self.y+self.vel))
		elif orientation == 1:
			screen.blit(blfD,(self.x +self.vel,self.y+self.vel))
		elif orientation == 2:
			screen.blit(blfB,(self.x +self.vel,self.y+self.vel))
		elif orientation == -2:
			screen.blit(blfH,(self.x +self.vel,self.y+self.vel))

class projectileS(object):
	def __init__(self,x1,y1,facing):
		self.x = x1
		self.y = y1
		self.facing = facing
		self.vel = 8 * facing

	def draw(self,screen,orientation):
		if orientation == -1:
			screen.blit(blfG,(self.x +self.vel,self.y+self.vel))
		elif orientation == 1:
			screen.blit(blfD,(self.x +self.vel,self.y+self.vel))
		elif orientation == 2:
			screen.blit(blfB,(self.x +self.vel,self.y+self.vel))
		elif orientation == -2:
			screen.blit(blfH,(self.x +self.vel,self.y+self.vel))

class atack(object):					#attaque de notre heros
	def __init__(self,x1,y1,facing):
		self.x = x1
		self.y = y1
		self.facing = facing
		self.vel = 8 * facing

	def draw(self,screen,orientation):
		if orientation == -1:
			screen.blit(blfG,(self.x +self.vel,self.y+self.vel))
		elif orientation == 1:
			screen.blit(blfD,(self.x +self.vel,self.y+self.vel))
####################################################################################################################################################

#                                                                  DIALOGUE                                                                        #
####################################################################################################################################################


def choix_hache(x1,y1,vie,Sco):				#Dialogue pour le choix de la Hache
	x1=240
	y1=-50
	while not y1>=60:
		y1=y1+15
		sousGAMEPLAY(PDD,map06,x1,y1,vie)
		screen.blit(prisonporte,(515,280))
		screen.blit(gentil2G,(500,400))
		screen.blit(hache, (400,100))
		actualiser()
	chaine = "Ah tu est encore vivant jeune chevalier !"
	locuteur = "Benoit"
	dialogue(chaine,locuteur)
	actualiser()
	attenteclic()
	sousGAMEPLAY(PDD,map06,x1,y1,vie)
	screen.blit(prisonporte,(515,280))
	screen.blit(gentil2G,(500,400))
	screen.blit(hache, (400,100))
	chaine = "Peut-tu me passer cette hache ?"
	locuteur = "Benoit"
	dialogue(chaine,locuteur)
	actualiser()
	attenteclic()
	sousGAMEPLAY(PDD,map06,x1,y1,vie)
	screen.blit(prisonporte,(515,280))
	screen.blit(gentil2G,(500,400))
	screen.blit(hache, (400,100))
	chaine = "J'en ai besoin pour sortir de cette prison."
	locuteur = "Benoit"
	dialogue(chaine,locuteur)
	actualiser()
	attenteclic()
	sousGAMEPLAY(PDD,map06,x1,y1,vie)
	screen.blit(prisonporte,(515,280))
	screen.blit(gentil2G,(500,400))
	screen.blit(hache, (400,100))
	chaine = "Par ou tu vas sortir ? Il n'y a qu'une porte en fer"
	locuteur = "Vous"
	dialogue(chaine,locuteur)
	actualiser()
	attenteclic()
	sousGAMEPLAY(PDD,map06,x1,y1,vie)
	screen.blit(prisonporte,(515,280))
	screen.blit(gentil2G,(500,400))
	screen.blit(hache, (400,100))
	chaine = "Ne t'inquiète pas, il y a un courant d'air derriere l'armoire."
	locuteur = "Benoit"
	dialogue(chaine,locuteur)
	actualiser()
	attenteclic()
	sousGAMEPLAY(PDD,map06,x1,y1,vie)
	screen.blit(prisonporte,(515,280))
	screen.blit(gentil2G,(500,400))
	screen.blit(hache, (400,100))
	chaine = "Mais cette hache pourrait me servir pour casser la palissade !"
	locuteur = "Vous"
	dialogue(chaine,locuteur)
	actualiser()
	attenteclic()
	valeurCHX = choix(map06,choixhache)
	screen.blit(prisonporte,(515,280))
	sousGAMEPLAY(PDD,map06,x1,y1,vie)
	screen.blit(gentil2G,(500,400))
	screen.blit(hache, (400,100))
	chaine = "Aller s'il te plaît !"
	locuteur = "Benoit"
	dialogue(chaine,locuteur)
	actualiser()
	attenteclic()
	sousGAMEPLAY(PDD,map06,x1,y1,vie)
	screen.blit(prisonporte,(515,280))
	screen.blit(gentil2G,(500,400))
	screen.blit(hache, (400,100))
	if valeurCHX == 0:
		chaine = "Non désolé je préfère la garder."
		locuteur = "Vous"
		dialogue(chaine,locuteur)
		actualiser()
		attenteclic()
		sousGAMEPLAY(PDD,map06,x1,y1,vie)
		screen.blit(prisonporte,(515,280))
		screen.blit(gentil2G,(500,400))
		screen.blit(hache, (400,100))
		chaine = "Tu ne pas me laisser croupir ici quand même ?!"
		locuteur = "Benoit"
		dialogue(chaine,locuteur)
		actualiser()
		attenteclic()
		sousGAMEPLAY(PDD,map06,x1,y1,vie)
		screen.blit(prisonporte,(515,280))
		screen.blit(gentil2G,(500,400))
		screen.blit(hache, (400,100))
		chaine = "Non vraiment desole, je dois enquêter sur les bruits"
		locuteur = "Vous"
		dialogue(chaine,locuteur)
		actualiser()
		attenteclic()
		sousGAMEPLAY(PDD,map06,x1,y1,vie)
		screen.blit(prisonporte,(515,280))
		screen.blit(gentil2G,(500,400))
		screen.blit(hache, (400,100))
		chaine = "Alors pars, ne reste pas !"
		locuteur = "Benoit"
		dialogue(chaine,locuteur)
		actualiser()
		attenteclic()
		sousGAMEPLAY(PDD,map06,x1,y1,vie)
		screen.blit(prisonporte,(515,280))
		screen.blit(gentil2G,(500,400))
		screen.blit(hache, (400,100))
		xh=400
		yh=100
		xg2=300
		yg2=500
	if valeurCHX == 1:
		chaine = "Finalement tu as raison, tiens prend la"
		locuteur = "Vous"
		dialogue(chaine,locuteur)
		actualiser()
		attenteclic()
		sousGAMEPLAY(PDD,map06,x1,y1,vie)
		screen.blit(prisonporte,(515,280))
		screen.blit(gentil2G,(500,400))
		screen.blit(hache, (400,100))
		chaine = "Merci beaucoup ! Tu me sauve la vie !"
		locuteur = "Benoit"
		dialogue(chaine,locuteur)
		actualiser()
		attenteclic()
		sousGAMEPLAY(PDD,map06,x1,y1,vie)
		screen.blit(prisonporte,(515,280))
		screen.blit(gentil2G,(500,400))
		screen.blit(hache, (400,100))
		xg2=500
		walkCount=0
		while not xg2==690:
			clock.tick(20)
			xg2=xg2+1
			screen.blit(map06,(0,0))
			screen.blit(prisonporte,(515,280))
			screen.blit(PDD,(x1,y1))
			screen.blit(gentil2D,(xg2,300))
			Interface(0,hache,vie,Sco)
			screen.blit(walkrightAB[walkCount//3], (xg2,300))
			walkCount=walkCount+1
			if walkCount>=10:
				walkCount=0
			actualiser()
		xh=900
		yh=900
		xg2=900
		yg2=900
		action.append("donnerH")
	return xh,yh,xg2,yg2

def sauvetage_g1 (x1,y1,vie,Sco):				#dialogue du sauvetage de Armant
	x1=350
	y1=520
	xg1=110
	yg1=180
	while not y1<=220:
		y1= y1-10
		sousGAMEPLAY(PDG,map05,x1,y1,vie)
		screen.blit(gentil1D,(xg1,yg1))
	chaine = "OH,c'est toi ! Merci d'etre venu me sauver"
	locuteur = "Armant"
	dialogue(chaine,locuteur)
	actualiser()
	attenteclic()
	sousGAMEPLAY(PDG,map05,x1,y1,vie)
	screen.blit(gentil1D,(xg1,yg1))
	chaine = "Qu'est-ce qui t'est arrivé ?"
	locuteur = "VOUS"
	dialogue(chaine,locuteur)
	actualiser()
	attenteclic()
	sousGAMEPLAY(PDG,map05,x1,y1,vie)
	screen.blit(gentil1D,(xg1,yg1))
	chaine = "On s'est fait attaquer par surprise, on a rien pu faire..."
	locuteur = "Armant"
	dialogue(chaine,locuteur)
	actualiser()
	attenteclic()
	sousGAMEPLAY(PDG,map05,x1,y1,vie)
	screen.blit(gentil1D,(xg1,yg1))
	chaine = "Même Luna et Kay ?!"
	locuteur = "VOUS"
	dialogue(chaine,locuteur)
	actualiser()
	attenteclic()
	sousGAMEPLAY(PDG,map05,x1,y1,vie)
	screen.blit(gentil1D,(xg1,yg1))
	chaine = "Oui GAMENON les a battus à plat de couture."
	locuteur = "Armant"
	dialogue(chaine,locuteur)
	actualiser()
	attenteclic()
	sousGAMEPLAY(PDG,map05,x1,y1,vie)
	screen.blit(gentil1D,(xg1,yg1))
	chaine = "Mais pourtant ce sont les plus forts de toute la guilde !"
	locuteur = "VOUS"
	dialogue(chaine,locuteur)
	actualiser()
	attenteclic()
	sousGAMEPLAY(PDG,map05,x1,y1,vie)
	screen.blit(gentil1D,(xg1,yg1))
	chaine = "Oui... Les autres sont aussi dans le donjon va les sauver ! Vite !"
	locuteur = "Armant"
	dialogue(chaine,locuteur)
	actualiser()
	attenteclic()
	valeurCHX = choix(map05,choixarmant)
	sousGAMEPLAY(PDG,map05,x1,y1,vie)
	screen.blit(gentil1D,(xg1,yg1))
	if valeurCHX == 0 :
		chaine = "Reste avec moi ! Il ne faut pas qu'on se sépare"
		locuteur = "VOUS"
		dialogue(chaine,locuteur)
		actualiser()
		attenteclic()
		sousGAMEPLAY(PDG,map05,x1,y1,vie)
		screen.blit(gentil1D,(xg1,yg1))
		chaine = " Euh... J'ai une importante competition de bilboquet sur gazon..."
		locuteur = "Armant"
		dialogue(chaine,locuteur)
		actualiser()
		attenteclic()
		sousGAMEPLAY(PDG,map05,x1,y1,vie)
		screen.blit(gentil1D,(xg1,yg1))
	if valeurCHX == 1 :
		chaine = "D'accord ! bon vent stagiaire! "
		locuteur = "VOUS"
		dialogue(chaine,locuteur)
		actualiser()
		attenteclic()
		sousGAMEPLAY(PDG,map05,x1,y1,vie)
		screen.blit(gentil1D,(xg1,yg1))
		chaine = " J'espère que tu reussira à les sauver... À bientot !"
		locuteur = "Armant"
		dialogue(chaine,locuteur)
		actualiser()
		attenteclic()
		sousGAMEPLAY(PDG,map05,x1,y1,vie)
		screen.blit(gentil1D,(xg1,yg1))
	walkCount=0
	while not xg1>=350:
		clock.tick(20)
		xg1=xg1+10
		yg1=yg1+10
		screen.blit(gentil1D,(xg1,yg1))
		screen.blit(map05, (0,0))
		screen.blit(PDD, (300,200))
		Interface(0,hache,vie,Sco)
		screen.blit(walkrightA[walkCount//3], (xg1,yg1))
		walkCount=walkCount+1
		if walkCount>=10:
			walkCount=0
		actualiser()
	while yg1<520 :
		yg1=yg1+15
		sousGAMEPLAY(PDG,map05,x1,y1,vie)
		screen.blit(gentil1D,(xg1,yg1))
		actualiser()

def fuite(x1,y1,vie,Sco):					#fuite du mechant 2
	x2=300
	y2=200
	sousGAMEPLAY(PDD,Centrale,100,220,vie)
	screen.blit(MECH2G,(x2,y2))
	chaine = "AH... tu m'as battu..."
	locuteur = "Joulen"
	dialogue(chaine,locuteur)
	actualiser()
	attenteclic()
	sousGAMEPLAY(PDD,Centrale,100,220,vie)
	screen.blit(MECH2G,(x2,y2))
	chaine = "Je n'en ai pas fini avec toi !"
	locuteur = "Joulen"
	dialogue(chaine,locuteur)
	actualiser()
	attenteclic()
	walkCount=0
	while not y2>=240:
		clock.tick(20)
		x2=x2+10
		y2=y2+10
		screen.blit(PDD,(100,220))
		screen.blit(Centrale, (0,0))
		screen.blit(walkrightMB[walkCount//3], (x2,y2))
		walkCount=walkCount+1
		if walkCount>=10:
			walkCount=0
		Interface(0,hache,vie,Sco)
		actualiser()
	while not x2>=685:
		clock.tick(20)
		x2=x2+10
		screen.blit(PDD,(100,220))
		screen.blit(Centrale, (0,0))
		screen.blit(walkrightMB[walkCount//3], (x2,y2))
		walkCount=walkCount+1
		if walkCount>=10:
			walkCount=0
		Interface(0,hache,vie,Sco)
		actualiser()
	sousGAMEPLAY(PDG,Centrale,100,220,vie)
	screen.blit(MECH2G,(x2,y2))
	chaine = "On se retrouvera ..."
	locuteur = "Joulen"
	dialogue(chaine,locuteur)
	actualiser()
	attenteclic()

def discussionONE(x1,y1,vie,Sco):					#Discussion mechant 1
	chaine = "TOI ?!"
	locuteur = "Terra"
	dialogue(chaine,locuteur)
	actualiser()
	attenteclic()
	sousGAMEPLAY(PDD,map10,100,200,vie)
	screen.blit(MECH1G,(300,200))
	chaine = "Comment es-tu arrivé ici ?"
	locuteur = "Terra"
	dialogue(chaine,locuteur)
	actualiser()
	attenteclic()
	sousGAMEPLAY(PDD,map10,100,200,vie)
	screen.blit(MECH1G,(300,200))
	chaine = "J’ai réussi à m'échapper, tes gardes sont inefficaces !"
	locuteur = "VOUS"
	dialogue(chaine,locuteur)
	actualiser()
	attenteclic()
	sousGAMEPLAY(PDD,map10,100,200,vie)
	screen.blit(MECH1G,(300,200))
	if Sco==0:
		chaine = "HA mais je vois tu n'as sauvé personne"
		locuteur = "Terra"
		dialogue(chaine,locuteur)
		actualiser()
		attenteclic()
		sousGAMEPLAY(PDD,map10,100,200,vie)
		screen.blit(MECH1G,(300,200))
		chaine = "Alors il y avait bien quelqu'un derrière la palissade"
		locuteur = "VOUS"
		dialogue(chaine,locuteur)
		actualiser()
		attenteclic()
		sousGAMEPLAY(PDD,map10,100,200,vie)
		screen.blit(MECH1G,(300,200))
		if 6 in visiter :
			chaine = "Je n'aurai pas du donner la hache a Benoit."
			locuteur = "VOUS"
			dialogue(chaine,locuteur)
			actualiser()
			attenteclic()
			sousGAMEPLAY(PDD,map10,100,200,vie)
			screen.blit(MECH1G,(300,200))
			chaine = "Mais Lui il en s'en sortira"
			locuteur = "VOUS"
			dialogue(chaine,locuteur)
			actualiser()
			attenteclic()
			sousGAMEPLAY(PDD,map10,100,200,vie)
			screen.blit(MECH1G,(300,200))
			chaine = "Tu parles du passage derrière l'armoire ?"
			locuteur = "Terra"
			dialogue(chaine,locuteur)
			actualiser()
			attenteclic()
			sousGAMEPLAY(PDD,map10,100,200,vie)
			screen.blit(MECH1G,(300,200))
			chaine = "C'est un trou sans fond ! Bye Bye ton ami"
			locuteur = "Terra"
			dialogue(chaine,locuteur)
			actualiser()
			attenteclic()
			sousGAMEPLAY(PDD,map10,100,200,vie)
			screen.blit(MECH1G,(300,200))
			chaine = "Tu mens !"
			locuteur = "VOUS"
			dialogue(chaine,locuteur)
			actualiser()
			attenteclic()
			sousGAMEPLAY(PDD,map10,100,200,vie)
			screen.blit(MECH1G,(300,200))
			chaine = "Que trépasse si je faiblis ! Tu n'auras pas tous mes amis"
			locuteur = "VOUS"
			dialogue(chaine,locuteur)
			actualiser()
			attenteclic()
			sousGAMEPLAY(PDD,map10,100,200,vie)
			screen.blit(MECH1G,(300,200))
			chaine = "Maintenant c'est ton tour de mourir chevalier"
			locuteur = "Terra"
			dialogue(chaine,locuteur)
			actualiser()
			attenteclic()
			sousGAMEPLAY(PDD,map10,100,200,vie)
			screen.blit(MECH1G,(300,200))
		else :
			chaine = "Tu vas payer pour eux !"
			locuteur = "VOUS"
			dialogue(chaine,locuteur)
			actualiser()
			attenteclic()
			sousGAMEPLAY(PDD,map10,100,200,vie)
			screen.blit(MECH1G,(300,200))
			chaine = "Viens affronter ton destin chevalier"
			locuteur = "Terra"
			dialogue(chaine,locuteur)
			actualiser()
			attenteclic()
			sousGAMEPLAY(PDD,map10,100,200,vie)
			screen.blit(MECH1G,(300,200))
	if Sco==1:
		chaine = "Tu as sauvé un de tes amis en plus"
		locuteur = "Terra"
		dialogue(chaine,locuteur)
		actualiser()
		attenteclic()
		sousGAMEPLAY(PDD,map10,100,200,vie)
		screen.blit(MECH1G,(300,200))
		chaine = "Bien sûr, je ne te laisserai plus faire du mal à mes compagnons!"
		locuteur = "VOUS"
		dialogue(chaine,locuteur)
		actualiser()
		attenteclic()
		sousGAMEPLAY(PDD,map10,100,200,vie)
		screen.blit(MECH1G,(300,200))
		chaine = "C'est ce qu'on va voir chevalier..."
		locuteur = "Terra"
		dialogue(chaine,locuteur)
		actualiser()
		attenteclic()
		sousGAMEPLAY(PDD,map10,100,200,vie)
		screen.blit(MECH1G,(300,200))
	screen.blit(scenario3,(0,0))
	actualiser()
	attenteclic()

def mortdeTerra(x1,y1,vie,Sco):							#mort du mechant 1
	sousGAMEPLAY(PDD,map10,100,200,vie)
	screen.blit(MECH1G,(300,200))
	chaine = "Comment...Comment as tu fait pour me vaincre?"
	locuteur = "Terra"
	dialogue(chaine,locuteur)
	attenteclic()
	actualiser()
	chaine = "C'est impossible...Je ne...peux...pas mourir..."
	locuteur = "VOUS"
	dialogue(chaine,locuteur)
	sousGAMEPLAY(PDD,map10,100,200,vie)
	screen.blit(MECH1G,(300,200))
	attenteclic()
	actualiser()
	chaine = "Je...suis..."
	locuteur = "Terra"
	dialogue(chaine,locuteur)
	sousGAMEPLAY(PDD,map10,100,200,vie)
	screen.blit(crane,(300,200))
	chaine = "Une bonne chose de faite"
	locuteur = "Terra"
	dialogue(chaine,locuteur)
	actualiser()
	attenteclic()

def libererKAI(x1,y1,vie,Sco):
	sousGAMEPLAY(PDD,map11,300,450,vie)
	screen.blit(gentil3G,(530,140))
	screen.blit(prisonporte,(520,200))
	chaine = "Kai !!"
	locuteur = "VOUS"
	dialogue(chaine,locuteur)
	actualiser()
	attenteclic()
	sousGAMEPLAY(PDD,map11,300,450,vie)
	screen.blit(gentil3G,(530,140))
	screen.blit(prisonporte,(520,200))
	chaine = "C'est toi chevalier ??"
	locuteur = "KAI"
	dialogue(chaine,locuteur)
	actualiser()
	attenteclic()
	sousGAMEPLAY(PDD,map11,300,450,vie)
	screen.blit(gentil3G,(530,140))
	screen.blit(prisonporte,(520,200))
	chaine = "Oui c'est moi, tu vas bien ?"
	locuteur = "VOUS"
	dialogue(chaine,locuteur)
	actualiser()
	attenteclic()
	sousGAMEPLAY(PDD,map11,300,450,vie)
	screen.blit(gentil3G,(530,140))
	screen.blit(prisonporte,(520,200))
	chaine = "Oui ne t'inquiete pas mais récupere la clef"
	locuteur = "KAI"
	dialogue(chaine,locuteur)
	actualiser()
	attenteclic()
	sousGAMEPLAY(PDD,map11,300,450,vie)
	screen.blit(gentil3G,(530,140))
	screen.blit(prisonporte,(520,200))
	chaine = "vite avant que terra ne revienne"
	locuteur = "KAI"
	dialogue(chaine,locuteur)
	actualiser()
	attenteclic()
	chx=choix(map11,choixKAI)
	if chx==0:
		sousGAMEPLAY(PDD,map11,300,450,vie)
		screen.blit(gentil3G,(530,140))
		screen.blit(prisonporte,(520,200))
		chaine = "J'ai vaincu Terra facilement"
		locuteur = "VOUS"
		dialogue(chaine,locuteur)
		actualiser()
		attenteclic()
		sousGAMEPLAY(PDD,map11,300,450,vie)
		screen.blit(gentil3G,(530,140))
		screen.blit(prisonporte,(520,200))
		chaine = "Ha bon ?! Comment as tu fais ?"
		locuteur = "KAI"
		dialogue(chaine,locuteur)
		actualiser()
		attenteclic()
		sousGAMEPLAY(PDD,map11,300,450,vie)
		screen.blit(gentil3G,(530,140))
		screen.blit(prisonporte,(520,200))
		chaine = "Terra n'arrivait pas à ma cheville"
		locuteur = "VOUS"
		dialogue(chaine,locuteur)
		actualiser()
		attenteclic()
		sousGAMEPLAY(PDD,map11,300,450,vie)
		screen.blit(gentil3G,(530,140))
		screen.blit(prisonporte,(520,200))
		chaine = "Ah bon, un coup de chance plutôt ?"
		locuteur = "KAI"
		dialogue(chaine,locuteur)
		actualiser()
		attenteclic()
		sousGAMEPLAY(PDD,map11,300,450,vie)
		screen.blit(gentil3G,(530,140))
		screen.blit(prisonporte,(520,200))
		chaine = "Non je l'ai surpassé, personne ne rivalise"
		locuteur = "VOUS"
		dialogue(chaine,locuteur)
		actualiser()
		attenteclic()
		sousGAMEPLAY(PDD,map11,300,450,vie)
		screen.blit(gentil3G,(530,140))
		screen.blit(prisonporte,(520,200))
		chaine = "Bon allez, fais moi sortir"
		locuteur = "KAI"
		dialogue(chaine,locuteur)
		actualiser()
		attenteclic()
	if chx==1:
		sousGAMEPLAY(PDD,map11,300,450,vie)
		screen.blit(gentil3G,(530,140))
		screen.blit(prisonporte,(520,200))
		chaine = "C'est finit pour lui, il ne reviendra pas"
		locuteur = "VOUS"
		dialogue(chaine,locuteur)
		actualiser()
		attenteclic()
		sousGAMEPLAY(PDD,map11,300,450,vie)
		screen.blit(gentil3G,(530,140))
		screen.blit(prisonporte,(520,200))
		chaine = "Ha bon ?! Comment tu sais ?"
		locuteur = "KAI"
		dialogue(chaine,locuteur)
		actualiser()
		attenteclic()
		sousGAMEPLAY(PDD,map11,300,450,vie)
		screen.blit(gentil3G,(530,140))
		screen.blit(prisonporte,(520,200))
		chaine = "Je l'ai battu !"
		locuteur = "VOUS"
		dialogue(chaine,locuteur)
		actualiser()
		attenteclic()
		sousGAMEPLAY(PDD,map11,300,450,vie)
		screen.blit(gentil3G,(530,140))
		screen.blit(prisonporte,(520,200))
		chaine = "Serieux ?"
		locuteur = "KAI"
		dialogue(chaine,locuteur)
		actualiser()
		attenteclic()
		sousGAMEPLAY(PDD,map11,300,450,vie)
		screen.blit(gentil3G,(530,140))
		screen.blit(prisonporte,(520,200))
		chaine = "Oui j'ai réussis à deviner ses pièges"
		locuteur = "VOUS"
		dialogue(chaine,locuteur)
		actualiser()
		attenteclic()
		sousGAMEPLAY(PDD,map11,300,450,vie)
		screen.blit(gentil3G,(530,140))
		screen.blit(prisonporte,(520,200))
		chaine = "Whaou tu m'impressionne "
		locuteur = "KAI"
		dialogue(chaine,locuteur)
		actualiser()
		attenteclic()
		sousGAMEPLAY(PDD,map11,300,450,vie)
		screen.blit(gentil3G,(530,140))
		screen.blit(prisonporte,(520,200))
		chaine = "Merci mais il faut que je te libère"
		locuteur = "VOUS"
		dialogue(chaine,locuteur)
		actualiser()
		attenteclic()
		sousGAMEPLAY(PDD,map11,300,450,vie)
		screen.blit(gentil3G,(530,140))
		screen.blit(prisonporte,(520,200))
		chaine = "Merci tiens une potion de vie pour te soigner"
		locuteur = "KAI"
		dialogue(chaine,locuteur)
		actualiser()
		attenteclic()
		vie=5
	return vie

def mauvaiseclef(x1,y1,vie,Sco):
	sousGAMEPLAY(PDD,map11,x1,y1,vie)
	screen.blit(gentil3G,(530,140))
	screen.blit(prisonporte,(520,200))
	chaine = "La clef ne marche pas"
	locuteur = "VOUS"
	dialogue(chaine,locuteur)
	actualiser()
	attenteclic()
	sousGAMEPLAY(PDD,map11,x1,y1,vie)
	screen.blit(gentil3G,(530,140))
	screen.blit(prisonporte,(520,200))
	chaine = "Ho non cela doit être la clef de l'aile Royale"
	locuteur = "KAI"
	dialogue(chaine,locuteur)
	actualiser()
	attenteclic()
	sousGAMEPLAY(PDD,map11,x1,y1,vie)
	screen.blit(gentil3G,(530,140))
	screen.blit(prisonporte,(520,200))
	chaine = "Ma clef doit être la bas, vas-y"
	locuteur = "KAI"
	dialogue(chaine,locuteur)
	actualiser()
	attenteclic()


def revelation(x1,y1,vie,Sco) :
	sousGAMEPLAY(PDG,map14,x1,y1,vie)
	chaine = "He ho ! il y a quelqu'un ?..."
	locuteur = "VOUS"
	dialogue(chaine,locuteur)
	actualiser()
	attenteclic()
	sousGAMEPLAY(PDG,map14,x1,y1,vie)
	if "salle6" in visiter :
		chaine = "Encore TOI"
		locuteur = "Benoit"
		dialogue(chaine,locuteur)
		actualiser()
		attenteclic()
		sousGAMEPLAY(PDG,map14,x1,y1,vie)
		chaine = "Qu'est ce tu fais derrière mon armoire ?"
		locuteur = "Benoit"
		dialogue(chaine,locuteur)
		actualiser()
		attenteclic()
		sousGAMEPLAY(PDD,map11,x1,y1,vie)
		screen.blit(gentil3G,(530,140))
		screen.blit(prisonporte,(520,200))
		chaine = "J'ai bien fait de ne pas te donner la hache"
		locuteur = "VOUS"
		dialogue(chaine,locuteur)
		actualiser()
		attenteclic()
		sousGAMEPLAY(PDD,map11,x1,y1,vie)
		screen.blit(gentil3G,(530,140))
		screen.blit(prisonporte,(520,200))
		chaine = "Pourquoi ?"
		locuteur = "Benoit"
		dialogue(chaine,locuteur)
		actualiser()
		attenteclic()
		sousGAMEPLAY(PDD,map11,x1,y1,vie)
		screen.blit(gentil3G,(530,140))
		screen.blit(prisonporte,(520,200))
		chaine = "C'est un puit sans fond derrière"
		locuteur = "VOUS"
		dialogue(chaine,locuteur)
		actualiser()
		attenteclic()
		sousGAMEPLAY(PDD,map11,x1,y1,vie)
		screen.blit(gentil3G,(530,140))
		screen.blit(prisonporte,(520,200))
		chaine = "Alors tu ma sauver la vie ?"
		locuteur = "Benoit"
		dialogue(chaine,locuteur)
		actualiser()
		attenteclic()
		sousGAMEPLAY(PDD,map11,x1,y1,vie)
		screen.blit(gentil3G,(530,140))
		screen.blit(prisonporte,(520,200))
		chaine = "Oui oui j'ai trouver Kai et Armant aussi "
		locuteur = "VOUS"
		dialogue(chaine,locuteur)
		actualiser()
		attenteclic()
		sousGAMEPLAY(PDD,map11,x1,y1,vie)
		screen.blit(gentil3G,(530,140))
		screen.blit(prisonporte,(520,200))
		chaine = "Ok ok mais me laisse pas croupir ici"
		locuteur = "Benoit"
		dialogue(chaine,locuteur)
		actualiser()
		attenteclic()
	if "donnerH" in action:
		sousGAMEPLAY(PDG,map14,x1,y1,vie)
		screen.blit(crane,(250,250))
		chaine = "Ho mon dieu, c'est benoît !"
		locuteur = "VOUS"
		dialogue(chaine,locuteur)
		actualiser()
		attenteclic()
		sousGAMEPLAY(PDG,map14,x1,y1,vie)
		screen.blit(crane,(250,250))
		chaine = "Il est tomber, comme avait dis Terra..."
		locuteur = "VOUS"
		dialogue(chaine,locuteur)
		actualiser()
		attenteclic()
		sousGAMEPLAY(PDG,map14,x1,y1,vie)
		screen.blit(crane,(250,250))
		chaine = "Repose en paix camarde..."
		locuteur = "VOUS"
		dialogue(chaine,locuteur)
		actualiser()
		attenteclic()


def combatbossdeux(x1,y1,vie,Sco):
	if "fuiteJoul" in action:
		sousGAMEPLAY(PDG,map19,360,460,vie)
		screen.blit(MECH2D,(360,150))
		chaine = "JOULEN !"
		locuteur = "VOUS"
		dialogue(chaine,locuteur)
		actualiser()
		attenteclic()
		sousGAMEPLAY(PDG,map19,360,460,vie)
		screen.blit(MECH2D,(360,150))
		chaine = "Je t'attendais, prépare toi à mourir"
		locuteur = "Joulen"
		dialogue(chaine,locuteur)
		actualiser()
		attenteclic()
		sousGAMEPLAY(PDG,map19,360,460,vie)
		screen.blit(MECH2D,(360,150))
		chaine = "Tu ne t'échapera pas cette fois-ci"
		locuteur = "VOUS"
		dialogue(chaine,locuteur)
		actualiser()
		attenteclic()
	else :
		sousGAMEPLAY(PDG,map19,360,460,vie)
		screen.blit(MECH2D,(360,150))
		chaine = "Un chevalier ? tu es venu sauver tes amis ?"
		locuteur = "Joulen"
		dialogue(chaine,locuteur)
		actualiser()
		attenteclic()
		sousGAMEPLAY(PDG,map19,360,460,vie)
		screen.blit(MECH2D,(360,150))
		chaine = "Alors ne te met pas en travers de mon chemin"
		locuteur = "VOUS"
		dialogue(chaine,locuteur)
		actualiser()
		attenteclic()
		sousGAMEPLAY(PDG,map19,360,460,vie)
		screen.blit(MECH2D,(360,150))
		chaine = "Tu ne sauveras personne, prépare toi à mourir! "
		locuteur = "Joulen"
		dialogue(chaine,locuteur)
		actualiser()
		attenteclic()
	fightdeux(vie)

def mortJulen(x1,y1,vie,Sco):
	sousGAMEPLAY(PDG,map19,x1,y1,vie)
	screen.blit(MECH2D,(360,150))
	chaine = "Mais...comment est ce possible..."
	locuteur = "Joulen"
	dialogue(chaine,locuteur)
	actualiser()
	attenteclic()
	sousGAMEPLAY(PDG,map19,x1,y1,vie)
	screen.blit(MECH2D,(360,150))
	chaine = "D'ou te viens une telle puissance..."
	locuteur = "VOUS"
	dialogue(chaine,locuteur)
	actualiser()
	attenteclic()
	sousGAMEPLAY(PDG,map19,x1,y1,vie)
	screen.blit(MECH2D,(360,150))
	haine = "Un simple chevalier ne peut pas me..."
	locuteur = "Joulen"
	dialogue(chaine,locuteur)
	actualiser()
	attenteclic()
	sousGAMEPLAY(PDG,map19,x1,y1,vie)
	screen.blit(MECH2D,(360,150))
	haine = "Un simple chevalier ne peut pas me..."
	locuteur = "Joulen"
	dialogue(chaine,locuteur)
	actualiser()
	attenteclic()
	sousGAMEPLAY(PDG,map19,x1,y1,vie)
	screen.blit(crane,(360,150))
	haine = "Il ne reste plus que BADGAMENOM..."
	locuteur = "VOUS"
	dialogue(chaine,locuteur)
	actualiser()
	attenteclic()

def KAIliberer(x1,y1,vie,Sco):
	sousGAMEPLAY(PDD,map11,x1,y1,vie)
	screen.blit(gentil3G,(530,140))
	chaine = "Ah enfin tu es revenu pour moi"
	locuteur = "KAI"
	dialogue(chaine,locuteur)
	actualiser()
	attenteclic()
	sousGAMEPLAY(PDD,map11,x1,y1,vie)
	screen.blit(gentil3G,(530,140))
	chaine = "Je ne laisse jamais tomber un ami"
	locuteur = "VOUS"
	dialogue(chaine,locuteur)
	actualiser()
	attenteclic()
	sousGAMEPLAY(PDD,map11,x1,y1,vie)
	screen.blit(gentil3G,(530,140))
	chaine = "Heuresement pour moi"
	locuteur = "KAI"
	dialogue(chaine,locuteur)
	actualiser()
	attenteclic()
	if 18 in visiter :
		sousGAMEPLAY(PDD,map11,x1,y1,vie)
		screen.blit(gentil3G,(530,140))
		chaine = "Au fait Mystic faisait que rêpeter une phrase"
		locuteur = "VOUS"
		dialogue(chaine,locuteur)
		actualiser()
		attenteclic()
		sousGAMEPLAY(PDD,map11,x1,y1,vie)
		screen.blit(gentil3G,(530,140))
		chaine = "Il disait quoi ?"
		locuteur = "KAI"
		dialogue(chaine,locuteur)
		actualiser()
		attenteclic()
		chx=choix(map11,chMystic)
		if chx==0:
			sousGAMEPLAY(PDD,map11,x1,y1,vie)
			screen.blit(gentil3G,(530,140))
			chaine = "Quand les nuages cachent la mer..."
			locuteur = "VOUS"
			dialogue(chaine,locuteur)
			actualiser()
			attenteclic()
			sousGAMEPLAY(PDD,map11,x1,y1,vie)
			screen.blit(gentil3G,(530,140))
			chaine = "...La magie fait gronder le tonerre"
			locuteur = "KAI"
			dialogue(chaine,locuteur)
			actualiser()
			attenteclic()
			sousGAMEPLAY(PDD,map11,x1,y1,vie)
			screen.blit(gentil3G,(530,140))
			chaine = "Quoi??"
			locuteur = "VOUS"
			dialogue(chaine,locuteur)
			actualiser()
			attenteclic()
			sousGAMEPLAY(PDD,map11,x1,y1,vie)
			screen.blit(gentil3G,(530,140))
			chaine = "C'est une vielle légende"
			locuteur = "KAI"
			dialogue(chaine,locuteur)
			actualiser()
			attenteclic()
			sousGAMEPLAY(PDD,map11,x1,y1,vie)
			screen.blit(gentil3G,(530,140))
			chaine = "Sa serait un code dans une des salles du chateau"
			locuteur = "KAI"
			dialogue(chaine,locuteur)
			actualiser()
			attenteclic()
			sousGAMEPLAY(PDD,map11,x1,y1,vie)
			screen.blit(gentil3G,(530,140))
			chaine = "Je resoudrais cette légende"
			locuteur = "VOUS"
			dialogue(chaine,locuteur)
			actualiser()
			attenteclic()
		if chx==1:
			sousGAMEPLAY(PDD,map11,x1,y1,vie)
			screen.blit(gentil3G,(530,140))
			chaine = "Quand les nuages survolent la mer..."
			locuteur = "VOUS"
			dialogue(chaine,locuteur)
			actualiser()
			attenteclic()
			sousGAMEPLAY(PDD,map11,x1,y1,vie)
			screen.blit(gentil3G,(530,140))
			chaine = "Non sa me dis rien du tout"
			locuteur = "KAI"
			dialogue(chaine,locuteur)
			actualiser()
			attenteclic()
			sousGAMEPLAY(PDD,map11,x1,y1,vie)
			screen.blit(gentil3G,(530,140))
			chaine = "Elle doit juste etre fatigué"
			locuteur = "KAI"
			dialogue(chaine,locuteur)
			actualiser()
			attenteclic()
			sousGAMEPLAY(PDD,map11,x1,y1,vie)
			screen.blit(gentil3G,(530,140))
			chaine = "Je vais aller la rejoindre"
			locuteur = "KAI"
			dialogue(chaine,locuteur)
			actualiser()
			attenteclic()
	sousGAMEPLAY(PDD,map11,x1,y1,vie)
	screen.blit(gentil3G,(530,140))
	chaine = "Bonne chance, je te rejoindrais quand mes pouvoirs seront rétablit"
	locuteur = "KAI"
	dialogue(chaine,locuteur)
	actualiser()
	attenteclic()


def libererben(x1,y1,vie,Sco):
	sousGAMEPLAY(PDD,map06,x1,y1,vie)
	screen.blit(gentil2D,(500,400))
	chaine = "Enfin tu es revenus, avec la clef j'espère"
	locuteur = "benoît"
	dialogue(chaine,locuteur)
	actualiser()
	attenteclic()
	sousGAMEPLAY(PDD,map06,x1,y1,vie)
	screen.blit(gentil2D,(500,400))
	chaine = "Estime toi heureux que je sois venu te sauver"
	locuteur = "VOUS"
	dialogue(chaine,locuteur)
	actualiser()
	attenteclic()
	sousGAMEPLAY(PDD,map06,x1,y1,vie)
	screen.blit(gentil2D,(500,400))
	chaine = "Oui merci oui, quand je raconterai a tout le monde comment je t'ai sauvé"
	locuteur = "benoît"
	dialogue(chaine,locuteur)
	actualiser()
	attenteclic()
	sousGAMEPLAY(PDD,map06,x1,y1,vie)
	screen.blit(gentil2D,(500,400))
	chaine = "Trop tard j'ai croiser les autres et je l'ai ai liberé"
	locuteur = "VOUS"
	dialogue(chaine,locuteur)
	actualiser()
	attenteclic()
	sousGAMEPLAY(PDD,map06,x1,y1,vie)
	screen.blit(gentil2D,(500,400))
	chaine = "Alors va finir le travail et sauve Luna ''hero''"
	locuteur = "benoît"
	dialogue(chaine,locuteur)
	actualiser()
	attenteclic()
	sousGAMEPLAY(PDD,map06,x1,y1,vie)
	screen.blit(gentil2D,(500,400))
	chaine = "Je n'ai pas besoin de toi"
	locuteur = "VOUS"
	dialogue(chaine,locuteur)
	actualiser()
	attenteclic()

def MysticPerdu(x1,y1,vie,Sco):
	sousGAMEPLAY(PDD,map18,x1,y1,vie)
	screen.blit(gentil4D,(160,300))
	chaine = "Quand les nuages survolent la mer..."
	locuteur = "Mystic"
	dialogue(chaine,locuteur)
	actualiser()
	attenteclic()
	sousGAMEPLAY(PDD,map18,x1,y1,vie)
	screen.blit(gentil4D,(160,300))
	chaine = "Quoi ?"
	locuteur = "VOUS"
	dialogue(chaine,locuteur)
	actualiser()
	attenteclic()
	sousGAMEPLAY(PDD,map18,x1,y1,vie)
	screen.blit(gentil4D,(160,300))
	chaine = "Quand les nuages survolent la mer..."
	locuteur = "Mystic"
	dialogue(chaine,locuteur)
	actualiser()
	attenteclic()
	sousGAMEPLAY(PDD,map18,x1,y1,vie)
	screen.blit(gentil4D,(160,300))
	chaine = "ça va Mystic ?"
	locuteur = "VOUS"
	dialogue(chaine,locuteur)
	actualiser()
	attenteclic()
	sousGAMEPLAY(PDD,map18,x1,y1,vie)
	screen.blit(gentil4D,(160,300))
	chaine = "Quand les nuages survolent la mer..."
	locuteur = "Mystic"
	dialogue(chaine,locuteur)
	actualiser()
	attenteclic()
	sousGAMEPLAY(PDD,map18,x1,y1,vie)
	screen.blit(gentil4D,(160,300))
	chaine = "Il a l'air en transe total"
	locuteur = "VOUS"
	dialogue(chaine,locuteur)
	actualiser()
	attenteclic()
#                                                                  SEQ DE JEUX                                                                     #
####################################################################################################################################################


def ManeMenu(fond,carre): 			#affichage de l'ecran d'acceuil
	screen.blit(fond, (0,0))
	screen.blit(rendu_texte1, text_rect1)
	screen.blit(rendu_texte2, text_rect2)
	if carre == 1 :
		screen.blit(select,(100,180))
	if carre == 2 :
		screen.blit(select,(400,180))
	actualiser()



def MENU():					#Animation menu
	fond = fondM
	sexe = 0
	sonMane.play()
	FIN = False
	while not FIN:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				END()
			if  event.type == KEYDOWN:
				if event.key == K_LEFT :
					sexe = 1
					ManeMenu(fond,sexe)
				if event.key == K_RIGHT :
					sexe = 2
					ManeMenu(fond,sexe)
				if event.key == K_SPACE :
					sonMane.stop()
					swordson.play()
					FIN = True
		if text_rect1.centerx > screen_rect.centerx:
			print (text_rect1.centerx)
			text_rect1.move_ip(-5, -1)
		if text_rect2.centerx > screen_rect.centerx:
			print (text_rect2.centerx)
			text_rect2.move_ip(-5, 1)
		if text_rect2.centerx <= screen_rect.centerx:
			fond = fond2
		ManeMenu(fond,sexe)
		actualiser()
		clock.tick(60)
	return sexe


def fighter(event,vie):				#premier combat mechant 2
	facing=-1
	face=1
	x1=200
	y1=200
	x2=400
	y2=0
	bouledefeu = []
	lance = []
	FIN = False
	sens = 1
	lonap=150
	limite=0
	walkCount=0
	timer=0
	Orientation=PDD
	while not FIN :
		timer=+1
		clock.tick(20)
		arreter=True
		screen.blit(Centrale,(0,0))
		tirage=randint(1,15)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				END()
		for test in bouledefeu:
			if test.x < 700 and test.x > -50:
				test.x += test.vel
			else:
				bouledefeu.pop(bouledefeu.index(test))
		for bullets in lance:
			if bullets.x < 700 and bullets.x > -50:
				bullets.x += bullets.vel
			else:
				lance.pop(lance.index(bullets))
				limite=limite-1
		if tirage==2 :
			bouledefeu.append(projectile(round(x2 + 64 //2), round(y2 + 64//2),facing))
		if event.type == KEYDOWN:
			if event.key == K_SPACE :
				if limite<=4:
					lance.append(atack(round(x1 + 64 //2), round(y1 + 64//2),face))
					limite=limite+1
					timer=0
			elif event.key == K_LEFT:
				if x1>50:
					arreter=False
					screen.blit(walkleft[walkCount//3],(x1,y1))
					x1=x1-10
					walkCount=walkCount+1
					Orientation = PDG
			elif event.key == K_RIGHT:
				if x1<580 or 230<y1<250:
					arreter=False
					screen.blit(walkright[walkCount//3],(x1,y1))
					x1=x1+10
					walkCount=walkCount+1
					Orientation = PDD
			elif event.key == K_UP :
				if y1>90:
					arreter=False
					y1=y1-10
					screen.blit(Orientation,(x1,y1))
			elif event.key == K_DOWN :
				if y1<400:
					arreter=False
					y1=y1+10
					screen.blit(Orientation,(x1,y1))
		if y2<50 :
			sens = 1
		if y2>350 :
			sens = -1
		y2 = y2 + 8*sens
		if walkCount >=10 :
			walkCount =0
		if arreter==True :
			screen.blit(Orientation,(x1,y1))
		Interface(valide,objet,vie,Sco)
		if lonap<=0 :
			FIN=True
		pygame.draw.rect(screen,(255,0,0),(10,70,150,20))
		pygame.draw.rect(screen,(0,128,0),(10,70,lonap,20))
		screen.blit(MECH2D,(x2,y2))
		for test in bouledefeu:
			test.draw(screen,facing)
			if x1-30<test.x<x1+30:
				if y1-30<test.y<y1+30:
					vie= vie-1
					x1=50
					y1=10
					doul1.play()
		for bullets in lance:
			bullets.draw(screen,face)
			if x2-30<bullets.x<x2+30:
				if y2-70<bullets.y<y2+70:
					lance.pop(lance.index(bullets))
					lonap=lonap-25
					limite=limite-1
		actualiser()
		if vie == 0 :
			mort()
	return vie

def intro_Scenario():
	Sco=0							#intro d'histoire
	screen.blit(t1, (0,0))
	VIE(5)
	screen.blit(PDD, (300,200))
	actualiser()
	pygame.time.delay(2000)
	walkCount=0
	xC = -10
	yC = 200
	FIN = False
	while not FIN:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				END()
		while xC < 250 :
			clock.tick(20)
			xC = xC+5
			screen.blit(t1, (0,0))							#blit la map
			screen.blit(PDD, (300,200))						#blit notre perso
			screen.blit(CwalkR[walkCount//3], (xC,yC))		#blit le perso qui se déplace
			walkCount=walkCount+1							#Incrémentation du selecteur
			if walkCount>=10:
				walkCount=0
			Interface(0,hache,vie,Sco)
			actualiser()
		screen.blit(t1, (0,0))
		screen.blit(PDG, (300,200))
		screen.blit(coursierD, (xC,yC))
		Interface(0,hache,vie,Sco)
		chaine = "Bonjour mon chevalier vaillant, voici une lettre du roi pour vous."
		locuteur = "Messager"
		dialogue(chaine,locuteur)
		attenteclic()


		while xC>-40 :
			clock.tick(20)
			xC = xC-5
			screen.blit(t1, (0,0))
			screen.blit(PDG, (300,200))
			screen.blit(CwalkL[walkCount//3], (xC,yC))
			walkCount=walkCount+1
			screen.blit(inv1, (0,0))
			VIE(vie)
			actualiser()
			if walkCount>=10:
				walkCount=0
		chaine = "Je me demande bien ce que peut me vouloir le roi..."
		locuteur = "Vous"
		dialogue(chaine,locuteur)
		attenteclic()
		screen.blit(t1, (0,0))
		screen.blit(PDD, (300,200))
		screen.blit(inv1, (0,0))
		VIE(vie)
		screen.blit(indication_espace, (500,100))
		actualiser()
		attentespace()
		lettreroi()
		FIN = True


def IntroGAMEPLAY(Orientation,CHmap,x1,y1,vie):				#Suite de l'intro avant de rentrer dans le donjon
	if CHmap == map03 :
		valide = False
		objet = 0
		FIN = False
		arreter=True
		walkCount=0
		while not FIN :
			arreter=True
			clock.tick(20)
			screen.blit(map03,(0,0))
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					END()
				if x1>385 and y1>360 :
					if event.type == KEYDOWN:
						if event.key == K_SPACE :
							chaine = "Route barrée"
							locuteur = "paneau"
							dialogue(chaine,locuteur)
							attenteclic()
							chaine = "Mince, je vais devoir faire un détour par cette cité..."
							locuteur = "VOUS"
							dialogue(chaine,locuteur)
							attenteclic()
					screen.blit(paneau,(385,510))
					actualiser()
				if event.type == KEYDOWN:
					if event.key == K_LEFT :
						if x1>240 or y1 == 370 :
							arreter=False
							screen.blit(walkleft[walkCount//3],(x1,y1))
							x1=x1-10
							walkCount=walkCount+1
							Orientation = PDG
					if event.key == K_RIGHT :
						if x1 < 380:
							arreter=False
							screen.blit(walkright[walkCount//3],(x1,y1))
							x1=x1+10
							walkCount=walkCount+1
							Orientation = PDD
					if event.key == K_UP :
						if x1>220:
							arreter=False
							y1 = y1-10
							screen.blit(Orientation,(x1,y1))
					if event.key == K_DOWN :
						if y1<370:
							arreter=False
							y1 = y1+10
							screen.blit(Orientation,(x1,y1))
			if walkCount >=10 :
				walkCount =0
			if arreter==True :
				screen.blit(Orientation,(x1,y1))
			Interface(valide,objet,vie,Sco)
			actualiser()
			if y1<-20 :
				FIN = True
		CHmap = mp_rue
		xB=320
		yB=-40
		x1=320
		y1=560
		FIN = False
		while not FIN :
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					END()
			if y1>320:
				y1=y1-1
			screen.blit(mp_rue,(0,0))
			screen.blit(PDG,(x1,y1))
			Interface(valide,objet,vie,Sco)
			actualiser()
			yB=yB+1
			screen.blit(MECH2D, (xB+90,yB-100))
			screen.blit(MECH1D, (xB-30,yB-100))
			screen.blit(BADD, (xB,yB))
			actualiser()
			if y1<=320 and yB>=200:
				FIN=True
		chaine = "Qu'est ce qu'il se passe ?!"
		locuteur = "VOUS"
		dialogue(chaine,locuteur)
		attenteclic()
		sousGAMEPLAY(PDG,CHmap,x1,y1,vie)
		screen.blit(MECH2D, (xB+90,yB-100))
		screen.blit(MECH1D, (xB-30,yB-100))
		screen.blit(BADD, (xB,yB))
		actualiser()
		chaine = "Un chevalier ! Je croyais vous avoir dis de tous les enfermer hier..."
		locuteur = "GAMENON"
		dialogue(chaine,locuteur)
		attenteclic()
		sousGAMEPLAY(PDG,CHmap,x1,y1,vie)
		screen.blit(MECH2D, (xB+90,yB-100))
		screen.blit(MECH1D, (xB-30,yB-100))
		screen.blit(BADD, (xB,yB))
		actualiser()
		chaine = "Je vais devoir m'en occuper moi même !"
		locuteur = "GAMENON"
		dialogue(chaine,locuteur)
		attenteclic()
		sousGAMEPLAY(PDG,CHmap,x1,y1,vie)
		screen.blit(BADD, (xB,yB))
		screen.blit(MECH2D, (xB+90,yB-100))
		screen.blit(MECH1D, (xB-30,yB-100))
		actualiser()
		chaine = "Qu'avez vous fais à mes amis ?!"
		locuteur = "VOUS"
		dialogue(chaine,locuteur)
		attenteclic()
		sousGAMEPLAY(PDG,CHmap,x1,y1,vie)
		screen.blit(MECH2D, (xB+90,yB-100))
		screen.blit(MECH1D, (xB-30,yB-100))
		screen.blit(BADD, (xB,yB))
		actualiser()
		chaine = "Tu vas voir par toi même."
		locuteur = "GAMENON"
		dialogue(chaine,locuteur)
		attenteclic()
		sousGAMEPLAY(PDG,CHmap,x1,y1,vie)
		screen.blit(MECH2D, (xB+90,yB-100))
		screen.blit(MECH1D, (xB-30,yB-100))
		screen.blit(BADD, (xB,yB))
		actualiser()
		screen.blit(tutoC,(0,0))
		actualiser()
		attenteclic()
		sousGAMEPLAY(PDG,CHmap,x1,y1,vie)
		screen.blit(MECH2D, (xB+90,yB-100))
		screen.blit(MECH1D, (xB-30,yB-100))
		screen.blit(BADD, (xB,yB))
		actualiser()
		xblf=xB
		yblf=yB
		FIN = False
		while not FIN :
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					END()
			if event.type == KEYDOWN:
				chaine = "FIRE BALL"
				locuteur = "GAMENON"
				dialogue(chaine,locuteur)
				while not yblf+50>y1:
					sousGAMEPLAY(PDG,CHmap,x1,y1,vie)
					screen.blit(MECH2D, (xB+90,yB-100))
					screen.blit(MECH1D, (xB-30,yB-100))
					screen.blit(BADD, (xB,yB))
					blfB_rect = ((xblf,yblf))
					screen.blit(blfB,blfB_rect)
					yblf=yblf+1
					actualiser()
					FIN = True
		screen.blit(mp_rue, (0,0))
		screen.blit(crane,(x1,y1))
		screen.blit(MECH2D, (xB+90,yB-100))
		screen.blit(MECH1D, (xB-30,yB-100))
		screen.blit(BADD, (xB,yB))
		chaine = "Emmenez moi ce chevalier au cachot !"
		locuteur = "GAMENON"
		dialogue(chaine,locuteur)
		actualiser()
		attenteclic()
		screen.blit(scenario2,(0,0))
		valeurCHX = choix(Centrale,chbaston)
		if valeurCHX==1:
			vie=fighter(event,vie)
			fuite(x1,y1,vie,Sco)
		salle3(PDD,entree,valide,objet,vie,Sco)
	if CHmap == mp_prison :
		walkCount=0
		valide = False
		objet = 0
		xp = 50
		yp = 370
		boostATK_rect=((500,100))
		Possesion=0
		pioche_rect = ((xp,yp))
		FIN = False
		while not FIN :
			arreter=True
			clock.tick(20)
			screen.blit(mp_prison,(0,0))
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					END()
				if event.type == KEYDOWN:
					if event.key == K_LEFT :
						if (290<y1<450 and (230>x1>40 or 240<x1<410)) or (y1<240 and x1>40):
							arreter=False
							screen.blit(walkleft[walkCount//3],(x1,y1))
							x1=x1-10
							walkCount=walkCount+1
							Orientation = PDG
					if event.key == K_RIGHT :
						if (290<y1<450 and (x1<150 or 200<x1<390)) or (y1<240 and x1<600):
							arreter=False
							screen.blit(walkright[walkCount//3],(x1,y1))
							x1=x1+10
							walkCount=walkCount+1
							Orientation = PDD
					if event.key == K_UP :
						if y1>320 or (290<x1<370 and y1>40) or 40<y1<240 or (y1<240 and x1<50):
							arreter=False
							y1=y1-10
							screen.blit(Orientation,(x1,y1))
					if event.key == K_DOWN :
						if y1<220 or 290<y1<390 or (290<x1<370 and y1<390):
							arreter=False
							y1=y1+10
							screen.blit(Orientation,(x1,y1))
					if event.key == K_SPACE :
						if x1-5<xp<x1+40 and y1-5<yp<y1+40:
							pioche_rect=((620,440))
							Possesion=1
						if y1<500 and x1>100 and Possesion==1:
							x1=x1+80;
							Possesion=2
							pioche_rect=((-200,-200))
			if walkCount >=10 :
				walkCount =0
			if arreter==True :
				screen.blit(Orientation,(x1,y1))
			Interface(valide,objet,vie,Sco)
			screen.blit(pioche, pioche_rect)
			screen.blit(boostATK,boostATK_rect)
			actualiser()
			if y1<0:
				FIN = True
		CHmap= mp_couloirPr
		x1=70
		y1=480
		FIN = False
		while not FIN :
			arreter=True
			clock.tick(20)
			screen.blit(mp_couloirPr,(0,0))
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					END()
				if event.type == KEYDOWN:
					if event.key == K_LEFT :
						if x1>70 :
							arreter=False
							screen.blit(walkleft[walkCount//3],(x1,y1))
							x1=x1-10
							walkCount=walkCount+1
							Orientation = PDG
					if event.key == K_RIGHT :
						if y1<240:
							arreter=False
							screen.blit(walkright[walkCount//3],(x1,y1))
							x1=x1+10
							walkCount=walkCount+1
							Orientation = PDD
					if event.key == K_UP :
						if y1>140:
							arreter=False
							y1=y1-10
							screen.blit(Orientation,(x1,y1))
					if event.key == K_DOWN :
						if x1<120 or y1<200:
							arreter=False
							y1=y1+10
							screen.blit(Orientation,(x1,y1))
			if walkCount >=10 :
				walkCount =0
			if arreter==True :
				screen.blit(Orientation,(x1,y1))
			Interface(valide,objet,vie,Sco)
			actualiser()
			if x1>680:
				FIN= True

def combatbossONE(vie,Sco):				#combat contre le mechant 1
	x1=10
	y1=200
	posCENT=(300,200)
	posREMA=(100,100)
	posREMB=(500,100)
	posREMC=(500,300)
	posREMD=(100,300)
	xpo=100
	ypo=100
	face=1
	parole="gris rouge"
	FIN = False
	lance=[]
	bouledefeu=[]
	pygame.time.set_timer(USEREVENT, 6000)
	toucher=False
	walkCount=0
	lonap=150
	Orientation=PDD
	limite=0
	valide=0
	objet=hache
	facing=1
	while not FIN :
		arreter=True
		clock.tick(20)
		screen.blit(map10,(0,0))
		for bullets in lance:
			if bullets.x < 700 and bullets.x > -50:
				bullets.x += bullets.vel
			else:
				lance.pop(lance.index(bullets))
				limite=limite-1
		for test in bouledefeu:
			if test.x < 700 and test.x > -50:
				test.x += test.vel
			else:
				bouledefeu.pop(bouledefeu.index(test))
		for event in pygame.event.get():
			if event.type == USEREVENT :
				if toucher == False:
					screen.blit(map10,(0,0))
					screen.blit(PDD,(x1,y1))
					screen.blit(MECH1G,(x1+100,y1))
					xg=x1+100
					actualiser()
					while not xg == x1:
						xg=xg-1
						screen.blit(map10,(0,0))
						screen.blit(PDD,(x1,y1))
						screen.blit(MECH1G,(x1+100,y1))
						screen.blit(blfG,(xg,y1))
						actualiser()
					vie=vie-1
				toucher=False
				POStir= randint(1,4)
				print(POStir)
				if POStir==1:
					xpo=100
					ypo=100
					parole="gris rouge"
				if POStir==2:
					xpo=500
					ypo=100
					parole="gris gris"
				if POStir ==3:
					xpo=500
					ypo=300
					parole="rouge"
				if POStir==4:
					xpo=100
					ypo=300
					parole="orange"
			if event.type == pygame.QUIT:
				END()
			if event.type == KEYDOWN:
				if event.key == K_LEFT :
					if (x1>50 and y1>80) or 220<y1<260:
						arreter=False
						screen.blit(walkleft[walkCount//3],(x1,y1))
						x1=x1-10
						walkCount=walkCount+1
						Orientation = PDG
						facing=-1
				if event.key == K_RIGHT :
					if x1<585 or y1>80:
						arreter=False
						screen.blit(walkright[walkCount//3],(x1,y1))
						x1=x1+10
						walkCount=walkCount+1
						Orientation = PDD
						facing=1
				if event.key == K_UP :
					if (y1>90 and x1>30) or 275<x1<315:
						arreter=False
						y1=y1-10
						screen.blit(Orientation,(x1,y1))
				if event.key == K_DOWN :
					if y1<400 and x1>30:
						arreter=False
						y1=y1+10
						screen.blit(Orientation,(x1,y1))
				if event.key == K_SPACE and limite<=5:
					lance.append(atack(round(x1 + 64 //2), round(y1 + 64//2),facing))
					limite=limite+1
		screen.blit(MECH1G,posREMA)
		screen.blit(MECH1G,posREMB)
		screen.blit(MECH1G,posREMC)
		screen.blit(MECH1G,posREMD)
		dialogue(parole,"BADOX")
		pygame.draw.rect(screen,(255,0,0),(10,70,150,20))
		pygame.draw.rect(screen,(0,128,0),(10,70,lonap,20))
		for bullets in lance:
			bullets.draw(screen,face)
			if xpo-10<bullets.x<xpo+50:
				if ypo-10<bullets.y<ypo+70:
					toucher = True
					lance.pop(lance.index(bullets))
					lonap=lonap-25
					limite=limite-1
		if vie == 0:
			mort(Sco)
		if lonap <= 0:
			FIN =True
		if walkCount >=10 :
			walkCount =0
		if arreter==True :
			screen.blit(Orientation,(x1,y1))
		Interface(valide,objet,vie,Sco)
		actualiser()
	mortdeTerra(x1,y1,vie,Sco)
	return vie


def fightdeux(vie):
	facing=-1
	face=1
	x1=200
	y1=200
	x2=400
	y2=0
	bouledefeu = []
	lance = []
	FIN = False
	sens = 1
	lonap=150
	limite=0
	walkCount=0
	timer=0
	Orientation=PDD
	while not FIN :
		timer=+1
		clock.tick(20)
		arreter=True
		screen.blit(map19,(0,0))
		tirage=randint(1,15)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				END()
			if event.type == KEYDOWN:
				if event.key == K_SPACE :
					if limite<=4:
						lance.append(atack(round(x1 + 64 //2), round(y1 + 64//2),face))
						limite=limite+1
						timer=0
				elif event.key == K_LEFT:
					if x1>50:
						arreter=False
						screen.blit(walkleft[walkCount//3],(x1,y1))
						x1=x1-10
						walkCount=walkCount+1
						Orientation = PDG
				elif event.key == K_RIGHT:
					if x1<580 or 230<y1<250:
						arreter=False
						screen.blit(walkright[walkCount//3],(x1,y1))
						x1=x1+10
						walkCount=walkCount+1
						Orientation = PDD
				elif event.key == K_UP :
					if y1>90:
						arreter=False
						y1=y1-10
						screen.blit(Orientation,(x1,y1))
				elif event.key == K_DOWN :
					if y1<400:
						arreter=False
						y1=y1+10
						screen.blit(Orientation,(x1,y1))
		for test in bouledefeu:
			if test.x > 700 :
				bouledefeu.pop(bouledefeu.index(test))
			elif test.x < -50 :
				bouledefeu.pop(bouledefeu.index(test))
				print("oui")
				bouledefeu.append(projectileS(round(x2 + 64 //2), round(y2 + 64//2),-1))
			else:
				test.x += test.vel
		for bullets in lance:
			if bullets.x < 700 and bullets.x > -50:
				bullets.x += bullets.vel
			else:
				lance.pop(lance.index(bullets))
				limite=limite-1
		if tirage==2 :
			bouledefeu.append(projectile(round(x2 + 64 //2), round(y2 + 64//2),facing))
		if y2<100 :
			sens = 1
		if y2>350 :
			sens = -1
		y2 = y2 + 8*sens
		if lonap<=0 :
			FIN=True
		if walkCount >=10 :
			walkCount =0
		if arreter==True :
			screen.blit(Orientation,(x1,y1))
		Interface(valide,objet,vie,Sco)
		pygame.draw.rect(screen,(255,0,0),(10,70,150,20))
		pygame.draw.rect(screen,(0,128,0),(10,70,lonap,20))
		screen.blit(MECH2D,(x2,y2))
		for test in bouledefeu:
			test.draw(screen,facing)
			if x1-30<test.x<x1+30:
				if y1-30<test.y<y1+30:
					vie= vie-1
					x1=50
					y1=10
					doul1.play()
		for bullets in lance:
			bullets.draw(screen,face)
			if x2-30<bullets.x<x2+30:
				if y2-70<bullets.y<y2+70:
					lance.pop(lance.index(bullets))
					lonap=lonap-25
					limite=limite-1
		actualiser()
		if vie == 0 :
			mort(Sco)
	mortJulen(x1,y1,vie,Sco)
	return vie






#######################################################################################################################################################


#                                                                  SALLE                                                                           #
####################################################################################################################################################



def salle3(Orientation,position,valide,objet,vie,Sco):
	valide = False
	objet = 0
	walkCount=0
	if position==entree:
		x1=50
		y1=200
	else:
		x1=600
		y1=245
	FIN = False
	while not FIN :
		arreter=True
		clock.tick(20)
		screen.blit(Centrale,(0,0))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				END()
			if event.type == KEYDOWN:
				if event.key == K_a :
					if "minimap_active" in action:
						minimapacl(220,295)
						actualiser()
						fermercarte()
				if event.key == K_LEFT :
					if x1>50:
						arreter=False
						screen.blit(walkleft[walkCount//3],(x1,y1))
						x1=x1-10
						walkCount=walkCount+1
						Orientation = PDG
				if event.key == K_RIGHT :
					if x1<580 or 230<y1<250:
						arreter=False
						screen.blit(walkright[walkCount//3],(x1,y1))
						x1=x1+10
						walkCount=walkCount+1
						Orientation = PDD
				if event.key == K_UP :
					if y1>90:
						arreter=False
						y1=y1-10
						screen.blit(Orientation,(x1,y1))
				if event.key == K_DOWN :
					if y1<400:
						arreter=False
						y1=y1+10
						screen.blit(Orientation,(x1,y1))
				if event.key == K_SPACE:
					if 200<x1<500 and 100<y1<400:
						if "findujeu" in action:
							END()
		if walkCount >=10 :
			walkCount =0
		if arreter==True :
			screen.blit(Orientation,(x1,y1))
		Interface(valide,objet,vie,Sco)
		actualiser()
		if x1>680:
			FIN= True
	salle4(Orientation,entree,valide,objet,vie,Sco)

def salle4(Orientation,position,valide,objet,vie,Sco):
	FIN = False
	xpal=280
	ypal=100
	walkCount=0
	if position==entree:
		x1=0
		y1=160
		if not 4 in visiter :
			chaine = "Ha ! Aidez moi ! A l'aide"
			locuteur = "?????"
			dialogue(chaine,locuteur)
			actualiser()
			attenteclic()
			sousGAMEPLAY(Orientation,map04,x1,y1,vie)
			screen.blit(palissade,(xpal,ypal))
			chaine = "Les cris viennent de derrière la palissade ! "
			locuteur = "VOUS"
			dialogue(chaine,locuteur)
			actualiser()
			attenteclic()
			sousGAMEPLAY(Orientation,map04,x1,y1,vie)
			screen.blit(palissade,(xpal,ypal))
			chaine = "Je dois trouver un moyen de passer"
			locuteur = "VOUS"
			dialogue(chaine,locuteur)
			actualiser()
			attenteclic()
			visiter.append(4)
	elif position==sortie:
		x1=290
		y1=10
	elif position==sortie1:
		x1=650
		y1=160
	else :
		x1=290
		y1=470
	while not FIN:
		arreter=True
		clock.tick(20)
		screen.blit(map04,(0,0))
		if not "palissadeCasser" in action :
			screen.blit(palissade,(xpal,ypal))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				END()
			if event.type == KEYDOWN:
				if event.key == K_a :
					if "minimap_active" in action:
						minimapacl(270,295)
						actualiser()
						fermercarte()
				if event.key == K_LEFT :
					if x1>280 or 120<y1<230:
						arreter=False
						screen.blit(walkleft[walkCount//3],(x1,y1))
						x1=x1-10
						walkCount=walkCount+1
						Orientation = PDG
				if event.key == K_RIGHT :
					if x1<320 or 120<y1<210:
						arreter=False
						screen.blit(walkright[walkCount//3],(x1,y1))
						x1=x1+10
						walkCount=walkCount+1
						Orientation = PDD
				if event.key == K_UP :
					if not "palissadeCasser" in action :
						if y1>170 :
							arreter=False
							y1=y1-10
							screen.blit(Orientation,(x1,y1))
					else :
						if y1>170 or 240<x1<300 :
							arreter=False
							y1=y1-10
							screen.blit(Orientation,(x1,y1))
				if event.key == K_DOWN:
					if y1<240 or 280<x1<330 :
						arreter=False
						y1=y1+10
						screen.blit(Orientation,(x1,y1))
			if walkCount >=10 :
				walkCount =0
			if arreter==True :
				screen.blit(Orientation,(x1,y1))
			Interface(valide,objet,vie,Sco)
			if valide==True :
				if event.type == KEYDOWN:
					if event.key == K_SPACE :
						if 250<x1<370 and 150<y1<230:
							action.append("palissadeCasser")
							valide=False
			actualiser()
			if y1>520:
				FIN=True
				salle6(Orientation,entree,valide,objet,vie,Sco)
			if y1<0:
				FIN=True
				salle5(Orientation,entree,valide,objet,vie,Sco)
			if x1<0:
				FIN=True
				salle3(Orientation,entree,valide,objet,vie,Sco)
			if x1>685:
				FIN=True
				salle7(Orientation,entree,valide,objet,vie,Sco)


def salle5(Orientation,position,valide,objet,vie,Sco):
	x1=340
	y1=460
	FIN = False
	walkCount=0
	if not 5 in visiter :
		sauvetage_g1(x1,y1,vie,Sco)
		Sco=+1
		visiter.append(5)
	while not FIN:
		arreter=True
		clock.tick(20)
		screen.blit(map05,(0,0))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				END()
			if event.type == KEYDOWN:
				if event.key == K_a :
					if "minimap_active" in action:
						minimapacl(270,253)
						actualiser()
						fermercarte()
				if event.key == K_LEFT :
					if x1>90 :
						arreter=False
						screen.blit(walkleft[walkCount//3],(x1,y1))
						x1=x1-10
						walkCount=walkCount+1
						Orientation = PDG
				if event.key == K_RIGHT :
					if x1<540:
						arreter=False
						screen.blit(walkright[walkCount//3],(x1,y1))
						x1=x1+10
						walkCount=walkCount+1
						Orientation = PDD
				if event.key == K_UP :
					if y1>90 :
						arreter=False
						y1=y1-10
						screen.blit(Orientation,(x1,y1))
				if event.key == K_DOWN:
					if y1<420 or 330<x1<370 :
						arreter=False
						y1=y1+10
						screen.blit(Orientation,(x1,y1))
		if walkCount >=10 :
			walkCount =0
		if arreter==True :
			screen.blit(Orientation,(x1,y1))
		Interface(valide,objet,vie,Sco)
		actualiser()
		if y1>520 :
			FIN=True
			salle4(Orientation,sortie,valide,objet,vie,Sco)

def salle6(Orientation,position,valide,objet,vie,Sco):
	x1=200
	y1=60
	FIN = False
	walkCount=0
	if not 6 in visiter:
		xh,yh,xg2,yg2 = choix_hache(x1,y1,vie,Sco)
		visiter.append(6)
	if not "donnerH" in action :
		xh,yh = 400,100
		xg2=500
		yg2=400
	else :
		xg2,yg2 = 0,0
	if "hacheprise" in action and not "palissadeCasser" in action:
		xh=800
		yh=400
	if "palissadeCasser" in action:
		xh,yh=900,800
	while not FIN:
		arreter=True
		clock.tick(20)
		screen.blit(map06,(0,0))
		if not "liberer2" in action:
			screen.blit(prisonporte,(515,280))
			screen.blit(gentil2G,(xg2,yg2))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				END()
			if event.type == KEYDOWN:
				if event.key == K_a :
					if "minimap_active" in action:
						minimapacl(270,350)
						actualiser()
						fermercarte()
				if event.key == K_LEFT :
					if x1>40 :
						arreter=False
						screen.blit(walkleft[walkCount//3],(x1,y1))
						x1=x1-10
						walkCount=walkCount+1
						Orientation = PDG
				if event.key == K_RIGHT :
					if x1<220 or (70<y1<270 and x1<590):
						arreter=False
						screen.blit(walkright[walkCount//3],(x1,y1))
						x1=x1+10
						walkCount=walkCount+1
						Orientation = PDD
				if event.key == K_UP :
					if y1>60 or 150<x1<220 :
						arreter=False
						y1=y1-10
						screen.blit(Orientation,(x1,y1))
				if event.key == K_DOWN:
					if (y1<420 and x1<250) or y1<200 :
						arreter=False
						y1=y1+10
						screen.blit(Orientation,(x1,y1))
				if event.key == K_SPACE :
					if xh-30<x1<xh+30 and yh-30<y1<yh+30 :
						xh=800
						yh=400
						valide=True
						objet=hache
						action.append("hacheprise")
					if x1>480 and y1>180:
						if "recupenigme" in action:
							action.append("liberer2")
							valide=False
							libererben(x1,y1,vie,Sco)
							Sco=+1
			hache_rect = ((xh,yh))
			if walkCount >=10 :
				walkCount =0
			if arreter==True :
				screen.blit(Orientation,(x1,y1))
			Interface(valide,objet,vie,Sco)
			screen.blit(hache, hache_rect)
			actualiser()
		if y1<0 :
			FIN=True
			salle4(Orientation,sortie2,valide,objet,vie,Sco)

def salle7(Orientation,position,valide,objet,vie,Sco):
	if position==entree:
		x1=0
		y1=210
	elif position==sortie:
		x1=330
		y1=20
	elif position==sortie1:
		x1=600
		y1=210
	FIN = False
	walkCount=0
	if not 7 in visiter :
		visiter.append(7)
	while not FIN:
		screen.blit(map07,(0,0))
		if not "salle12" in action:
			screen.blit(porte,(650,200))
		if not "minimap_active" in action :
			screen.blit(item_carte,(200,200))
		arreter=True
		clock.tick(20)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				END()
			if event.type == KEYDOWN:
				if event.key== K_q :
					salle12(Orientation,entree,valide,objet,vie,Sco)
				if event.key == K_a :
					if "minimap_active" in action:
						minimapacl(326,295)
						actualiser()
						fermercarte()
				if event.key == K_LEFT :
					if x1>40 or 160<y1<250:
						arreter=False
						screen.blit(walkleft[walkCount//3],(x1,y1))
						x1=x1-10
						walkCount=walkCount+1
						Orientation = PDG
				if event.key == K_RIGHT :
					if (x1<190 or (( y1<190 or y1>260 )and x1<600) or 480<x1<600) or ("clefRoyale" in action and 170<y1<230):
						arreter=False
						screen.blit(walkright[walkCount//3],(x1,y1))
						x1=x1+10
						walkCount=walkCount+1
						Orientation = PDD
				if event.key == K_UP :
					if (y1>110 and (40<x1<220 or 480<x1<600)) or y1>280 or 110<y1<220 or 300<x1<400:
						arreter=False
						y1=y1-10
						screen.blit(Orientation,(x1,y1))
				if event.key == K_DOWN:
					if  y1<170 or (y1<420 and ( 40<x1<220 or 480<x1<600 )) or 250<y1<420:
						arreter=False
						y1=y1+10
						screen.blit(Orientation,(x1,y1))
				if event.key == K_SPACE:
					if x1>600 and y1<300:
						if "clefRoyale" in action:
							valide=False
							action.append("salle12")
					if 180<y1<220 and 180<x1<220:
						if not "minimap_active" in action:
							action.append("minimap_active")
		if walkCount >=10 :
			walkCount =0
		if arreter==True :
			screen.blit(Orientation,(x1,y1))
		Interface(valide,objet,vie,Sco)
		actualiser()
		if y1<0 :
			salle8(Orientation,entree,valide,objet,vie,Sco)
		if x1<0 :
			salle4(Orientation,sortie1,valide,objet,vie,Sco)
		if x1>680:
			salle12(Orientation,entree,valide,objet,vie,Sco)

def salle8(Orientation,position,valide,objet,vie,Sco):
	if position== entree:
		x1=100
		y1=520
	else :
		x1=600
		y1=200
	FIN= False
	walkCount=0
	if not 8 in visiter :
		MSC1.stop()
		sonAilefeu.play()
		visiter.append(8)
	while not FIN:
		screen.blit(map08,(0,0))
		arreter=True
		clock.tick(20)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				END()
			if event.type == KEYDOWN:
				if event.key == K_a :
					if "minimap_active" in action:
						minimapacl(320,251)
						actualiser()
						fermercarte()
				if event.key == K_LEFT :
					if x1>80:
						arreter=False
						screen.blit(walkleft[walkCount//3],(x1,y1))
						x1=x1-10
						walkCount=walkCount+1
						Orientation = PDG
				if event.key == K_RIGHT :
					if x1<209 or y1<200:
						arreter=False
						screen.blit(walkright[walkCount//3],(x1,y1))
						x1=x1+10
						walkCount=walkCount+1
						Orientation = PDD
				if event.key == K_UP :
					if y1>100:
						arreter=False
						y1=y1-10
						screen.blit(Orientation,(x1,y1))
				if event.key == K_DOWN:
					if x1<209 or y1<200:
						arreter=False
						y1=y1+10
						screen.blit(Orientation,(x1,y1))
				if x1>685:
					salle9(Orientation,entree,valide,objet,vie,Sco)
				if y1>521 :
					salle7(Orientation,sortie,valide,objet,vie,Sco)
			if walkCount >=10 :
				walkCount =0
			if arreter==True :
				screen.blit(Orientation,(x1,y1))
			Interface(valide,objet,vie,Sco)
			actualiser()

def salle9(Orientation,position,valide,objet,vie,Sco):
	x1=0
	y1=80
	FIN = False
	walkCount=0
	t=0
	if not 9 in visiter :
		visiter.append(9)
	bouledefeu = []
	bouledefeuS = []
	pygame.time.set_timer(USEREVENT, 3000)
	pygame.time.set_timer(USEREVENT+1, 3500)
	bouledefeu.append(projectile(80,-50,2))
	bouledefeu.append(projectile(400,-50,2))
	bouledefeuS.append(projectileS(380,600,-2))
	bouledefeuS.append(projectileS(500,600,-2))
	bouledefeuS.append(projectileS(150,600,-2))
	bouledefeu.append(projectile(240,-50,2))
	bouledefeuS.append(projectileS(640,600,-2))
	bouledefeu.append(projectile(550,-50,2))
	while not FIN:
		t=t+1
		tirage=randint(1,10)
		clock.tick(20)
		arreter=True
		screen.blit(map09,(0,0))
		for event in pygame.event.get():
			if event.type == USEREVENT:
				bouledefeu.append(projectile(80,-50,2))
				bouledefeu.append(projectile(400,-50,2))
				bouledefeuS.append(projectileS(380,600,-2))
				bouledefeuS.append(projectileS(500,600,-2))
			if event.type == USEREVENT+1:
				bouledefeuS.append(projectileS(150,600,-2))
				bouledefeu.append(projectile(240,-50,2))
				bouledefeuS.append(projectileS(640,600,-2))
				bouledefeu.append(projectile(550,-50,2))
			if tirage==2 and t>20:
				bouledefeu.append(projectile(240,-50,2))
				bouledefeuS.append(projectileS(640,600,-2))
				bouledefeu.append(projectile(550,-50,2))
				t=0
			if tirage==3 and t>20:
				bouledefeu.append(projectile(80,-50,2))
				bouledefeu.append(projectile(400,-50,2))
				bouledefeuS.append(projectileS(380,600,-2))
				t=0
			if event.type == pygame.QUIT:
				END()
			if event.type == KEYDOWN:
				if event.key == K_q :
					salle10(Orientation,entree,valide,objet,vie,Sco)
				if event.key == K_a :
					if "minimap_active" in action:
						minimapacl(370,250)
						actualiser()
						fermercarte()
				if event.key == K_LEFT :
					if 340>x1>240 or ((x1<280 or x1>360) and (y1<120 or y1>270)) or x1>360 or (x1>240 and 170<y1<210) :
						arreter=False
						screen.blit(walkleft[walkCount//3],(x1,y1))
						x1=x1-10
						walkCount=walkCount+1
						Orientation = PDG
				if event.key == K_RIGHT :
					if x1<280 or  (170<y1<210 and x1<430) or (x1>300 and(y1<170 or y1>210)):
						arreter=False
						screen.blit(walkright[walkCount//3],(x1,y1))
						x1=x1+10
						walkCount=walkCount+1
						Orientation = PDD
				if event.key == K_UP :
					if 260>y1>60 or y1>260 or ((220<x1<290 or 340<x1<450) and y1>60) or (x1>450 and (210<y1<60 or 500<y1<240)) :
						arreter=False
						y1=y1-10
						screen.blit(Orientation,(x1,y1))
				if event.key == K_DOWN:
					if 250<y1<320 or y1<120 or ((220<x1<290 or 340<x1<450) and y1<320) or (x1>450 and (210<y1<60 or 320<y1<240)) :
						arreter=False
						y1=y1+10
						screen.blit(Orientation,(x1,y1))
		for test in bouledefeuS:
			test.draw(screen,-2)
			if y1-20<test.y<y1+20 and x1-10<test.x<x1+30:
				x1=0
				y1=80
				vie=vie-1
				doul1.play()
			elif test.y < 700 and test.y > -100:
				test.y = test.y- 3
			else:
				bouledefeuS.pop(bouledefeuS.index(test))
		for test in bouledefeu:
			test.draw(screen,2)
			if y1-20<test.y<y1+20 and x1-30<test.x<x1+30:
				x1=0
				y1=80
				vie=vie-1
				doul1.play()
			elif test.y < 700 and test.y > -100:
				test.y += 3
			else:
				bouledefeu.pop(bouledefeu.index(test))
		if walkCount >=10 :
			walkCount =0
		if arreter==True :
			screen.blit(Orientation,(x1,y1))
		Interface(valide,objet,vie,Sco)
		actualiser()
		if vie==0:
			mort(Sco)
		if x1>685:
			salle10(Orientation,entree,valide,objet,vie,Sco)
		if x1<0 :
			salle8(Orientation,sortie,valide,objet,vie,Sco)

def salle10(Orientation,position,valide,objet,vie,Sco):
	if position==entree:
		x1=7
		y1=240
	else:
		x1=600
		y1=245
	if not 10 in visiter :
		visiter.append(10)
	if not "combat boss 1" in action:
		discussionONE(x1,y1,vie,Sco)
		vie=combatbossONE(vie,Sco)
		action.append("combat boss 1")
	walkCount=0
	FIN = False
	while not FIN :
		arreter=True
		clock.tick(20)
		screen.blit(map10,(0,0))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				END()
			if event.type == KEYDOWN:
				if event.key == K_a :
					if "minimap_active" in action:
						minimapacl(418,250)
						actualiser()
						fermercarte()
				if event.key == K_LEFT :
					if (x1>50 and y1>80) or 220<y1<260:
						arreter=False
						screen.blit(walkleft[walkCount//3],(x1,y1))
						x1=x1-10
						walkCount=walkCount+1
						Orientation = PDG
				if event.key == K_RIGHT :
					if x1<600 or y1<500:
						arreter=False
						screen.blit(walkright[walkCount//3],(x1,y1))
						x1=x1+10
						walkCount=walkCount+1
						Orientation = PDD
				if event.key == K_UP :
					if (y1>90 and x1>30) or 275<x1<315:
						arreter=False
						y1=y1-10
						screen.blit(Orientation,(x1,y1))
				if event.key == K_DOWN :
					if y1<400 and x1>30:
						arreter=False
						y1=y1+10
						screen.blit(Orientation,(x1,y1))
		if walkCount >=10 :
			walkCount =0
		if arreter==True :
			screen.blit(Orientation,(x1,y1))
		if y1<0 :
			salle11(Orientation,entree,valide,objet,vie,Sco)
		if x1<0:
			salle9(Orientation,sortie,valide,objet,vie,Sco)
		Interface(valide,objet,vie,Sco)
		actualiser()

def salle11(Orientation,position,valide,objet,vie,Sco):
	walkCount=0
	x1,y1=290,460
	if not 11 in visiter :
		vie=libererKAI(x1,y1,vie,Sco)
		visiter.append(11)
	FIN = False
	while not FIN :
		arreter=True
		clock.tick(20)
		screen.blit(map11,(0,0))
		screen.blit(gentil3G,(530,140))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				END()
			if event.type == KEYDOWN:
				if event.key == K_a :
					if "minimap_active" in action:
						minimapacl(418,250)
						actualiser()
						fermercarte()
				if event.key == K_LEFT :
					if x1>45:
						arreter=False
						screen.blit(walkleft[walkCount//3],(x1,y1))
						x1=x1-10
						walkCount=walkCount+1
						Orientation = PDG
				if event.key == K_RIGHT :
					if x1<580:
						arreter=False
						screen.blit(walkright[walkCount//3],(x1,y1))
						x1=x1+10
						walkCount=walkCount+1
						Orientation = PDD
				if event.key == K_UP :
					if y1>250:
						arreter=False
						y1=y1-10
						screen.blit(Orientation,(x1,y1))
				if event.key == K_DOWN :
					if y1<395 or 320>x1>285:
						arreter=False
						y1=y1+10
						screen.blit(Orientation,(x1,y1))
				if event.key == K_SPACE :
					if 50<x1<200 and 200<y1<500:
						valide=True
						objet=clef
						action.append("clefRoyale")
					if x1>500 and y1<280:
						 if "clefRoyale" in action:
						 		if not "clefrecupKAI" in action:
						 			mauvaiseclef(x1,y1,vie,Sco)
						 if "clefrecupKAI" in action:
						 	KAIliberer(x1,y1,vie,Sco)
						 	Sco=Sco+1
						 	valide=False
						 salle7(Orientation,sortie,valide,objet,vie,Sco)
		if walkCount >=10 :
			walkCount =0
		if arreter==True :
			screen.blit(Orientation,(x1,y1))
		if y1>521 :
			salle10(Orientation,sortie,valide,objet,vie,Sco)
		if not "clefRoyale" in action :
			screen.blit(clef,(100,340))
		if not "libererKAI" in action :
			screen.blit(prisonporte,(520,200))
		Interface(valide,objet,vie,Sco)
		actualiser()

def salle12(Orientation,position,valide,objet,vie,Sco):
	walkCount=0
	if not 12 in visiter :
		visiter.append(12)
	if position==entree:
		x1,y1=10,120
	elif position==sortie:
		x1,y1=560,460
	FIN = False
	while not FIN :
		arreter=True
		clock.tick(20)
		screen.blit(map12,(0,0))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				END()
			if event.type == KEYDOWN:
				if event.key == K_a :
					if "minimap_active" in action:
						minimapacl(370,290)
						actualiser()
						fermercarte()
				if event.key == K_LEFT :
					if y1<225 or (x1>520 and y1>120):
						arreter=False
						screen.blit(walkleft[walkCount//3],(x1,y1))
						x1=x1-10
						walkCount=walkCount+1
						Orientation = PDG
				if event.key == K_RIGHT :
					if x1<580:
						arreter=False
						screen.blit(walkright[walkCount//3],(x1,y1))
						x1=x1+10
						walkCount=walkCount+1
						Orientation = PDD
				if event.key == K_UP :
					if y1>110:
						arreter=False
						y1=y1-10
						screen.blit(Orientation,(x1,y1))
				if event.key == K_DOWN :
					if y1<190 or 500<x1<600:
						arreter=False
						y1=y1+10
						screen.blit(Orientation,(x1,y1))
		if walkCount >=10 :
			walkCount =0
		if arreter==True :
			screen.blit(Orientation,(x1,y1))
		if y1>521 :
			salle13(Orientation,entree,valide,objet,vie,Sco)
		if x1<0:
			salle7(Orientation,sortie1,valide,objet,vie,Sco)
		Interface(valide,objet,vie,Sco)
		actualiser()

def salle13(Orientation,position,valide,objet,vie,Sco):
	walkCount=0
	if not 13 in visiter :
		visiter.append(13)
	if position==entree:
		x1,y1=100,100
	elif position== sortie1:
		x1,y1=10,150
	elif position==sortie:
		x1,y1=600,150
	FIN = False
	while not FIN :
		arreter=True
		clock.tick(20)
		screen.blit(map13,(0,0))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				END()
			if event.type == KEYDOWN:
				if event.key == K_a :
					if "minimap_active" in action:
						minimapacl(370,340)
						actualiser()
						fermercarte()
				if event.key == K_LEFT :
					if (x1>35 and y1>70) or 120<y1<180:
						arreter=False
						screen.blit(walkleft[walkCount//3],(x1,y1))
						x1=x1-10
						walkCount=walkCount+1
						Orientation = PDG
				if event.key == K_RIGHT :
					if (x1<570 and y1>70) or 120<y1<180:
						arreter=False
						screen.blit(walkright[walkCount//3],(x1,y1))
						x1=x1+10
						walkCount=walkCount+1
						Orientation = PDD
				if event.key == K_UP :
					if (y1>90 and 30<x1<590) or 80<x1<120:
						arreter=False
						y1=y1-10
						screen.blit(Orientation,(x1,y1))
				if event.key == K_DOWN :
					if (y1<325 and 30<x1<590):
						arreter=False
						y1=y1+10
						screen.blit(Orientation,(x1,y1))
		if walkCount >=10 :
			walkCount =0
		if arreter==True :
			screen.blit(Orientation,(x1,y1))
		if y1<0 :
			salle12(Orientation,sortie,valide,objet,vie,Sco)
		if x1<0:
			salle14(Orientation,entree,valide,objet,vie,Sco)
		if x1>685:
			salle15(Orientation,entree,valide,objet,vie,Sco)
		Interface(valide,objet,vie,Sco)
		actualiser()

def salle14(Orientation,position,valide,objet,vie,Sco):
	walkCount=0
	x1,y1=600,200
	if not 14 in visiter :
		revelation(600,200,vie,Sco)
		visiter.append(14)
	FIN = False
	while not FIN :
		arreter=True
		clock.tick(20)
		screen.blit(map14,(0,0))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				END()
			if event.type == KEYDOWN:
				if event.key == K_a :
					if "minimap_active" in action:
						minimapacl(320,340)
						actualiser()
						fermercarte()
				if event.key == K_LEFT :
					if x1>160:
						arreter=False
						screen.blit(walkleft[walkCount//3],(x1,y1))
						x1=x1-10
						walkCount=walkCount+1
						Orientation = PDG
				if event.key == K_RIGHT :
					if x1<575 or 180<y1<225:
						arreter=False
						screen.blit(walkright[walkCount//3],(x1,y1))
						x1=x1+10
						walkCount=walkCount+1
						Orientation = PDD
				if event.key == K_UP :
					if y1>90 and x1<590:
						arreter=False
						y1=y1-10
						screen.blit(Orientation,(x1,y1))
				if event.key == K_DOWN :
					if y1<350 and x1<590:
						arreter=False
						y1=y1+10
						screen.blit(Orientation,(x1,y1))
		if walkCount >=10 :
			walkCount =0
		if arreter==True :
			screen.blit(Orientation,(x1,y1))
		if x1>685:
			salle13(Orientation,sortie1,valide,objet,vie,Sco)
		Interface(valide,objet,vie,Sco)
		actualiser()

def salle15(Orientation,position,valide,objet,vie,Sco):
	enigme=[]
	walkCount=0
	violetactive=False
	bleuactive=False
	grisactive=False
	jauneactive=False
	if not 15 in visiter :
		visiter.append(15)
	if position==entree:
		x1,y1=10,290
	elif position==sortie1:
		x1,y1=300,100
	elif position==sortie:
		x1,y1=600,290
	FIN = False
	while not FIN :
		arreter=True
		clock.tick(20)
		screen.blit(map15,(0,0))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				END()
			if event.type == KEYDOWN:
				if event.key == K_a :
					if "minimap_active" in action:
						minimapacl(420,330)
						actualiser()
						fermercarte()
				if event.key == K_LEFT :
					if x1>40 or 270<y1<300:
						arreter=False
						screen.blit(walkleft[walkCount//3],(x1,y1))
						x1=x1-10
						walkCount=walkCount+1
						Orientation = PDG
				if event.key == K_RIGHT :
					if x1<575 or 240<y1<300:
						arreter=False
						screen.blit(walkright[walkCount//3],(x1,y1))
						x1=x1+10
						walkCount=walkCount+1
						Orientation = PDD
				if event.key == K_UP :
					if y1>150 and 25<x1<590:
						arreter=False
						y1=y1-10
						screen.blit(Orientation,(x1,y1))
				if event.key == K_DOWN :
					if y1<410 and 25<x1<590:
						arreter=False
						y1=y1+10
						screen.blit(Orientation,(x1,y1))
				if event.key == K_SPACE and y1<280:
					if 80<x1<160:
						if not 3 in enigme:
							enigme.append(3)
							violetactive=True
							print("violet")
					if 200<x1<280 :
						if not 1 in enigme:
							enigme.append(1)
							grisactive=True
							print("gris")
					if 400<x1<480:
						if not 2 in enigme:
							enigme.append(2)
							bleuactive=True
							print("bleu")
					if 520<x1<600:
						if not 4 in enigme:
							enigme.append(4)
							jauneactive=True
							print("jaune")
		if jauneactive==True and grisactive==True and violetactive==True and bleuactive==True :
			print(enigme)
			if enigme==[1,2,3,4]:
				salle16(Orientation,sortie,valide,objet,vie,Sco)
			else:
				violetactive=False
				bleuactive=False
				grisactive=False
				jauneactive=False
				enigme=[]
		if walkCount >=10 :
			walkCount =0
		if arreter==True :
			screen.blit(Orientation,(x1,y1))
		if x1>685 :
			salle17(Orientation,entree,valide,objet,vie,Sco)
		if x1<0:
			salle13(Orientation,sortie,valide,objet,vie,Sco)
		Interface(valide,objet,vie,Sco)
		actualiser()

def salle16(Orientation,position,valide,objet,vie,Sco):
	walkCount=0
	if not 16 in visiter :
		visiter.append(16)
	x1,y1=320,230
	FIN = False
	while not FIN :
		arreter=True
		clock.tick(20)
		screen.blit(map16,(0,0))
		if not "recupenigme" in action:
			screen.blit(clef,(120,230))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				END()
			if event.type == KEYDOWN:
				if event.key == K_a :
					if "minimap_active" in action:
						minimapacl(420,290)
						actualiser()
						fermercarte()
				if event.key == K_LEFT :
					if x1>70:
						arreter=False
						screen.blit(walkleft[walkCount//3],(x1,y1))
						x1=x1-10
						walkCount=walkCount+1
						Orientation = PDG
				if event.key == K_RIGHT :
					if x1<350:
						arreter=False
						screen.blit(walkright[walkCount//3],(x1,y1))
						x1=x1+10
						walkCount=walkCount+1
						Orientation = PDD
				if event.key == K_UP :
					if y1>180:
						arreter=False
						y1=y1-10
						screen.blit(Orientation,(x1,y1))
				if event.key == K_DOWN :
					if y1<240:
						arreter=False
						y1=y1+10
						screen.blit(Orientation,(x1,y1))
				if event.key== K_SPACE:
					if x1>320:
						salle15(Orientation,sortie1,valide,objet,vie,Sco)
					if x1<140 :
						action.append("recupenigme")
						valide=True
						objet=clef
		if walkCount >=10 :
			walkCount =0
		if arreter==True :
			screen.blit(Orientation,(x1,y1))
		Interface(valide,objet,vie,Sco)
		actualiser()


def salle17(Orientation,position,valide,objet,vie,Sco):
	walkCount=0
	if position == entree:
		x1,y1=10,200
	elif position == sortie1:
		x1,y1=600,200
	else :
		x1,y1=320,10
	if not 17 in visiter :
		visiter.append(17)
	FIN = False
	while not FIN :
		arreter=True
		clock.tick(20)
		screen.blit(map17,(0,0))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				END()
			if event.type == KEYDOWN:
				if event.key == K_a :
					if "minimap_active" in action:
						minimapacl(470,340)
						actualiser()
						fermercarte()
				if event.key == K_LEFT :
					if (x1>40 and y1>60) or 170<y1<220:
						arreter=False
						screen.blit(walkleft[walkCount//3],(x1,y1))
						x1=x1-10
						walkCount=walkCount+1
						Orientation = PDG
				if event.key == K_RIGHT :
					if (x1<580 and y1>60) or 170<y1<220:
						arreter=False
						screen.blit(walkright[walkCount//3],(x1,y1))
						x1=x1+10
						walkCount=walkCount+1
						Orientation = PDD
				if event.key == K_UP :
					if (y1>80 and 15<x1<600) or 280<x1<350:
						arreter=False
						y1=y1-10
						screen.blit(Orientation,(x1,y1))
				if event.key == K_DOWN :
					if (y1<400 and 15<x1<600):
						arreter=False
						y1=y1+10
						screen.blit(Orientation,(x1,y1))
		if walkCount >=10 :
			walkCount =0
		if arreter==True :
			screen.blit(Orientation,(x1,y1))
		if x1>685 :
			salle18(Orientation,entree,valide,objet,vie,Sco)
		if x1<0 :
			salle15(Orientation,sortie,valide,objet,vie,Sco)
		if y1<0 :
			salle19(Orientation,entree,valide,objet,vie,Sco)
		Interface(valide,objet,vie,Sco)
		actualiser()



def salle18(Orientation,position,valide,objet,vie,Sco):
	walkCount=0
	x1,y1=10,100
	if not 18 in visiter :
		visiter.append(18)
	FIN = False
	while not FIN :
		arreter=True
		clock.tick(20)
		screen.blit(map18,(0,0))
		if not "libererMystic" in action:
			screen.blit(prisonporte,(600,320))
			screen.blit(gentil4D,(200,400))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				END()
			if event.type == KEYDOWN:
				if event.key == K_a :
					if "minimap_active" in action:
						minimapacl(520,340)
						actualiser()
						fermercarte()
				if event.key == K_LEFT :
					if y1<150 or x1>560:
						arreter=False
						screen.blit(walkleft[walkCount//3],(x1,y1))
						x1=x1-10
						walkCount=walkCount+1
						Orientation = PDG
				if event.key == K_RIGHT :
					if x1<600:
						arreter=False
						screen.blit(walkright[walkCount//3],(x1,y1))
						x1=x1+10
						walkCount=walkCount+1
						Orientation = PDD
				if event.key == K_UP :
					if y1>70:
						arreter=False
						y1=y1-10
						screen.blit(Orientation,(x1,y1))
				if event.key == K_DOWN :
					if y1<140 or (x1>560 and y1<200):
						arreter=False
						y1=y1+10
						screen.blit(Orientation,(x1,y1))
				if event.key == K_SPACE:
					if 300<x1<500 and 70<y1<250:
						action.append("ramasserclef18")
						valide=True
						objet=clef
					if "ramasserclef18" in action:
						if x1>560 and y1>140:
							action.append("libererMystic")
							MysticPerdu(x1,y1,vie,Sco)
							Sco=Sco +1
							valide=False
		if not "ramasserclef18" in action:
			screen.blit(clef,(400,150))
		if walkCount >=10 :
			walkCount =0
		if arreter==True :
			screen.blit(Orientation,(x1,y1))
		if x1<0 :
			salle17(Orientation,sortie1,valide,objet,vie,Sco)
		Interface(valide,objet,vie,Sco)
		actualiser()


def salle19(Orientation,position,valide,objet,vie,Sco):
	walkCount=0
	if position == entree:
		x1,y1=320,460
	else :
		x1,y1=320,0
	if not 19 in visiter :
		combatbossdeux(x1,y1,vie,Sco)
		visiter.append(19)
	FIN = False
	while not FIN :
		arreter=True
		clock.tick(20)
		screen.blit(map19,(0,0))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				END()
			if event.type == KEYDOWN:
				if event.key == K_a :
					if "minimap_active" in action:
						minimapacl(470,290)
						actualiser()
						fermercarte()
				if event.key == K_LEFT :
					if (x1>40 and 65<y1<405):
						arreter=False
						screen.blit(walkleft[walkCount//3],(x1,y1))
						x1=x1-10
						walkCount=walkCount+1
						Orientation = PDG
				if event.key == K_RIGHT :
					if (x1<600 and 65<y1<405):
						arreter=False
						screen.blit(walkright[walkCount//3],(x1,y1))
						x1=x1+10
						walkCount=walkCount+1
						Orientation = PDD
				if event.key == K_UP :
					if 270<x1<360 or (80<y1 and x1>40):
						arreter=False
						y1=y1-10
						screen.blit(Orientation,(x1,y1))
				if event.key == K_DOWN :
					if 270<x1<360 or (y1<400 and x1>40):
						arreter=False
						y1=y1+10
						screen.blit(Orientation,(x1,y1))
		if walkCount >=10 :
			walkCount =0
		if arreter==True :
			screen.blit(Orientation,(x1,y1))
		if y1<0 :
			salle20(Orientation,entree,valide,objet,vie,Sco)
		if y1>521:
			salle17(Orientation,sortie,valide,objet,vie,Sco)
		Interface(valide,objet,vie,Sco)
		actualiser()


def salle20(Orientation,position,valide,objet,vie,Sco):
	walkCount=0
	x1,y1=320,460
	if not 20 in visiter:
		visiter.append(20)
	FIN = False
	while not FIN :
		arreter=True
		clock.tick(20)
		screen.blit(map20,(0,0))
		if not "clefrecupKAI" in action:
			screen.blit(clef,(320,350))
		if not "findujeu" in action:
			screen.blit(oeuf,(320,150))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				END()
			if event.type == KEYDOWN:
				if event.key == K_a:
					if "minimap_active" in action:
						minimapacl(470,240)
						actualiser()
						fermercarte()
				if event.key == K_LEFT :
					if (x1>40 and 65<y1<405):
						arreter=False
						screen.blit(walkleft[walkCount//3],(x1,y1))
						x1=x1-10
						walkCount=walkCount+1
						Orientation = PDG
				if event.key == K_RIGHT :
					if (x1<600 and 65<y1<405):
						arreter=False
						screen.blit(walkright[walkCount//3],(x1,y1))
						x1=x1+10
						walkCount=walkCount+1
						Orientation = PDD
				if event.key == K_UP :
					if 80<y1:
						arreter=False
						y1=y1-10
						screen.blit(Orientation,(x1,y1))
				if event.key == K_DOWN :
					if 260<x1<360 or (y1<400 and x1>40):
						arreter=False
						y1=y1+10
						screen.blit(Orientation,(x1,y1))
				if event.key == K_SPACE:
					if 280<x1<400 and 300<y1<400:
						chaine = "La clef de la cellule de KAI"
						locuteur = "VOUS"
						dialogue(chaine,locuteur)
						actualiser()
						attenteclic()
						action.append("clefrecupKAI")
						valide=True
						objet=clef
					if 280<x1<400 and 50<y1<250:
						screen.blit(scenario4,(0,0))
						actualiser()
						attenteclic()
						action.append("findujeu")
		if walkCount >=10 :
			walkCount =0
		if arreter==True :
			screen.blit(Orientation,(x1,y1))
		if y1>521:
			salle19(Orientation,sortie,valide,objet,vie,Sco)
		Interface(valide,objet,vie,Sco)
		actualiser()
##################################################################################################################################################


#                                                          debut du programme brut                                                               #
##################################################################################################################################################

clock = pygame.time.Clock()

sexe = MENU()					#Choix du personnage
if sexe == 1 :
	PDD = P1D					#attribution des variables de base
	PDG = P1G
	walkleft = walkleftH
	walkright = walkrightH
elif sexe == 2 :
	PDD = P2D
	PDG = P2G
	walkleft = walkleftF
	walkright = walkrightF

valide = False
objet = 0


tuto()
vie = 5
intro_Scenario()
pygame.event.clear()
pts_scenario(scenario1)
attenteclic()

Orientation = PDD
Orientation_rect = Orientation.get_rect()
global x1
global y1
x1= 0
y1= 200
walkCount=0
arreter=True
Sco=0
Orientation_rect = ((x1,y1))
sousGAMEPLAY(Orientation,map01,x1,y1,vie)
pygame.event.clear()
FIN = False
while not FIN :
	arreter=True
	clock.tick(20)
	screen.blit(map01,(0,0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			END()
		if event.type == KEYDOWN:
			if event.key == K_LEFT :
				if x1>170 :
					arreter=False
					screen.blit(walkleft[walkCount//3],(x1,y1))
					x1=x1-10
					walkCount=walkCount+1
					Orientation = PDG
			if event.key == K_RIGHT :
				if x1<340 or (150<y1<250):
					arreter=False
					screen.blit(walkright[walkCount//3],(x1,y1))
					x1=x1+10
					walkCount=walkCount+1
					Orientation = PDD
			if event.key == K_UP :
				if (y1 > 110 and x1 < 350) or (y1>160):
					arreter=False
					y1=y1-10
					screen.blit(Orientation,(x1,y1))
			if event.key == K_DOWN :
				if (y1 < 280 and x1 < 350) or (y1<240):
					arreter=False
					y1=y1+10
					screen.blit(Orientation,(x1,y1))
	if walkCount >=10 :
		walkCount =0
	if arreter==True :
		screen.blit(Orientation,(x1,y1))
	Interface(valide,objet,vie,Sco)
	actualiser()
	if x1 > 685 :
		x1 = 0
		FIN = True
FIN = False
while not FIN :
	arreter=True
	clock.tick(20)
	screen.blit(map02,(0,0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			END()
		if event.type == KEYDOWN:
			if event.key == K_LEFT :
				if x1<390 or y1>190 :
					arreter=False
					screen.blit(walkleft[walkCount//3],(x1,y1))
					x1=x1-10
					walkCount=walkCount+1
					Orientation = PDG
			if event.key == K_RIGHT :
				if  230>y1>190 or (x1<100 and 140<y1<240):
					arreter=False
					screen.blit(walkright[walkCount//3],(x1,y1))
					x1=x1+10
					walkCount=walkCount+1
					Orientation = PDD
			if event.key == K_UP :
				if (y1 > 220) or (y1>160 and x1<80) or (360<x1<410):
					arreter=False
					y1=y1-10
					screen.blit(Orientation,(x1,y1))
			if event.key == K_DOWN :
				if (y1 > 260) or (y1<240 and x1<80) or (380<x1<430 and y1<230):
					arreter=False
					y1=y1+10
					screen.blit(Orientation,(x1,y1))
	if walkCount >=10 :
		walkCount =0
	if arreter==True :
		screen.blit(Orientation,(x1,y1))
	Interface(valide,objet,vie,Sco)
	actualiser()
	if x1 > 685 :
		CHmap = map03
		x1= 0
		y1 = 370
		FIN = True
	if y1 < 60 :
		CHmap = mp_prison
		x1= 30
		y1 = 420
		doul1.play()
		vie =4
		FIN = True
IntroGAMEPLAY(Orientation,CHmap,x1,y1,vie)
salle3(Orientation,entree,valide,objet,vie,Sco)




attenteclic()
END()
