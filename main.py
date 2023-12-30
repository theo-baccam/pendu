import pygame
from functools import partial

import pygame_functions as pf
import start_menu as sm
import hangman_game as hg
import add_word as aw

available_options = [
    partial(hg.hangman_game, pf.screen),
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

    sm.start_menu(pf.screen)
    pygame.display.flip()

pf.pygame_quit()
