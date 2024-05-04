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
        self.speed_x = self.speed
        self.speed_y = self.speed
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Ball(GameSprite):
    def update(self):
        # self.rect.y += self.speed
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.y > 490:
            self.speed_y *= -1
        if self.rect.y < 0:
            self.speed_y *= -1
        if sprite.collide_rect(rocket1, ball):
            self.speed_x *= -1
        if sprite.collide_rect(rocket2, ball):
            self.speed_x *= -1
class Rocket(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s]and self.rect.y < 300:
            self .rect.y += self.speed
    def update1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 300:
            self.rect.y += self.speed
ball = Ball('lox.png', 15, 100, 100, 30, 30)
rocket1 = Rocket('rocket.png', 20, 600, 250, 100, 200)
rocket2 = Rocket('rocket1.png', 20, 0, 300, 100, 200)
window = display.set_mode((700, 500))
display.set_caption('Ракетки бьют лоха')
font1 = font.SysFont('Arial', 50)
font2 = font.SysFont('Arial', 36)
text_win_left = font1.render('Левый избил лоха', 1, (0, 0, 0))
text_win_right = font1.render('Правый избил лоха', 1, (0, 0, 0))

left = 0
right = 0
clock = time.Clock()
finish = False
game = True
while game:
    if finish != True:
        window.fill((0, 244, 0))
        ball.reset()
        ball.update()
        rocket1.reset()
        rocket1.update1()
        rocket2.reset()
        rocket2.update()
        if ball.rect.x < 0:
            right += 1
            ball.rect.x = 100
            ball.rect.y = 100
        if ball.rect.x > 700:
            left += 1
            ball.rect.x = 100
            ball.rect.y = 100
        text_left = font2.render('Левый' + str(left), 1, (0, 0, 0))
        text_right = font2.render('Правый' + str(right), 1, (0, 0, 0))
        window.blit(text_left, (10, 10))
        window.blit(text_right, (10, 40))
        
        
        
        if left == 10:
            window.blit(text_win_left, (250, 150))
            finish = True
        if right == 10:
            window.blit(text_win_right, (250, 150))
            finish = True
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(60)
