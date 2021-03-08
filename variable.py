import time, sys, pygame
from random import *
from pygame.locals import *
pygame.init()

####################################################################################################################################################################

#variable des maps de jeux
mp_prison = pygame.image.load("map/Map_prison.png")
mp_couloirPr = pygame.image.load("map/escalier prison.png")
mp_rue = pygame.image.load("map/rue.png")
Centrale = pygame.image.load("map/Centre.png")
map01 = pygame.image.load("map/Map01.png")
map02 = pygame.image.load("map/Map02.png")
map03 = pygame.image.load("map/MAP03.png")
map04 = pygame.image.load("map/map04.png")
map05 = pygame.image.load("map/map05.png")
map06 = pygame.image.load("map/map06.png")
map07 = pygame.image.load("map/map07.png")
map08 = pygame.image.load("map/map08.png")
map09 = pygame.image.load("map/map09.png")
map10 = pygame.image.load("map/map10.png")
map11 = pygame.image.load("map/map11.png")
map12 = pygame.image.load("map/map12.png")
map13 = pygame.image.load("map/map13.png")
map14 = pygame.image.load("map/map14.png")
map15 = pygame.image.load("map/map15.png")
map16 = pygame.image.load("map/map16.png")
map17 = pygame.image.load("map/map17.png")
map18 = pygame.image.load("map/map18.png")
map19 = pygame.image.load("map/map19.png")
map20 = pygame.image.load("map/map20.png")
#variable des maps de transition ou de menu
t3 = pygame.image.load("diapo/trans3.png")
t1 = pygame.image.load("diapo/trans1.png")
t2 = pygame.image.load("diapo/trans3.png")
t1txt = pygame.image.load("diapo/t1.png")
t2txt = pygame.image.load("diapo/t2.png")
ttuto = pygame.image.load("diapo/Tuto.png")
scenario1 = pygame.image.load("diapo/Pts_Scenario1.png")
scenario2 = pygame.image.load("diapo/Pts_Scenario2.png")
scenario3 = pygame.image.load("diapo/Pts_Scenario3.png")
scenario4 = pygame.image.load("diapo/Pts_Scenario4.png")
select = pygame.image.load("anim/selection.png")
imgCombat = pygame.image.load("diapo/COMBAT.png")
tutoC = pygame.image.load("diapo/tuto combat.png")
minimap = pygame.image.load("map/mini map.png")
brouille = pygame.image.load("map/brouillard.png")
point = pygame.image.load("map/point.png")
ecran_mort = pygame.image.load("anim/ecran de mort.png")

# variables des joueurs
P1D = pygame.image.load("perso/perso 1/1.D.png")
P1G = pygame.image.load("perso/perso 1/1.G.png")
P2D = pygame.image.load("perso/perso 2/2.D.png")
P2G = pygame.image.load("perso/perso 2/2.G.png")
walkrightH = [pygame.image.load("perso/perso 1/1.D1.png"), pygame.image.load("perso/perso 1/1.D2.png"), pygame.image.load("perso/perso 1/1.D3.png"), pygame.image.load("perso/perso 1/1.D4.png")]
walkleftH = [pygame.image.load("perso/perso 1/1.G1.png"), pygame.image.load("perso/perso 1/1.G2.png"), pygame.image.load("perso/perso 1/1.G3.png"), pygame.image.load("perso/perso 1/1.G4.png")]
walkrightF = [pygame.image.load("perso/perso 2/2.D1.png"), pygame.image.load("perso/perso 2/2.D2.png"), pygame.image.load("perso/perso 2/2.D3.png"), pygame.image.load("perso/perso 2/2.D4.png")]
walkleftF = [pygame.image.load("perso/perso 2/2.G1.png"), pygame.image.load("perso/perso 2/2.G2.png"), pygame.image.load("perso/perso 2/2.G3.png"), pygame.image.load("perso/perso 2/2.G4.png")]

coursierG = pygame.image.load("perso/postier/pos G.png")
coursierD = pygame.image.load("perso/postier/pos D.png")
CwalkR = [pygame.image.load("perso/postier/pos D1.png"),pygame.image.load("perso/postier/pos D2.png"),pygame.image.load("perso/postier/pos D3.png"),pygame.image.load("perso/postier/pos D4.png")]
CwalkL = [pygame.image.load("perso/postier/pos G1.png"),pygame.image.load("perso/postier/pos G2.png"),pygame.image.load("perso/postier/pos G3.png"),pygame.image.load("perso/postier/pos G4.png")]

BADD = pygame.image.load("perso/BADGAMENON/D.png")
BADG = pygame.image.load("perso/BADGAMENON/G.png")
walkrightB = [pygame.image.load("perso/BADGAMENON/D1.png"),pygame.image.load("perso/BADGAMENON/D2.png"),pygame.image.load("perso/BADGAMENON/D3.png"),pygame.image.load("perso/BADGAMENON/D4.png")]
walkleftB = [pygame.image.load("perso/BADGAMENON/G1.png"),pygame.image.load("perso/BADGAMENON/G2.png"),pygame.image.load("perso/BADGAMENON/G3.png"),pygame.image.load("perso/BADGAMENON/G4.png")]


MECH1D = pygame.image.load("perso/mechant 1/D.png")
MECH1G = pygame.image.load("perso/mechant 1/G.png")
MECH2D = pygame.image.load("perso/mechant 2/D.png")
MECH2G = pygame.image.load("perso/mechant 2/G.png")
walkrightMA = [pygame.image.load("perso/mechant 1/D.1.png"),pygame.image.load("perso/mechant 1/D.2.png"),pygame.image.load("perso/mechant 1/D.3.png"),pygame.image.load("perso/mechant 1/D.4.png")]
walkleftMA = [pygame.image.load("perso/mechant 1/G.1.png"),pygame.image.load("perso/mechant 1/G.2.png"),pygame.image.load("perso/mechant 1/G.3.png"),pygame.image.load("perso/mechant 1/G.4.png")]
walkrightMB = [pygame.image.load("perso/mechant 2/D.1.png"),pygame.image.load("perso/mechant 2/D.2.png"),pygame.image.load("perso/mechant 2/D.3.png"),pygame.image.load("perso/mechant 2/D.4.png")]
walkleftMB = [pygame.image.load("perso/mechant 2/G.1.png"),pygame.image.load("perso/mechant 2/G.2.png"),pygame.image.load("perso/mechant 2/G.3.png"),pygame.image.load("perso/mechant 2/G.4.png")]


gentil1D = pygame.image.load("perso/gentil 1/D.png")
gentil1G = pygame.image.load("perso/gentil 1/G.png")
walkrightA = [pygame.image.load("perso/gentil 1/D.1.png"),pygame.image.load("perso/gentil 1/D.2.png"),pygame.image.load("perso/gentil 1/D.3.png"),pygame.image.load("perso/gentil 1/D.4.png")]
walkleftA = [pygame.image.load("perso/gentil 1/G.1.png"),pygame.image.load("perso/gentil 1/G.2.png"),pygame.image.load("perso/gentil 1/G.3.png"),pygame.image.load("perso/gentil 1/G.4.png")]

gentil2D = pygame.image.load("perso/gentil 2/D.png")
gentil2G = pygame.image.load("perso/gentil 2/G.png")
walkrightAB = [pygame.image.load("perso/gentil 2/D.1.png"),pygame.image.load("perso/gentil 2/D.2.png"),pygame.image.load("perso/gentil 2/D.3.png"),pygame.image.load("perso/gentil 2/D.4.png")]
walkleftAB = [pygame.image.load("perso/gentil 2/G.1.png"),pygame.image.load("perso/gentil 2/G.2.png"),pygame.image.load("perso/gentil 2/G.3.png"),pygame.image.load("perso/gentil 2/G.4.png")]

gentil3D = pygame.image.load("perso/gentil 3/D.png")
gentil3G = pygame.image.load("perso/gentil 3/G.png")
walkrightABC = [pygame.image.load("perso/gentil 3/D.1.png"),pygame.image.load("perso/gentil 3/D.2.png"),pygame.image.load("perso/gentil 3/D.3.png"),pygame.image.load("perso/gentil 3/D.4.png")]
walkleftABC = [pygame.image.load("perso/gentil 3/G.1.png"),pygame.image.load("perso/gentil 3/G.2.png"),pygame.image.load("perso/gentil 3/G.3.png"),pygame.image.load("perso/gentil 3/G.4.png")]

gentil4D = pygame.image.load("perso/gentil 4/D.png")
gentil4G = pygame.image.load("perso/gentil 4/G.png")

gentil5D = pygame.image.load("perso/gentil 5/D.png")
gentil5G = pygame.image.load("perso/gentil 5/G.png")
# variable des choix
entree = 1
sortie = 0
sortie1 = -1
sortie2 = -2
fen= pygame.image.load("diapo/choixFEN.png")
curseur= pygame.image.load("anim/selecteur.png")
choixarmant = pygame.image.load("anim/Prop_armant.png")
choixhache = pygame.image.load("anim/Prop_hache.png")
chbaston = pygame.image.load("anim/chbaston.png")
choixKAI = pygame.image.load("anim/choixKAI.png")
chMystic= pygame.image.load("anim/chMystic.png")
s0 = pygame.image.load("anim/score 0-5.png")
s1 = pygame.image.load("anim/score 1-5.png")
s2 = pygame.image.load("anim/score 2-5.png")
s3 = pygame.image.load("anim/score 3-5.png")
s4 = pygame.image.load("anim/score 4-5.png")
s5 = pygame.image.load("anim/score 5-5.png")



# variable de la fenetre et sa creation
screen_size = (685,521)
screen = pygame.display.set_mode (screen_size)
pygame.display.set_caption("SAVE THE DUNGEONS")
fondM = pygame.image.load("diapo/FondBASE.png")
fond2 = pygame.image.load("diapo/Fond.png")
screen_rect = screen.get_rect()
clock = pygame.time.Clock()
pygame.key.set_repeat(1,10)
minimap = pygame.image.load("map/mini map.png")


#variables des sons
swordson = pygame.mixer.Sound("sons/sword.wav")
sonMane = pygame.mixer.Sound("sons/Tmenu.wav")
sonTrans = pygame.mixer.Sound("sons/sonTrans.wav")
MSC1 = pygame.mixer.Sound("sons/MscEpic1.wav")
MSC2 = pygame.mixer.Sound("sons/MscEpic2.wav")
doul1= pygame.mixer.Sound("sons/doul1.wav")
sonmort = pygame.mixer.Sound("sons/game-over.wav")
sonbonus = pygame.mixer.Sound("sons/1-up.wav")
sonAilefeu = pygame.mixer.Sound("sons/FEU.wav")

#variables des animations de texte
police1 = pygame.font.Font("police/DIMIS.ttf", 70)
police2 = pygame.font.Font("police/Dark.ttf", 30)
police3 = pygame.font.Font("police/Formers.ttf",20)
rendu_texte1 = police1.render("SAVE The Dungeon", True, pygame.Color("white"))
rendu_texte2 = police2.render("Nothing will be forgotten", True, pygame.Color("red"))
text_rect1 = rendu_texte1.get_rect(midleft=(900, screen_rect.centery))
text_rect2 = rendu_texte2.get_rect(midleft=(900, screen_rect.centery))
BD = pygame.image.load("diapo/boite dialogue.png")
indication_espace = pygame.image.load("diapo/astucesEspace.png")




#variable objets
inv1 = pygame.image.load("items/inventaireETparchemin.png")
inventaire = pygame.image.load("items/inventaire.png")
parchemin = pygame.image.load("items/Parchemin.png")
item_carte = pygame.image.load("items/parchemin miniature.png")
coeur = pygame.image.load("items/coeur.png")
pioche = pygame.image.load("items/pioche.png")
pioche_rect = pioche.get_rect()
xp=60
yp=370
pioche_rect = ((xp,yp))
boostATK = pygame.image.load("items/miniepee.png")
boostATK_rect = boostATK.get_rect()
blfB= pygame.image.load("items/boule de feuB.png")
blfD= pygame.image.load("items/boule de feuD.png")
blfH= pygame.image.load("items/boule de feuH.png")
blfG= pygame.image.load("items/boule de feuG.png")
crane = pygame.image.load("items/Crane.png")
paneau = pygame.image.load("items/paneau.png")
palissade = pygame.image.load("items/palissade.png")
bonusATK = pygame.image.load("items/bonatck.png")
hache = pygame.image.load("items/hache.png")
hache_rect = hache.get_rect()
porte = pygame.image.load("items/porte verouille.png")
prisonporte = pygame.image.load("items/porte de prison.png")
clef = pygame.image.load("items/Key 2.png")
oeuf = pygame.image.load("items/easter eggs.png")



#variable visite/action
visiter=[]
action=[]
enigme=[]
####################################################################################################################################################################