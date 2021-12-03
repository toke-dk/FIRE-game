import pygame

pygame.init()


def update_bar(screen, point):
    # dette er bare en test for at se om det virker
    point_max = 100
    point_min = -100
    x_load = 270
    black = (0, 0, 0)

    if point_min <= point <= point_max:
        y_bar = 400 - (point*2.35)

    elif point_min >= point:
        y_bar = 665

    elif point_max <= point:
        y_bar = 165

    loadedbar = pygame.image.load("Billeder/loadedbar.png")
    loadedbar_rect = loadedbar.get_rect()

    loadedbar_rect.height = 800
    loadedbar_rect.width = 400
    loadedbar = pygame.transform.scale(loadedbar, (400, 800))

    # set det fra dette link: https://stackoverflow.com/questions/20842801/how-to-display-text-in-pygame
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = myfont.render('Some Text', False, (200, 15, 10))
    screen.blit(loadedbar, (x_load, 20))

    pygame.draw.rect(screen, black, (368, y_bar, 206, 10), width=0, border_radius=0, border_top_left_radius=-1,
                     border_top_right_radius=-1, border_bottom_left_radius=-1, border_bottom_right_radius=-1)

