
class CoordinatePlane(object):

    def __init__(self, proportional):        
        self.xMin = 0
        self.xMax = 0
        self.yMin = 0
        self.yMax = 0
        self.xCenter = 0
        self.yCenter = 0
        self.xPixelScale = 0 ### units/pixel
        self.yPixelScale = 0 ### units/pixel
        self.proportional = proportional
    
    def SetWindow(self, xMin, xMax, yMin, yMax):
        self.xMin = xMin
        self.xMax = xMax
        self.yMin = yMin
        self.yMax = yMax
        self.xCenter = (xMax - xMin)/2
        self.yCenter = (yMax - yMin)/2
        self.xPixelScale = (xMax - xMin)/width
        self.yPixelScale = (yMax - yMin)/height
        
        
    def SetCenter(self, x, y):
        self.xCenter = x
        self.yCenter = y
        
    def SetXWindowRadius(self, radius):
        self.xMin = self.xCenter - radius
        self.xMax = self.xCenter + radius
        self.xPixelScale = (self.xMax - self.xMin)/width
        if(self.proportional):
            self.yPixelScale = self.xPixelScale
            self.yMax = self.yCenter + self.yPixelScale*height/2
            self.yMin = self.yCenter - self.yPixelScale*height/2
    
    def SetYWindowRadius(self, radius):
        self.yMin = self.yCenter - radius
        self.yMax = self.yCenter + radius
        self.yPixelScale = (self.yMax - self.yMin)/width
        if(self.proportional):
            self.xPixelScale = self.yPixelScale
            self.xMax = self.xCenter + self.xPixelScale*width/2
            self.xMin = self.xCenter - self.xPixelScale*width/2
            
    def MapX(self, x):
        return map(x, self.xMin, self.xMax, 0, width)
    
    def MapY(self, y):
        return height - map(y, self.yMin, self.yMax, 0, height)
        
    def Point(self, x, y):
        noSmooth()
        point(self.MapX(x), self.MapY(y))
        
    def Circle(self, x, y, r):
        ellipse(self.MapX(x), self.MapY(y), 2*r/self.xPixelScale, 2*r/self.yPixelScale)
        
    def Line(self, x1, y1, x2, y2):
        line(self.MapX(x1), self.MapY(y1), self.MapX(x2), self.MapY(y2))