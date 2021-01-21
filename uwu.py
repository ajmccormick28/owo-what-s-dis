class TrackWall:
  def __init__ (self, xStart, yStart, trackType, trackSize, checkPoints = False):
    self.xStart = xStart
    self.yStart = yStart
    self.trackType = trackType
    self.trackSize = trackSize
    self.checkPoints = checkPoints
    

  def checkPoint(self, carX, carY):
    if self.checkPoints == True:
      if carX >= self.xStart - 12 and carX <= self.xStart + self.trackSize - 12 and carY >= self.yStart - 12 and carY <= self.yStart + self.trackSize - 12:
        print("its working") 
      
      
  def wallDetect(self, carX, carY):
    #"vert", "hori", "rgUp", "rgDown", "lfDown", "lfUp"

    if self.trackType == "vert":
      if carY > self.yStart and carY < self.yStart + self.trackSize:
        #left wall 12
        if carX >= self.xStart - 12 and carX <= self.xStart - 0:
          
          return "stopLeft"

        #right wall
        elif carX <= self.xStart + self.trackSize - 34 and carX >= self.xStart + self.trackSize - 46:
          
          return "stopRight"
        
          
    elif self.trackType == "hori":
      
      if carX > self.xStart and carX < self.xStart + self.trackSize:
       
        #print(carY, self.yStart + self.trackSize - 1)
        #Top Part of Track
        if carY >= self.yStart + -12 and carY <= self.yStart + 0:
          
          
          return 'stopUp'

        # Bottom Part of Track piece
        elif carY <= self.yStart + self.trackSize - 34 and carY >= self.yStart + self.trackSize - 46:
          
          return 'stopDown'

    # Checking left and bottom walls of track piece      
    elif self.trackType == 'rgup':
      if carX > self.xStart - 12 and carX < self.xStart + self.trackSize - 12 and carY > self.yStart - 12 and carY < self.yStart + self.trackSize - 12:
        #Check for if the car is in the corner 
        if carX >= self.xStart - 12 and carX <= self.xStart - 0 and carY <= self.yStart + self.trackSize - 34 and carY >= self.yStart + self.trackSize - 46:
          
          return 'stopBoth'
        # Check if car is against left wall
        elif carX >= self.xStart - 12 and carX <= self.xStart - 0:
          
          return 'stopLeft'
        # Check if car is against bottom wall
        elif carY <= self.yStart + self.trackSize - 34 and carY >= self.yStart + self.trackSize - 46:
          
          return 'stopBottom'
       

      # Start here 8/24
    elif self.trackType == 'rgdown':
      if carX > self.xStart - 12 and carX < self.xStart + self.trackSize - 12 and carY > self.yStart - 12 and carY < self.yStart + self.trackSize - 12:
          #Check for if the car is in the corner 
          if carX >= self.xStart - 12 and carX <= self.xStart - 0 and carY >= self.yStart + -12 and carY <= self.yStart + 0:
            
            return 'stopBoth'
          # Check if car is against left wall
          elif carX >= self.xStart - 12 and carX <= self.xStart - 0:
            
            return 'stopLeft'
          # Check if car is against top wall
          elif carY >= self.yStart + -12 and carY <= self.yStart + 0:
            return 'stopTop'
      

    # top wall and right wall
    
    elif self.trackType == 'lfdown':
      
      
       if carX > self.xStart - 12 and carX < self.xStart + self.trackSize - 12 and carY > self.yStart - 12 and carY < self.yStart + self.trackSize - 12:
          #Check for if the car is in the corner 
          if carX <= self.xStart + self.trackSize - 34 and carX >= self.xStart + self.trackSize - 46 and carY <= self.yStart + self.trackSize - 34 and carY >= self.yStart + self.trackSize - 46:
            
            return 'stopBoth'
          # Check if car is against right wall
          elif carX <= self.xStart + self.trackSize - 34 and carX >= self.xStart + self.trackSize - 46:
            
            return "stopRight"
        
          # Check if car is against top wall
          elif carY >= self.yStart + -12 and carY <= self.yStart + 0:
            return 'stopTop'
        
    
    elif self.trackType == 'lfup':
      if carX > self.xStart - 12 and carX < self.xStart + self.trackSize - 12 and carY > self.yStart - 12 and carY < self.yStart + self.trackSize - 12:
          #Check for if the car is in the corner 
          if carX <= self.xStart + self.trackSize - 34 and carX >= self.xStart + self.trackSize - 46 and carY <= self.yStart + self.trackSize - 34 and carY >= self.yStart + self.trackSize - 46:
            return 'stopBoth'
          # Check if car is against right wall
          elif carX <= self.xStart + self.trackSize - 34 and carX >= self.xStart + self.trackSize - 46:
           
            return 'stopRight'
          # Check if car is against bottom wall
          elif carY <= self.yStart + self.trackSize - 34 and carY >= self.yStart + self.trackSize - 46:
            
            return 'stopBottom'

    return ""
