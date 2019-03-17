import pygame
import pygame_textinput
pygame.init()
size = (400, 500)
screen = pygame.display.set_mode(size)
screen.fill((0, 0, 255))
running = True
while running:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False
        elif event == pygame.KEYDOWN:
            pass
pygame.quit()
