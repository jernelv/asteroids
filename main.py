import pygame

from constants import *
import player
import asteroid, asteroidfield, shot

def main():
    pygame.init()
    game_time = pygame.time.Clock()
    dt = 0
    print("Starting Asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    asteroids = pygame.sprite.Group()
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)

    shots = pygame.sprite.Group()
    shot.Shot.containers = (shots, updatable, drawable)

    asteroidfield.AsteroidField.containers = (updatable)
    field = asteroidfield.AsteroidField()
    
    player.Player.containers = (updatable, drawable)
    player1 = player.Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,PLAYER_RADIUS)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0,0,0))
        for object in updatable:
            object.update(dt)

        

        for object in drawable:
            object.draw(screen)

        #check for collisions
        for thing in asteroids:
            if player1.does_collide(thing):
                print("Game Over!")
                return
        
        for thing in asteroids:
            for bullet in shots:
                if bullet.does_collide(thing):
                    bullet.kill()
                    thing.split()
        #player1.update(dt)
        #player1.draw(screen)
        pygame.display.flip()
        time_passed = game_time.tick(60)
        dt = time_passed/1000
if __name__ == "__main__":
    main()
