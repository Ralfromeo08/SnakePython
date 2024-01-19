import pygame, sys , random
from pygame.math import Vector2
from button import Button
import pickle

class Highscore:
    def __init__(self, filename="highscore.dat"):
        self.filename = filename
        self.highscore = self.load_highscore()

    def load_highscore(self):
        try:
            with open(self.filename, "rb") as file:
                return pickle.load(file)
        except (FileNotFoundError, EOFError):
            return 0

    def save_highscore(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self.highscore, file)

    def update_highscore(self, score):
        if score > self.highscore:
            self.highscore = score
            self.save_highscore()

    def get_highscore(self):
        return self.highscore

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
        self.direction = Vector2(0,0)\
                          
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

class BOMB:
    def __init__(self):
        self.randomize()
        self.bombs = []  # List to store bomb positions
        self.num_bombs = 3  # Adjust the number of bombs as needed

    def generate_bombs(self):
        self.bombs = []  # Clear existing bombs
        for _ in range(self.num_bombs):
            bomb_pos = Vector2(random.randint(0, cell_number - 1), random.randint(0, cell_number - 1))
            self.bombs.append(bomb_pos)

    def draw_Bomb(self):
        bomb_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(bomb, bomb_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

class BOMB2:
    def __init__(self):
        self.randomize2()
        self.bombs2 = []  # List to store bomb positions
        self.num_bombs2 = 3  # Adjust the number of bombs as needed

    def generate_bombs2(self):
        self.bombs2 = []  # Clear existing bombs
        for _ in range(self.num_bombs2):
            bomb2_pos = Vector2(random.randint(0, cell_number - 1), random.randint(0, cell_number - 1))
            self.bombs2.append(bomb2_pos)

    def draw_Bomb2(self):
        bomb2_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(bomb2, bomb2_rect)

    def randomize2(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

class MAIN:
    
        def __init__(self):
            self.highscore_manager = Highscore()
            self.snake = SNAKE()
            self.fruit = FRUIT()
            self.bomb = BOMB()
            self.bomb = BOMB2()
            self.pause = False
            self.score = 0
            
            self.current_question = None
            self.question_index = 0 
            self.questions = [
                {"question": "What is the capital of France?", "options": ["1. Paris", "2. Berlin", "3. London", "4. Madrid"], "answer": "1. Paris"},
                {"question": "Planet is known as the Red Planet?", "options": ["1. Earth", "2. Venus", "3. Mars", "4. Saturn"], "answer": "3. Mars"},
                {"question": "Earth's Twin Sister?","options": ["1. Earth", "2. Venus", "3. Mars", "4. Saturn"], "answer": "2. Venus"},
                {"question": "Planet is closest to the Sun?","options": ["1. Mercury", "2. Venus", "3. Earth", "4. Mars"], "answer": "1. Mercury"},
                {"question": "'Morning Star' or 'Evening Star'?","options": ["1. Mars", "2. Venus", "3. Jupiter", "4. Saturn"], "answer": "2. Venus"},
                {"question": "dwarf planet beyond Neptune","options": ["1. Pluto", "2. Eris", "3. Haumea", "4. Makemake"], "answer": "1. Pluto"},
                {"question": "Which planet has the Great Red Spot","options": ["1. Mars", "2. Jupiter", "3. Saturn", "4. Uranus"], "answer": "2. Jupiter"},
                {"question": "Only Living planet","options": ["1. Mars", "2. Earth", "3. Saturn", "4. Uranus"], "answer": "2. Earth"},
                {"question": "It has Rings", "options": ["1. Mars", "2. Earth", "3. Saturn", "4. Uranus"],"answer": "3. Saturn"},
                {"question": "distinctive black and orange striped coat?","options": ["1. Cheetah", "2. Lion", "3. Tiger", "4. Jaguar"], "answer": "3. Tiger"},
                {"question": "largest mammal in the world?","options": ["1. Elephant", "2. Blue Whale", "3. Giraffe", "4. Gorilla"], "answer": "2. Blue Whale"},
                {"question": "bird known to mimic human speech?","options": ["1. Penguin", "2. Parrot", "3. Owl", "4. Eagle"], "answer": "2. Parrot"},
                {"question": "largest species of bear?","options": ["1. Polar Bear", "2. Grizzly Bear", "3. Panda Bear", "4. Black Bear"],"answer": "1. Polar Bear"},
                {"question": "carries its baby in a pouch?","options": ["1. Koala", "2. Kangaroo", "3. Sloth", "4. Lemur"], "answer": "2. Kangaroo"},
                {"question": "What is the fastest land animal?","options": ["1. Cheetah", "2. Gazelle", "3. Lion", "4. Zebra"], "answer": "1. Cheetah"},
                {"question": "changing color to match its surroundings?","options": ["1. Iguana", "2. Chameleon", "3. Turtle", "4. Snake"], "answer": "2. Chameleon"},
                {"question": "largest species of turtle?","options": ["1. Leatherback Turtle", "2. Loggerhead Turtle", "3. Box Turtle", "4. Snapping Turtle"],"answer": "1. Leatherback Turtle"},
                {"question": "insect produce bioluminescence?","options": ["1. Firefly", "2. Ladybug", "3. Beetle", "4. Butterfly"], "answer": "1. Firefly"},
                {"question": "Who did the Most?","options": ["1. Ralf", "2. Irawa", "3. 50-50", "4. I knew it prefers to not answer"], "answer": "1. Ralf"}
                # Add more questions as needed
            ]

        def update(self):
            self.snake.move_snake()
            self.check_collision()
            self.check_fail()
            self.check_collision_with_bombs()  # Updated method name

            current_score = len(self.snake.body) - 3
            if current_score % 5 == 0 and current_score // 5 > self.question_index:
                self.question_index += 1
                self.show_question()

        def show_question(self):
            if not self.current_question:
                question_index = (len(self.snake.body) - 3) // 5 - 1
                self.current_question = self.questions[question_index]

                # Display the question on the screen
                question_text = get_font(25).render(self.current_question["question"], True, "black")
                question_rect = question_text.get_rect(center=(400, 300))
                screen.fill((255, 255, 255))
                SCREEN.blit(question_text, question_rect)

                # Display answer options
                option_y = 350
                for option in self.current_question["options"]:
                    option_text = get_font(20).render(option, True, "black")
                    option_rect = option_text.get_rect(center=(400, option_y))
                    SCREEN.blit(option_text, option_rect)
                    option_y += 30

                pygame.display.update()

                # Wait for the player's input (answer)
                selected_option = None
                while selected_option is None:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        elif event.type == pygame.KEYDOWN:
                            if pygame.K_1 <= event.key <= pygame.K_9:
                                selected_option = int(event.unicode) - int('1')

                # Clear the question from the screen
                screen.fill((255, 246, 255))
                main_game.draw_elements()
                pygame.display.update()

                # Check if the selected option is correct
                if self.current_question["options"][selected_option] == self.current_question["answer"]:
                    print("correct")
                    noice_fx.play()
                else:
                    print("wrong")
                    #death_fx.play()
                    pygame.time.delay(3000)
                    self.game_over()

                # Reset the current question
                self.current_question = None
        
        def show_question(self):
            if not self.current_question:
                question_index = (len(self.snake.body) - 3) // 5 - 1
                self.current_question = self.questions[question_index]

                # Display the question on the screen
                question_text = get_font(25).render(self.current_question["question"], True, "black")
                question_rect = question_text.get_rect(center=(400, 300))
                screen.fill((255, 255, 255))
                SCREEN.blit(question_text, question_rect)

                # Display answer options
                option_y = 350
                for option in self.current_question["options"]:
                    option_text = get_font(20).render(option, True, "black")
                    option_rect = option_text.get_rect(center=(400, option_y))
                    SCREEN.blit(option_text, option_rect)
                    option_y += 30

                pygame.display.update()

                # Wait for the player's input (answer)
                selected_option = None
                while selected_option is None:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        elif event.type == pygame.KEYDOWN:
                            if pygame.K_1 <= event.key <= pygame.K_9:
                                selected_option = int(event.unicode) - int('1')

                


                    
                # Clear the question from the screen
                screen.fill((255, 246, 255))
                main_game.draw_elements()
                pygame.display.update()


                # Check if the selected option is correct
                if self.current_question["options"][selected_option] == self.current_question["answer"]:
                    print("correct")
                    
                    correct = get_font(25).render("CORRECT!", True, "white")
                    correct_rect = correct.get_rect(center=(400, 300))  # Adjust the position as needed
                    SCREEN.blit(correct, correct_rect)
                    screen.fill((0, 255, 0))
                else:
                    print("wrong")
                    incorrect = get_font(25).render("INCORRECT!", True, "white")
                    incorrect_rect = incorrect.get_rect(center=(400, 300))  # Adjust the position as needed
                    SCREEN.blit(incorrect, incorrect_rect)
                    screen.fill((255, 0, 0))

                # Reset the current question
                self.current_question = None

        def draw_elements(self):
            self.draw_grass()
            self.fruit.draw_fruit()
            self.snake.draw_snake()
            self.draw_score()
            self.bomb.draw_Bomb2()
            self.bomb.draw_Bomb2()
            self.draw_highscore()
        
        def draw_highscore(self):
            highscore_text = get_font(10).render(f"Highscore: {self.highscore_manager.get_highscore()}", True, "black")
            highscore_rect = highscore_text.get_rect(topright=(790, 720))
            SCREEN.blit(highscore_text, highscore_rect)

        def check_collision_with_bombs(self):
            for bomb_pos in self.bomb.bombs2:
                if bomb_pos == self.snake.body[0]:
                    self.game_over()
                    #death_fx.play()

        def check_collision(self):
            if self.bomb.pos == self.snake.body[0]:
                self.game_over()
                death_fx.play()
            elif self.bomb.pos == self.snake.body[0]:
                self.game_over()
                death_fx.play()
            if self.fruit.pos == self.snake.body[0]:
                gawk_fx.play()
                self.fruit.randomize()
                self.snake.add_block()
                self.score += 1

            for block in self.snake.body[1:]:
                if block == self.fruit.pos:
                    gawk_fx.play()
                    self.fruit.randomize()

        
        def check_fail(self):
            if not 0 <= self.snake.body[0].x < cell_number or not 0 <=self.snake.body[0].y < cell_number:
                death_fx.play()
                self.highscore_manager.update_highscore(len(self.snake.body) - 3)
                self.game_over()

            
            for block in self.snake.body[1:]:
                
                if block == self.snake.body[0]:
                    self.highscore_manager.update_highscore(len(self.snake.body) - 3)
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
            self.score = len(self.snake.body) - 3  # Update the score based on the snake's body length
            score_text = str(self.score)
            score_surface = game_font.render(score_text, True, (56, 74, 12))
            score_x = int(cell_size * cell_number - 60)
            score_y = int(cell_size * cell_number - 40)
            score_rect = score_surface.get_rect(center=(score_x, score_y))
            apple_rect = apple.get_rect(midright=(score_rect.left, score_rect.centery))
            bg_rect = pygame.Rect(apple_rect.left, apple_rect.top, apple_rect.width + score_rect.width + 6,
                                  apple_rect.height)

            pygame.draw.rect(screen, (167, 209, 61), bg_rect)
            screen.blit(score_surface, score_rect)
            screen.blit(apple, apple_rect)
            pygame.draw.rect(screen, (56, 74, 12), bg_rect, 2)


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
bomb = pygame.image.load('Assets/bomb.png').convert_alpha()
bomb = pygame.transform.scale(bomb, (40, 40))
bomb2 = pygame.image.load('Assets/bomb2.png').convert_alpha()
bomb2 = pygame.transform.scale(bomb, (40, 40))
pygame.mixer.music.load('Music/bg_music.mp3')
pygame.mixer.music.set_volume(0.6)
pygame.mixer.music.play(-1, 0.0)
death_fx = pygame.mixer.Sound("Music/death.mp3")
death_fx.set_volume(1)
noice_fx = pygame.mixer.Sound("Music/noice.mp3")
noice_fx.set_volume(1)
gawk_fx = pygame.mixer.Sound("Music/gawk.mp3")
gawk_fx.set_volume(1)
FPS = 10


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
                main_game.draw_elements()  # Draw the elements after updating
                pygame.display.update()

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
        clock.tick(FPS)
        
def paused():
    countdown_time = 3  # Set the countdown time in seconds
    pygame.time.set_timer(SCREEN_UPDATE, 0)  # Disable the regular screen update
    paused_start_time = pygame.time.get_ticks()

    while pause:
        elapsed_time = (pygame.time.get_ticks() - paused_start_time) // 1000
        remaining_time = max(0, countdown_time - elapsed_time)


        MENU_TEXT = get_font(15).render(f"Game Paused", True, "black")
        MENU_RECT = MENU_TEXT.get_rect(center=(400, 100))
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.time.set_timer(SCREEN_UPDATE, 100)
                    MENU_TEXT = get_font(15).render(f"Resuming in {remaining_time} seconds", True, "black")
                    MENU_RECT = MENU_TEXT.get_rect(center=(400, 100))
                    SCREEN.blit(MENU_TEXT, MENU_RECT)  # Re-enable the regular screen update
                    play()

        pygame.display.update()
        clock.tick(FPS)
    

main_menu()
