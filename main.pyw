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


pygame.init()
pygame.display.set_caption('Color link')
white = (255, 255, 255)
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
    pygame.display.update()
    clock.tick(FPS)
