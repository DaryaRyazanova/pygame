import pygame
width, height = map(int, input().split())
pygame.init()
size = width, height
screen = pygame.display.set_mode(size)
screen.fill((0, 0, 0))
pygame.draw.line(screen, (255, 255, 255), (0, 0), (width, height), 5)
pygame.draw.line(screen, (255, 255, 255), (0, height), (width, 0), 5)
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()



