class Ring:

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.r = 0
        self.a = 255
    def show(self):
        if self.a >0:
            stroke(255,255,255,self.a)
            noFill()
            ellipse(self.x,self.y,self.r,self.r)
            self.r+=3
            self.a -=1
    def reset(self,x,y):
        self.x = x
        self.y = y
        self.r = 0
        self.a = 255
rings=[]
draw_ellipse = False
def setup():
    size(500,500)
    
def draw():
    global radius, draw_ellipse ,rings
    background(0)       
    for obj in rings:
        obj.show()
def mouseReleased():


    list_len=0
    for obj in rings:

        if obj.a <= 0:
            obj.reset(mouseX,mouseY)
            break
        else: 
            list_len+=1
        if len(rings)==list_len:
            rings.append(Ring(mouseX,mouseY))
            break
    if len(rings)==0:
        rings.append(Ring(mouseX,mouseY))
    #print(obj)
    print(len(rings))
