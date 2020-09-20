import pygame
import time
#Attribution: pythonprogramming.net, github.com, geeksforgeeks.com, techwithtim.net

pygame.init()
points=50
green = (0, 255, 0) 
blue = (0, 0, 128) 
tips=0.00

window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Grizz Hacks")
font=pygame.font.Font('freesansbold.ttf',24)
text=font.render('Congrats! You earned ' + str(tips), True, green, blue)
text2=font.render('for the charity of your choice!', True, green,blue)

# Images
forward1=pygame.image.load("forward1.png")
backward1=pygame.image.load("backward1.png")
# obstacle=pygame.image.load("pizzamonster.png")
target = pygame.image.load('table3.png')
astroid = pygame.image.load('astroid.png')


# Build Character
def character(x,y):
  direction = forward1
  direction = pygame.transform.scale(direction, (200, 200))
  window.blit(direction, (x,y))

    
    



clock = pygame.time.Clock()

# Character display 
x = 50
y = 50
prevx=50
prevy=50
astx=100
asty=100
width = 40
height = 60
points=50
destx=300
desty=25
dest2x=25
dest2y=100
pizzaToDeliver=10
oldPizza=10
tips=0.00
times= 0
times1= 0



def drawHitBox():
  hitbox = (x + 20, y, 28, 60)

# Jumping
isJump = False
jumpCount = 10
bg = pygame.image.load("bg.jpg")


def background():
  window.blit(bg, (0,0))

  # Target
  destination = pygame.transform.scale(target, (200, 200))
  window.blit(destination,(destx, desty))
  window.blit(destination,(dest2x,dest2y))

  # Astroid
  window.blit(astroid, (astx,asty))

def collisiontesthorizontal(x,astx):
    if x>astx+60 and x<astx+100:
      return True
    else:
      return False
def collisiontestvertical(y,desty):
    if y>desty and y<desty+100:
      return True
    else:
      return False


  



run = True
while run:
  clock.tick()
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  background()

  # Movement
  keys = pygame.key.get_pressed()

  if 1==1:
  
    if keys[pygame.K_RIGHT]:
      x += 10
      direction = forward1

    if keys[pygame.K_LEFT] and x > vel:
      x -= 10
      direction = backward1
    if keys[pygame.K_UP]:
       y -= 10
       direction = forward1
    if keys[pygame.K_DOWN]:
       y += 10
       direction = backward1
     
    if not(isJump):
      if keys[pygame.K_SPACE]:
        isJump = True
        y -= 10

      

    else:
      if jumpCount >= -10:
        neg = 1
        if jumpCount < 0:
          neg = -1
        y -= (jumpCount ** 2) * .5 * neg
        jumpCount -= 1
      else:
        isJump = False
        jumpCount = 10
  #Collision Tests and Incrementing Points
    if collisiontesthorizontal(x,astx):
      if pizzaToDeliver<10:
          pizzaToDeliver+=1
          print(pizzaToDeliver)
      pass
    if collisiontestvertical(y,desty) and collisiontesthorizontal(y,desty):
          if prevx-x<=-30 or prevx-x>=30 or prevy-y<=-30 or prevy-y>=30:
            pizzaToDeliver-=1
            tips+=0.05
            times+=1
            print(pizzaToDeliver)
            milliseconds=clock.tick()
            print(milliseconds)
            seconds=milliseconds/1000
            if seconds>=5:
              tips-=0.02
            print(tips)
            prevx=x
            prevy=y
    if collisiontestvertical(y,desty) and collisiontesthorizontal(y,desty):
          if prevx-x<=-30 or prevx-x>=30 or prevy-y<=-30 or prevy-y>=30:
            pizzaToDeliver-=1
            tips+=0.05
            #print(pizzaToDeliver)
            milliseconds=clock.tick()
            print(milliseconds)
            seconds=milliseconds/100
            if seconds>=5:
              tips-=0.02
            print(tips)
            times1+=1
            prevx=x
            prevy=y
          else: 
            tips+=0
    if times1==1 and times==1:
      times1=0
      times=0
    if pizzaToDeliver<=0:
      text=font.render('Congrats! You earned ' + str(tips), True, green, blue)
      text2=font.render('for the charity of your choice!', True, green,blue)
      window.blit(text,(0,25))
      window.blit(text2,(0,50))


      
      


  character(x,y)
 


 


  #window.blit(text,(0,25))
  #window.blit(text2,(0,50))
  pygame.display.update()
  
  

pygame.quit





