from sharedvars import *
import pygame


def init():
    var.image_set()


def update():
    if var.head_start[0] <= pygame.mouse.get_pos()[0] <= var.head_start[0] + var.head1.get_width() * 2 \
            and var.head_start[1] <= pygame.mouse.get_pos()[1] <= var.head_start[1] + var.head1.get_height():
        var.hover = "head"
    elif var.shol_start[0] <= pygame.mouse.get_pos()[0] <= var.shol_start[0] + var.shol1.get_width() \
            and var.shol_start[1] <= pygame.mouse.get_pos()[1] <= var.shol_start[1] + var.shol1.get_height() or \
            var.shol_start[2] <= pygame.mouse.get_pos()[0] <= var.shol_start[2] + var.shol1.get_width() and \
            var.shol_start[1] <= pygame.mouse.get_pos()[1] <= var.shol_start[1] + var.shol1.get_height():
        var.hover = "shoulder"
    elif var.back_start[0] <= pygame.mouse.get_pos()[0] <= var.back_start[0] + var.back1.get_width() * 2 \
            and var.back_start[1] <= pygame.mouse.get_pos()[1] <= var.back_start[1] + var.back1.get_height():
        var.hover = "back"
    else:
        var.hover = ""


def draw(screen):
    screen.fill((255, 255, 255), (0, 0, var.screen_w, var.screen_h))

    if var.hover == "head":
        screen.blit(var.head1r, var.head_start)
        screen.blit(pygame.transform.flip(var.head1r, True, False),
                    (var.head_start[0] + var.head1r.get_width(), var.head_start[1]))
    else:
        screen.blit(var.head1, var.head_start)
        screen.blit(pygame.transform.flip(var.head1, True, False),
                    (var.head_start[0] + var.head1.get_width(), var.head_start[1]))

    if var.hover == "back":
        screen.blit(var.back1r, var.back_start)
        screen.blit(pygame.transform.flip(var.back1r, True, False),
                    (var.back_start[0] + var.back1r.get_width(), var.back_start[1]))
    else:
        screen.blit(var.back1, var.back_start)
        screen.blit(pygame.transform.flip(var.back1, True, False),
                    (var.back_start[0] + var.back1.get_width(), var.back_start[1]))
        
    if var.hover == "shoulder":
        screen.blit(var.shol1r, (var.shol_start[0], var.shol_start[1]))
        screen.blit(pygame.transform.flip(var.shol1r, True, False),
                    (var.shol_start[2], var.shol_start[1]))
    else:
        screen.blit(var.shol1, (var.shol_start[0], var.shol_start[1]))
        screen.blit(pygame.transform.flip(var.shol1, True, False),
                    (var.shol_start[2], var.shol_start[1]))


def on_event(event):
    pass
