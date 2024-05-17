import pygame


class Desk(pygame.sprite.Sprite):
    def __init__(self, image, width, height, position):
        super().__init__()
        self.image = image
        self.width = width
        self.height = height
        self.position = position
        self.scale = 0.8
        self.scale_desk()
        self.rect = self.image.get_rect(topleft=self.position)
    
    def scale_desk(self):
        scaled_size = (self.width * self.scale, self.height * self.scale)

        self.image = pygame.transform.scale(self.image, scaled_size)


class Coin(pygame.sprite.Sprite):
    def __init__(self, image, width, height, position):
        super().__init__()
        self.image = image
        self.width = width
        self.height = height
        self.position = position
        self.scale = 0.8
        self.scale_coin()
        self.rect = self.image.get_rect(topleft=self.position)
    
    def scale_coin(self):
        scaled_size = (self.width * self.scale, self.height * self.scale)

        self.image = pygame.transform.scale(self.image, scaled_size)


class PowerUp(pygame.sprite.Sprite):
    def __init__(self, image, width, height, position):
        super().__init__()
        self.image = image
        self.width = width
        self.height = height
        self.position = position
        self.scale = 0.8
        self.scale_pu()
        self.rect = self.image.get_rect(topleft=self.position)
    
    def scale_pu(self):
        scaled_size = (self.width * self.scale, self.height * self.scale)

        self.image = pygame.transform.scale(self.image, scaled_size)