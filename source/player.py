import pygame, config.parser as pr

class Player(pygame.sprite.Sprite):
    def __init__(self, win) -> None:
        super().__init__()
        self.win = win
        self.x = 0
        self.y = 0

        self.hitbox = (self.x, self.y)

        self.playerImage = pygame.image.load('assets/resources/entity/player.png')
        self.playerImage = pygame.transform.scale(self.playerImage, (40, 40))

        self.speed = pr.playerSpeed

    def flip(self) -> None:
        self.playerImage = pygame.transform.flip(self.playerImage, True, False)

    def movement(self) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]: self.y -= self.speed
        if keys[pygame.K_s]: self.y += self.speed
        if keys[pygame.K_d]: self.x += self.speed
        if keys[pygame.K_a]: self.x -= self.speed
    
    def render(self) -> None:
        self.win.blit(self.playerImage, (self.x, self.y))
        self.hitbox = (self.x, self.y)
        pygame.draw.rect(self.win, (255, 255, 255), (self.hitbox[0],self.hitbox[1], 40,40), 2)