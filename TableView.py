try:
    import sys
    import pygame
    from pygame.locals import *
except ImportError as err:
    print("couldn't load module. %s" % (err))
    sys.exit(2)

#borrowed from http://www.pygame.org/docs/tut/tom/games6.html#AEN198
def load_png(name):
    """ Load image and return image object"""
    fullname = sys.os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except pygame.error as message:
        print('Cannot load image:' + fullname)
        raise SystemExit(message)
    return image, image.get_rect()

class TableView():
    """ Set the table """
    def __init__(self):
        self.name = ""
        # Initialise screen
        pygame.init()
        screen = pygame.display.set_mode((1680, 1050))
        pygame.display.set_caption('Commander')

        # Fill background
        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((0, 0, 0))

        # Blit everything to the screen
        screen.blit(background, (0, 0))
        pygame.display.flip()

        # Initialise clock
        clock = pygame.time.Clock()

        # Colours
        red = (255,0,0)
        blue = (0,0, 255)

        # Event loop
        playtime = 0
        FPS = 60

        while 1:
            # Make sure game doesn't run at more than 60 frames per second

            milliseconds = clock.tick(FPS)
            playtime += milliseconds / 1000.0
            text = "FPS: {0:.2f}   Playtime: {1:.2f}".format(clock.get_fps(), playtime)
            pygame.display.set_caption(text)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                elif event.type == KEYDOWN:
                    if event.key == K_a:
                        sleep(1111)
                    if event.key == K_z:
                        sleep(1111)
                    if event.key == K_UP:
                        sleep(1111)
                    if event.key == K_DOWN:
                        sleep(1111)
                elif event.type == KEYUP:
                    if event.key == K_a or event.key == K_z:
                        sleep(1111)
                    if event.key == K_UP or event.key == K_DOWN:
                        sleep(1111)
                # draw grid
                for i in range(10):
                    for j in range(7):
                        pygame.draw.rect(screen, red, (340+ i*100, 70 + j*130, 100, 130), 1)

                pygame.display.flip()

if __name__ == '__main__':
    TableView()
