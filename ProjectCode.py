import pygame
import random



pygame.init()



screen_w = 800

screen_h = 600

fps = 60

play_s = 5

bullet_s = 7

enemy_s = 2

enemy_num = 10

w_score = 1000



wh = (255, 255, 255)

red = (255, 0, 0)


bl = (0, 0, 0)

gr = (0, 255, 0)

screen = pygame.display.set_mode((screen_w, screen_h))

pygame.display.set_caption("Galactica")

font = pygame.font.SysFont("Times New Roman", 24)

large_font = pygame.font.SysFont("Times New Roman", 48)

class Player:

    def __init__(self):

        self.rect = pygame.Rect(screen_w // 2 - 25, screen_h - 50, 50, 40)



    def move(self, keys):

        if keys[pygame.K_LEFT] and self.rect.left > 0:

            self.rect.x -= play_s

        if keys[pygame.K_RIGHT] and self.rect.right < screen_w:

            self.rect.x += play_s

class Bullet:

    def __init__(self, x, y):

        self.rect = pygame.Rect(x - 2, y - 10, 5, 10)



    def update(self):

        self.rect.y -= bullet_s



    def off_screen(self):

        return self.rect.top < 0

class Enemy:

    def __init__(self, x, y):

        self.rect = pygame.Rect(x, y, 50, 40)



    def update(self):

        self.rect.y += enemy_s



    def off_screen(self):

        return self.rect.top > screen_h

def spawn_enemies():

        return [Enemy(random.randint(0, screen_w - 50), random.randint(-1000, -200)) for _ in range(enemy_num)]

def display_start_screen():

    screen.fill(bl)

    title_text = large_font.render("Galactica", True, gr)

    instructions = [

    "Welcome to Galactica!",

    "Navigate using Left/Right arrows.",

    "Press Space to shoot.",

    "Reach 1000 points to win.",

    "Press Enter to Start"

    ]

    screen.blit(title_text, (screen_w // 2 - title_text.get_width() // 2, screen_h // 4))



    y_offset = screen_h // 3

    for line in instructions:

        instruction_text = font.render(line, True, wh)

        screen.blit(instruction_text, (screen_w // 2 - instruction_text.get_width() // 2, y_offset))

        y_offset += 40



    pygame.display.flip()



    waiting = True

    while waiting:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()

                return

            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:

                waiting = False

                return


def run_game():

    player = Player()

    bullets = []

    enemies = spawn_enemies()



    score = 0

    clock = pygame.time.Clock()



    while True:

        clock.tick(fps)

        screen.fill(bl)



        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()

                return

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:

                    bullets.append(Bullet(player.rect.centerx, player.rect.top))

                if event.key == pygame.K_ESCAPE:

                    pygame.quit()

                    return



        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()

                return

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:

                    bullets.append(Bullet(player.rect.centerx, player.rect.top))



        keys = pygame.key.get_pressed()

        player.move(keys)



        for bullet in list(bullets):

            bullet.update()

            if bullet.off_screen():

                bullets.remove(bullet)



        for enemy in list(enemies):

            enemy.update()

            if enemy.off_screen():

                enemy.rect.top = 0

                enemy.rect.x = random.randint(0, screen_w - 50)



        for bullet in list(bullets):

            for enemy in list(enemies):

                if bullet.rect.colliderect(enemy.rect):

                    bullets.remove(bullet)

                    enemies.remove(enemy)

                    score += 10

                    break



        if len(enemies) == 0:

            enemies = spawn_enemies()



        for enemy in enemies:

            if player.rect.colliderect(enemy.rect):

                draw_game_over_screen(score)

                return



        if score >= w_score:

            display_win_screen(score)

            return



        pygame.draw.rect(screen, wh, player.rect)

        for bullet in bullets:

            pygame.draw.rect(screen, wh, bullet.rect)

        for enemy in enemies:

            pygame.draw.rect(screen, red, enemy.rect)



        score_text = font.render(f'Score: {score}', True, wh)

        screen.blit(score_text, (10, 10))



        pygame.display.flip()


def draw_game_over_screen(score):

    screen.fill(bl)

    game_over_text = large_font.render("Game Over", True, red)

    score_text = font.render(f"Final Score: {score}", True, wh)

    restart_text = font.render("Press 'R' to Restart or 'Q' to Quit", True, wh)



    screen.blit(game_over_text, (screen_w // 2 - game_over_text.get_width() // 2, screen_h // 4))

    screen.blit(score_text, (screen_w // 2 - score_text.get_width() // 2, screen_h // 3))

    screen.blit(restart_text, (screen_w // 2 - restart_text.get_width() // 2, screen_h // 1.5))



    pygame.display.flip()



    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()

                return

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_r:

                    run_game()

                    return

                elif event.key == pygame.K_q:

                    pygame.quit()

                    return

def display_win_screen(score):

    screen.fill(bl)

    win_text = large_font.render("You Win!", True, gr)

    score_text = font.render(f"Final Score: {score}", True, wh)

    restart_text = font.render("Press 'R' to Restart or 'Q' to Quit", True, wh)



    screen.blit(win_text, (screen_w // 2 - win_text.get_width() // 2, screen_h // 4))

    screen.blit(score_text, (screen_w // 2 - score_text.get_width() // 2, screen_h // 2))

    screen.blit(restart_text, (screen_w // 2 - restart_text.get_width() // 2, screen_h // 1.5))



    pygame.display.flip()



    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()

                return

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_r:

                    run_game()

                    return

                elif event.key == pygame.K_q:

                    pygame.quit()

                    return

display_start_screen()

run_game()
