
import pygame
from pygame import *
from random import randint


pygame.init()


win_width = 600
win_height = 400


window = display.set_mode((win_width, win_height))
display.set_caption("Ping_Pong")

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:  
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - self.rect.height - 5:  
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()  
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - self.rect.height - 5:
            self.rect.y += self.speed


racket1 = Player('racket1.png', 30, 200, 20, 150, 4)  
racket2 = Player('racket2.png', 520, 200, 20, 150, 4)  
ball = GameSprite('tenis_ball.png', 200, 200, 50, 50, 4)  


run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    
    racket1.update_r()
    racket2.update_l()

    
    window.fill((0, 0, 0))  

    
    window.blit(racket1.image, racket1.rect)
    window.blit(racket2.image, racket2.rect)
    window.blit(ball.image, ball.rect)

    
    display.update()


pygame.quit()
