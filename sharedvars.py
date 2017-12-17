import pygame
import os


class StateSwitcher(Exception):
    def __init__(self, value):
        Exception.__init__(self)
        self.value = value

    def ___str___(self):
        return repr(self.value)


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
        self.retr = None
        self.retrr = None
        self.right = None
        self.left = None
        self.rightr = None
        self.leftr = None
        self.imgDir = "Images"

        self.showlist = []
        self.backlist = []
        self.shollist = []
        self.shownum = 0
        self.arr_offset = 50

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
        self.retr = pygame.image.load(self.imgDir + "\\return.png").convert_alpha()
        self.retrr = pygame.image.load(self.imgDir + "\\returnred.png").convert_alpha()
        self.right = pygame.image.load(self.imgDir + "\\right.png").convert_alpha()
        self.left = pygame.transform.flip(self.right, 1, 0)
        self.rightr = pygame.image.load(self.imgDir + "\\rightred.png").convert_alpha()
        self.leftr = pygame.transform.flip(self.rightr, 1, 0)

        for i in os.listdir(self.imgDir + "\\Back"):
                self.backlist.append(pygame.image.load(self.imgDir + "\\Back\\" + i))
        for i in os.listdir(self.imgDir + "\Shoulders"):
                self.shollist.append(pygame.image.load(self.imgDir + "\Shoulders\\" + i))

        self.shol_start = self.shol_start + (self.shol_start[0] + var.shol1.get_width() + self.shol_break,)


pygame.font.init()
font_tnr = pygame.font.Font(None, 36)

var = Var()
