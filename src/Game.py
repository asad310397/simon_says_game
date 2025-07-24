import pygame
import random
from Config import Config


class Game:
    def __init__(self, display, surface):
        pygame.font.init()
        pygame.mixer.init()

        self.surface = surface
        self.display = display
        self.gameStart = 0
        self.patternIndex = 0
        self.quitVar = False
        self.playerTurn = 1
        self.turnDelay = 0
        self.pattern = []
        self.score = 0

        self.rects = Config["squares"].copy()
        for color in self.rects.keys():
            self.rects[color]["rect"] = None

        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(
            Config["game"]["font"], Config["game"]["font-size"]
        )

    def addColor(self):
        self.pattern.append(random.choice(list(self.rects.keys())))
        self.patternIndex = 0

    def drawScreen(self):
        # reset game space
        self.display.fill(Config["colors"]["black"])
        self.display.blit(self.surface, (0, 0))
        text = ""

        # display the score
        if self.gameStart == 1:
            text = self.font.render(
                "Score: " + str(self.score),
                True,
                Config["colors"]["white"],
            )
        elif self.gameStart == 0:
            text = self.font.render(
                "Press Space To Start",
                True,
                Config["colors"]["white"],
            )
        elif self.gameStart == -1:
            text = self.font.render(
                "You Lose, Press Space To Play Again",
                True,
                Config["colors"]["white"],
            )
        textRect = text.get_rect(center=(400, 20))
        self.display.blit(text, textRect)

        # draw the squares
        for color in self.rects.keys():
            # draw the rectangle
            self.rects[color]["rect"] = pygame.draw.rect(
                self.surface,
                self.rects[color]["color"],
                self.rects[color]["position"],
            )

            # decrease the alpha if it's flashing
            if self.rects[color]["color"][3] > 180:
                self.rects[color]["color"][3] -= 11

            if self.rects[color]["color"][3] < 180 and pygame.mixer.get_busy() == False:
                self.rects[color]["color"][3] = 180
                self.patternIndex += 1

                if self.patternIndex >= len(self.pattern):
                    self.patternIndex = 0
                    if self.playerTurn == 0:
                        self.playerTurn = 1
                    else:
                        self.turnDelay = Config["game"]["turn-delay"]
                        self.addColor()
                        self.playerTurn = 0

    def loop(self):
        self.quitVar = False

        while self.quitVar == False:
            self.drawScreen()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quitVar = True
                if event.type == pygame.KEYDOWN:
                    if self.gameStart < 1 and event.key == pygame.K_SPACE:
                        self.gameStart = 1
                        self.patternIndex = 0
                        self.quitVar = False
                        self.playerTurn = 0
                        self.pattern = []
                        self.score = 0
                        self.addColor()
                if (
                    self.gameStart == 1
                    and self.playerTurn == 1
                    and event.type == pygame.MOUSEBUTTONDOWN
                ):
                    correctColor = False
                    for color in self.rects.keys():
                        currColor = self.rects[color]
                        if (
                            currColor["rect"].collidepoint(event.pos)
                            and self.patternIndex < len(self.pattern)
                            and self.pattern[self.patternIndex] == color
                        ):
                            correctColor = True
                            # if color hasn't already begun flashing
                            if self.rects[color]["color"][3] == 180:
                                pygame.mixer.music.load(self.rects[color]["note"])
                                pygame.mixer.music.play()
                                self.rects[color]["color"][3] = 250
                                self.score += 1
                    if correctColor == False:
                        self.score = 0
                        self.gameStart = -1

            # on display the pattern
            if self.gameStart == 1 and self.playerTurn == 0 and self.turnDelay == 0:
                if (
                    self.patternIndex < len(self.pattern)
                    and pygame.mixer.get_busy() == False
                ):
                    currColorInPattern = self.pattern[self.patternIndex]
                    # if color hasn't already begun flashing
                    if self.rects[currColorInPattern]["color"][3] == 180:
                        pygame.mixer.music.load(self.rects[currColorInPattern]["note"])
                        pygame.mixer.music.play()
                        self.rects[currColorInPattern]["color"][3] = 250
            elif self.gameStart == 1 and self.playerTurn == 0 and self.turnDelay > 0:
                self.turnDelay -= 1

            pygame.display.flip()
            self.clock.tick(Config["game"]["fps"])

        pygame.display.quit()
        exit()
