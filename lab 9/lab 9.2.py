import pygame
import random

pygame.init()
WIDTH, HEIGHT = 600, 400  # Ширина и высота окна
CELL_SIZE = 20  # Размер одной клетки (и еды)
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Создание окна
pygame.display.set_caption("Snake Game")  # Название окна

# Цвета
WHITE = (255, 255, 255)  # Белый цвет фона
GREEN = (0, 255, 0)      # Зелёный цвет змейки
RED = (255, 0, 0)        # Красный цвет еды
BLACK = (0, 0, 0)        # Чёрный цвет текста

snake = [(100, 100)]  # Начальная позиция змейки (один сегмент)
snake_dir = (CELL_SIZE, 0)  # Начальное направление движения (вправо)

# Начальная позиция и размер еды
food = (random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE))
food_size = random.choice([CELL_SIZE, CELL_SIZE * 2])  # Размер еды: обычная или большая
food_timer = 100  # Таймер, через сколько ходов еда исчезнет

score = 0   # Очки игрока
level = 1   # Уровень игрока
speed = 10  # Начальная скорость игры (кадров в секунду)

running = True
clock = pygame.time.Clock()  # Таймер для регулировки скорости игры

while running:
    screen.fill(WHITE)  # Очистка экрана (фон белый)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Если нажата кнопка "закрыть окно"
            running = False

        # Обработка нажатия клавиш
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dir != (0, CELL_SIZE):      # Вверх
                snake_dir = (0, -CELL_SIZE)
            if event.key == pygame.K_DOWN and snake_dir != (0, -CELL_SIZE):   # Вниз
                snake_dir = (0, CELL_SIZE)
            if event.key == pygame.K_LEFT and snake_dir != (CELL_SIZE, 0):    # Влево
                snake_dir = (-CELL_SIZE, 0)
            if event.key == pygame.K_RIGHT and snake_dir != (-CELL_SIZE, 0):  # Вправо
                snake_dir = (CELL_SIZE, 0)

    # Создание новой головы змейки
    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])

    # Проверка на столкновение со стенками или с собой
    if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT or new_head in snake:
        running = False  # Завершение игры
        break

    snake.insert(0, new_head)  # Добавление новой головы в змейку

    # Проверка на поедание еды (с учётом размера еды)
    if new_head[0] < food[0] + food_size and new_head[0] + CELL_SIZE > food[0] and \
       new_head[1] < food[1] + food_size and new_head[1] + CELL_SIZE > food[1]:
        score += food_size // CELL_SIZE  # Очки зависят от размера еды
        food = (random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE))
        food_size = random.choice([CELL_SIZE, CELL_SIZE * 2])  # Новый размер еды
        food_timer = 100  # Сброс таймера еды
        if score % 4 == 0:  # Каждые 4 очка — новый уровень
            level += 1
            speed += 2  # Увеличение скорости
    else:
        snake.pop()  # Удаление последнего сегмента — змейка не растёт

    # Таймер исчезновения еды
    food_timer -= 1
    if food_timer <= 0:
        food = (random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE))
        food_size = random.choice([CELL_SIZE, CELL_SIZE * 2])
        food_timer = 100

    # Отрисовка еды
    pygame.draw.rect(screen, RED, (food[0], food[1], food_size, food_size))

    # Отрисовка змейки
    for part in snake:
        pygame.draw.rect(screen, GREEN, (part[0], part[1], CELL_SIZE, CELL_SIZE))

    # Отображение текста (счёт и уровень)
    font = pygame.font.Font(None, 30)
    text = font.render(f"Очки: {score}  Уровень: {level}", True, BLACK)
    screen.blit(text, (10, 10))

    pygame.display.update()  # Обновление экрана
    clock.tick(speed)  # Задержка в зависимости от скорости

pygame.quit()  # Завершение игры
