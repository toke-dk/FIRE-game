import pygame



def update_bar(screen, point, unloadedbar, loadedbar):
    # dette er bare en test for at se om det virker
    point_max = 100
    point_min = -100


    unloadedbar_rect = unloadedbar.get_rect()
    loadedbar_rect = loadedbar.get_rect()

    unloadedbar_rect.x = 100
    unloadedbar_rect.y = 200

    loadedbar_rect.height = 200
    loadedbar_rect.width = 100
    loadedbar = pygame.transform.scale(loadedbar, (20, 40))
    print(loadedbar.get_width())


    # set det fra dette link: https://stackoverflow.com/questions/20842801/how-to-display-text-in-pygame
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = myfont.render('Some Text', False, (200, 15, 10))
    screen.blit(loadedbar, (0,0))
    pygame.display.update()
    #if point_min >= point >= point_max():


    pygame.display.flip()
