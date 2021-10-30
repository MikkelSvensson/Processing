from circle import Circle

circles = []
#for _ in range(100):
#    circles.append(Circle)
img = PImage
#randomSeed(2)
def setup():
    size(800, 800)
    global img
    img = loadImage("kitten.jpg")
    img.loadPixels()
    background(0)

def draw():
    #background(0)
    #global img
    
    
    total = 50
    count = 0
    attempts = 0
    while count < total:
        newC = newCircle()
        if newC is not None:
            circles.append(newC)
            count+=1
        attempts+=1
        if attempts > 1000:
            noLoop()
            println("Finised")
            break
    for c in circles:
        if c.growing:
            if c.edges():
                c.growing = False
            else:
                for other in circles:
                    if c is not other:
                        d = dist(c.x,c.y,other.x,other.y)
                        if d-2 < c.r+other.r:
                            c.growing = False
                            break
        c.show()
        c.grow()
def newCircle():
     x = random(width)
     y = random(height)
    
     valid = True
     for c in circles:
         d = dist(x,y,c.x,c.y)
         if d<c.r: #if on top of other circle
             valid=False
             break
     if valid:
         index = int(x)+int(y)*img.width
         col = img.pixels[index]
         return Circle(x,y,col)
     else:
         return None
