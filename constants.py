# Constants
WIDTH = 500
HEIGHT = 500
FPS = 75

# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
TEAL = (0, 255, 255)

# Player config
PLAYER_ACC = 0.5
PLAYER_FRIC = -0.10
PLAYER_GRAV = 0.90

# Platforms
PLATFORMS = [(0, HEIGHT - 40, WIDTH, 40),
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20),
                 (125, HEIGHT - 350, 100, 20),
                 (350, 200, 100, 20),
                 (175, 70, 50, 20),
             ]