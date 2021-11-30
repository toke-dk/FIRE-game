import pygame


def update_bar(screen):
    # dette er bare en test for at se om det virker

    # set det fra dette link: https://stackoverflow.com/questions/20842801/how-to-display-text-in-pygame
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = myfont.render('Some Text', False, (200, 15, 10))
    screen.blit(textsurface, (0,0))
    pygame.display.flip()


    #Jeg kan lide bananer