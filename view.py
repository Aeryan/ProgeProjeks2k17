from sharedvars import *
import pygame


def init():
    if var.hover == "back":
        var.showlist = var.backlist
    elif var.hover == "shoulder":
        var.showlist = var.shollist
    elif var.hover == "arm":
        var.showlist = var.armslist
    elif var.hover == "foot":
        var.showlist = var.legslist
    var.hover = ""


def update():
    if var.screen_w - var.retr.get_width() <= pygame.mouse.get_pos()[0] <= var.screen_w \
            and 0 <= pygame.mouse.get_pos()[1] <= var.retr.get_height():
        var.hover = "return"
    elif var.screen_w-var.rightr.get_width() - var.arr_offset <= pygame.mouse.get_pos()[0] <= var.screen_w - \
            var.arr_offset and (var.screen_h-var.right.get_height())/2 <= pygame.mouse.get_pos()[1] \
            <= (var.screen_h+var.right.get_height())/2:
        var.hover = "right"
    elif var.arr_offset <= pygame.mouse.get_pos()[0] <= var.arr_offset + var.left.get_width() \
            and (var.screen_h-var.right.get_height())/2 <= pygame.mouse.get_pos()[1] \
            <= (var.screen_h+var.right.get_height())/2:
        var.hover = "left"
    else:
        var.hover = ""


def draw(screen):
    screen.fill((255, 255, 255))

    if var.hover == "return":
        screen.blit(var.retrr, (var.screen_w-var.retr.get_width(), 0))
    else:
        screen.blit(var.retr, (var.screen_w-var.retr.get_width(), 0))

    if var.hover == "right":
        screen.blit(var.rightr, (var.screen_w-var.rightr.get_width() - var.arr_offset,
                                 (var.screen_h-var.right.get_height())/2))
    else:
        screen.blit(var.right, (var.screen_w-var.right.get_width() - var.arr_offset,
                                (var.screen_h-var.right.get_height())/2))

    if var.hover == "left":
        screen.blit(var.leftr, (var.arr_offset, (var.screen_h-var.left.get_height())/2))
    else:
        screen.blit(var.left, (var.arr_offset, (var.screen_h-var.left.get_height())/2))
    screen.blit(var.showlist[var.shownum], ((var.screen_w - var.showlist[var.shownum].get_width())/2,
                                            (var.screen_h - var.showlist[var.shownum].get_height())/2))


def on_event(event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if var.hover == "return":
            raise StateSwitcher("selector")
        elif var.hover == "left":
            if var.shownum == 0:
                var.shownum = len(var.showlist) - 1
            else:
                var.shownum -= 1
        elif var.hover == "right":
            if var.shownum == len(var.showlist) - 1:
                var.shownum = 0
            else:
                var.shownum += 1
