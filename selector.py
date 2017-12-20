from sharedvars import *
import pygame


def init():
    var.image_set()
    pygame.display.set_caption("Personaaltreener")


def update():
    if var.head_start1[0] <= pygame.mouse.get_pos()[0] <= var.head_start1[0] + var.head1.get_width() * 2 \
            and var.head_start1[1] <= pygame.mouse.get_pos()[1] <= var.head_start1[1] + var.head1.get_height():
        var.hover = "head"
    elif var.head_start2[0] <= pygame.mouse.get_pos()[0] <= var.head_start2[0] + var.head2.get_width() * 2 \
            and var.head_start2[1] <= pygame.mouse.get_pos()[1] <= var.head_start2[1] + var.head2.get_height():
        var.hover = "head"
    elif var.head_start3[0] <= pygame.mouse.get_pos()[0] <= var.head_start3[0] + var.head3.get_width() * 2 \
            and var.head_start3[1] <= pygame.mouse.get_pos()[1] <= var.head_start3[1] + var.head3.get_height():
        var.hover = "head"

    elif var.shol_start1[0] <= pygame.mouse.get_pos()[0] <= var.shol_start1[0] + var.shol1.get_width() \
            and var.shol_start1[1] <= pygame.mouse.get_pos()[1] <= var.shol_start1[1] + var.shol1.get_height() or \
            var.shol_start1[2] <= pygame.mouse.get_pos()[0] <= var.shol_start1[2] + var.shol1.get_width() and \
            var.shol_start1[1] <= pygame.mouse.get_pos()[1] <= var.shol_start1[1] + var.shol1.get_height():
        var.hover = "shoulder"
    elif var.shol_start2[0] <= pygame.mouse.get_pos()[0] <= var.shol_start2[0] + var.shol2.get_width() \
            and var.shol_start2[1] <= pygame.mouse.get_pos()[1] <= var.shol_start2[1] + var.shol1.get_height() or \
            var.shol_start2[2] <= pygame.mouse.get_pos()[0] <= var.shol_start2[2] + var.shol2.get_width() and \
            var.shol_start2[1] <= pygame.mouse.get_pos()[1] <= var.shol_start2[1] + var.shol2.get_height():
        var.hover = "shoulder"
    elif var.shol_start3[0] <= pygame.mouse.get_pos()[0] <= var.shol_start3[0] + var.shol3.get_width() \
            and var.shol_start3[1] <= pygame.mouse.get_pos()[1] <= var.shol_start3[1] + var.shol3.get_height():
        var.hover = "shoulder"
    
    elif var.back_start1[0] <= pygame.mouse.get_pos()[0] <= var.back_start1[0] + var.back1.get_width() * 2 \
            and var.back_start1[1] <= pygame.mouse.get_pos()[1] <= var.back_start1[1] + var.back1.get_height():
        var.hover = "back"
    elif var.back_start3[0] <= pygame.mouse.get_pos()[0] <= var.back_start3[0] + var.back3.get_width() \
            and var.back_start3[1] <= pygame.mouse.get_pos()[1] <= var.back_start3[1] + var.back3.get_height():
        var.hover = "back"
        
    elif var.chest_start2[0] <= pygame.mouse.get_pos()[0] <= var.chest_start2[0] + var.chest2.get_width() * 2 \
            and var.chest_start2[1] <= pygame.mouse.get_pos()[1] <= var.chest_start2[1] + var.chest2.get_height():
        var.hover = "chest"
    elif var.chest_start3[0] <= pygame.mouse.get_pos()[0] <= var.chest_start3[0] + var.chest3.get_width() \
            and var.chest_start3[1] <= pygame.mouse.get_pos()[1] <= var.chest_start3[1] + var.chest3.get_height():
        var.hover = "chest"
    
    elif var.abs_start2[0] <= pygame.mouse.get_pos()[0] <= var.abs_start2[0] + var.abs2.get_width() * 2 \
            and var.abs_start2[1] <= pygame.mouse.get_pos()[1] <= var.abs_start2[1] + var.abs2.get_height():
        var.hover = "abs"
    elif var.abs_start3[0] <= pygame.mouse.get_pos()[0] <= var.abs_start3[0] + var.abs3.get_width() \
            and var.abs_start3[1] <= pygame.mouse.get_pos()[1] <= var.abs_start3[1] + var.abs3.get_height():
        var.hover = "abs"

    elif var.foot_start1[0] <= pygame.mouse.get_pos()[0] <= var.foot_start1[0] + var.foot1.get_width() * 2 \
            and var.foot_start1[1] <= pygame.mouse.get_pos()[1] <= var.foot_start1[1] + var.foot1.get_height():
        var.hover = "foot"
    elif var.foot_start2[0] <= pygame.mouse.get_pos()[0] <= var.foot_start2[0] + var.foot2.get_width() * 2 \
            and var.foot_start2[1] <= pygame.mouse.get_pos()[1] <= var.foot_start2[1] + var.foot2.get_height():
        var.hover = "foot"
    elif var.foot_start3[0] <= pygame.mouse.get_pos()[0] <= var.foot_start3[0] + var.foot3.get_width() \
            and var.foot_start3[1] <= pygame.mouse.get_pos()[1] <= var.foot_start3[1] + var.foot3.get_height():
        var.hover = "foot"

    elif var.arm_start1[0] <= pygame.mouse.get_pos()[0] <= var.arm_start1[0] + var.arm1.get_width() \
            and var.arm_start1[1] <= pygame.mouse.get_pos()[1] <= var.arm_start1[1] + var.arm1.get_height() or \
            var.arm_start1[2] <= pygame.mouse.get_pos()[0] <= var.arm_start1[2] + var.arm1.get_width() and \
            var.arm_start1[1] <= pygame.mouse.get_pos()[1] <= var.arm_start1[1] + var.arm1.get_height():
        var.hover = "arm"
    elif var.arm_start2[0] <= pygame.mouse.get_pos()[0] <= var.arm_start2[0] + var.arm2.get_width() \
            and var.arm_start2[1] <= pygame.mouse.get_pos()[1] <= var.arm_start2[1] + var.arm2.get_height() or \
            var.arm_start2[2] <= pygame.mouse.get_pos()[0] <= var.arm_start2[2] + var.arm2.get_width() and \
            var.arm_start2[1] <= pygame.mouse.get_pos()[1] <= var.arm_start2[1] + var.arm2.get_height():
        var.hover = "arm"

    else:
        var.hover = ""


def draw(screen):
    screen.fill((255, 255, 255))

    if var.hover == "head":
        screen.blit(var.head1r, var.head_start1)
        screen.blit(pygame.transform.flip(var.head1r, True, False),
                    (var.head_start1[0] + var.head1r.get_width(), var.head_start1[1]))
        screen.blit(var.head2r, var.head_start2)
        screen.blit(pygame.transform.flip(var.head2r, True, False),
                    (var.head_start2[0] + var.head2r.get_width(), var.head_start2[1]))
        screen.blit(var.head3r, var.head_start3)

    else:
        screen.blit(var.head1, var.head_start1)
        screen.blit(pygame.transform.flip(var.head1, True, False),
                    (var.head_start1[0] + var.head1.get_width(), var.head_start1[1]))
        screen.blit(var.head2, var.head_start2)
        screen.blit(pygame.transform.flip(var.head2, True, False),
                    (var.head_start2[0] + var.head2.get_width(), var.head_start2[1]))
        screen.blit(var.head3, var.head_start3)

    if var.hover == "foot":
        screen.blit(var.foot1r, var.foot_start1)
        screen.blit(pygame.transform.flip(var.foot1r, True, False),
                    (var.foot_start1[0] + var.foot1r.get_width(), var.foot_start1[1]))
        screen.blit(var.foot2r, var.foot_start2)
        screen.blit(pygame.transform.flip(var.foot2r, True, False),
                    (var.foot_start2[0] + var.foot2r.get_width(), var.foot_start2[1]))
        screen.blit(var.foot3r, var.foot_start3)

    else:
        screen.blit(var.foot1, var.foot_start1)
        screen.blit(pygame.transform.flip(var.foot1, True, False),
                    (var.foot_start1[0] + var.foot1.get_width(), var.foot_start1[1]))
        screen.blit(var.foot2, var.foot_start2)
        screen.blit(pygame.transform.flip(var.foot2, True, False),
                    (var.foot_start2[0] + var.foot2.get_width(), var.foot_start2[1]))
        screen.blit(var.foot3, var.foot_start3)

    if var.hover == "back":
        screen.blit(var.back1r, var.back_start1)
        screen.blit(pygame.transform.flip(var.back1r, True, False),
                    (var.back_start1[0] + var.back1r.get_width(), var.back_start1[1]))
        screen.blit(var.back3r, var.back_start3)
    else:
        screen.blit(var.back1, var.back_start1)
        screen.blit(pygame.transform.flip(var.back1, True, False),
                    (var.back_start1[0] + var.back1.get_width(), var.back_start1[1]))
        screen.blit(var.back3, var.back_start3)
        
    if var.hover == "chest":
        screen.blit(var.chest2r, var.chest_start2)
        screen.blit(pygame.transform.flip(var.chest2r, True, False),
                    (var.chest_start2[0] + var.chest2r.get_width(), var.chest_start2[1]))
        screen.blit(var.chest3r, var.chest_start3)
    else:
        screen.blit(var.chest2, var.chest_start2)
        screen.blit(pygame.transform.flip(var.chest2, True, False),
                    (var.chest_start2[0] + var.chest2.get_width(), var.chest_start2[1]))
        screen.blit(var.chest3, var.chest_start3)
    
    if var.hover == "abs":
        screen.blit(var.abs2r, var.abs_start2)
        screen.blit(pygame.transform.flip(var.abs2r, True, False),
                    (var.abs_start2[0] + var.abs2r.get_width(), var.abs_start2[1]))
        screen.blit(var.abs3r, var.abs_start3)
    else:
        screen.blit(var.abs2, var.abs_start2)
        screen.blit(pygame.transform.flip(var.abs2, True, False),
                    (var.abs_start2[0] + var.abs2.get_width(), var.abs_start2[1]))
        screen.blit(var.abs3, var.abs_start3)
        
    if var.hover == "shoulder":
        screen.blit(var.shol1r, (var.shol_start1[0], var.shol_start1[1]))
        screen.blit(pygame.transform.flip(var.shol1r, True, False),
                    (var.shol_start1[2], var.shol_start1[1]))
        screen.blit(var.shol2r, (var.shol_start2[0], var.shol_start2[1]))
        screen.blit(pygame.transform.flip(var.shol2r, True, False),
                    (var.shol_start2[2], var.shol_start2[1]))
        screen.blit(var.shol3r, var.shol_start3)
    else:
        screen.blit(var.shol1, (var.shol_start1[0], var.shol_start1[1]))
        screen.blit(pygame.transform.flip(var.shol1, True, False),
                    (var.shol_start1[2], var.shol_start1[1]))
        screen.blit(var.shol2, (var.shol_start2[0], var.shol_start2[1]))
        screen.blit(pygame.transform.flip(var.shol2, True, False),
                    (var.shol_start2[2], var.shol_start2[1]))
        screen.blit(var.shol3, var.shol_start3)

    if var.hover == "arm":
        screen.blit(var.arm1r, (var.arm_start1[0], var.arm_start1[1]))
        screen.blit(pygame.transform.flip(var.arm1r, True, False),
                    (var.arm_start1[2], var.arm_start1[1]))
        screen.blit(var.arm2r, (var.arm_start2[0], var.arm_start2[1]))
        screen.blit(pygame.transform.flip(var.arm2r, True, False),
                    (var.arm_start2[2], var.arm_start2[1]))
    else:
        screen.blit(var.arm1, (var.arm_start1[0], var.arm_start1[1]))
        screen.blit(pygame.transform.flip(var.arm1, True, False),
                    (var.arm_start1[2], var.arm_start1[1]))
        screen.blit(var.arm2, (var.arm_start2[0], var.arm_start2[1]))
        screen.blit(pygame.transform.flip(var.arm2, True, False),
                    (var.arm_start2[2], var.arm_start2[1]))
    

def on_event(event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if var.hover != "" and var.hover != "head":
            raise StateSwitcher("view")
