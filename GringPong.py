from pygame import *

window = display.set_mode((1280, 720))
display.set_caption("Gring Pong - The Game")
background = transform.scale(image.load("benidorm.jpg"), (1280, 720))

game = True
clock = time.Clock()
FPS = 60

while game:

    for e in event.get():
        if e.type == QUIT:
            game = False

    clock.tick(FPS)
    window.blit(background, (0, 0))
    display.update()