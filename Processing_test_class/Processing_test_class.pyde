from star import Star
star_count=1000
stars=[[None,None]]*star_count


def setup():
    size(600, 600)
    for item in range(star_count):
        stars[item]=Star()
def draw():
    translate(width/2,height/2)
    background(0)
    for item in range(len(stars)):
        stars[item].update()
        stars[item].show()
        
