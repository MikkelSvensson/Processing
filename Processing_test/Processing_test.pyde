stars=[]
star_count=500

def show(star):
    x=star[0]
    y=star[1]
    z=star[2]
    pz=star[3]
    fill(255)
    noStroke()
    
    sx = map(x/z,0,1,0,width)
    sy = map(y/z,0,1,0,width)
    
    r=map(z,0,width,16,0)
    
    #ellipse(sx,sy,r,r)
    
    px = map(x/pz,0,1,0,width)
    py = map(y/pz,0,1,0,width)
    stroke(255)
    line(px,py,sx,sy)
    
def update(star):
    x=star[0]
    y=star[1]
    z=star[2]
    pz=star[3]
    pz = z
    z=z-speed
    if z<1:
        z=random(width)
        x = random(-width/2,width/2)
        y = random(-height/2,height/2)
        pz=z
    return [x,y,z,pz]
def setup():
    size(600, 600)
    for coordinate in range(star_count):
        x = random(-width/2,width/2)
        y = random(-height/2,height/2)
        z = random(width)
        pz = z
        stars.append([x,y,z,pz])
def draw():
    global speed
    speed=map(mouseX,0,width,0,20)
    translate(width/2,height/2)
    background(0)
    for star in range(len(stars)):
        stars[star]=update(stars[star])
        show(stars[star])
        
