size(800, 800)
background(0)
blendMode(ADD)
distance=15
i = 0
while i < distance:
    
    println(i)
    j = 0
    while j<distance:
        posX = i * width/distance
        posY = j * height/distance
        #float dist = random(20)
        
        #float col = random(255)
        col = 255
        sqSz = random(45)
        fill(col, 0, 0)
        rect(posX, posY, sqSz, sqSz)
        fill(0, col, 0)
        rect(posX + 10, posY + distance, sqSz, sqSz)
        fill(0, 0, col)
        rect(posX + 20, posY + distance * 2, sqSz, sqSz)
        j += 1
    i += 1

#save("img.png");
