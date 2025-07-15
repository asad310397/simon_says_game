import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Simon")

FPS = 30
score = 0
clock = pygame.time.Clock()
font = pygame.font.Font("./PressStart2P-Regular.ttf", 20)
red_rect, green_rect, blue_rect, yellow_rect = None, None, None, None
pattern = []

red_color = (255, 0, 0)
yellow_color = (255, 255, 0)
blue_color = (0, 0, 255)
green_color = (0, 255, 0)
alpha = 0


def drawScreen():
    global red_rect
    text = font.render("Score: " + str(score), True, (255, 255, 255))
    textRect = text.get_rect(center=(400, 20))
    screen.blit(text, textRect)
    red_rect = pygame.draw.rect(screen, red_color, (10, 40, 390, 270))
    yellow_rect = pygame.draw.rect(screen, yellow_color, (10, 320, 390, 270))

    blue_rect = pygame.draw.rect(screen, blue_color, (410, 40, 380, 270))
    green_rect = pygame.draw.rect(screen, green_color, (410, 320, 380, 270))


quitVar = False
while quitVar == False:
    drawScreen()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitVar = True

    pygame.display.update()
    clock.tick(FPS)
    alpha += 1

pygame.display.quit()
exit()
