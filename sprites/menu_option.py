import pygame as pg

from settings import *


class MenuOption(pg.sprite.Sprite):
    def __init__(self, x, y, width=250, height=100, active=False, font="", text="Default Menu Text"):
        """
        x, y - position of top left corner on the screen
        height, width - dimensions in pixels
        """
        pg.sprite.Sprite.__init__(self)
        self.font = font
        # top left coordinate
        self.x, self.y = x, y
        self.text = "Start Game"
        self.width = width
        self.height = height
        self.active = active
        # Replace with the size of the option
        self.image = pg.Surface((self.width, self.height))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.text = text
        # this is the function to be called on this menu option being selected
        self.on_select = None

    def toggle_active(self):
        if self.active:
            self.active = False
        else:
            self.active = True

    def draw(self, screen):
        if self.active:
            color = YELLOW
        else:
            color = GREEN

        # Draw left vertical line
        pg.draw.line(screen, color, (self.x, self.y), (self.x, self.y+self.height))
        # Draw right vertical line
        pg.draw.line(screen, color, (self.x+self.width, self.y), (self.x+self.width, self.y+self.height))
        # draw top horizontal line
        pg.draw.line(screen, color, (self.x, self.y), (self.x+self.width, self.y))
        # draw bottom horizontal line
        pg.draw.line(screen, color, (self.x, self.y+self.height), (self.x+self.width, self.y+self.height))
        # render(Text, Antialias, Color, Background=None)
        text_surface = self.font.render(self.text, False, (0, 0, 0))

        center_of_option = (self.x+self.width/2, self.y+self.height/2)
        screen.blit(text_surface, text_surface.get_rect(center=center_of_option))
