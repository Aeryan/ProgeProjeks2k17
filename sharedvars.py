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
        self.screen_h = 640
        self.head1 = None
        self.head1r = None
        self.head2 = None
        self.head2r = None
        self.head3 = None
        self.head3r = None
   
        self.back1 = None
        self.back1r = None
        self.back3 = None
        self.back3r = None
        
        self.chest2 = None
        self.chest2r = None
        self.chest3 = None
        self.chest3r = None

        self.abs2 = None
        self.abs2r = None
        self.abs3 = None
        self.abs3r = None
        
        self.foot1 = None
        self.foot1r = None
        self.foot2 = None
        self.foot2r = None
        self.foot3 = None
        self.foot3r = None

        self.arm1 = None
        self.arm1r = None
        self.arm2 = None
        self.arm2r = None
        
        self.shol1 = None
        self.shol1r = None
        self.shol2 = None
        self.shol2r = None
        self.shol3 = None
        self.shol3r = None
        
        self.retr = None
        self.retrr = None
        self.right = None
        self.left = None
        self.rightr = None
        self.leftr = None
        self.imgDir = "Images"

        self.showlist = []
        self.showdata = []
        self.backlist = []
        self.backdata = []
        self.shollist = []
        self.sholdata = []
        self.armslist = []
        self.armsdata = []
        self.legslist = []
        self.legsdata = []
        self.abslist = []
        self.absdata = []
        self.chestlist = []
        self.chestdata = []
        self.shownum = 0
        self.arr_offset = 50

        pygame.font.init()
        self.font = pygame.font.SysFont('Comic Sans MS', 20)

        self.hover = ""
        self.head_start1 = (350, 150)
        self.back_start1 = (self.head_start1[0]-15, self.head_start1[1] + 35)
        self.shol_start1 = (self.head_start1[0]-30, self.head_start1[1] + 45)
        self.shol_break1 = 28
        self.arm_start1 = (self.head_start1[0] - 75, self.head_start1[1] + 62)
        self.arm_break1 = 53
        self.foot_start1 = (self.head_start1[0] - 41, self.head_start1[1] + 120)

        self.head_start2 = (self.head_start1[0] + 300, self.head_start1[1])
        self.back_start2 = (self.head_start2[0] - 15, self.head_start2[1] + 35)
        self.shol_start2 = (self.head_start2[0] - 30, self.head_start2[1] + 45)
        self.shol_break2 = 35
        self.chest_start2 = (self.head_start2[0] - 12, self.head_start2[1] + 40)
        self.abs_start2 = (self.head_start2[0] - 12, self.head_start2[1] + 90)
        self.arm_start2 = (self.head_start2[0] - 75, self.head_start2[1] + 62)
        self.arm_break2 = 47
        self.foot_start2 = (self.head_start2[0] - 38, self.head_start2[1] + 125)

        self.head_start3 = (self.head_start2[0] + 300, self.head_start2[1])
        self.back_start3 = (self.head_start3[0] - 10, self.head_start3[1] + 45)
        self.shol_start3 = (self.head_start3[0] - 5, self.head_start3[1] + 46)
        self.chest_start3 = (self.head_start3[0] + 7, self.head_start3[1] + 48)
        self.abs_start3 = (self.head_start3[0] + 10, self.head_start3[1] + 80)
        self.foot_start3 = (self.head_start3[0] - 5, self.head_start3[1] + 115)

    def image_set(self):
        self.head1 = pygame.image.load(os.path.join(self.imgDir, "head1.png")).convert_alpha()
        self.head1r = pygame.image.load(os.path.join(self.imgDir, "head1red.png")).convert_alpha()
        self.head2 = pygame.image.load(os.path.join(self.imgDir, "head2.png")).convert_alpha()
        self.head2r = pygame.image.load(os.path.join(self.imgDir, "head2red.png")).convert_alpha()
        self.head3 = pygame.image.load(os.path.join(self.imgDir, "head3.png")).convert_alpha()
        self.head3r = pygame.image.load(os.path.join(self.imgDir, "head3red.png")).convert_alpha()
        
        self.back1 = pygame.image.load(os.path.join(self.imgDir, "back1.png")).convert_alpha()
        self.back1r = pygame.image.load(os.path.join(self.imgDir, "back1red.png")).convert_alpha()
        self.back3 = pygame.image.load(os.path.join(self.imgDir, "back3.png")).convert_alpha()
        self.back3r = pygame.image.load(os.path.join(self.imgDir, "back3red.png")).convert_alpha()
        
        self.chest2 = pygame.image.load(os.path.join(self.imgDir, "chest2.png")).convert_alpha()
        self.chest2r = pygame.image.load(os.path.join(self.imgDir, "chest2red.png")).convert_alpha()
        self.chest3 = pygame.image.load(os.path.join(self.imgDir, "chest3.png")).convert_alpha()
        self.chest3r = pygame.image.load(os.path.join(self.imgDir, "chest3red.png")).convert_alpha()
        
        self.abs2 = pygame.image.load(os.path.join(self.imgDir, "abs2.png")).convert_alpha()
        self.abs2r = pygame.image.load(os.path.join(self.imgDir, "abs2red.png")).convert_alpha()
        self.abs3 = pygame.image.load(os.path.join(self.imgDir, "abs3.png")).convert_alpha()
        self.abs3r = pygame.image.load(os.path.join(self.imgDir, "abs3red.png")).convert_alpha()
        
        self.shol1 = pygame.image.load(os.path.join(self.imgDir, "shoulder1.png")).convert_alpha()
        self.shol1r = pygame.image.load(os.path.join(self.imgDir, "shoulder1red.png")).convert_alpha()
        self.shol2 = pygame.image.load(os.path.join(self.imgDir, "shoulder2.png")).convert_alpha()
        self.shol2r = pygame.image.load(os.path.join(self.imgDir, "shoulder2red.png")).convert_alpha()
        self.shol3 = pygame.image.load(os.path.join(self.imgDir, "shoulder3.png")).convert_alpha()
        self.shol3r = pygame.image.load(os.path.join(self.imgDir, "shoulder3red.png")).convert_alpha()
        
        self.arm1 = pygame.image.load(os.path.join(self.imgDir, "arm1.png")).convert_alpha()
        self.arm1r = pygame.image.load(os.path.join(self.imgDir, "arm1red.png")).convert_alpha()
        self.arm2 = pygame.image.load(os.path.join(self.imgDir, "arm2.png")).convert_alpha()
        self.arm2r = pygame.image.load(os.path.join(self.imgDir, "arm2red.png")).convert_alpha()
        
        self.foot1 = pygame.image.load(os.path.join(self.imgDir, "foot1.png")).convert_alpha()
        self.foot1r = pygame.image.load(os.path.join(self.imgDir, "foot1red.png")).convert_alpha()
        self.foot2 = pygame.image.load(os.path.join(self.imgDir, "foot2.png")).convert_alpha()
        self.foot2r = pygame.image.load(os.path.join(self.imgDir, "foot2red.png")).convert_alpha()
        self.foot3 = pygame.image.load(os.path.join(self.imgDir, "foot3.png")).convert_alpha()
        self.foot3r = pygame.image.load(os.path.join(self.imgDir, "foot3red.png")).convert_alpha()

        self.retr = pygame.image.load(os.path.join(self.imgDir, "return.png")).convert_alpha()
        self.retrr = pygame.image.load(os.path.join(self.imgDir, "returnred.png")).convert_alpha()
        self.right = pygame.image.load(os.path.join(self.imgDir, "right.png")).convert_alpha()
        self.left = pygame.transform.flip(self.right, 1, 0)
        self.rightr = pygame.image.load(os.path.join(self.imgDir, "rightred.png")).convert_alpha()
        self.leftr = pygame.transform.flip(self.rightr, 1, 0)

        for i in os.listdir(os.path.join(self.imgDir, "Back")):
                try:
                    self.backlist.append(pygame.image.load(os.path.join(self.imgDir, "Back", i)))
                except pygame.error:
                    f = open(os.path.join(self.imgDir, "Back", i))
                    for j in f:
                        if j[0] != " ":
                            self.backdata.append([])
                        self.backdata[-1].append(j[:-1])
                    f.close()
        for i in os.listdir(os.path.join(os.path.join(self.imgDir, "Shoulders"))):
                try:
                    self.shollist.append(pygame.image.load(os.path.join(self.imgDir, "Shoulders", i)))
                except pygame.error:
                    f = open(os.path.join(self.imgDir, "Shoulders", i))
                    for j in f:
                        if j[0] != " ":
                            self.sholdata.append([])
                        self.sholdata[-1].append(j[:-1])
                    f.close()
        for i in os.listdir(os.path.join(os.path.join(self.imgDir, "Arms"))):
                try:
                    self.armslist.append(pygame.image.load(os.path.join(self.imgDir, "Arms", i)))
                except pygame.error:
                    f = open(os.path.join(self.imgDir, "Arms", i))
                    for j in f:
                        if j[0] != " ":
                            self.armsdata.append([])
                        self.armsdata[-1].append(j[:-1])
                    f.close()
        for i in os.listdir(os.path.join(os.path.join(self.imgDir, "Feet"))):
                try:
                    self.legslist.append(pygame.image.load(os.path.join(self.imgDir, "Feet", i)))
                except pygame.error:
                    f = open(os.path.join(self.imgDir, "Feet", i))
                    for j in f:
                        if j[0] != " ":
                            self.legsdata.append([])
                        self.legsdata[-1].append(j[:-1])
                    f.close()
        for i in os.listdir(os.path.join(os.path.join(self.imgDir, "Abs"))):
                try:
                    self.abslist.append(pygame.image.load(os.path.join(self.imgDir, "Abs", i)))
                except pygame.error:
                    f = open(os.path.join(self.imgDir, "Abs", i))
                    for j in f:
                        if j[0] != " ":
                            self.absdata.append([])
                        self.absdata[-1].append(j[:-1])
                    f.close()
        for i in os.listdir(os.path.join(os.path.join(self.imgDir, "Chest"))):
                try:
                    self.chestlist.append(pygame.image.load(os.path.join(self.imgDir, "Chest", i)))
                except pygame.error:
                    f = open(os.path.join(self.imgDir, "Chest", i))
                    for j in f:
                        if j[0] != " ":
                            self.chestdata.append([])
                        self.chestdata[-1].append(j[:-1])
                    f.close()

        self.shol_start1 = self.shol_start1 + (self.shol_start1[0] + var.shol1.get_width() + self.shol_break1,)
        self.arm_start1 = self.arm_start1 + (self.arm_start1[0] + var.arm1.get_width() + self.arm_break1,)
        self.shol_start2 = self.shol_start2 + (self.shol_start2[0] + var.shol2.get_width() + self.shol_break2,)
        self.arm_start2 = self.arm_start2 + (self.arm_start2[0] + var.arm2.get_width() + self.arm_break2,)


pygame.font.init()
font_tnr = pygame.font.Font(None, 36)

var = Var()
