if __name__ == '__main__':
    print('Ввод стороны окна и количества клеток')
    w, n = map(int, input().split())
    while w % n != 0:
        print('Повторить ввод: W должно делиться на N')
        w, n = map(int, input().split())


    import pygame


    pygame.init()
    size = w, w
    screen = pygame.display.set_mode(size)
    screen.fill('white')

    for r in range(n):
        for c in range(n):
            if (r + c) % 2 == 0:
                screen.fill('black', (c * (w // n), r * (w // n), w // n, w // n))



    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
