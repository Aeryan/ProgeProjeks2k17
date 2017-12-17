import pygame


class Var:

    def __init__(self):
        self.screen_w = 1280
        self.screen_h = 500
        self.hand1 = None
        self.head1 = None
        self.foot1 = None
        self.back1 = None
        self.shoulder1 = None
        self.imgDir = "Images"

    def image_set(self):
        self.head1 = pygame.image.load(self.imgDir + "\head1.png").convert_alpha()
        self.foot1 = pygame.image.load(self.imgDir + "\\foot1.png").convert()
        self.hand1 = pygame.image.load(self.imgDir + "\hand1.png").convert_alpha()
        self.back1 = pygame.image.load(self.imgDir + "\\back1.png").convert_alpha()
        self.shoulder1 = pygame.image.load(self.imgDir + "\shoulder1.png").convert_alpha()


pygame.font.init()
font_tnr = pygame.font.Font(None, 36)

var = Var()
