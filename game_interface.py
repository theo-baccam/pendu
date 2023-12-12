import pygame
from game_logic import *

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
running = True

word = WordHandler
verif = VerifyInput
lett = LetterHandler
game = GameState

word_list = word.word_list_loader()

random_word = word.random_word_select(word_list)
play_field = "_" * len(random_word)

count = 0

background = (32, 32, 64)
foreground = (0, 192, 255)

font_path = "./NotoSansMono-Regular.ttf"

main_font_size = 20
main_font = pygame.font.Font(font_path, main_font_size)

used_letters_font_size = 15
used_letters_font = pygame.font.Font(font_path, used_letters_font_size)


while running:
    lose_surface = main_font.render("Perdu!", True, foreground)
    lose_center = lose_surface.get_width() / 2
    lose_x, lose_y = 320 - lose_center, 30

    win_surface = main_font.render("Gagné!", True, foreground)
    win_center = win_surface.get_width() / 2
    win_x, win_y = 320 - win_center, 30

    solution_surface = main_font.render(random_word, True, foreground)
    solution_center = solution_surface.get_width() / 2
    solution_x, solution_y = 320 - solution_center, 420

    used_letters_surface = used_letters_font.render(
        " ".join(lett.used_letters), True, foreground
    )
    used_letters_center = used_letters_surface.get_width() / 2
    used_letters_x, used_letters_y = 320 - used_letters_center, 450

    count_surface = main_font.render(f"{count}/7", True, foreground)
    count_x, count_y = 550, 30

    word_surface = main_font.render(play_field, True, foreground)
    word_center = word_surface.get_width() / 2
    word_x, word_y = 320 - word_center, 420

    screen.fill(background)

    if game.lose_state(count):
        screen.blit(lose_surface, (lose_x, lose_y))
        screen.blit(solution_surface, (solution_x, solution_y))
        screen.blit(used_letters_surface, (used_letters_x, used_letters_y))
        screen.blit(count_surface, (count_x, count_y))
        pygame.display.flip()
        pygame.time.delay(1000)
        running = False
    elif game.win_state(play_field, random_word):
        screen.blit(win_surface, (win_x, win_y))
        screen.blit(solution_surface, (solution_x, solution_y))
        screen.blit(used_letters_surface, (used_letters_x, used_letters_y))
        screen.blit(count_surface, (count_x, count_y))
        pygame.display.flip()
        pygame.time.delay(1000)
        running = False

    screen.blit(word_surface, (word_x, word_y))
    screen.blit(used_letters_surface, (used_letters_x, used_letters_y))
    screen.blit(count_surface, (count_x, count_y))

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key >= pygame.K_a and event.key <= pygame.K_z:
                letter = chr(event.key).lower()
                if verif.was_used(letter):
                    continue
                lett.add_to_used_letters(letter)
                if not verif.is_in_word(letter, random_word):
                    count += 1
                    continue
                play_field = modify_play_field(letter, play_field, random_word)

pygame.quit()
