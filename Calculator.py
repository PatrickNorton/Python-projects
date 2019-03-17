import pygame
import sympy
pygame.init()
screen = pygame.display.set_mode((600, 400))
font = pygame.font.SysFont('Arial', 30)
textsurface = font.render('\u25ae', True, (0, 0, 0))
screen.fill((255, 255, 255))
screen.blit(textsurface, (0, 0))
pygame.display.set_caption('Calculator')
pygame.display.flip()
running = True
text = ''
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                pass
                #! Figure out how to pass inputs to the math parser
            elif event.key == pygame.K_BACKSPACE:
                text = text[:-1]
            else:
                text += event.unicode
            textsurface = font.render(text+'\u25ae', True, (0, 0, 0))
            screen.fill((255, 255, 255))
            screen.blit(textsurface, (0, 0))
            pygame.display.update()
pygame.quit()
