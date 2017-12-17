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
        self.head1 = None
        self.head1r = None
        self.foot1 = None
        self.foot1r = None
        self.arm1 = None
        self.arm1r = None
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
        self.armslist = []
        self.legslist = []
        self.shownum = 0
        self.arr_offset = 50

        self.hover = ""
        self.head_start = (300, 100)
        self.back_start = (285, 135)
        self.shol_start = (270, 145)
        self.shol_break = 28
        self.arm_start = (225, 162)
        self.arm_break = 53
        self.foot_start = (259, 220)

    def image_set(self):
        self.head1 = pygame.image.load(os.path.join(self.imgDir, "head1.png")).convert_alpha()
        self.head1r = pygame.image.load(os.path.join(self.imgDir, "head1red.png")).convert_alpha()
        self.foot1 = pygame.image.load(os.path.join(self.imgDir, "foot1.png")).convert()
        self.back1 = pygame.image.load(os.path.join(self.imgDir, "back1.png")).convert_alpha()
        self.back1r = pygame.image.load(os.path.join(self.imgDir, "back1red.png")).convert_alpha()
        self.shol1 = pygame.image.load(os.path.join(self.imgDir, "shoulder1.png")).convert_alpha()
        self.shol1r = pygame.image.load(os.path.join(self.imgDir, "shoulder1red.png")).convert_alpha()
        self.arm1 = pygame.image.load(os.path.join(self.imgDir, "arm1.png")).convert_alpha()
        self.arm1r = pygame.image.load(os.path.join(self.imgDir, "arm1red.png")).convert_alpha()
        self.foot1 = pygame.image.load(os.path.join(self.imgDir, "foot1.png")).convert_alpha()
        self.foot1r = pygame.image.load(os.path.join(self.imgDir, "foot1red.png")).convert_alpha()

        self.retr = pygame.image.load(os.path.join(self.imgDir, "return.png")).convert_alpha()
        self.retrr = pygame.image.load(os.path.join(self.imgDir, "returnred.png")).convert_alpha()
        self.right = pygame.image.load(os.path.join(self.imgDir, "right.png")).convert_alpha()
        self.left = pygame.transform.flip(self.right, 1, 0)
        self.rightr = pygame.image.load(os.path.join(self.imgDir, "rightred.png")).convert_alpha()
        self.leftr = pygame.transform.flip(self.rightr, 1, 0)

        for i in os.listdir(os.path.join(self.imgDir, "Back")):
                self.backlist.append(pygame.image.load(os.path.join(self.imgDir, "Back", i)))
        for i in os.listdir(os.path.join(os.path.join(self.imgDir, "Shoulders"))):
                self.shollist.append(pygame.image.load(os.path.join(self.imgDir, "Shoulders", i)))
        for i in os.listdir(os.path.join(os.path.join(self.imgDir, "Arms"))):
                self.armslist.append(pygame.image.load(os.path.join(self.imgDir, "Arms", i)))
        for i in os.listdir(os.path.join(os.path.join(self.imgDir, "Feet"))):
                self.legslist.append(pygame.image.load(os.path.join(self.imgDir, "Feet", i)))

        self.shol_start = self.shol_start + (self.shol_start[0] + var.shol1.get_width() + self.shol_break,)
        self.arm_start = self.arm_start + (self.arm_start[0] + var.arm1.get_width() + self.arm_break,)


pygame.font.init()
font_tnr = pygame.font.Font(None, 36)

var = Var()
