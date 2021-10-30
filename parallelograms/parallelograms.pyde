qWidth=10
qheight=qWidth*0.5

x = 0
y = 0
flip=True
def setup():
    size(int(800*1.777777778),800)
    background(10)
    frameRate(10000)
def new_location(x,y,flip):
    global qx1,qy1,qx2,qy2,qx3,qy3,qheight,qWidth
    qx0=x
    qy0=y
    
    
    if flip: qx1=qx0+qWidth
    else: qx1=qx0-qWidth
    qy1=qy0-qWidth
    qx2=qx1
    qy2=qy1+qheight
    qx3=qx0
    qy3=qy0+qheight
    
    quad(qx0,qy0,qx1,qy1,qx2,qy2,qx3,qy3)
def draw():
    global qheight,qWidth,x,y,flip
    #noLoop()
    noStroke()
    fill(random(50,230),random(50,230),random(50,230))
    
    
    if not int(random(100))<= 35:
        new_location(x,y,flip)
    y += qheight
    if y > height+qWidth:
        if flip: x+=qWidth*2
        y=0
        flip = not flip
    if x > width:
        noLoop()
        print("Done")

    
