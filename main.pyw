import pygame


def draw_text(text, x, y):
    font = "Starborn.ttf"
    font = pygame.font.Font(font, 30)
    text_surface = font.render(text, True, white)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)


def draw_grid(num):
    for i in range(num):
        for j in range(num):
            pygame.draw.rect(
                screen, white, (200, 100, 50+(i*50), 50+(j*50)), 1)


def draw_color(x, y, col):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    pygame.draw.circle(screen, col, (225+(x*50), 125+(y*50)), 20)
    if (mouse[0] > (200 + (x*50)) and mouse[0] < (250 + (x*50)) and mouse[1] > (100 + (y*50)) and mouse[1] < (150 + (y*50))):
        if (click[0]):
            draw_text("mouse on color", 200, 30)


pygame.init()
pygame.display.set_caption('Color link')
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
FPS = 60


running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    draw_text(str(pygame.mouse.get_pos()), 700, 25)
    draw_grid(5)
    draw_color(0, 0, blue)
    draw_color(4, 0, blue)
    draw_color(0, 1, green)
    draw_color(4, 1, green)
    draw_color(0, 2,  (255, 0, 0))
    draw_color(4, 2,  red)
    pygame.display.update()
    clock.tick(FPS)
