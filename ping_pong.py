from pygame import *
font.init()
class GameSprite(sprite.Sprite):
    def __init__(self, image_name, speed, x, y, w, h):
        super().__init__()
        self.image = transform.scale(image.load(image_name), (w, h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Ball(GameSprite):
    def update(self):
        self.rect.y += self.speed
        x += speed.x
        y += speed.y
        if self.rect.y > 490:
            speed.y *= -1
        if self.rect.y > 5:
            speed.y *= -1
        if sprite.collide.rect(rocket1, ball):
            speed.x *= -1
        if sprite.collide.rect(rocket2, ball):
            speed.x *= -1
class Rocket(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_W] and self.rect.y > 5:
            self.rect.y += self.speed
        if keys_pressed[K_S]and self.rect.y < 595:
            self .rect.y -= self.speed
    def update1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y += self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 595:
            self.rect.y -= self.speed
ball = Ball('lox.png', 50, 100, 100, 15, 15)
rocket1 = ('rocket.png', 45, 400, 500, 10, 50)
rocket2 = ('rocket1.png', 45, 100, 500, 10, 50)
window = display.set_mode((700, 500))
display.set_caption('Ракетки бьют лоха')

window.fill((0, 244, 0))
clock = time.Clock()
game = True
while game:
    ball.reset()
    ball.update()
    ball.update1()
    rocket1.reset()
    rocket1.update()
    rocket2.reset()
    rocket2.update()
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(60)
