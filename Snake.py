import pygame
import time
import random


pygame.init()


window_width = 600
window_height = 400


black = (0, 0, 0)
white = (255, 255, 255)
red = (213, 50, 80)
green = (0, 255, 0)


snake_block = 10
snake_speed = 15


game_display = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('SNAKE')

clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)
start_font = pygame.font.SysFont(None, 75)
end_font = pygame.font.SysFont(None, 30)  

def your_score(score):
    value = score_font.render(f"Score: {score}", True, black)
    game_display.blit(value, [10, 10])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_display, green, [x[0], x[1], snake_block, snake_block])

def message(msg, color, position):
    mesg = end_font.render(msg, True, color)
    mesg_rect = mesg.get_rect(center=position)
    game_display.blit(mesg, mesg_rect)

def draw_signature():
    signature_font = pygame.font.SysFont(None, 20)
    signature = signature_font.render("Codé par Ghani Abdullah", True, black)
    game_display.blit(signature, [10, window_height - 20])

def gameLoop():
    game_over = False
    game_close = False

    x1 = window_width / 2
    y1 = window_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, window_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, window_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            game_display.fill(white)
            message("Game Over! Q: Quit or C: Play Again", red, (window_width / 2, window_height / 2))
            your_score(Length_of_snake - 1)
            draw_signature()
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        game_display.fill(white)
        pygame.draw.rect(game_display, black, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        your_score(Length_of_snake - 1)

        draw_signature()
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, window_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, window_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

def game_intro():
    intro = True
    while intro:
        game_display.fill(white)
        title = start_font.render("SNAKE", True, black)
        title_rect = title.get_rect(center=(window_width / 2, window_height / 3))
        game_display.blit(title, title_rect)

        draw_signature()

        start_button = pygame.Rect(window_width / 2 - 100, window_height / 2 - 25, 200, 50)
        pygame.draw.rect(game_display, black, start_button)
        start_text = font_style.render("Start Game", True, white)
        start_text_rect = start_text.get_rect(center=start_button.center)
        game_display.blit(start_text, start_text_rect)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if start_button.collidepoint(pos):
                    intro = False
                    gameLoop()

game_intro()
