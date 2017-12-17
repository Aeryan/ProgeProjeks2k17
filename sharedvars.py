import pygame


class Var:

    def __init__(self):
        self.screen_w = 1280
        self.screen_h = 600
        self.hand1 = None
        self.head1 = None
        self.head1r = None
        self.foot1 = None
        self.back1 = None
        self.back1r = None
        self.shol1 = None
        self.shol1r = None
        self.imgDir = "Images"

        self.hover = ""
        self.head_start = (100, 100)
        self.back_start = (85, 135)
        self.shol_start = (70, 145)
        self.shol_break = 28

    def image_set(self):
        self.head1 = pygame.image.load(self.imgDir + "\head1.png").convert_alpha()
        self.head1r = pygame.image.load(self.imgDir + "\head1red.png").convert_alpha()
        self.foot1 = pygame.image.load(self.imgDir + "\\foot1.png").convert()
        self.hand1 = pygame.image.load(self.imgDir + "\hand1.png").convert_alpha()
        self.back1 = pygame.image.load(self.imgDir + "\\back1.png").convert_alpha()
        self.back1r = pygame.image.load(self.imgDir + "\\back1red.png").convert_alpha()
        self.shol1 = pygame.image.load(self.imgDir + "\shoulder1.png").convert_alpha()
        self.shol1r = pygame.image.load(self.imgDir + "\shoulder1red.png").convert_alpha()

        self.shol_start = self.shol_start + (self.shol_start[0] + var.shol1.get_width() + self.shol_break,)


pygame.font.init()
font_tnr = pygame.font.Font(None, 36)

var = Var()
