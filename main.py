import pygame
import sys
from sharedvars import *
from pygame.locals import *

current_state = ''


def quit_game():
    pygame.quit()
    sys.exit()


def switch_state(new_state):
    global current_state

    current_state = __import__(new_state)
    current_state.init()

if __name__ == '__main__':

    pygame.init()

    flags = SRCALPHA | DOUBLEBUF

    screen = pygame.display.set_mode((var.screen_w, var.screen_h), flags)

    switch_state('select')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            else:
                current_state.on_event(event)
        current_state.update()
        current_state.draw(screen)

        pygame.display.flip()