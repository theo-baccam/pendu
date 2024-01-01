# main.py est le fichier python qui est exécuté par le joueur, le reste des
# fichiers sont des juste des modules contenant des fonctions et des variables.

# Les imports sont organisé en trois catégories:
# Les modules standards, les modules tiers et les modules locaux.

from functools import partial

import pygame

import pygame_functions as pf
import start_menu as sm
import hangman_game as hg
import add_word as aw

# Ici, functools.partial() me permet de mettres des fonctions avec des
# paramètres pré-remplis sans l'appeller
available_options = (
    partial(hg.hangman_game, pf.screen),
    partial(aw.add_word, pf.screen),
    pf.pygame_quit,
)

# La boucle principale pygame
while pf.running:
    # Boucle pour recevoir les inputs du joueur
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pf.running = False
            break

        # Si une touche n'est pas appuyé, ne rien faire.
        if event.type != pygame.KEYDOWN:
            continue

        # J'utilise le modulo wrap, ce qui veut dire que si l'option tout en
        # bas est selectionné, et que l'utilisateur appuie sur BAS, il revient
        # en haut.
        if event.key == pygame.K_UP:
            sm.selection_value = (sm.selection_value + 3 - 1) % 3
        elif event.key == pygame.K_DOWN:
            sm.selection_value = (sm.selection_value + 3 + 1) % 3

        # Entrée pour confirmer la sélection
        if event.key == pygame.K_RETURN:
            available_options[sm.selection_value]()

    # Fonction pour afficher les menus principaux
    sm.start_menu(pf.screen)
    pygame.display.flip()

pf.pygame_quit()
