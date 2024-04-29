import pygame
import time
import random
pygame.font.init()

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
# This moves 7 px
PLAYER_VEL = 7
STAR_WIDTH = 10
STAR_HEIGHT = 20
# Add desired system font here ex. comicsans
FONT = pygame.font.SysFont("arial", 20)

def draw(player, elapsed_time):
    WIN.blit(BG, (0, 0))

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    # Space the text down and over from the edge of the screen
    WIN.blit(time_text, (10, 10))

    pygame.draw.rect(WIN, (255, 245, 225), player, border_radius=PLAYER_RADIUS)

    pygame.display.update()

def main():
    run = True

    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    star_add_increment = 2000
    star_count = 0

    stars = []

    while run:
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time

        if star_count > star_add_increment:
            for _ in range(3):
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, - STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)

            # Pick max star add increment 2s and then every 50 ms increase increment
            star_add_increment = max(200, star_add_increment - 50)
            star_count = 0    

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

        for star in stars[:]:
            star.y += STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break     

        draw(player, elapsed_time)    

    pygame.quit()       

if __name__ == "__main__":
    main() 