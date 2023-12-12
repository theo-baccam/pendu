from game_logic import *
import pygame
import os

word = WordHandler
verif = VerifyInput
lett = LetterHandler
game = GameState

pygame.init()

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

pygame.font.init()

hangman_directory = os.path.dirname(os.path.abspath(__file__))
font_path = os.path.join(hangman_directory, "NotoSansMono-Regular.ttf")

MAIN_FONT_SIZE = 20
MAIN_FONT = pygame.font.Font(font_path, MAIN_FONT_SIZE)

USED_LETTERS_FONT_SIZE = 15
USED_LETTERS_FONT = pygame.font.Font(font_path, USED_LETTERS_FONT_SIZE)

BACKGROUND = (32, 32, 64)
FOREGROUND = (0, 192, 255)

play_field = "_" * len(word.random_word)

life_count = 0

SCREEN_TOP = 30
SCREEN_BOTTOM = 450
HALF_SCREEN_WIDTH = SCREEN_WIDTH / 2

LOSE_SURFACE = MAIN_FONT.render("Perdu!", True, FOREGROUND)

WIN_SURFACE = MAIN_FONT.render("Gagné!", True, FOREGROUND)

solution_surface = MAIN_FONT.render(word.random_word, True, FOREGROUND)
solution_center = solution_surface.get_width() / 2
solution_x, solution_y = HALF_SCREEN_WIDTH - solution_center, SCREEN_BOTTOM - 30


def render_lose_screen(LOSE_SURFACE):
    LOSE_CENTER = LOSE_SURFACE.get_width() / 2
    LOSE_X, LOSE_Y = HALF_SCREEN_WIDTH - LOSE_CENTER, SCREEN_TOP
    screen.blit(LOSE_SURFACE, (LOSE_X, LOSE_Y))
    screen.blit(solution_surface, (solution_x, solution_y))
    pygame.display.flip()
    pygame.time.delay(1000)
    return False


def render_win_screen(WIN_SURFACE):
    WIN_CENTER = WIN_SURFACE.get_width() / 2
    WIN_X, WIN_Y = HALF_SCREEN_WIDTH - WIN_CENTER, SCREEN_TOP
    screen.blit(WIN_SURFACE, (WIN_X, WIN_Y))
    screen.blit(solution_surface, (solution_x, solution_y))
    pygame.display.flip()
    pygame.time.delay(1000)
    return False


def render_main_ui(word_surface, life_count_surface, used_letters_surface):
    word_center = word_surface.get_width() / 2
    word_x, word_y = HALF_SCREEN_WIDTH - word_center, SCREEN_BOTTOM - 30
    screen.blit(word_surface, (word_x, word_y))
    life_count_x, life_count_y = 550, SCREEN_TOP
    screen.blit(life_count_surface, (life_count_x, life_count_y))
    used_letters_center = used_letters_surface.get_width() / 2
    used_letters_x, used_letters_y = (
        SCREEN_WIDTH / 2 - used_letters_center,
        SCREEN_BOTTOM,
    )
    screen.blit(used_letters_surface, (used_letters_x, used_letters_y))


while running:
    life_count_surface = MAIN_FONT.render(f"{life_count}/7", True, FOREGROUND)

    word_surface = MAIN_FONT.render(play_field, True, FOREGROUND)

    used_letters_surface = USED_LETTERS_FONT.render(
        " ".join(lett.used_letters), True, FOREGROUND
    )

    screen.fill(BACKGROUND)
    render_main_ui(word_surface, life_count_surface, used_letters_surface)

    if game.lose_state(life_count):
        running = render_lose_screen(LOSE_SURFACE)
    elif game.win_state(play_field, word.random_word):
        running = render_win_screen(WIN_SURFACE)


    pygame.display.flip()
    for event in pygame.event.get():
        if event.type != pygame.KEYDOWN:
            continue
        if not event.key >= pygame.K_a and event.key <= pygame.K_z:
            continue
        letter = chr(event.key).lower()
        if verif.was_used(letter):
            continue
        lett.add_to_used_letters(letter)
        if not verif.is_in_word(letter, word.random_word):
            life_count += 1
            continue
        play_field = modify_play_field(letter, play_field, word.random_word)

pygame.quit()
