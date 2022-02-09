import pygame, sys
pygame.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 233, 0)
SKY = (100, 240, 255)
size=(800, 500)
screen = pygame.display.set_mode(size)
while True:
    for event in pygame.event.get():
          if event.type == pygame.QUIT:
                 sys.exit()
    screen.fill(SKY)
    pygame.draw.circle(screen, YELLOW, (700,100), 60)
    pygame.draw.rect(screen, GREEN, [(0, 350), (800,150)])
    pygame.display.flip()
