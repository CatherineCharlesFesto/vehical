import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Changer")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Custom event type for changing sprites
CHANGE_SPRITE_EVENT = pygame.USEREVENT + 1

# Sprite class
class MySprite(pygame.sprite.Sprite):
    def __init__(self, color, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.current_image_index = 0
        self.images = [] # To store multiple images for changing

    def add_image(self, image_surface):
        self.images.append(image_surface)

    def change_image(self):
        if self.images:
            self.current_image_index = (self.current_image_index + 1) % len(self.images)
            self.image = self.images[self.current_image_index]

# Create sprites
sprite1 = MySprite(RED, 50, 200, 50, 50)
sprite2 = MySprite(BLUE, 700, 200, 50, 50)

# Create alternative images for sprites
alt_image1 = pygame.Surface([50, 50])
alt_image1.fill((0, 255, 0)) # Green
sprite1.add_image(alt_image1)

alt_image2 = pygame.Surface([50, 50])
alt_image2.fill((255, 255, 0)) # Yellow
sprite2.add_image(alt_image2)

# Create a sprite group
all_sprites = pygame.sprite.Group()
all_sprites.add(sprite1)
all_sprites.add(sprite2)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Post the custom event to change sprites
                pygame.event.post(pygame.event.Event(CHANGE_SPRITE_EVENT))
        if event.type == CHANGE_SPRITE_EVENT:
            sprite1.change_image()
            sprite2.change_image()

    # Drawing
    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
