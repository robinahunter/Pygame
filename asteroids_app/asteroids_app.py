import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Game constants
WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Asteroids")

BG = pygame.image.load("spacebg.jpg")

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
PLAYER_RADIUS = 10
# This moves 5 px
PLAYER_VEL = 5

def draw(player):
    WIN.blit(BG, (0, 0))

    pygame.draw.rect(WIN, (255, 245, 225), player, border_radius=PLAYER_RADIUS)

    pygame.display.update()

def main():
    run = True

    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

    clock = pygame.time.Clock()

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        # Pygame Key Codes
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL    


        draw(player)    

    pygame.quit()       

if __name__ == "__main__":
    main() 