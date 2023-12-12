from game_logic import *
import pygame

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

font_path = "./NotoSansMono-Regular.ttf"

MAIN_FONT_SIZE = 20
MAIN_FONT = pygame.font.Font(font_path, MAIN_FONT_SIZE)

USED_LETTERS_FONT_SIZE = 15
USED_LETTERS_FONT = pygame.font.Font(font_path, USED_LETTERS_FONT_SIZE)

BACKGROUND = (32, 32, 64)
FOREGROUND = (0, 192, 255)

play_field = "_" * len(word.random_word)

life_count = 0

while running:
    lose_surface = MAIN_FONT.render("Perdu!", True, FOREGROUND)
    lose_center = lose_surface.get_width() / 2
    lose_x, lose_y = 320 - lose_center, 30

    win_surface = MAIN_FONT.render("Gagné!", True, FOREGROUND)
    win_center = win_surface.get_width() / 2
    win_x, win_y = 320 - win_center, 30

    solution_surface = MAIN_FONT.render(word.random_word, True, FOREGROUND)
    solution_center = solution_surface.get_width() / 2
    solution_x, solution_y = 320 - solution_center, 420

    used_letters_surface = USED_LETTERS_FONT.render(
        " ".join(lett.used_letters), True, FOREGROUND
    )
    used_letters_center = used_letters_surface.get_width() / 2
    used_letters_x, used_letters_y = 320 - used_letters_center, 450

    life_count_surface = MAIN_FONT.render(f"{life_count}/7", True, FOREGROUND)
    life_count_x, life_count_y = 550, 30

    word_surface = MAIN_FONT.render(play_field, True, FOREGROUND)
    word_center = word_surface.get_width() / 2
    word_x, word_y = 320 - word_center, 420

    screen.fill(BACKGROUND)

    if game.lose_state(life_count):
        screen.blit(lose_surface, (lose_x, lose_y))
        screen.blit(solution_surface, (solution_x, solution_y))
        screen.blit(used_letters_surface, (used_letters_x, used_letters_y))
        screen.blit(life_count_surface, (life_count_x, life_count_y))
        pygame.display.flip()
        pygame.time.delay(1000)
        running = False
    elif game.win_state(play_field, word.random_word):
        screen.blit(win_surface, (win_x, win_y))
        screen.blit(solution_surface, (solution_x, solution_y))
        screen.blit(used_letters_surface, (used_letters_x, used_letters_y))
        screen.blit(life_count_surface, (life_count_x, life_count_y))
        pygame.display.flip()
        pygame.time.delay(1000)
        running = False

    screen.blit(word_surface, (word_x, word_y))
    screen.blit(used_letters_surface, (used_letters_x, used_letters_y))
    screen.blit(life_count_surface, (life_count_x, life_count_y))

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key >= pygame.K_a and event.key <= pygame.K_z:
                letter = chr(event.key).lower()
                if verif.was_used(letter):
                    continue
                lett.add_to_used_letters(letter)
                if not verif.is_in_word(letter, word.random_word):
                    life_count += 1
                    continue
                play_field = modify_play_field(letter, play_field, word.random_word)

pygame.quit()
