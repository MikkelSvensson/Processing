    
def indexfunction(x,y):
    return int(x+y*kitten.width)

def setup():
    background(255)
    global kitten
    size(1462*2,1462)
    kitten = loadImage("mikkel_480x480.jpg")
    kitten.filter(GRAY)
    image(kitten,0,0)
    #elipse_size=7
    noStroke()
    kitten.loadPixels()
    for y in range(kitten.height-1):
        for x in range(1,kitten.width-1):
            #elipse_spacing=elipse_size
            pix = kitten.pixels[indexfunction(x,y)]
            oldR = red(pix)
            oldG = green(pix)
            oldB = blue(pix)
            factor = 8
            newR = round(factor * oldR / 255) * (255/factor)
            newG = round(factor * oldG / 255) * (255/factor)
            newB = round(factor * oldB / 255) * (255/factor)
            kitten.pixels[indexfunction(x,y)] = color(newR, newG, newB)
            
            errR = oldR - newR
            errG = oldG - newG
            errB = oldB - newB
            
            index = indexfunction(x+1,y)
            c = kitten.pixels[index]
            r = red(c)
            g = green(c)
            b = blue(c)
            r = r + errR *7/16.0
            g = g + errG *7/16.0
            b = b + errB *7/16.0
            kitten.pixels[index] = color(r,g,b)
            
            

            
            index = indexfunction(x-1,y+1)
            c = kitten.pixels[index]
            r = red(c)
            g = green(c)
            b = blue(c)
            r = r + errR *3/16.0
            g = g + errG *3/16.0
            b = b + errB *3/16.0
            kitten.pixels[index] = color(r,g,b)
            
            index = indexfunction(x,y+1)
            c = kitten.pixels[index]
            r = red(c)
            g = green(c)
            b = blue(c)
            r = r + errR *5/16.0
            g = g + errG *5/16.0
            b = b + errB *5/16.0
            kitten.pixels[index] = color(r,g,b)

            index = indexfunction(x+1,y+1)
            c = kitten.pixels[index]
            r = red(c)
            g = green(c)
            b = blue(c)
            r = r + errR *1/16.0
            g = g + errG *1/16.0
            b = b + errB *1/16.0
            kitten.pixels[index] = color(r,g,b)


#            if x%elipse_spacing==0 and y%elipse_spacing==0:
 #               elipse_size=map(r+g+b,0,255*3,6,5)
  #              fill(r,g,b)
   #             ellipse(x+512*2, y, elipse_size, elipse_size)
            
    kitten.updatePixels()
    image(kitten,512,0)
    kitten.save("test.png")
    
    


def draw():
    pass
