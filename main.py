import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 800
GRID_SIZE = 40
FPS = 10
RESET_DELAY = 1000  # 1000 milliseconds (1 second) delay after resetting the snake
COUNTDOWN_TIME = 3  # Countdown time in seconds before the snake starts moving

# Colors
GRASS = (205, 240, 255)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0,0,0)

# Snake class
class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((WIDTH // 2), (HEIGHT // 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = RED
        self.score = 0
        self.is_counting_down = True
        self.countdown_timer = COUNTDOWN_TIME * FPS

        self.head_up = pygame.image.load('Assets/head_up.png').convert_alpha()
        self.head_up = pygame.transform.scale(self.head_up,(40,40))
        self.head_down = pygame.image.load('Assets/head_down.png').convert_alpha()
        self.head_down= pygame.transform.scale(self.head_down,(40,40))
        self.head_right = pygame.image.load('Assets/head_right.png').convert_alpha()
        self.head_right = pygame.transform.scale(self.head_right,(40,40))
        self.head_left = pygame.image.load('Assets/head_left.png').convert_alpha()
        self.head_left = pygame.transform.scale(self.head_left,(40,40))


        self.tail_up = pygame.image.load('Assets/tail_down.png').convert_alpha()
        self.tail_up = pygame.transform.scale(self.tail_up,(40,40))
        self.tail_down = pygame.image.load('Assets/tail_up.png').convert_alpha()
        self.tail_down = pygame.transform.scale(self.tail_down,(40,40))
        self.tail_right = pygame.image.load('Assets/tail_left.png').convert_alpha()
        self.tail_right = pygame.transform.scale(self.tail_right,(40,40))
        self.tail_left = pygame.image.load('Assets/tail_right.png').convert_alpha()
        self.tail_left = pygame.transform.scale(self.tail_left,(40,40))

        self.body_vertical = pygame.image.load('Assets/body_vertical.png').convert_alpha()
        self.body_vertical = pygame.transform.scale(self.body_vertical,(40,40))
        self.body_horizontal = pygame.image.load('Assets/body_horizontal.png').convert_alpha()
        self.body_horizontal = pygame.transform.scale(self.body_horizontal,(40,40))

        self.body_tr = pygame.image.load('Assets/body_tr.png').convert_alpha()
        self.body_tr = pygame.transform.scale(self.body_tr, (40, 40))
        self.body_tl = pygame.image.load('Assets/body_tl.png').convert_alpha()
        self.body_tl = pygame.transform.scale(self.body_tl, (40, 40))
        self.body_br = pygame.image.load('Assets/body_br.png').convert_alpha()
        self.body_br = pygame.transform.scale(self.body_br, (40, 40))
        self.body_bl = pygame.image.load('Assets/body_bl.png').convert_alpha()
        self.body_bl = pygame.transform.scale(self.body_bl, (40, 40))

    def get_head_position(self):
        return self.positions[0]

    def update(self):
        if self.is_counting_down:
            self.countdown_timer -= 1
            if self.countdown_timer == 0:
                self.is_counting_down = False
        else:
            cur = self.get_head_position()
            x, y = self.direction
            new = (((cur[0] + (x * GRID_SIZE)) % WIDTH), (cur[1] + (y * GRID_SIZE)) % HEIGHT)
            if len(self.positions) > 2 and new in self.positions[2:]:
                self.reset_with_delay()
            else:
                self.positions.insert(0, new)
                if len(self.positions) > self.length:
                    self.positions.pop()

    def reset(self):
        self.length = 2
        self.positions = [((WIDTH // 2), (HEIGHT // 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.score = 0
        self.is_counting_down = True
        self.countdown_timer = COUNTDOWN_TIME * FPS

    def reset_with_delay(self):
        self.reset()
        pygame.time.delay(RESET_DELAY)

    def resume_with_countdown(self):
        self.is_counting_down = True
        self.countdown_timer = COUNTDOWN_TIME * FPS

    def render(self, surface):
        for i, p in enumerate(self.positions):
            if i == 0:  # Head of the snake
                head_directions = {UP: self.head_up, DOWN: self.head_down, LEFT: self.head_left, RIGHT: self.head_right}
                surface.blit(head_directions[self.direction], (p[0], p[1]))
            elif i == self.length - 1:  # Tail of the snake
                tail_directions = {UP: self.tail_up, DOWN: self.tail_down, LEFT: self.tail_left, RIGHT: self.tail_right}
                surface.blit(tail_directions[self.direction], (p[0], p[1]))
            else:  # Body of the snake
                if i - 1 < 0 or i + 1 >= len(self.positions):
                    continue  # Skip rendering if going out of bounds

                prev_segment = self.positions[i - 1]
                next_segment = self.positions[i + 1]

                if prev_segment[0] < p[0] and next_segment[1] < p[1]:
                    surface.blit(self.body_tl, (p[0], p[1]))
                elif prev_segment[0] < p[0] and next_segment[1] > p[1]:
                    surface.blit(self.body_bl, (p[0], p[1]))
                elif prev_segment[0] > p[0] and next_segment[1] < p[1]:
                    surface.blit(self.body_tr, (p[0], p[1]))
                elif prev_segment[0] > p[0] and next_segment[1] > p[1]:
                    surface.blit(self.body_br, (p[0], p[1]))
                else:
                    surface.blit(self.body_vertical, (p[0], p[1]))  # Default to horizontal body
# Fruit class
class Fruit:
    def __init__(self):
        self.position = (0, 0)
        self.color = RED
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE,
                         random.randint(0, (HEIGHT // GRID_SIZE) - 1) * GRID_SIZE)

    def render(self, surface):
        pygame.draw.rect(surface, self.color, (self.position[0], self.position[1], GRID_SIZE, GRID_SIZE))


# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Main menu function
def main_menu():
    screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    clock = pygame.time.Clock()

    font = pygame.font.Font(None, 74)
    title_text = font.render("Snake Game", True, BLACK)
    subtitle_text = font.render("Press Enter to Play", True, BLACK)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return  # Start the game

        surface.fill(GRASS)
        surface.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 4))
        surface.blit(subtitle_text, (WIDTH // 2 - subtitle_text.get_width() // 2, HEIGHT // 2))
        screen.blit(surface, (0, 0))
        pygame.display.update()
        clock.tick(FPS)

# Main game function
def main():
    main_menu()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()

    snake = Snake()
    fruit = Fruit()

    is_paused = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if snake.direction != DOWN:
                        snake.direction = UP
                elif event.key == pygame.K_DOWN:
                    if snake.direction != UP:
                        snake.direction = DOWN
                elif event.key == pygame.K_LEFT:
                    if snake.direction != RIGHT:
                        snake.direction = LEFT
                elif event.key == pygame.K_RIGHT:
                    if snake.direction != LEFT:
                        snake.direction = RIGHT
                elif event.key == pygame.K_ESCAPE:
                    if is_paused:
                        snake.resume_with_countdown()
                    is_paused = not is_paused

        if not is_paused:
            snake.update()
            if snake.get_head_position() == fruit.position:
                snake.length += 1
                snake.score += 1  # Increase score when eating a fruit
                fruit.randomize_position()

        surface.fill(GRASS)
        snake.render(surface)
        fruit.render(surface)

        # Display countdown timer
        if snake.is_counting_down:
            countdown_font = pygame.font.Font(None, 48)
            countdown_text = countdown_font.render(
                f"Game starting in {snake.countdown_timer // FPS + 1}...", True, BLACK
            )
            surface.blit(
                countdown_text, (WIDTH // 2 - countdown_text.get_width() // 2, HEIGHT // 2)
            )
        else:
            # Display score
            font = pygame.font.Font(None, 36)
            score_text = font.render(f"Score: {snake.score}", True, BLACK)
            surface.blit(score_text, (10, 10))

            # Display pause message
            if is_paused:
                pause_font = pygame.font.Font(None, 48)
                pause_text = pause_font.render("Game paused. Press ESC to resume.", True, BLACK)
                surface.blit(pause_text, (WIDTH // 2 - pause_text.get_width() // 2, HEIGHT // 2))

        screen.blit(surface, (0, 0))
        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
