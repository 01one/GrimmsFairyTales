import pygame,sys
from pygame.locals import*
pygame.init()
import glob
story1=glob.glob("data/001.The FrogKing/*.jpg")
tales=[pygame.image.load(item) for item in story1]
print(story1)

clock=pygame.time.Clock()

screen_width=1000
screen_height=720
screen=pygame.display.set_mode((screen_width,screen_height),RESIZABLE)
color=(144, 238,144)


img_w=screen_width
def scale_image(img):
	w=img.get_width()
	h=img.get_height()
	img=img
	if w>screen_width:
		if w>h:
			w_s=w-screen_width
			c=1/(w/w_s)
			w=screen_width
			h=h-int(h*c)
			img=pygame.transform.smoothscale(img,(w,h))
		if w<h:
			h_s=h-screen_height
			c=1/(h/h_s)
			h=screen_height
			w=w-int(w*c)
			img=pygame.transform.smoothscale(img,(w,h))

	if h>screen_height:
		h_s=h-screen_height
		c=1/(h/h_s)
		h=screen_height
		w=w-int(w*c)
		img=pygame.transform.smoothscale(img,(w,h))
	img_w=w
	return img

n_w=0
n=0
scale=True
game_running=True
img=tales[0]
while game_running:
	#img=tales[n]
	clock.tick(30)
	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()
		if event.type==pygame.VIDEORESIZE:
			screen_width,screen_height=event.size
			n_w=abs(img_w-screen_width)
			n_w=n_w//2
			img=scale_image(img)
		keys = pygame.key.get_pressed()
		if keys[pygame.K_RIGHT]:
			if n+1>11:
				n=11
			else:
				n+=1
			img=tales[n]
			img=scale_image(img)
				
		if keys[pygame.K_LEFT]:
			if n-1<0:
				n=0
			else:
				n-=1
			img=tales[n]
			img=scale_image(img)
	screen.fill(color)
	if scale==True:
		img=scale_image(img)
		scale=False
	screen.blit(img,(n_w,0))
	pygame.display.update()
