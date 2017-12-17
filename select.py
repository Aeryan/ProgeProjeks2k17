from sharedvars import *
import pygame


def init():
    var.image_set()


def update():
    if var.head_start[0] <= pygame.mouse.get_pos()[0] <= var.head_start[0] + var.head1.get_width() * 2 \
            and var.head_start[1] <= pygame.mouse.get_pos()[1] <= var.head_start[1] + var.head1.get_height():
        var.hover = "head"
    else:
        var.hover = ""


def draw(screen):
    screen.fill((255, 255, 255), (0, 0, var.screen_w, var.screen_h))
    if var.hover == "head":
        screen.blit(var.head1r, (100, 100))
        screen.blit(pygame.transform.flip(var.head1r, True, False), (100 + var.head1r.get_width(), 100))
    else:
        screen.blit(var.head1, (100, 100))
        screen.blit(pygame.transform.flip(var.head1, True, False), (100 + var.head1.get_width(), 100))


def on_event(event):
    pass
