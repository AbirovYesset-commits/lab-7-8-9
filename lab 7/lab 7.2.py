import pygame
import os

pygame.init()

# Окно
WIDTH, HEIGHT = 800, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Музыкальный плеер")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Шрифты
font = pygame.font.SysFont("Arial", 28)
title_font = pygame.font.SysFont("Arial", 36, bold=True)

# Звук
pygame.mixer.init()

# Плейлист
sounds = [
    "SMOKEDOPE2016 - IM NOT GOD BUT I WISH I WAS ft. JOEYY (prod. SIKA).mp3",
    "In Da Party.mp3",
    "Dope Love.mp3"
]

# Проверим, что файлы есть
print("Файлы в папке:", os.listdir())

index = 0
isPaused = False
isPlayed = False
running = True

def draw_screen():
    screen.fill(WHITE)
    
    # Название трека
    title = title_font.render("Текущий трек:", True, BLACK)
    screen.blit(title, (30, 30))
    
    track = font.render(sounds[index], True, BLACK)
    screen.blit(track, (30, 80))

    # Подсказки по клавишам
    help_text = font.render("← Назад  |  → Вперед  |  Пробел — Пауза/Продолжить", True, BLACK)
    screen.blit(help_text, (30, HEIGHT - 50))

    pygame.display.flip()

while running:
    draw_screen()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:

            # Влево ←
            if event.key == pygame.K_LEFT:
                index = (index - 1) % len(sounds)
                pygame.mixer.music.load(sounds[index])
                pygame.mixer.music.play()
                isPaused = False
                isPlayed = True

            # Вправо →
            elif event.key == pygame.K_RIGHT:
                index = (index + 1) % len(sounds)
                pygame.mixer.music.load(sounds[index])
                pygame.mixer.music.play()
                isPaused = False
                isPlayed = True

            # Пробел — пауза/возобновление
            elif event.key == pygame.K_SPACE:
                if isPlayed and not isPaused:
                    pygame.mixer.music.pause()
                    isPaused = True
                elif isPlayed and isPaused:
                    pygame.mixer.music.unpause()
                    isPaused = False
                else:
                    pygame.mixer.music.load(sounds[index])
                    pygame.mixer.music.play()
                    isPlayed = True
                    isPaused = False

pygame.quit()
