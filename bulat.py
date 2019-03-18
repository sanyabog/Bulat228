
import pygame
from random import randint






pygame.init()
win=pygame.display.set_mode((1000,500))
pygame.display.set_caption("Bulat")

wingame=pygame.Surface((2000,500))

pygame.mouse.set_visible(False)

class Menu:
	def __init__(self,punkts=[120,140,'punkts',(255,0,0),(140,0,150),0]):
		self.punkts=punkts
	def drawmenu(self,holst,font,num_punkt):
		for i in self.punkts:
			if num_punkt==i[5]:
				holst.blit(font.render(i[2],1,i[4]),(i[0],i[1]))
			else:
				holst.blit(font.render(i[2],1,i[3]),(i[0],i[1]))
		holst.blit(font.render('max score: ',0,(125,200,0)),[50,50])
		holst.blit(font.render(str(maxscore),0,(125,200,0)),[70,90])
		holst.blit(font.render('max kills: ',0,(125,200,0)),[80,290])
		holst.blit(font.render(str(maxkills),0,(125,200,0)),[100,340])
		if score>-1:
			holst.blit(font.render('your score: '+ str(int(score)),0,(125,200,0)),[650,110])
			holst.blit(font.render('your kills: '+ str(kills),0,(125,200,0)),[650,310])
	def menu(self):
		global game, lives
		done=True
		
		pygame.key.set_repeat(500,400)
		punkt=0
		while done:
			wingame.blit(fon,(0,0))
			for e in pygame.event.get():
				if e.type==pygame.QUIT: done=False; game=False
				if e.type==pygame.KEYDOWN:
					if (e.key==pygame.K_UP or e.key==pygame.K_w) and punkt>0: punkt-=1
					elif (e.key==pygame.K_DOWN or e.key==pygame.K_s) and punkt<len(self.punkts)-1: punkt+=1
					if (e.key==pygame.K_SPACE):
						if punkt==0:
							done=False
							if lives<1: restart()
						if punkt==1:
							done=False
							game=False
						if punkt==2:
							done=False
							restart()
			gamemenu.drawmenu(wingame,score_font,punkt)
			win.blit(wingame,[0,0])
			pygame.display.update()



class warior():
	def __init__(self):
		
		self.x =1010
		self.y=randint(0,1)*50+250
		self.type=int((randint(-5,16)+fonspeed)%29/10)
		self.damage=(self.type)*10+10
		self.lives=(self.type)*10+10
		self.ydar=False

	def draw(self):
		wingame.blit(imagewar[self.type],(self.x,self.y))

	def update(self):
		global lives, x, y, fonspeed, kills,damage
		self.x-=fonspeed+3
		if insert(x,self.x,y,self.y,bam//15+1) and bam>0 and self.ydar==False: #при ударе
			self.lives-=damage
			self.ydar=True
			############################print (self.lives+self.type)
		elif insert(x,self.x,y,self.y,0.5) and pygame.mixer.Channel(1).get_busy()==0: #без удара
			lives-=self.damage
			pygame.mixer.Channel(1).play(pain)
		if bam==0:self.ydar=False

		if war.lives<1:
			kills+=1
			self.x=-200
		if self.x<-100:
			wariors.pop(wariors.index(war))








widht=100
height=110
Rkv=((widht/2)**2+(height/2)**2)
damage=10

g=10
speedx=10

clock=pygame.time.Clock()


pygame.font.init() #инициализируем шрифты
score_font=pygame.font.Font('fonts/ravie.ttf',32)

mfon=pygame.mixer.Sound('sounds/tatar.ogg')
pain=pygame.mixer.Sound('sounds/pain.ogg')
dam=pygame.mixer.Sound('sounds/dam.ogg')

bulat=pygame.transform.scale(pygame.image.load('picture/1.png'),(widht,height))
imagewar=[
	pygame.transform.scale(pygame.image.load('picture/easywar.png'),(widht,height)),
	pygame.transform.scale(pygame.image.load('picture/mediumwar.png'),(widht,height)),
	pygame.transform.scale(pygame.image.load('picture/hardwar.png'),(widht,height))]

fon=pygame.image.load('picture/fon.jpg').convert()


punkts=[
	(450,100,"Play",(255,0,255),(255,0,0),0),
	(450,200,"QUIT",(255,0,255),(255,0,0),1)]
gamemenu=Menu(punkts)


def restart():
	global fonspeed,fx,wariors,x,y,lives,jump,speedy,numjamp,bam,ydar,ramah,game, kills, score
	fonspeed=5
	fx=0
	wariors=[]
	x=30
	y=300
	lives=40
	jump=False
	speedy=0
	numjamp=0
	bam=0
	ydar=False
	ramah=0
	kills=0
	score=0
	pygame.key.set_repeat(100,1)

	pygame.mixer.Channel(0).play(mfon,-1)

def maxs(score):
	f=open('fonts/maxscore.txt','r')
	maxscore=int(f.read())
	if maxscore<score:
		f=open('fonts/maxscore.txt','w')
		f.write(str(score))
		maxscore=score
	f.close()
	return maxscore
def maxk(kills):
	f=open('fonts/maxkills.txt','r')
	maxkills=int(f.read())
	if maxkills<kills:
		f=open('fonts/maxkills.txt','w')
		f.write(str(kills))
		maxkills=kills
	f.close()
	return maxkills

def draw():
	wingame.blit(fon,(fx,0))
	for war in wariors: war.draw()  
	wingame.blit(bulat,(x,y))
	wingame.blit(score_font.render('lives: '+ str(lives),0,(255,0,0)),[600,10])
	wingame.blit(score_font.render('kills: '+ str(kills),0,(255,0,0)),[100,10])
	wingame.blit(score_font.render('score: '+ str(int(score)),0,(255,0,0)),[300,10])

	win.blit(wingame,(0,0))
	pygame.display.update()

def jumping():
	global nachy, y, speedy, g, jump, numjamp
	y-=(speedy**2/3)*abs(speedy+0.1)/(speedy+0.1)
	if y<0: y=0 
	speedy-=g*0.1
	if y>=nachy:
		jump=False
		numjamp=0
		y=nachy

def insert(x1,x2,y1,y2,bam):
	if (((x1-x2)**2+((y1-y2))**2)<Rkv*bam): return 1
	else: return 0



pygame.event.set_blocked([pygame.MOUSEMOTION,
	pygame.MOUSEBUTTONUP,
	pygame.MOUSEBUTTONDOWN,
	pygame.JOYAXISMOTION,
	pygame.JOYBALLMOTION,
	pygame.JOYHATMOTION,
	pygame.JOYBUTTONUP,
	pygame.JOYBUTTONDOWN,
	pygame.VIDEORESIZE,
	pygame.VIDEOEXPOSE,
	pygame.USEREVENT])
game=True
maxscore=maxs(0)
maxkills=maxk(0)
lives=0
score=-1
gamemenu.menu()
punkts.append((420,300,"Restart",(255,0,255),(255,0,0),2))
gamemenu=Menu(punkts)

pygame.key.set_repeat(1,1)

restart()

while game:
	clock.tick(30)
	fonspeed+=0.001
	score+=0.01

	if randint(0,50+int(fonspeed))//54>0 and len(wariors)<6: wariors.append(warior())

	if bam>0:bam-=1

	for e in pygame.event.get():
		if e.type==pygame.QUIT: #проверка выхода
				game=False
		if (e.type==pygame.KEYDOWN and e.key==pygame.K_ESCAPE): 
			maxscore=maxs(int(score))
			maxkills=maxk(kills)
			gamemenu.menu()
			pygame.key.set_repeat(1,1)
		if e.type==pygame.KEYUP:
			if e.key==pygame.K_w and bam==0: ydar=False
						
	if  lives<1:
		maxscore=maxs(int(score))
		maxkills=maxk(kills)
		gamemenu.menu()


	if jump==True: jumping()

	keys=pygame.key.get_pressed()
	if keys[pygame.K_d] and x<400:
		x+=speedx
	elif keys[pygame.K_a] and x>20:
		x-=speedx
	if keys[pygame.K_SPACE] and (jump==False or speedy<-4) and numjamp<3:
		jump=True
		speedy=10
		numjamp+=1
		if numjamp<2: nachy=y
	elif keys[pygame.K_s] and y<300:
		y+=50
	if keys[pygame.K_w] and bam==0 and ydar==False:
		bam=29
		ydar=True
		pygame.mixer.Channel(2).play(dam)

	fx-=fonspeed
	if fx<-1795: fx=0

	if len(wariors)>1: 
		for war in wariors: war.update()
	draw()




	