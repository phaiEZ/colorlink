import pygame


def draw_text(text, x, y):
    font = "Starborn.ttf"
    font = pygame.font.Font(font, 30)
    text_surface = font.render(text, True, gridcolor)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)


def draw_grid(num):
    for i in range(num):
        for j in range(num):
            pygame.draw.rect(
                screen, gridcolor, (200, 100, 50+(i*50), 50+(j*50)), 1)


def draw_color(x, y, col):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    pygame.draw.circle(screen, col, (225+(x*50), 125+(y*50)), 20)
    if (mouse[0] > (200 + (x*50)) and mouse[0] < (250 + (x*50)) and mouse[1] > (100 + (y*50)) and mouse[1] < (150 + (y*50))):
        if (click[0]):
            draw_text("mouse on color", 200, 30)


def draw_lines(x, y, col):
    pygame.draw.rect(screen, col, (200+(x*50), 100+(y*50), 50, 50))


pygame.init()
pygame.display.set_caption('Color link')


blue = ("#0000ff")
red = ("#ff0000")
green = ("#00FF00")
brown = ("#A52A2A")
pink = ("#b37f8c")

gridcolor = (255, 255, 255)
bgcolor = (0, 0, 0)
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
FPS = 60

colormap = [[1, 0, 0, 0, 1],
            [2, 0, 0, 0, 2],
            [3, 0, 0, 0, 3],
            [4, 0, 0, 0, 4],
            [5, 0, 0, 0, 5], ]

running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    draw_text(str(pygame.mouse.get_pos()), 700, 25)
    draw_grid(5)
    draw_color(0, 0, red)
    draw_lines(1, 0, red)
    draw_lines(1, 1, red)
    draw_lines(1, 2, red)
    draw_color(4, 0, red)
    pygame.display.update()
    clock.tick(FPS)
