import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, picture_path, pos_x, pos_y):
        super().__init__()
        self.image = pygame.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]