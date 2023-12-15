import pygame


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Шарики')
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)

    v = 100
    radius = 10
    clock = pygame.time.Clock()
    balls = []
    running = True
    screen.fill('black')
    while running:
        screen.fill('black')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:

                balls.append([[event.pos[0], event.pos[1]], [-1, -1], ])
        for ball in balls:
            ball[0][0] += ball[1][0] * (v / 1000)
            ball[0][1] += ball[1][1] * (v / 1000)
            if ball[0][0] < radius:
                ball[0][0] = radius
                ball[1][0] *= -1
            if ball[0][1] < radius:
                ball[0][1] = radius
                ball[1][1] *= -1
            if ball[0][0] > width - radius:
                ball[0][0] = width - radius
                ball[1][0] *= -1
            if ball[0][1] > height - radius:
                ball[0][1] = height - radius
                ball[1][1] *= -1
        for ball in balls:
            pygame.draw.circle(screen, 'white', ball[0], radius)

        pygame.display.flip()
    pygame.quit()