#Second exercise;

import pygame
pygame.init()
screen = pygame.display.set_mode((1163, 535))

isDone = True
index = 0
sounds = [
    r"C:\Users\user\Desktop\PP2\lab 7\Miyagi - Captain.mp3",
    r"C:\Users\user\Desktop\PP2\lab 7\MiyaGi & Эндшпиль - Fire Man.mp3",
    r"C:\Users\user\Desktop\PP2\lab 7\Виктор Цой - Группа крови.mp3"
]

color = (255, 255, 255)

isPaused = False
isPlayed = True
while isDone:
    screen.fill(color)
    pygame.display.update()
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            isDone = False

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            if index == len(sounds) - 1:
                index = 0
            else:
                index += 1
            isPaused = False
            isPlayed = True

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            if index == 0:
                index = len(sounds) - 1
            else:
                index -= 1
            isPaused = False
            isPlayed = True

        if event.type == pygame.KEYDOWN and isPlayed:
            if isPaused:
                pygame.mixer.music.unpause()
                isPaused = not isPaused
            else:
                pygame.mixer.music.load(sounds[index])
                pygame.mixer.music.play(2)
            isPlayed = not isPlayed

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not isPlayed:
            pygame.mixer.music.pause()
            isPlayed = not isPlayed
            isPaused = not isPaused

    pygame.display.flip()