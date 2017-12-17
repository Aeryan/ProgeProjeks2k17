from sharedvars import *
import pygame


def init():
    var.image_set()
    pygame.display.set_caption("Personaaltreener")


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
    elif var.foot_start[0] <= pygame.mouse.get_pos()[0] <= var.foot_start[0] + var.foot1.get_width() * 2 \
            and var.foot_start[1] <= pygame.mouse.get_pos()[1] <= var.foot_start[1] + var.foot1.get_height():
        var.hover = "foot"
    elif var.arm_start[0] <= pygame.mouse.get_pos()[0] <= var.arm_start[0] + var.arm1.get_width() \
            and var.arm_start[1] <= pygame.mouse.get_pos()[1] <= var.arm_start[1] + var.arm1.get_height() or \
            var.arm_start[2] <= pygame.mouse.get_pos()[0] <= var.arm_start[2] + var.arm1.get_width() and \
            var.arm_start[1] <= pygame.mouse.get_pos()[1] <= var.arm_start[1] + var.arm1.get_height():
        var.hover = "arm"
    else:
        var.hover = ""


def draw(screen):
    screen.fill((255, 255, 255))

    if var.hover == "head":
        screen.blit(var.head1r, var.head_start)
        screen.blit(pygame.transform.flip(var.head1r, True, False),
                    (var.head_start[0] + var.head1r.get_width(), var.head_start[1]))
    else:
        screen.blit(var.head1, var.head_start)
        screen.blit(pygame.transform.flip(var.head1, True, False),
                    (var.head_start[0] + var.head1.get_width(), var.head_start[1]))
        
    if var.hover == "foot":
        screen.blit(var.foot1r, var.foot_start)
        screen.blit(pygame.transform.flip(var.foot1r, True, False),
                    (var.foot_start[0] + var.foot1r.get_width(), var.foot_start[1]))
    else:
        screen.blit(var.foot1, var.foot_start)
        screen.blit(pygame.transform.flip(var.foot1, True, False),
                    (var.foot_start[0] + var.foot1.get_width(), var.foot_start[1]))

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
    
    if var.hover == "arm":
        screen.blit(var.arm1r, (var.arm_start[0], var.arm_start[1]))
        screen.blit(pygame.transform.flip(var.arm1r, True, False),
                    (var.arm_start[2], var.arm_start[1]))
    else:
        screen.blit(var.arm1, (var.arm_start[0], var.arm_start[1]))
        screen.blit(pygame.transform.flip(var.arm1, True, False),
                    (var.arm_start[2], var.arm_start[1]))
    

def on_event(event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if var.hover != "":
            raise StateSwitcher("view")
