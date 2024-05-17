import pygame
from sys import exit

# inicializuje hru - spustíme pygame
pygame.init()

# vytvoř hodiny
clock = pygame.time.Clock()


# naše proměnné, které udávají výšku a šířku
screen_height = 600
screen_width = 800
# vytvoříme obraz
screen = pygame.display.set_mode((screen_width, screen_height))


def monster_animation():
    global monster_surf, monster_index
    monster_index += 0.1

    if monster_index > len(monster_walk):
        monster_index = 0
    monster_surf = monster_walk[int(monster_index)]


# player_x a player_y v nové verzi kódu už řeší pouze spawn
player_x = 100
player_y = 200
# vytvoření surface pro postavičku hráče - načtení obrázku
player_surf = pygame.image.load("player_sprite.png").convert_alpha()

# kvůli detekci kolize nejprve vytvoříme rectangle pro hráče
player_rect = player_surf.get_rect(midbottom=(player_x, player_y))


# vytvoření surface pro postavičku monster - nepřítele - načtení obrázku
monster_walk_1 = pygame.image.load("monster_sprite.png").convert_alpha()
monster_walk_2 = pygame.image.load("monster_sprite_walk.png").convert_alpha()
monster_walk = [monster_walk_1, monster_walk_2]
monster_index = 0

monster_surf = monster_walk[monster_index]
# kvůli detekci kolize nejprve vytvoříme rectangle pro monstrum
monster_rect = monster_surf.get_rect(midbottom=(300, 600))

# počítání životů - začátek
lives = 3

# vytvoření fontu - None znamená defaultní font, 25 je velikost
font = pygame.font.Font(None, 25)

monster_direction = "Left"

game_over = False

# herní smyčka
while True:
    # kontroluje nám události, které se dějí v naší hře
    for event in pygame.event.get():
        # pokud dojde k události vypnout, vypne
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if game_over == False:

        # proměnná key, pod ní schováme stisknutou klávesu
        key = pygame.key.get_pressed()

        # pokud je stisknutá šipka doleva, atd.
        # změna ovládání - nyní pohybujeme vytvořením rectanglem
        if key[pygame.K_LEFT]:
            player_rect.left -= 10
        elif key[pygame.K_RIGHT]:
            player_rect.right += 10
        elif key[pygame.K_UP]:
            player_rect.top -= 10
        elif key[pygame.K_DOWN]:
            player_rect.bottom += 10

        # obarví obrazovku na bílo
        screen.fill((255, 255, 255))

        # renderování našeho fontu - pomocí fontu vytvoříme text, antialiasing a barvu
        text = font.render(f"Lives: {lives}", False, "#000000")

        # text vypíšeme do obrazovky
        screen.blit(text, (700, 10))

        # pohyb monstra
        if monster_rect.x <= 0:
            monster_direction = "Right"
        elif monster_rect.x >= screen_width - 50:
            monster_direction = "Left"
        
        if monster_direction == "Left":
            monster_rect.x -= 5
        if monster_direction == "Right":
            monster_rect.x += 5


        monster_animation()
        # na screen vykresli - surface hráče, na x,y
        screen.blit(player_surf, player_rect)
        # na screen vykresli - surface monstra, na x,y
        screen.blit(monster_surf, monster_rect)

        # detekce kolize a ubírání životů v případě kolize
        if player_rect.colliderect(monster_rect):
            lives -= 1
        if lives <= 0:
            game_over = True

    else:
        screen.fill((0, 0, 0))
        

    # updatuje vše
    pygame.display.update()

    # omez tickrate (jak rychle hra poběží) na 60 fps
    clock.tick(60)
