import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BROWN = (165, 42, 42)
BLUE = (0, 0, 255)

# Set the dimensions of the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Set the size of each segment of the snake
SEGMENT_SIZE = 20

# Set the size of each barrier block
BARRIER_SIZE = SEGMENT_SIZE

# Set the minimum and maximum number of barriers to generate
MIN_BARRIERS = 5
MAX_BARRIERS = 10

# Define the possible directions the snake can move
DIRECTIONS = {
    'UP': (0, -SEGMENT_SIZE),
    'DOWN': (0, SEGMENT_SIZE),
    'LEFT': (-SEGMENT_SIZE, 0),
    'RIGHT': (SEGMENT_SIZE, 0)
}

# Initialize Pygame
pygame.init()

# Set the font for the score display
font = pygame.font.SysFont('Arial', 30)

# Set the caption for the game window
pygame.display.set_caption('Snake Game')

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Define a function to draw the snake
def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, [segment[0], segment[1], SEGMENT_SIZE, SEGMENT_SIZE])

# Define a function to generate a new piece of food
def generate_food(snake, barriers):
    while True:
        x = random.randrange(SEGMENT_SIZE, SCREEN_WIDTH - SEGMENT_SIZE, SEGMENT_SIZE)
        y = random.randrange(SEGMENT_SIZE, SCREEN_HEIGHT - SEGMENT_SIZE, SEGMENT_SIZE)
        if [x, y] not in snake and [x, y] not in barriers:
            return [x, y]

# Define a function to generate a random set of barriers
def generate_barriers():
    barriers = []
    num_barriers = random.randint(MIN_BARRIERS, MAX_BARRIERS)
    for i in range(num_barriers):
        x = random.randrange(0, SCREEN_WIDTH - BARRIER_SIZE, BARRIER_SIZE)
        y = random.randrange(0, SCREEN_HEIGHT - BARRIER_SIZE, BARRIER_SIZE)
        barriers.append([x, y])
    return barriers

# Define the main function for the game
def main():
    # Generate the barriers
    barriers = generate_barriers()

    # Initialize the snake
    snake = [[SCREEN_WIDTH/2, SCREEN_HEIGHT/2], [SCREEN_WIDTH/2-SEGMENT_SIZE, SCREEN_HEIGHT/2], [SCREEN_WIDTH/2-2*SEGMENT_SIZE, SCREEN_HEIGHT/2]]
    direction = 'RIGHT'

    # Generate the first piece of food
    food = generate_food(snake, barriers)

    # Initialize the score
    score = 0

    # Set the clock for the game
    clock = pygame.time.Clock()

    # Set the game loop flag
    game_over = False

    # Start the game loop
    while not game_over:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != 'RIGHT':
                    direction = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    direction = 'RIGHT'
                elif event.key == pygame.K_UP and direction != 'DOWN':
                    direction = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    direction = 'DOWN'

        # Move the snake
        head = snake[0]
        new_head = [head[0] + DIRECTIONS[direction][0], head[1] + DIRECTIONS[direction][1]]

        # Check if the snake has collided with the walls or barriers
        if (new_head[0] < SEGMENT_SIZE or new_head[0] > SCREEN_WIDTH - SEGMENT_SIZE or
            new_head[1] < SEGMENT_SIZE or new_head[1] > SCREEN_HEIGHT - SEGMENT_SIZE or
            new_head in snake or new_head in barriers):
            game_over = True

        # Check if the snake has eaten the food
        if new_head == food:
            snake.insert(0, new_head)
            food = generate_food(snake, barriers)
            score += 10
        else:
            snake.insert(0,new_head)
        snake.pop()

    # Draw the background
        screen.fill(BLACK)

        # Draw the barriers
        for barrier in barriers:
            pygame.draw.rect(screen, BLUE, [barrier[0], barrier[1], BARRIER_SIZE, BARRIER_SIZE])

        # Draw the walls around the ground
        pygame.draw.rect(screen, BROWN, [0, 0, SCREEN_WIDTH, SEGMENT_SIZE])
        pygame.draw.rect(screen, BROWN, [0, 0, SEGMENT_SIZE, SCREEN_HEIGHT])
        pygame.draw.rect(screen, BROWN, [SCREEN_WIDTH - SEGMENT_SIZE, 0, SEGMENT_SIZE, SCREEN_HEIGHT])
        pygame.draw.rect(screen, BROWN, [0, SCREEN_HEIGHT - SEGMENT_SIZE, SCREEN_WIDTH, SEGMENT_SIZE])

        # Draw the snake
        draw_snake(snake)

        # Draw the food
        pygame.draw.rect(screen, RED, [food[0], food[1], SEGMENT_SIZE, SEGMENT_SIZE])

        # Draw the score
        score_text = font.render('Score: ' + str(score), True, WHITE)
        screen.blit(score_text, [10, 10])

        # Update the screen
        pygame.display.update()

        # Set the game speed
        clock.tick(10)

main()

# Exit the game
pygame.quit()
quit()
