import pygame
from random import randint


class Enemy:
    size = 0
    speed = 2
    window_width = 0
    window_height = 0

    def __init__(self, width, height, block_size):
        self.size = block_size
        self.window_width = width
        self.window_height = height
        self.pos_x = randint(0, width-self.size)
        self.pos_y = randint(-1 * height, 0)
        self.image = pygame.image.load("coconut.png")
        self.image.convert()
        # self.speed = randint(4, 7)

    def draw(self, display):
        # display.blit(self.image, (self.pos_x, self.pos_y))
        pygame.draw.rect(display, (255, 0, 0), [self.pos_x, self.pos_y, self.size, self.size])

    def reset(self):
        self.pos_x = randint(0, self.window_width - self.size)
        self.pos_y = randint(-1 * self.window_height, 0)

    def move_y(self, height, level):
        if self.pos_y > height:
            self.reset()
            return 1
        else:
            self.pos_y += self.speed + level
            return 0
