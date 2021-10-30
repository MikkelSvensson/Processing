pic_height=300
bc=color(229, 231, 228)
c_one=color(225, 72 , 53)
c_two=color(46 , 157, 201)
pxy=[]
iterations = 100
draw_color_one = color
draw_color_two = color
draw_color = color
margin = 50
count=0
def setup():
    global pxy,draw_color_one,draw_color_two, draw_color,margin
    size(pic_height,int(pic_height*sqrt(2)))
    background(bc)
    blendMode(SUBTRACT)
    pxy=[int(random(margin,width-margin)),int(random(margin,height-margin))]
    draw_color_one=color(red(bc)-red(c_one),green(bc)-green(c_one),blue(bc)-blue(c_one))
    draw_color_two=color(red(bc)-red(c_two),green(bc)-green(c_two),blue(bc)-blue(c_two))
    draw_color = draw_color_one
    stroke(draw_color_one)
def draw():
    global pxy,draw_color,iterations,count,bc
    if count == 0: background(bc)
    strokeWeight(3) 
    noFill()
    #arc(50, 55, 60, 60, HALF_PI, PI)
    
    pxy=drawLine(pxy[0],pxy[1])
    if count == iterations:
        noLoop()
    if int(random(100)) < 20:
        draw_color = changeColor(draw_color)
        stroke(draw_color)
    count+=1
def changeColor(current):
    global draw_color_one, draw_color_two
    if current == draw_color_one:
        return draw_color_two
    else: 
        return draw_color_one

    
def mouseReleased():
    global count
    count=0
    loop()
def drawLine(x,y):
    global margin
    if int(random(2))==1:
        newx=int(random(margin,width-margin))
        line(x,y,newx,y)
        return [newx,y]
    else:
        newy=int(random(margin,height-margin))
        line(x,y,x,newy)
        return [x,newy]
