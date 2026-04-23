import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Constants for grid and display configuration
GRID_SIZE = 10
CELL_SIZE = 50
WINDOW_SIZE = GRID_SIZE * CELL_SIZE
BACKGROUND_COLOR = (0, 0, 0)
REGENERATION_INTERVAL = 5  # seconds
FPS = 60

def generate_random_color_grid():

    return [
        [
            (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            for _ in range(GRID_SIZE)
        ]
        for _ in range(GRID_SIZE)
    ]

def draw_color_grid(screen, color_grid):
    
    for row_index in range(GRID_SIZE):
        for col_index in range(GRID_SIZE):
            cell_color = color_grid[row_index][col_index]
            cell_rectangle = (
                col_index * CELL_SIZE,
                row_index * CELL_SIZE,
                CELL_SIZE,
                CELL_SIZE
            )
            pygame.draw.rect(screen, cell_color, cell_rectangle)

def main():
  
    # Create the display window
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption(
        "Procedural Color Grid (Press SPACE to Regenerate)"
    )

    # Initialize game state and timing
    color_grid = generate_random_color_grid()
    clock = pygame.time.Clock()
    last_regeneration_time = time.time()
    is_running = True

    # Main game loop
    while is_running:
        # Check if 5 seconds have passed and regenerate grid if needed
        current_time = time.time()
        if current_time - last_regeneration_time >= REGENERATION_INTERVAL:
            color_grid = generate_random_color_grid()
            last_regeneration_time = current_time

        # Fill screen with background color
        screen.fill(BACKGROUND_COLOR)

        # Draw the color grid on the screen
        draw_color_grid(screen, color_grid)

        # Update the display to show changes
        pygame.display.flip()

        # Handle user input events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                # Regenerate grid when SPACE key is pressed
                color_grid = generate_random_color_grid()
                last_regeneration_time = time.time()

        # Control frame rate to 60 FPS
        clock.tick(FPS)

    # Clean up and close Pygame
    pygame.quit()

if __name__ == "__main__":
    main()