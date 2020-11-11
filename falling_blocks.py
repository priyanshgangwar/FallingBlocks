import pygame
import friend
import enemy

width, height = 800, 600
block_size = 40
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

clock = pygame.time.Clock()


def level_up(score):
    if score >= 800:
        return 7
    elif score >= 600:
        return 6
    elif score >= 425:
        return 5
    elif score >= 275:
        return 4
    elif score >= 150:
        return 3
    elif score >= 50:
        return 2
    else:
        return 1


def check_collision(friend_block, enemy_block):
    if block_size > friend_block.pos_x - enemy_block.pos_x > - block_size:
        if block_size > friend_block.pos_y - enemy_block.pos_y > - block_size:
            return True


def draw_text(game_display, text, x, y, size, color, bg=None):
    font = pygame.font.SysFont(None, size)
    text_surface = font.render(text, True, color, bg)
    text_surface_size = font.size(text)
    game_display.blit(text_surface, (x-text_surface_size[0]/2, y-text_surface_size[1]/2))


def game_over(game_display, score):
    g_over = True
    draw_text(game_display, " Game Over ", width/2, height/3, 100, red, black)
    draw_text(game_display, "score: {}".format(score), width/2, height/2, 50, black, white)
    draw_text(game_display, "Press r to replay", width/2, height - 20, 30, black, white)
    pygame.display.update()

    while g_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game_loop(game_display)
        clock.tick(10)


def game_intro(game_display):
    intro_loop = True

    while intro_loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    intro_loop = False

        game_display.fill(white)
        draw_text(game_display, "Falling Blocks", width/2, height/3, 100, red)
        draw_text(game_display, "Press p to Play", width/2, 2*height/3, 30, red)
        pygame.display.update()
        clock.tick(10)


def game_loop(game_display):
    game_running = True
    score = 0
    friend_block = friend.Friend(width, height, block_size)
    friend_block_move = 0

    number_of_enemies = 15
    enemies = []
    for i in range(number_of_enemies):
        enemies.append(enemy.Enemy(width, height, block_size))

    while game_running:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                game_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    friend_block_move = 1
                elif event.key == pygame.K_LEFT:
                    friend_block_move = -1

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    friend_block_move = 0

        game_display.fill(white)
        game_level = level_up(score)
        friend_block.move_x(friend_block_move)
        friend_block.draw(game_display)
        for i in range(number_of_enemies):
            score += enemies[i].move_y(height, game_level)
            enemies[i].draw(game_display)
            if check_collision(friend_block, enemies[i]):
                game_over(game_display, score)
        draw_text(game_display, "Score: {}".format(score), width / 2, 20, 30, black)
        draw_text(game_display, "Level: {}".format(game_level), 50, 20, 30, black)
        pygame.display.update()
        clock.tick(100)


def main():
    resolution = (width, height)
    # Initialise screen
    pygame.init()
    game_display = pygame.display.set_mode(resolution)
    pygame.display.set_caption('Falling Blocks')

    game_intro(game_display)
    game_loop(game_display)

    pygame.quit()
    quit()


if __name__ == '__main__':
    main()
