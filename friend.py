import pygame


class Friend:
    size = 0
    speed = 5
    window_width = 0
    window_height = 0

    def __init__(self, width, height, block_size):
        self.size = block_size
        self.window_width = width
        self.window_height = height
        self.pos_x = width/2
        self.pos_y = height-self.size

    def draw(self, display):
        pygame.draw.rect(display, (0, 0, 255), [self.pos_x, self.pos_y, self.size, self.size])

    def move_x(self, distance):
        if distance <= 0:
            if self.pos_x > 0:
                self.pos_x += distance * self.speed
        else:
            if self.pos_x < self.window_width-self.size:
                self.pos_x += distance * self.speed
