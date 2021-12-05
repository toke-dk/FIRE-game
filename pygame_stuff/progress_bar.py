import pygame

pygame.init()


def update_bar(screen, point):
    # dette er bare en test for at se om det virker

    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 30)

    loadedbar = pygame.image.load("Billeder/loadedbar.png")
    percent_color = (0,0,255)
    if round(point, 1) < 0:
        percent_color = (255,0,0)
    percent_text = myfont.render(f"{round(point, 1)}%", False, percent_color)
    screen.blit(percent_text, (screen.get_height(), screen.get_width()//2))

    loadedbar = pygame.transform.scale(loadedbar, (300, 600))
    loadedbar_rect = loadedbar.get_rect()

    point_max = 100
    point_min = -100
    x_load = screen.get_width()//1.3
    y_load = screen.get_height()//8
    y_margin_load_bar = 105
    x_margin_load_bar = 73
    black = (255, 255, 255)

    if point_min <= point <= point_max:
        y_bar = (y_load + y_margin_load_bar + (loadedbar_rect.height-2*y_margin_load_bar)//2) - ((point/100 * (loadedbar_rect.height-2*y_margin_load_bar))/2)

    elif point_min >= point:
        y_bar = y_load+loadedbar_rect.height-y_margin_load_bar-10

    elif point_max <= point:
        y_bar = y_load+y_margin_load_bar



    # set det fra dette link: https://stackoverflow.com/questions/20842801/how-to-display-text-in-pygame

    textsurface = myfont.render('Some Text', False, (200, 15, 10))
    screen.blit(loadedbar, (x_load, y_load))

    pygame.draw.rect(screen, black, (x_load+x_margin_load_bar, y_bar, loadedbar_rect.width-2*x_margin_load_bar, 10))

