import pygame
import random
import ctypes
pygame.init()
pygame.mixer.init()

w = 1350
h = 400
screen = pygame.display.set_mode((w,h))
pygame.display.set_caption("Dino game")

c = pygame.time.Clock()

bg = pygame.image.load("backm.jpg")
bgx = 0
bgx2 = 1350
bg = pygame.transform.scale(bg , (1350,1400))
night_bg = pygame.image.load("night_back.jpg")
night_bg = pygame.transform.scale(night_bg, (1350,1400))
bgn = 0
bgn2 = 1350

white= (255,255,255)

walk = [pygame.image.load("dinom1.png"),pygame.image.load("dinom2.png")]

tree1 = pygame.image.load("treem1.png")
tree2 = pygame.image.load("treem2.png")
tree3 = pygame.image.load("treem3.png")
tree4 = pygame.image.load("treem4.png")
tree5 = pygame.image.load("treem5.png")

dino1 = pygame.image.load("dinom1.png")
dino2 = pygame.image.load("dinom2.png")
stand = pygame.image.load("dinom3.png")
gameOver_dino = pygame.image.load("dinom4.png")
sattled = [pygame.image.load("dinom5.png"),pygame.image.load("dinom6.png")]
birds = [pygame.image.load("bird1.png"),pygame.image.load("bird2.png")]
birds_night = [pygame.image.load("bird1(night).png"),pygame.image.load("bird2(night).png")]

class T_Rex():
    def __init__(self, x, y, width, height):
        
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.isJump = False
        self.jumpCount = 10
        self.right = True
        self.walkCount = 0
        self.count = 0
        self.count1 = 0
        self.count2 = 0
        self.x1 = 0
        self.hitbox = (self.x+20, self.y, 28, 60)
        self.y_tree = 320
        self.back_moving = True
        self.total = self.count + self.count1
        self.night_moving = True
        self.down = False
        self.downCount = 0

    def draw(self, screen):
        if self.walkCount +1 >= 4:
            self.walkCount = 0
        if self.right:
            screen.blit(walk[self.walkCount//2], (self.x, self.y))
            self.walkCount += 1
            self.count += 1
            self.down = False
        if self.downCount +1 >= 4:
            self.downCount = 0
        elif self.down:
            screen.blit(sattled[int(self.downCount)//2], (self.x, self.y + 45))
            self.downCount += 1.1
            self.count2 += 1
            self.right = False
            self.isJump = False
        elif self.isJump == True: 
            screen.blit(stand , (self.x,self.y)) 
            self.right = False
            self.down = False
            #self.hitbox = (self.x, self.y, 80, 85)
        
        font = pygame.font.Font(None, 30)
        self.total = self.count + self.count1 + self.count2
        if self.total < 205:
            score_txt = font.render("Dino Score : " + str(self.total), 1, (0,0,0))
            screen.blit(score_txt, (1050,85))
        else:
            score_txt = font.render("Dino Score : " + str(self.total), 1, (255,255,255))
            screen.blit(score_txt, (1050,85))      


class Tree():
    def __init__(self, x, y, width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.countTree = 0
        self.hitbox =  (self.x, self.y, self.width, self.height)
        self.tree_moving = True
        self.sound = True 
        self.hit1 = False
        self.hit2 = False
        self.hit3 = False
        self.game_over = False
    
    def draw(self, screen):
        screen.blit(tree3, (self.x + 55, self.y))
        screen.blit(tree4, (self.x + 1450, dino.y_tree))
        screen.blit(tree1, (self.x + 1200, self.y))
        screen.blit(tree5, (self.x + 800, self.y))

        if self.tree_moving:
            if dino.total < 205:
                if self.x < -1350 :
                    self.x = 1350 
                self.x -= 12
            else:
                if self.x < -1350 :
                    self.x = 1350 
                self.x -= 13      
    
    def hit(self, screen):
        
        if  (self.x + 80< dino.x + 80 and dino.x + 80 < self.x + 230 and dino.y -40 + 85 > self.y) or (self.x + 850 < dino.x + 80 and dino.x + 80 < self.x + 980 and dino.y -40 + 85 > self.y) or (self.x + 1220 < dino.x + 80 and dino.x + 80 < self.x + 1320 and dino.y -40 + 85 > self.y) or (self.x + 1500 < dino.x + 80 and dino.x + 80 < self.x + 1530 and dino.y -70 + 85 > self.y):
            
            if dino.total < 205:
                die = pygame.mixer.music.load("die.mp3")
                pygame.mixer.music.play(1, (0.0))
                dino.back_moving = False
                dino.right = False
                run = False
                self.tree_moving = False
                screen.blit(bg, (bgx , -400))
                tree.draw(screen)
                screen.blit(gameOver_dino, (dino.x, dino.y))
                font = pygame.font.Font(None, 30)
                game_over_txt = font.render("Game Over", 10, (0,0,0))
                screen.blit(game_over_txt, (610, 80))
                pygame.mixer.music.stop()   
            elif dino.total > 205:
                die = pygame.mixer.music.load("die.mp3")
                pygame.mixer.music.play(1, (0.0))
                dino.night_moving = False
                run = False
                dino.back_moving = False
                dino.right = False
                self.tree_moving = False
                screen.blit(night_bg, (bgn , -400))
                screen.blit(night_bg,(1350-bgn, -400))
                tree.draw(screen)
                screen.blit(gameOver_dino, (dino.x, dino.y))
                font = pygame.font.Font(None, 30)
                game_over_txt = font.render("Game Over", 10, (255,255,255))
                screen.blit(game_over_txt, (610, 80))
                pygame.mixer.music.stop()        
class Bird():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.birdCount = 0
        self.left = True
        self.vel = 0
        self.night_bird = True
        
    def draw(self, screen):
        if self.birdCount + 1 >= 10:
            self.birdCount = 0

        if self.left:
            screen.blit(birds[int(self.birdCount)//5], (self.x, self.y))
            self.birdCount += 1
        #pygame.draw.rect(screen, (255,0,0), (self.x, self.y,63,60),2 )
        
        if self.x< -1350 :
            self.x = 1350 
        self.x -= 12
        if dino.total > 205:
            if self.night_bird:
                self.left = False
                screen.blit(birds_night[int(self.birdCount)//5], (self.x, self.y))
                self.birdCount += 1
            
        if dino.total > 309:
            self.left = False
            self.night_bird = False
    def hit(self, screen):
        if (dino.x < self.x and self.x + 50 < dino.x + 80) and (self.y + 60 > dino.y and dino.y > self.y) :
            print("hit")
        if (dino.x < self.x and self.x + 50 < dino.x + 80) and (self.y + 60 < dino.y + 45):
            print("not hit")
        if self.y < dino.y and dino.y < self.y + 30 and dino.x < self.x and self.x + 25 < dino.x + 80:
            print("Hit")
        if self.x < dino.x and dino.x + 80 < self.x + 63 and self.y + 60 > dino.y and dino.y > self.y :
            print("hit")
        if self.x < dino.x and dino.x + 80 < self.x + 63 and  self.y + 60 < dino.y + 45 :
            print("hit")        
                
def redrawGame():
   
    if dino.total > 205 and dino.night_moving:
        screen.blit(night_bg, (bgn , -400))
        screen.blit(night_bg, (bgn2 , -400))  
        tree.x -= 8
    elif dino.back_moving:
        screen.blit(bg, (bgx , -400))
        screen.blit(bg, (bgx2 , -400))

    tree.draw(screen)
    tree.hit(screen)
    dino.draw(screen)
    bird.draw(screen)
    bird.draw(screen)
    
    pygame.display.update()
    
dino = T_Rex(200, 282, 1350, 400)  
tree = Tree(0,280,93,87)
bird = Bird(1350, 250)

# def start_again():
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.K_ESCAPE and event.type == pygame.K_DOWN:
#                 return False
#             if event.type == pygame.K_SPACE and event.type == pygame.K_UP :
#                 return True

run = True
while run :
    if run:
        if dino.back_moving:
            bgx -= 12
            bgx2 -= 12
            if bgx < bg.get_width() * -1 :
                bgx = bg.get_width()   
            if bgx2 < bg.get_width() * -1 :
                bgx2 = bg.get_width()
                
        if dino.night_moving:
            bgn -= 14
            bgn2 -= 14
            if bgn < bg.get_width() * -1 :
                bgn = bg.get_width()   
            if bgn2 < bg.get_width() * -1 :
                bgn2 = bg.get_width()
                
            
        c.tick(20)
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                run = False
        if keys[pygame.K_DOWN]:
            dino.right = False
            dino.down = True
        else:
            dino.right = True
            dino.down = False
        if not(dino.isJump):
            if keys[pygame.K_SPACE] or keys[pygame.K_UP] :
                sound_jump = pygame.mixer.music.load("jump.mp3")
                pygame.mixer.music.play(1, (0.0))
                dino.count1 += 1
                dino.isJump = True
                dino.right = False
                dino.down = False
            else:
                pygame.mixer.music.stop()
        else:       
            if dino.jumpCount >= -10:
                neg = 1
                if dino.jumpCount < 0:
                    neg = -1
                dino.y -= (dino.jumpCount**2)*0.7*neg
                dino.jumpCount -= 1
            else:
                dino.isJump = False
                dino.right = True
                dino.down = False
                dino.jumpCount = 10
                
        redrawGame()
    # else:
    #     if not(run):
    #         run = start_again()
    
pygame.quit()