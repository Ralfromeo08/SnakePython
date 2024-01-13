import pygame, sys , random
from pygame.math import Vector2
from button import Button

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(0,0)
        self.new_block = False


        self.head_up = pygame.image.load('Assets/head_up.png').convert_alpha()
        self.head_up = pygame.transform.scale(self.head_up,(40,40))
        self.head_down = pygame.image.load('Assets/head_down.png').convert_alpha()
        self.head_down= pygame.transform.scale(self.head_down,(40,40))
        self.head_right = pygame.image.load('Assets/head_right.png').convert_alpha()
        self.head_right = pygame.transform.scale(self.head_right,(40,40))
        self.head_left = pygame.image.load('Assets/head_left.png').convert_alpha()
        self.head_left = pygame.transform.scale(self.head_left,(40,40))


        self.tail_up = pygame.image.load('Assets/tail_up.png').convert_alpha()
        self.tail_up = pygame.transform.scale(self.tail_up,(40,40))
        self.tail_down = pygame.image.load('Assets/tail_down.png').convert_alpha()
        self.tail_down = pygame.transform.scale(self.tail_down,(40,40))
        self.tail_right = pygame.image.load('Assets/tail_right.png').convert_alpha()
        self.tail_right = pygame.transform.scale(self.tail_right,(40,40))
        self.tail_left = pygame.image.load('Assets/tail_left.png').convert_alpha()
        self.tail_left = pygame.transform.scale(self.tail_left,(40,40))

        self.body_vertical = pygame.image.load('Assets/body_vertical.png').convert_alpha()
        self.body_vertical = pygame.transform.scale(self.body_vertical,(40,40))
        self.body_horizontal = pygame.image.load('Assets/body_horizontal.png').convert_alpha()
        self.body_horizontal = pygame.transform.scale(self.body_horizontal,(40,40))



        self.body_tr = pygame.image.load('Assets/body_tr.png').convert_alpha()
        self.body_tr = pygame.transform.scale(self.body_tr,(40,40))
        self.body_tl = pygame.image.load('Assets/body_tl.png').convert_alpha()
        self.body_tl = pygame.transform.scale(self.body_tl,(40,40))
        self.body_br = pygame.image.load('Assets/body_br.png').convert_alpha()
        self.body_br = pygame.transform.scale(self.body_br,(40,40))
        self.body_bl = pygame.image.load('Assets/body_bl.png').convert_alpha()
        self.body_bl = pygame.transform.scale(self.body_bl,(40,40))

    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()

        for index,block in enumerate(self.body):
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)

            if index == 0:
                screen.blit(self.head,block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail,block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical,block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal,block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl,block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl,block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr,block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br,block_rect)


    def update_head_graphics(self):
        head_relation =  self.body[1] - self.body[0]
        if head_relation == Vector2(1,0): self.head = self.head_left
        elif head_relation == Vector2(-1,0): self.head = self.head_right
        elif head_relation == Vector2(0,1): self.head = self.head_up
        elif head_relation == Vector2(0,-1): self.head = self.head_down

    def update_tail_graphics(self):
        tail_relation =  self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1,0): self.tail = self.tail_left
        elif tail_relation == Vector2(-1,0): self.tail = self.tail_right
        elif tail_relation == Vector2(0,1): self.tail = self.tail_up
        elif tail_relation == Vector2(0,-1): self.tail = self.tail_down


    
    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:] 

    def add_block(self):
        self.new_block = True

    def reset(self):
        
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(0,0)
        
          
class FRUIT:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size), cell_size,cell_size)
        screen.blit(apple,fruit_rect)

    def randomize(self):
        self.x = random.randint(0,cell_number-1)
        self.y = random.randint(0,cell_number-1)
        self.pos = Vector2(self.x,self.y)

class MAIN:
    
        def __init__(self):
            self.snake = SNAKE()
            self.fruit = FRUIT()
            self.pause = False
            self.score = 0
            self.questions = [
            {"question": "Question 1?", "a": "Answer A", "b": "Answer B", "c": "Answer C", "correct": "a"},
            {"question": "Question 2?", "a": "Answer A", "b": "Answer B", "c": "Answer C", "correct": "b"},
            # Add more questions in a similar format
        ]

        def update(self):
            self.snake.move_snake()
            self.check_collision()
            self.check_fail()

            if self.score % 5 == 0 and self.score > 0:
                self.ask_question()
        
        def ask_question(self):
            # Randomly select a question and answers
            selected_question = random.choice(self.questions)
            Q = selected_question["question"]
            A = selected_question["a"]
            B = selected_question["b"]
            C = selected_question["c"]
            correct_answer = selected_question["correct"]

            # Rest of your code for displaying the question and answers
            pop_up_rect = pygame.Rect(30, 150, 750, 500)
            pygame.draw.rect(screen, (255, 255, 255), pop_up_rect)

            # QUESTIONS
            question_text = get_font(20).render(Q, True, "black")
            question_rect = question_text.get_rect(center=(screen_width // 2, screen_height // 2))
            screen.blit(question_text, question_rect)

            # ANSWERS
            answer_text1 = get_font(20).render("A." + A, True, "black")
            answer_rect1 = answer_text1.get_rect(center=(250, 350))
            screen.blit(answer_text1, answer_rect1)

            answer_text2 = get_font(20).render("B." + B, True, "black")
            answer_rect2 = answer_text1.get_rect(center=(250, 450))
            screen.blit(answer_text2, answer_rect2)

            answer_text3 = get_font(20).render("C." + C, True, "black")
            answer_rect3 = answer_text1.get_rect(center=(250, 550))
            screen.blit(answer_text3, answer_rect3)

            pygame.display.update()
        
        def resume_game(self):
    # Add any necessary logic to resume the game
            pass


        def draw_elements(self):
            self.draw_grass()
            self.fruit.draw_fruit()
            self.snake.draw_snake()
            self.draw_score()

        def check_collision(self):
            if self.fruit.pos == self.snake.body[0]:
                self.fruit.randomize()
                self.snake.add_block()
                self.score += 1
                
            for block in self.snake.body[1:]:
                if block == self.fruit.pos:
                    self.fruit.randomize()

        
        def check_fail(self):
            if not 0 <= self.snake.body[0].x < cell_number or not 0 <=self.snake.body[0].y < cell_number:
                self.game_over()
                death_fx.play()
            
            for block in self.snake.body[1:]:

                if block == self.snake.body[0]:

                    self.game_over()
      

        def game_over(self):
            
            self.snake.reset()
            
            
        def draw_grass(self):
            grass_color = (205, 240, 255)
            for row in range(cell_number):
                if row % 2 == 0:
                    for col in range(cell_number):
                        if col % 2 == 0:
                            grass_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
                            pygame.draw.rect(screen,grass_color,grass_rect)
                else:
                    for col in range(cell_number):
                        if col % 2 != 0:
                            grass_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
                            pygame.draw.rect(screen,grass_color,grass_rect)

        def draw_score(self):
            score_text = str(len(self.snake.body) - 3)
            score_surface = game_font.render(score_text,True,(56,74,12))
            score_x = int(cell_size * cell_number - 60)
            score_y = int(cell_size * cell_number - 40)
            score_rect = score_surface.get_rect(center = (score_x,score_y))
            apple_rect = apple.get_rect(midright = (score_rect.left,score_rect.centery))
            bg_rect = pygame.Rect(apple_rect.left,apple_rect.top,apple_rect.width + score_rect.width + 6,apple_rect.height)

            pygame.draw.rect(screen,(167,209,61),bg_rect)
            screen.blit(score_surface,score_rect)
            screen.blit(apple,apple_rect)
            pygame.draw.rect(screen,(56,74,12),bg_rect,2)


pygame.init()
screen_width = 750
screen_height = 450
cell_size = 40
cell_number = 20
screen =  pygame.display.set_mode((cell_number*cell_size,cell_number*cell_size))
game_font = pygame.font.Font('Font/PoetsenOne-Regular.ttf', 25)
SCREEN = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Snake Trivia Game")
clock = pygame.time.Clock()
apple = pygame.image.load('Assets/fruit.png').convert_alpha()
apple = pygame.transform.scale(apple,(40,40))
BG = pygame.image.load("Assets/Background.png")
pygame.mixer.music.load('Music/bg_music.mp3')
pygame.mixer.music.set_volume(0.6)
pygame.mixer.music.play(-1, 0.0)
death_fx = pygame.mixer.Sound("Music/death.mp3")
death_fx.set_volume(1)


def get_font(size):
    return pygame.font.Font("Font/font.ttf", size)

main_game = MAIN()
SCREEN_UPDATE = pygame.USEREVENT


pygame.time.set_timer(SCREEN_UPDATE,100)
pause = True
        

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(35).render("Snake Trivia Game", True, "white")
        MENU_RECT = MENU_TEXT.get_rect(center=(400, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("Assets/Buttons/Play Rect.png"), pos=(400, 350), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("Assets/Buttons/Quit Rect.png"), pos=(400, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    
                    play()

                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def play():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 run = False

            if event.type == SCREEN_UPDATE:
                main_game.update()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused()
                if event.key == pygame.K_UP:
                    if main_game.snake.direction.y != 1:
                        main_game.snake.direction = Vector2(0, -1)
                if event.key == pygame.K_DOWN:
                    if main_game.snake.direction.y != -1:
                        main_game.snake.direction = Vector2(0, 1)
                if event.key == pygame.K_LEFT:
                    if main_game.snake.direction.x != 1:
                        main_game.snake.direction = Vector2(-1, 0)
                if event.key == pygame.K_RIGHT:
                    if main_game.snake.direction.x != -1:
                        main_game.snake.direction = Vector2(1, 0)

        # Use the same display surface for drawing
        screen.fill((255, 246, 255))
        main_game.draw_elements()
        pygame.display.update()
        clock.tick(60)

def paused():
    while pause:
        
        MENU_TEXT = get_font(15).render("Press Escape to Continue", True, "black")
        MENU_RECT = MENU_TEXT.get_rect(center=(400, 100))
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:    
                if event.key == pygame.K_ESCAPE:                        
                        play()
                        
        pygame.display.update()
        clock.tick(60)
    

main_menu()
