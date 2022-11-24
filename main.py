import pygame
import random

pygame.init()

yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 600
dis_height = 400

font = pygame.font.SysFont(None, 30)

screen = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by Ikra!')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

snake2_block = 10
snake2_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont(None, 30)


def game_intro():

    while True:

        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        draw_text('Main Menu', font, (0, 0, 0), screen, 250, 40)

        mx, my = pygame.mouse.get_pos()

        # creating buttons
        button_1 = pygame.Rect(200, 100, 200, 50)
        button_2 = pygame.Rect(200, 180, 200, 50)

        # defining functions when a certain button is pressed
        if button_1.collidepoint((mx, my)):
            if click:
                single_player()
        if button_2.collidepoint((mx, my)):
            if click:
                multiplayer()
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)

        # writing text on top of button
        draw_text('SINGLEPLAYER', font, (255, 255, 255), screen, 225, 115)
        draw_text('MULTIPLAYER', font, (255, 255, 255), screen, 230, 195)

        clock.tick(60)
        pygame.display.update()


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, green, [x[0], x[1], snake_block, snake_block])


def draw_snake2(snake2_block, snake2_list):
    for x in snake2_list:
        pygame.draw.rect(screen, blue, [x[0], x[1], snake2_block, snake2_block])


def end_message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [dis_width / 7, dis_height / 3])


def score_display_singleplayer(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    screen.blit(value, [5, 5])


def score_display_player1(score):
    value = score_font.render("Player 1 Score: " + str(score), True, yellow)
    screen.blit(value, [5, 5])


def score_display_player2(score):
    value = score_font.render("Player 2 Score: " + str(score), True, yellow)
    screen.blit(value, [425, 6])


def single_player():
    game_over = False
    game_lost = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    snake_length = 1

    foodx = round(random.randrange(2, dis_width - (2 * snake_block)) / 10.0) * 10.0
    foody = round(random.randrange(30, dis_height - (2 * snake_block)) / 10.0) * 10.0

    while not game_over:

        while game_lost:
            screen.fill(black)
            end_message("You Lost! Press C-Play Again or Q-Quit", red)
            score_display_singleplayer(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_lost = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_lost = False
                    if event.key == pygame.K_c:
                        single_player()

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

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_lost = True
        x1 += x1_change
        y1 += y1_change
        screen.fill(black)
        pygame.draw.rect(screen, red, [foodx, foody, snake_block, snake_block])
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_lost = True

        draw_snake(snake_block, snake_list)
        score_display_singleplayer(snake_length - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(2, dis_width - (2 * snake_block)) / 10.0) * 10.0
            foody = round(random.randrange(30, dis_height - (2 * snake_block)) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


def multiplayer():
    game_over = False
    p1_loss = False
    p2_loss = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x2 = dis_width / 2
    y2 = dis_width / 2

    x1_change = 0
    y1_change = 0

    x2_change = 0
    y2_change = 0

    snake_list = []
    snake_length = 1

    snake2_list = []
    snake2_length = 1

    foodx = round(random.randrange(2, dis_width - (2 * snake_block)) / 10.0) * 10.0
    foody = round(random.randrange(30, dis_height - (2 * snake_block)) / 10.0) * 10.0

    while not game_over:

        while p1_loss:
            screen.fill(black)
            end_message("Player 2 Wins! Press C-Play Again or Q-Quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    p1_loss = False
                    p2_loss = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        p1_loss = False
                        p2_loss = False
                    if event.key == pygame.K_c:
                        multiplayer()

        while p2_loss:
            screen.fill(black)
            end_message("Player 1 Wins! Press C-Play Again or Q-Quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    p1_loss = False
                    p2_loss = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        p1_loss = False
                        p2_loss = False
                    if event.key == pygame.K_c:
                        multiplayer()

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
                elif event.key == pygame.K_a:
                    x2_change = -snake2_block
                    y2_change = 0
                elif event.key == pygame.K_d:
                    x2_change = snake2_block
                    y2_change = 0
                elif event.key == pygame.K_s:
                    y2_change = snake2_block
                    x2_change = 0
                elif event.key == pygame.K_w:
                    y2_change = -snake2_block
                    x2_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            p1_loss = True
        x1 += x1_change
        y1 += y1_change

        if x2 >= dis_width or x2 < 0 or y2 >= dis_height or y2 < 0:
            p2_loss = True
        x2 += x2_change
        y2 += y2_change

        screen.fill(black)
        pygame.draw.rect(screen, red, [foodx, foody, snake_block, snake_block])

        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                p1_loss = True

        draw_snake(snake_block, snake_list)

        snake2_head = [x2, y2]
        snake2_list.append(snake2_head)
        if len(snake2_list) > snake2_length:
            del snake2_list[0]

        for x in snake2_list[:-1]:
            if x == snake2_head:
                p2_loss = True

        draw_snake2(snake_block, snake2_list)

        score_display_player1(snake_length - 1)
        if snake_length - 1 == 20:
            p2_loss = True

        score_display_player2(snake2_length - 1)
        if snake2_length - 1 == 20:
            p1_loss = True

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(2, dis_width - (2 * snake_block)) / 10.0) * 10.0
            foody = round(random.randrange(30, dis_height - (2 * snake_block)) / 10.0) * 10.0
            snake_length += 1

        if x2 == foodx and y2 == foody:
            foodx = round(random.randrange(2, dis_width - (2 * snake_block)) / 10.0) * 10.0
            foody = round(random.randrange(30, dis_height - (2 * snake_block)) / 10.0) * 10.0
            snake2_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


game_intro()
