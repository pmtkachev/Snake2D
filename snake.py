import pygame


class SnakePlayer(pygame.Rect):
    def __init__(self, x, y, scr):
        self.x = x
        self.y = y
        self.scr = scr
        self.width = 20
        self.height = 20
        self.speed = 5
        self.color = (17, 24, 15)
        self.up, self.down, self.r_way, self.l_way = False, False, False, False
        super().__init__((self.x, self.y, self.width, self.height))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.up, self.down, self.r_way, self.l_way = True, False, False, False
        if keys[pygame.K_DOWN]:
            self.up, self.down, self.r_way, self.l_way = False, True, False, False
        if keys[pygame.K_LEFT]:
            self.up, self.down, self.r_way, self.l_way = False, False, False, True
        if keys[pygame.K_RIGHT]:
            self.up, self.down, self.r_way, self.l_way = False, False, True, False

        if self.up:
            self.y -= 5
        if self.down:
            self.y += 5
        if self.l_way:
            self.x -= 5
        if self.r_way:
            self.x += 5

        if self.bottom <= 0:
            self.bottom = 605
        if self.top >= 600:
            self.top = -20
        if self.right <= 0:
            self.right = 605
        if self.left >= 600:
            self.left = -20
        pygame.draw.rect(self.scr, self.color, self)
