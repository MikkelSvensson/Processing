class Star:
    
    def __init__(self):
        self.z=random(width)
        self.x = random(-width/2,width/2)
        self.y = random(-height/2,height/2)
        self.speed=random(1,12)
    def show(self):
        fill(255)
        noStroke()
        
        self.sx = map(self.x/self.z,0,1,0,width)
        self.sy = map(self.y/self.z,0,1,0,width)
        
        self.r=map(self.z,0,width,16,0)
        
        #ellipse(self.sx,self.sy,self.r,self.r)
        
        self.px = map(self.x/self.pz,0,1,0,width)
        self.py = map(self.y/self.pz,0,1,0,width)
        stroke(255)
        line(self.px,self.py,self.sx,self.sy)
    
    def update(self):
        self.pz = self.z
        self.z=self.z-self.speed
        if self.z<1:
            self.z=random(width)
            self.x = random(-width/2,width/2)
            self.y = random(-height/2,height/2)
            self.pz=self.z
            self.speed=random(1,12)
