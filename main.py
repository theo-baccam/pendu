import pygame
from functools import partial

import pygame_functions as pf
import start_menu as sm
import add_word as aw


def new_game():
    print("new game")


def add_word():
    print("add word")


available_options = [
    new_game,
    partial(aw.add_word, pf.screen),
    pf.pygame_quit,
]

while pf.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pf.running = False
            break

        if event.type != pygame.KEYDOWN:
            continue

        if event.key == pygame.K_UP:
            sm.selection_value = (sm.selection_value + 3 - 1) % 3
        elif event.key == pygame.K_DOWN:
            sm.selection_value = (sm.selection_value + 3 + 1) % 3

        if event.key == pygame.K_RETURN:
            available_options[sm.selection_value]()

    sm.draw_background(pf.screen)
    sm.draw_title(pf.screen)
    sm.render_options(pf.screen)
    pygame.display.flip()

pf.pygame_quit()
