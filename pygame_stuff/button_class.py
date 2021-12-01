import pygame


class Button(pygame.sprite.Sprite):
    def __init__(self, screen, pos_x, pos_y, BUTTON_WIDTH, BUTTON_HEIGHT, first_col, hover_col, text, text_col, font):
        pygame.sprite.Sprite.__init__(self)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.first_col = first_col
        self.hover_col = hover_col
        self.zoom_scale = 1.05
        self.screen = screen
        self.font = font
        self.BUTTON_WIDTH = BUTTON_WIDTH
        self.BUTTON_HEIGHT = BUTTON_HEIGHT

        self.Rect = pygame.Rect(self.pos_x, self.pos_y, self.BUTTON_WIDTH, self.BUTTON_HEIGHT)
        self.text_img = self.font.render(text, True, text_col)
        self.text_rect = self.text_img.get_rect()
        self.text_rect.center = (self.pos_x, self.pos_y)

    def action(self, click_x, click_y):
        if click_x > self.Rect.left and click_x < self.Rect.right and click_y > self.Rect.top and click_y < self.Rect.bottom:
            return True

    def draw(self, cursor_x, cursor_y):

        if cursor_x > self.Rect.left and cursor_x < self.Rect.right and cursor_y > self.Rect.top and cursor_y < self.Rect.bottom:
            btn_color = self.hover_col
            self.Rect.width = int(self.BUTTON_WIDTH * self.zoom_scale)
            self.Rect.height = int(self.BUTTON_HEIGHT * self.zoom_scale)

        else:
            btn_color = self.first_col
            self.Rect.width = self.BUTTON_WIDTH
            self.Rect.height = self.BUTTON_HEIGHT

        self.Rect.center = (self.pos_x, self.pos_y)
        pygame.draw.rect(self.screen, btn_color, self.Rect, border_radius=10)

        self.screen.blit(self.text_img, self.text_rect)