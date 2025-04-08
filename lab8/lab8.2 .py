import pygame
import random

pygame.init()  # Инициализация Pygame
WIDTH, HEIGHT = 600, 400  # Ширина и высота окна
CELL_SIZE = 20  # Размер клетки (змеи и еды)
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Создание экрана
pygame.display.set_caption("Snake Game")  # Установка заголовка окна

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

snake = [(100, 100)]  # Начальная позиция змеи
snake_dir = (CELL_SIZE, 0)  # Движение направо
food = (random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE))
score = 0
level = 1
speed = 10

running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)  # Заливка экрана белым цветом
    
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Если нажата кнопка "Х" на окне, завершить игру
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dir != (0, CELL_SIZE):
                snake_dir = (0, -CELL_SIZE)
            if event.key == pygame.K_DOWN and snake_dir != (0, -CELL_SIZE):
                snake_dir = (0, CELL_SIZE)
            if event.key == pygame.K_LEFT and snake_dir != (CELL_SIZE, 0):
                snake_dir = (-CELL_SIZE, 0)
            if event.key == pygame.K_RIGHT and snake_dir != (-CELL_SIZE, 0):
                snake_dir = (CELL_SIZE, 0)
    
    # Перемещение змеи
    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
    
    # Проверка на столкновение со стенками или с собой
    if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT or new_head in snake:
        running = False
        break
    
    snake.insert(0, new_head)
    
    # Поедание еды
    if new_head == food:
        score += 1
        food = (random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE))
        if score % 4 == 0:
            level += 1
            speed += 2  # Увеличение скорости
    else:
        snake.pop()
    
    # Отображение еды на экране
    pygame.draw.rect(screen, RED, (food[0], food[1], CELL_SIZE, CELL_SIZE))
    
    # Отображение змеи на экране
    for part in snake:
        pygame.draw.rect(screen, GREEN, (part[0], part[1], CELL_SIZE, CELL_SIZE))
    
    font = pygame.font.Font(None, 30)
    text = font.render(f"Score: {score}  Level: {level}", True, BLACK)
    screen.blit(text, (10, 10))
    
    pygame.display.update()  # Обновление экрана
    clock.tick(speed)  # Контроль частоты кадров (скорости игры)

pygame.quit()  # Завершение работы Pygame
