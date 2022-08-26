import pygame, config.parser as pr

class Player(pygame.sprite.Sprite):
    def __init__(self, win) -> None:
        super().__init__()
        self.win = win
        self.x = 0
        self.y = 0

        self.hitbox = (self.x, self.y)

        self.playerImage = pygame.image.load('assets/resources/entity/player.png').convert_alpha()
        self.playerImage = pygame.transform.scale(self.playerImage, (40, 40))

        self.speed = pr.playerSpeed

    def movement(self) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.y > 0:self.y -= self.speed
        if keys[pygame.K_s] and self.y < pr.geometry[1]-40: self.y += self.speed
        if keys[pygame.K_d] and self.x < pr.geometry[0]-40: self.x += self.speed
        if keys[pygame.K_a] and self.x > 0: self.x -= self.speed
    
    def render(self) -> None:
        self.win.blit(self.playerImage, (self.x, self.y))
        self.hitbox = (self.x, self.y)