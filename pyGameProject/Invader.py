import pygame
import Colors


class Invader:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 20

    def draw(self, pygame_window):
        pygame.draw.rect(pygame_window, Colors.white, (self.x, self.y, self.width, self.height))

    def move_in_y(self, pygame_window):
        self.y += 20
        self.draw(pygame_window)


    # def update(self):