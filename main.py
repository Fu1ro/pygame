from pygame import *


window = display.set_mode((700, 500))
display.set_caption("Доганялки")
background = transform.scale(image.load("background.png"), (700, 500))
sprite1 = transform.scale(image.load("sprite1.png"), (100, 100))
sprite2 = transform.scale(image.load("sprite2.png"), (100, 100))

x1, y1 = 300, 200
x2, y2 = 400, 300
speed = 10
clock = time.Clock()
FPS = 60

game = True
while game:
    window.blit(background, (0,0))
    keys = key.get_pressed()
    for e in event.get():
        if e.type == QUIT:
            game = False
    if keys[K_DOWN]:
        y2 += speed
    if keys[K_UP]:
        y2 -= speed
    if keys[K_LEFT]:
        x2 -= speed
    if keys[K_RIGHT]:
        x2 += speed
    
    if keys[K_s]:
        y1 += speed
    if keys[K_w]:
        y1 -= speed
    if keys[K_a]:
        x1 -= speed
    if keys[K_d]:
        x1 += speed

    window.blit(sprite1, (x1,y1))
    window.blit(sprite2, (x2,y2))
    display.update()
    clock.tick(FPS)