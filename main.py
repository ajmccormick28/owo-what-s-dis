import math
import pygame
import os
import itertools
import uwu


true = True
false = False



#uwu.runt()
####

def load_pic(name, path="data"):
    return pygame.image.load(os.path.join(path, name))



####

def check(x, minval=0, maxval=255):
    return min(maxval, max(minval, x))


####

class PygView(object):

  
    def __init__(self, width=600, height=600, fps=30):
        """Initialize pygame, window, background, font,...
           default arguments 
        """
        pygame.init()
        pygame.display.set_caption("Press ESC to quit")
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF)
        self.background = pygame.Surface(self.screen.get_size()).convert()  
        self.background.fill((0,255,0)) # fill background white

        self.xAcc = 0
        self.xVel = 0
        self.yAcc = 0
        self.yVel = 0

        self.width = width
        self.height = height

        self.xStart = width - 75
        self.yStart = height - 200

        self.running = True
        self.pause = False


        self.carN = load_pic("carN.png")
        # rotozoom(Surface going to change, angle, scale)
        self.carN = pygame.transform.rotozoom(self.carN, 0, 0.75)
        #self.carN.set_colorkey((0, 0, 0))
        self.carNE = load_pic("carNE.png")
        self.carNE = pygame.transform.rotozoom(self.carNE, 0, 0.75)
        self.carE = load_pic("carE.png")
        self.carE = pygame.transform.rotozoom(self.carE, 0, 0.75)
        self.carSE = load_pic("carSE.png")
        self.carSE = pygame.transform.rotozoom(self.carSE, 0, 0.75)
        self.carS = load_pic("carS.png")
        self.carS = pygame.transform.rotozoom(self.carS, 0, 0.75)
        self.carSW = load_pic("carSW.png")
        self.carSW = pygame.transform.rotozoom(self.carSW, 0, 0.75)
        self.carW = load_pic("carW.png")
        self.carW = pygame.transform.rotozoom(self.carW, 0, 0.75)
        self.carNW = load_pic("carNW.png")
        self.carNW = pygame.transform.rotozoom(self.carNW, 0, 0.75)
        
        self.lfUp = load_pic("lfup.png")
        self.lfUp = pygame.transform.scale(self.lfUp, (100, 100))

        self.rgUp = load_pic("rgup.png")
        self.rgUp = pygame.transform.scale(self.rgUp, (100, 100))

        #self.lfDown
        self.LfDown = load_pic("lfdown.png")
        self.LfDown = pygame.transform.scale(self.LfDown, (100, 100))

        # self.rgDown
        self.RgDown = load_pic("rgdown.png")
        self.RgDown = pygame.transform.scale(self.RgDown, (100, 100))
        
        self.straight = load_pic("vert.png")
        self.straight = pygame.transform.scale(self.straight, (100, 100))

        self.horizontal = load_pic("hori.png")
        self.horizontal = pygame.transform.scale(self.horizontal, (100, 100))

        self.finish = load_pic("finishline.png")
        self.finish = pygame.transform.scale(self.finish, (100, 100))

        self.trackObjects = []
       

        

    def paint(self):
        """painting on the surface"""
        #------- try out some pygame draw functions --------
        # pygame.draw.line(Surface, color, start, end, width) 
        pygame.draw.circle(self.background, (0,200,0), (self.xStart, self.yStart), 10)
        self.screen.blit(self.carN, (0, 300))

        self.trackObjects.append(uwu.TrackWall(0, 0, "rgdown", 100, True))
        self.trackObjects.append(uwu.TrackWall(100, 0, "hori", 100))
        self.trackObjects.append(uwu.TrackWall(200, 0, "hori", 100, True))
        self.trackObjects.append(uwu.TrackWall(300, 0, "hori", 100))
        self.trackObjects.append(uwu.TrackWall(400, 0, "hori", 100))
        self.trackObjects.append(uwu.TrackWall(500, 0, "hori", 100))
        self.trackObjects.append(uwu.TrackWall(600, 0, "hori", 100))
        self.trackObjects.append(uwu.TrackWall(600, 0, "lfdown", 100, True))
        
        
        self.trackObjects.append(uwu.TrackWall(0, 100, "vert", 100))        
        self.trackObjects.append(uwu.TrackWall(100, 100, "rgdown", 100))
        self.trackObjects.append(uwu.TrackWall(200, 100, "lfdown", 100, True))
        self.trackObjects.append(uwu.TrackWall(300, 100, "rgdown", 100))
        self.trackObjects.append(uwu.TrackWall(400, 100, "lfdown", 100))
        self.trackObjects.append(uwu.TrackWall(500, 100, "rgdown", 100, True))
        self.trackObjects.append(uwu.TrackWall(600, 100, "lfup", 100))
        self.trackObjects.append(uwu.TrackWall(700, 100, "vert", 100))

        self.trackObjects.append(uwu.TrackWall(0, 200, "vert", 100))
        self.trackObjects.append(uwu.TrackWall(100, 200, "vert", 100))
        self.trackObjects.append(uwu.TrackWall(200, 200, "vert", 100))
        self.trackObjects.append(uwu.TrackWall(300, 200, "vert", 100))
        self.trackObjects.append(uwu.TrackWall(400, 200, "vert", 100))
        self.trackObjects.append(uwu.TrackWall(500, 200, "vert", 100, True))
        self.trackObjects.append(uwu.TrackWall(600, 200, "vert", 100))
        self.trackObjects.append(uwu.TrackWall(700, 200, "vert", 100))

        self.trackObjects.append(uwu.TrackWall(0, 300, "vert", 100))
        self.trackObjects.append(uwu.TrackWall(100, 300, "vert", 100, True))
        self.trackObjects.append(uwu.TrackWall(200, 300, "vert", 100))
        self.trackObjects.append(uwu.TrackWall(300, 300, "vert", 100))
        self.trackObjects.append(uwu.TrackWall(400, 300, "vert", 100, True))
        self.trackObjects.append(uwu.TrackWall(500, 300, "vert", 100))
        self.trackObjects.append(uwu.TrackWall(600, 300, "vert", 100))
        self.trackObjects.append(uwu.TrackWall(700, 300, "vert", 100))
        self.trackObjects.append(uwu.TrackWall(700, 300, "finish", 100, True))

        self.trackObjects.append(uwu.TrackWall(0, 400, "vert", 100, True))
        self.trackObjects.append(uwu.TrackWall(100, 400, "vert", 100, True))
        self.trackObjects.append(uwu.TrackWall(200, 400, "vert", 100))
        self.trackObjects.append(uwu.TrackWall(300, 400, "vert", 100))
        self.trackObjects.append(uwu.TrackWall(400, 400, "vert", 100))
        self.trackObjects.append(uwu.TrackWall(500, 400, "vert", 100))
        self.trackObjects.append(uwu.TrackWall(600, 400, "vert", 100, True))
        self.trackObjects.append(uwu.TrackWall(700, 400, "vert", 100))
        
        self.trackObjects.append(uwu.TrackWall(0, 500, "rgup", 100))
        self.trackObjects.append(uwu.TrackWall(100, 500, "lfup", 100, True))
        self.trackObjects.append(uwu.TrackWall(200, 500, "rgup", 100))
        self.trackObjects.append(uwu.TrackWall(300, 500, "lfup", 100))
        self.trackObjects.append(uwu.TrackWall(400, 500, "rgup", 100))
        self.trackObjects.append(uwu.TrackWall(500, 500, "lfup", 100, True))
        self.trackObjects.append(uwu.TrackWall(600, 500, "rgup", 100))
        self.trackObjects.append(uwu.TrackWall(700, 500, "lfup", 100))
  

    #calculates r for height and width
    def ratio(self, a, b):
        #a = float(a)
        #b = float(b)
        if b == 0.0:
            return a
        return self.ratio(b, a % b)

    #returns a string with ratio for height and width
    def get_ratio(self, a, b):
        if a == 0.0 and b == 0.0:
          return 0.0
        elif b == 0.0:
          return 10000.0
        r = self.ratio(a, b)
        return "%s" % float((a/r) / (b/r))


    def run(self):
        """The mainloop
        """
        self.paint() 
        running = True
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainloop = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        mainloop = False

                    elif event.key==pygame.K_p:
                        if pause == True:
                            pause = False
                        else:
                            pause = True

										#Maybe add a braking feature

                    elif event.key==pygame.K_a:
                        self.xAcc += .1
           
                    elif event.key==pygame.K_d:
                        self.xAcc -= .1

                    elif event.key==pygame.K_s:
                        self.yAcc -= .1
            
                    elif event.key==pygame.K_w:
                        self.yAcc += .1
                        
            self.yVel += self.yAcc
            if self.yVel > 5:
                self.yVel=5

            self.yStart -= self.yVel

            #Boundary Checking    
            """
            print("car height:", self.yStart + self.yVel)
            print("height:", self.height)
            if (self.yStart - self.yVel) > -20 and (self.yStart + self.yVel) + 40 < self.height:      
              self.yStart -= self.yVel
            """
            
            self.xVel += self.xAcc
            if self.xVel > 5:
                self.xVel = 5

            self.xStart -= self.xVel

            """
            # Do the same as line 123 
            print("car width:", self.xStart + self.xVel)
            print("width:", self.width)
            if (self.xStart - self.xVel) > 0 and (self.xStart + self.xVel) + 40 < self.width:
              self.xStart -= self.xVel
            """

            #self.background.fill((255,255,255)) # fill background white
          
            for i in range(len(self.trackObjects)):
                self.trackObjects[i].checkPoint(self.xStart, self.yStart)
              
                temp = self.trackObjects[i].wallDetect(self.xStart, self.yStart)
                if temp == "stopBoth":
                  self.xVel = 0
                  self.yVel = 0
                  #print ("Ahhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
                elif temp == "stopRight":
                  self.xVel = 1
                  #print ("ahhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
                elif temp == "stopLeft":
                  self.xVel = -1
                  
                elif temp == "stopUp":
                  self.yVel = -1
                  #print ("ahhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
                elif temp == "stopDown":
                  self.yVel = 1
            self.yVel = float(self.yVel)
            self.xVel = float(self.xVel)

            

            ratio = abs(float(self.get_ratio(self.xVel, self.yVel)))
 
            # Left-side of graph
            #print(ratio)
            if self.xVel == 0:
                if self.yVel >= 0:
                  self.screen.blit(self.carN, (self.xStart, self.yStart))  
                elif self.yVel < 0:
                    self.screen.blit(self.carS, (self.xStart, self.yStart))
            elif self.xVel > 0:
                # quant 3
                # Left
                if self.yVel == 0:
                  self.screen.blit(self.carW, (self.xStart, self.yStart))     
									
                elif self.yVel < 0:
                    # slight down and left
                    if ratio >= 2.0:
                      self.screen.blit(self.carW, (self.xStart, self.yStart))
                                             
                    # down and left
                    elif ratio > 0.5 and ratio < 2.0:
                        self.screen.blit(self.carSW, (self.xStart, self.yStart))
                        
                    # down and slightly left
                    elif ratio <= 0.5:
                        self.screen.blit(self.carS, (self.xStart, self.yStart))
                        
                # Quant 2
                elif self.yVel > 0:
                    # x-value is greater
                    # slightly up and left
                    if ratio >= 2.0:
                      self.screen.blit(self.carW, (self.xStart, self.yStart))            
                        
                    # both are about the same
                    #up and left
                    elif ratio > 0.5 and ratio < 2.0:
                        self.screen.blit(self.carNW, (self.xStart, self.yStart))
                       
                    # y-value is greater 
                    #up and slightly left
                    elif ratio <= 0.5:
                        self.screen.blit(self.carN, (self.xStart, self.yStart))
                       
            elif self.xVel < 0:
                # quant 3
                if self.yVel == 0:
                  # right
                  self.screen.blit(self.carE, (self.xStart, self.yStart))
                  
                elif self.yVel < 0:
                    # slighty down and right
                    if ratio >= 2.0:
                      self.screen.blit(self.carE, (self.xStart, self.yStart))

                    # down and right    
                    elif ratio > 0.5 and ratio < 2.0:
                        self.screen.blit(self.carSE, (self.xStart, self.yStart))
                        
                    # down and slighty right
                    elif ratio <= 0.5:
                        self.screen.blit(self.carS, (self.xStart, self.yStart))
                       
                # Quant 1
                elif self.yVel > 0:
                    # x-value is greater
                    # Slightly up and right
                    if ratio >= 2.0:
                      self.screen.blit(self.carE, (self.xStart, self.yStart))
                        
                        
                    # both are about the same
                    # Up and Right
                    elif ratio > 0.5 and ratio < 2.0:
                        self.screen.blit(self.carNE, (self.xStart, self.yStart))
                        

                    # y-value is greater 
                    # Up and slighty right
                    elif ratio <= 0.5:
                        self.screen.blit(self.carN, (self.xStart, self.yStart))
                       
           
            

 
            self.xAcc = 0
            self.yAcc = 0

            
            
            #pygame.draw.circle(self.background, (0,200,0), (self.xStart, self.yStart), 10)self.screen.blit(self.carN, (self.xStart, self.yStart))
            pygame.display.flip()
            pygame.draw.rect(self.background, (0,255,0), (50,50,100,25))
            self.screen.blit(self.background, (0, 0))
            """for i in range(8):
                self.screen.blit(self.road_asphalt02, (i*100,0))"""
            self.screen.blit(self.RgDown, (0, 0))
            for i in range(6):
              self.screen.blit(self.horizontal, (100 * (i + 1), 0))
            #self.screen.blit(self.horizontal, (600, 200))
            self.screen.blit(self.LfDown, (700, 0))
            
            
            self.screen.blit(self.straight, (0, 100))
            
            self.screen.blit(self.RgDown, (100, 100))
            self.screen.blit(self.LfDown, (200, 100))
            self.screen.blit(self.RgDown, (300, 100))
            self.screen.blit(self.LfDown, (400, 100))
            self.screen.blit(self.RgDown, (500, 100))
            self.screen.blit(self.LfDown, (600, 100))
            self.screen.blit(self.straight, (700, 100))
            for i in range(3):
              for j in range(8):
                self.screen.blit(self.straight, (100 * j, 100 * (i + 2)))

            self.screen.blit(self.finish, (700, 300))

            self.screen.blit(self.rgUp, (0, 500))
            self.screen.blit(self.lfUp, (100, 500))
            self.screen.blit(self.rgUp, (200, 500))
            self.screen.blit(self.lfUp, (300, 500))
            self.screen.blit(self.rgUp, (400, 500))
            self.screen.blit(self.lfUp, (500, 500))
            self.screen.blit(self.rgUp, (600, 500))
            self.screen.blit(self.lfUp, (700, 500))
            
           
            

            

            
        pygame.quit()





    
####

if __name__ == '__main__':

    # call with width of window and fps
    PygView().run()