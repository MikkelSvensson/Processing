class Circle:
    def __init__(self,x_,y_,c_):
        self.x=x_
        self.y=y_
        self.c=c_
        self.r=3
        self.growing = True
    
    def grow(self):
        if (self.growing):
            self.r = self.r + 0.5
    def edges(self):
        return self.x+self.r > width or self.x-self.r<0 or self.y+self.r > height or self.y-self.r <0
    def show(self):
        fill(self.c)
        noStroke()
        ellipse(self.x,self.y,self.r*2,self.r*2)
