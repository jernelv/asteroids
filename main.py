import pygame

from constants import *
import player

def main():
    pygame.init()
    game_time = pygame.time.Clock()
    dt = 0
    print("Starting Asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player1 = player.Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,PLAYER_RADIUS)
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0,0,0))
        player1.update(dt)
        player1.draw(screen)
        pygame.display.flip()
        time_passed = game_time.tick(60)
        dt = time_passed/1000
if __name__ == "__main__":
    main()
