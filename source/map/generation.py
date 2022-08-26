import pygame
import random
import math
import json

with open("./map/map.json", "r") as noiF:
    noisee = json.load(noiF)
    noisee = noisee[0]

cellSize = noisee["map.cellSize"]
nGrass = noisee["noise.data.grass"]
nWater = noisee["noise.data.water"]

bFLower = noisee["noise.data.biom.flower"]
bSand = noisee["noise.data.biom.sand"]
bBsh = noisee["noise.data.biom.bush"]

class Noise():
    def __init__(self) -> None:
        random.seed(random.randint(0, 9999999999))
    def generateWhiteNoise(self, width, height) -> None:
        noise = [[r for r in range(width)] for i in range(height)]
        for i in range(0, height):
            for j in range(0, width):
                noise[i][j] = random.randint(0, 1000)
        return noise

    def generate(self) -> list:
        noise = self.generateWhiteNoise(18, 11)
        list = []
        for i in noise:
            loval = []
            for o in i:
                if(o >= nGrass[0] and o <= nGrass[1]):
                    if(o >= bFLower[0] and o <= bFLower[1]):
                        rand = random.randint(0, 1)
                        if rand == 1:
                            loval.append('flower')
                        else: loval.append('flower1')
                    elif (o >= bBsh[0] and o <= bBsh[1]):
                        loval.append('bush')
                    else:
                        loval.append('grass')
                elif(o >= nWater[0] and o <= nWater[1]):
                    if(o >= bSand[0] and o <= bSand[1]):
                        loval.append('sand')
                    else:
                        loval.append('water')
                else:
                    loval.append('water')
            list.append(loval)
        return list


class World():
    def __init__(self, win) -> None:
        self.win = win
        nois = Noise()

        self.world = nois.generate()
        self.worldWidth, self.worldHeight = 18, 11
        self.cellSize = cellSize
        self.offsetX, self.offsetY = 0, 0

        self.grass = pygame.image.load("../source/assets/resources/blocks/grass.png").convert_alpha()
        self.grass = pygame.transform.scale(self.grass, (self.cellSize, self.cellSize)).convert_alpha()
        self.grass = self.grass.convert()

        self.flower = pygame.image.load("../source/assets/resources/blocks/flower.png")
        self.flower = pygame.transform.scale(self.flower, (self.cellSize, self.cellSize))
        self.flower = self.flower
        self.flower1 = pygame.image.load("../source/assets/resources/blocks/flower1.png")
        self.flower1 = pygame.transform.scale(self.flower1, (self.cellSize, self.cellSize))
        self.flower1 = self.flower1

        self.water = pygame.image.load("../source/assets/resources/blocks/water.png").convert_alpha()
        self.water = pygame.transform.scale(self.water, (self.cellSize, self.cellSize)).convert_alpha()
        self.water = self.water.convert()

        self.sand = pygame.image.load("../source/assets/resources/blocks/sand.png").convert_alpha()
        self.sand = pygame.transform.scale(self.sand, (self.cellSize, self.cellSize)).convert_alpha()
        self.sand = self.sand.convert()

        self.bush = pygame.image.load("../source/assets/resources/blocks/bush.png").convert_alpha()
        self.bush = pygame.transform.scale(self.bush, (self.cellSize, self.cellSize)).convert_alpha()
        self.bush = self.bush.convert()

    def render(self) -> None:
        for row in range(self.worldHeight):
            for col in range(self.worldWidth):
                x, y = col * self.cellSize + self.offsetX, row * self.cellSize + self.offsetY
                if self.world[row][col] == "grass":
                    self.win.blit(self.grass, (x, y))
                elif self.world[row][col] == "flower":
                    self.win.blit(self.flower, (x, y))
                elif self.world[row][col] == "flower1":
                    self.win.blit(self.flower1, (x, y))
                elif self.world[row][col] == "sand":
                    self.win.blit(self.sand, (x, y))
                elif self.world[row][col] == "water":
                    self.win.blit(self.water, (x, y))
                elif self.world[row][col] == "bush":
                    self.win.blit(self.bush, (x, y))
                else:
                    self.win.blit(self.water, (x, y))

    def draw(self, state: str) -> None:
        mousePX, mousePY = pygame.mouse.get_pos()
        b1, b2, b3 = pygame.mouse.get_pressed()
        mouseRow, mouseCol = mousePY // self.cellSize, mousePX // self.cellSize
        pygame.draw.rect(self.win, (0, 0, 0), (mouseCol*self.cellSize, mouseRow*self.cellSize, 40, 40), 2)
        if b1:
            self.world[mouseRow][mouseCol] = state
        elif b3:
            self.world[mouseRow][mouseCol] = 'water'