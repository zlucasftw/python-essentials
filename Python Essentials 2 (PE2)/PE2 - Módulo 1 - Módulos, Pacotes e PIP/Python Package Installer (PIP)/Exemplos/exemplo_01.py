# Como utilizar o pip: programa de teste simples

# Utilizando pygame

import pygame

run = True
width = 400
heigth = 400
pygame.init()
screen = pygame.display.set_mode((width, heigth))
font = pygame.font.SysFont(None, 48)
text = font.render("Welcome to pygame", True, (255, 255, 255))
screen.blit(text, ((width - text.get_width()) // 2, (heigth - text.get_height()) // 2))
pygame.display.flip()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT\
        or event.type == pygame.MOUSEBUTTONUP\
        or event.type == pygame.KEYUP:
            run = False
