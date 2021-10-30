class Box:
    def __init__(self):
        self.rgb=color(random(255),random(255),random(255))
        self.a=random(20,100)
        self.b=random(20,100)
    def show(self,x,y):
        noStroke()
        fill(self.rgb)
        rect(x,y,self.a,self.b)
