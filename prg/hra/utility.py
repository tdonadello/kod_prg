# v utility budou pomocné funkce, které využívá více částí našeho programu

import pygame


# funkce, která vyřízne a vrátí správnou část obrázku ze spritesheetu
def get_image(sheet, frame_x, frame_y, width, height, scale):
    img = pygame.Surface((width, height)).convert_alpha()
    img.blit(sheet, (0, 0), ((frame_x * width), (frame_y * height), width, height))
    img = pygame.transform.scale(img, (width*scale, height*scale))
    img.set_colorkey((0, 0, 0))
    return img