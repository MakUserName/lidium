import pygame, config.parser as pr, player, funcs as fc

pygame.init()
win = pygame.display.set_mode((pr.geometry[0], pr.geometry[1]))
pygame.display.set_caption(pr.caption+f' -v{pr.version}')
clock = pygame.time.Clock()

pl = player.Player(win)
pl.x = fc.load()[0][0]; pl.y = fc.load()[0][1]
rect = pygame.Rect(100, 100, 50, 50)

run = True
while run:
    clock.tick(pr.framerate)
    pygame.display.set_caption(pr.caption + f' -v{pr.version} -- {int(clock.get_fps())}')
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False
    win.fill((0, 0, 0))

    pl.render()
    pl.movement()

    pygame.display.update()
fc.save(pl.x, pl.y)
pygame.quit()