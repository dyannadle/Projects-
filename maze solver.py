import numpy as np
import pygame
import random
from collections import deque

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 15, 15  # Increased grid size
CELL_SIZE = WIDTH // COLS
WHITE = (245, 245, 245)
BLACK = (40, 40, 40)
BLUE = (50, 150, 255)
RED = (255, 50, 50)
GREEN = (50, 205, 50)
GRAY = (180, 180, 180)
FONT_COLOR = (20, 20, 20)
TIMER_LIMIT = 60  # 60 seconds to complete the maze

actions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up

def draw_text(screen, text, position, color=FONT_COLOR, font_size=30):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, position)

def is_valid(state, maze):
    r, c = state
    return 0 <= r < maze.shape[0] and 0 <= c < maze.shape[1] and maze[r, c] != -1

def get_next_state(state, action, maze):
    r, c = state
    dr, dc = actions[action]
    new_state = (r + dr, c + dc)
    return new_state if is_valid(new_state, maze) else state

def is_solvable(maze):
    rows, cols = maze.shape
    start, goal = (0, 0), (rows - 1, cols - 1)
    queue = deque([start])
    visited = set()
    while queue:
        r, c = queue.popleft()
        if (r, c) == goal:
            return True
        for dr, dc in actions:
            nr, nc = r + dr, c + dc
            if is_valid((nr, nc), maze) and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc))
    return False

def generate_maze(rows=ROWS, cols=COLS, obstacle_prob=0.3):
    while True:
        maze = np.zeros((rows, cols))
        goal = (rows - 1, cols - 1)
        maze[goal] = 10
        for r in range(rows):
            for c in range(cols):
                if (r, c) != (0, 0) and (r, c) != goal and random.uniform(0, 1) < obstacle_prob:
                    maze[r, c] = -1
        if is_solvable(maze):
            return maze

def draw_maze(screen, maze, player_pos, time_left, score, steps):
    screen.fill(WHITE)
    for r in range(maze.shape[0]):
        for c in range(maze.shape[1]):
            rect = pygame.Rect(c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if maze[r, c] == -1:
                pygame.draw.rect(screen, BLACK, rect)
            elif maze[r, c] == 10:
                pygame.draw.rect(screen, GREEN, rect)
            pygame.draw.rect(screen, GRAY, rect, 1)
    pygame.draw.rect(screen, BLUE, (player_pos[1] * CELL_SIZE, player_pos[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    draw_text(screen, f"Time Left: {int(time_left)}s", (20, 20), RED, font_size=28)
    draw_text(screen, f"Score: {score}", (WIDTH - 150, 20), RED, font_size=28)
    draw_text(screen, f"Steps: {steps}", (WIDTH // 2 - 50, 20), RED, font_size=28)
    pygame.display.flip()

def play_game():
    maze = generate_maze()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Maze Challenge")
    clock = pygame.time.Clock()
    player_pos = (0, 0)
    goal = (ROWS - 1, COLS - 1)
    start_time = pygame.time.get_ticks()
    score = 0
    steps = 0
    running = True
    
    while running:
        elapsed_time = (pygame.time.get_ticks() - start_time) / 1000
        time_left = max(0, TIMER_LIMIT - elapsed_time)
        if time_left <= 0:
            print("Time’s up! You lost!")
            break
        
        draw_maze(screen, maze, player_pos, time_left, score, steps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                new_pos = player_pos
                if event.key == pygame.K_RIGHT:
                    new_pos = get_next_state(player_pos, 0, maze)
                elif event.key == pygame.K_LEFT:
                    new_pos = get_next_state(player_pos, 1, maze)
                elif event.key == pygame.K_DOWN:
                    new_pos = get_next_state(player_pos, 2, maze)
                elif event.key == pygame.K_UP:
                    new_pos = get_next_state(player_pos, 3, maze)
                
                if new_pos == player_pos:
                    score -= 10  # Negative reward for hitting walls
                else:
                    score += 5  # Positive reward for moving forward
                    player_pos = new_pos
                    steps += 1
        
        if player_pos == goal:
            print("Congratulations! You won!")
            break
        clock.tick(10)
    
    pygame.quit()

play_game()
