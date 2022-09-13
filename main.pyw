import pygame


def draw_text(text):
    font = "Starborn.ttf"
    font = pygame.font.Font(font, 30)
    text_surface = font.render(text, True, white)
    text_rect = text_surface.get_rect()
    text_rect.center = (700, 25)
    screen.blit(text_surface, text_rect)


def draw_grid(num):
    for i in range(num):
        for j in range(num):
            pygame.draw.rect(
                screen, white, (200, 100, 50+(i*50), 50+(j*50)), 1)


def draw_color(x, y, col):
    pygame.draw.circle(screen, col, (225+(x*50), 125+(y*50)), 20)


pygame.init()
pygame.display.set_caption('Color link')
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

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
    draw_text(str(pygame.mouse.get_pos()))
    draw_grid(8)
    draw_color(5, 0, blue)
    draw_color(0, 0, blue)
    pygame.display.update()
    clock.tick(FPS)
