import pygame, config.parser as pr, player, funcs as fc
import map.generation as gen

pygame.init()
win = pygame.display.set_mode((pr.geometry[0], pr.geometry[1]))
pygame.display.set_caption(pr.caption+f' -v{pr.version}')
clock = pygame.time.Clock()

pl = player.Player(win)
pl.x = fc.load()[0][0]; pl.y = fc.load()[0][1]
rect = pygame.Rect(100, 100, 50, 50)

gener = gen.World(win)

vignet = pygame.image.load('./assets/resources/hud/vignet.png').convert_alpha()
cursor = pygame.image.load('./assets/resources/hud/cursor.png').convert_alpha()
cursor = pygame.transform.scale(cursor, (8,8))

blockList = ['water',
             'flower',
             'flower1',
             'sand',
             'grass',
             'bush']; blockIndex = 0; slotOffset = 5
run = True
while run:
    pygame.mouse.set_visible(False)
    clock.tick(pr.framerate)
    pygame.display.set_caption(pr.caption + f' -v{pr.version} ({int(clock.get_fps())})')
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and blockIndex > 0:blockIndex-=1
            elif event.key == pygame.K_RIGHT and blockIndex < len(blockList)-1: blockIndex += 1
    win.fill((0, 0, 0))
    gener.render()
    gener.draw(str(blockList[blockIndex]))

    pl.render()
    pl.movement()

    win.blit(vignet, (0, 0))
    msX, msY = pygame.mouse.get_pos()
    win.blit(cursor, (msX, msY))

    currentSlot = pygame.image.load(f'./assets/resources/blocks/{blockList[blockIndex]}.png').convert_alpha()
    currentSlot = pygame.transform.scale(currentSlot, (40, 40))
    currentSlot = currentSlot.convert()
    fontSlot = pygame.font.Font('./assets/resources/font/font.ttf', 20)
    textSlot = fontSlot.render(f'{blockList[blockIndex]}', True, (255, 255, 255)).convert_alpha()
    win.blit(textSlot, (0+slotOffset, 40+slotOffset))
    win.blit(currentSlot, (0+slotOffset, 0+slotOffset))

    pygame.display.update()
fc.save(pl.x, pl.y)
pygame.quit()