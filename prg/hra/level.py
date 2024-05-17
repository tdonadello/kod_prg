import pygame
# potřeba nainstalovat pomocí pip install pytmx
# umožní pracovat s .tmx soubory, které vytváří program Tiles, který používáme k vytvoření herního světa
from pytmx.util_pygame import load_pygame
from items import Desk, Coin, PowerUp
from monster import Monster
from player import Player


# vytvoř classu Level - jedná se o čistou pythonovskou classu, které nedědí vlastnosti žádné předchozí classy
# pytmx vyžaduje informace o screenu, proto jej musíme přidat do __init__ naší classy
class Level:
    def __init__(self, level_data, screen, sprite_groups):
        # využij funkci load_pygame, kterou jsme importovali z pytmx výše a načti data k levelu
        self.data = load_pygame(level_data)
        self.screen = screen
        self.sprite_groups = sprite_groups

        # pro každou vrstvu z vrstev, které se nacházejí v našem souboru s herním světem, vytvoř attribut (self.něco)
        for layer in self.data.visible_layers:
            setattr(self, layer.name, self.data.get_layer_by_name(layer.name))

        for key, group in sprite_groups.items():
            setattr(self, key, group)

        # vytvoř Surface pro pozadí - velikost pozadí je odvozena od velikosti herního světa a rozměrů jednotlivých tiles (dlaždic)
        self.background = pygame.Surface((self.data.width * self.data.tilewidth, self.data.height * self.data.tileheight))

        # spusť funkci create_desk() při vytvoření classy        
        self.init_items()

        

    def draw_background(self):
        # ve vrstvě self.ground má každý tiles 3 vlastnosti - pozici x a y a grafiku (obrázek)
        # pro každý tiles blitneme grafiku na self.background vytvořené výše a na souřadnice x a y které jsme získali z .tmx souboru
        for x, y, image in self.ground.tiles():
            self.background.blit(image, (x * self.data.tilewidth, y * self.data.tileheight))
        
        # vytvořené pozadí blitneme na obrazovku na souřadnice 0,0 - úplně nahoru
        self.screen.blit(self.background, (0,0))

    def init_items(self):
        self.create_items(self.furniture, Desk, self.desks_group)
        self.create_items(self.spawn_coins, Coin, self.coins_group)
        self.create_items(self.spawn_powerups, PowerUp, self.powerups_group)
        self.create_monsters(self.spawn_enemies_h, self.monsters_group)
        self.create_player(self.spawn_player, self.player_group)


    def create_items(self, layer, item_class, group):
        for item in layer:
            new_item = item_class(item.image, item.width, item.height, (item.x, item.y))
            group.add(new_item)
            self.all.add(new_item)

    def create_monsters(self, layer, group):
        for monster in layer:
            new_monster = Monster((monster.x, monster.y))
            group.add(new_monster)
            self.all.add(new_monster)
            
    def create_player(self, layer, group):
        for player in layer:
            new_player = Player((player.x, player.y), self.sprite_groups)
            group.add(new_player)
            self.all.add(new_player)
        