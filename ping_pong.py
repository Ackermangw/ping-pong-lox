from pygame import *
window = display.set_mode((700, 500))
window.fill((0, 244, 0))
clock = time.Clock()
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(40)