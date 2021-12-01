import pygame

pygame.init()


def update_bar(screen, point):
    # dette er bare en test for at se om det virker
    point_max = 100
    point_min = -100

    unloadedbar = pygame.image.load("Billeder/unloadedbar.png")
    loadedbar = pygame.image.load("Billeder/loadedbar.png")
    unloadedbar_rect = unloadedbar.get_rect()
    loadedbar_rect = loadedbar.get_rect()

    loadedbar_rect.height = 200
    loadedbar_rect.width = 100
    loadedbar = pygame.transform.scale(loadedbar, (160, 320))
    print(loadedbar.get_width())

    unloadedbar_rect.height = 200
    unloadedbar_rect.width = 100
    unloadedbar = pygame.transform.scale(unloadedbar, (160, 320))
    print(unloadedbar.get_width())

    # set det fra dette link: https://stackoverflow.com/questions/20842801/how-to-display-text-in-pygame
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = myfont.render('Some Text', False, (200, 15, 10))
    screen.blit(loadedbar, (0, 0))
    screen.blit(unloadedbar, (0, 0))
    pygame.display.update()
    #if point_min >= point >= point_max():


    pygame.display.flip()
