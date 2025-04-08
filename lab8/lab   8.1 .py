import pygame
import random

pygame.init()

# Установка параметров экрана
WIDTH, HEIGHT = 500, 700  # Размеры экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Создание окна
pygame.display.set_caption("Car Game")  # Название окна

# Загрузка изображений
car_img = pygame.image.load("car.png")  # Машина
coin_img = pygame.image.load("coin.png")  # Монета
road_img = pygame.image.load("road.jpg")  # Дорога

# Масштабирование изображений
car_width, car_height = 70, 140
coin_width, coin_height = 40, 40

car_img = pygame.transform.scale(car_img, (car_width, car_height))
coin_img = pygame.transform.scale(coin_img, (coin_width, coin_height))
road_img = pygame.transform.scale(road_img, (WIDTH, HEIGHT))

# Положение и скорость машины
car_x = WIDTH // 2 - car_width // 2
car_y = HEIGHT - car_height - 20
car_speed = 5

# Монета: начальные координаты и скорость
coin_x = random.randint(50, WIDTH - 50)
coin_y = -50
coin_speed = 10

# Счёт
score = 0
font = pygame.font.Font(None, 36)

# Таймер
clock = pygame.time.Clock()

# Главный игровой цикл
running = True
while running:
    # Отрисовка фона и объектов
    screen.blit(road_img, (0, 0))
    screen.blit(car_img, (car_x, car_y))
    screen.blit(coin_img, (coin_x, coin_y))
    
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление машиной
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 10:
        car_x -= car_speed
    if keys[pygame.K_RIGHT] and car_x < WIDTH - car_width - 10:
        car_x += car_speed
    # Возможность движения по вертикали
    # if keys[pygame.K_UP] and car_y > 0:
    #     car_y -= car_speed
    # if keys[pygame.K_DOWN] and car_y < HEIGHT - car_height:
    #     car_y += car_speed

    # Движение монеты
    coin_y += coin_speed
    if coin_y > HEIGHT:
        coin_y = -50
        coin_x = random.randint(50, WIDTH - 50)

    # Проверка на столкновение с монетой
    if (car_x < coin_x < car_x + car_width or car_x < coin_x + coin_width < car_x + car_width) and \
       (car_y < coin_y < car_y + car_height or car_y < coin_y + coin_height < car_y + car_height):
        score += 1
        coin_y = -50
        coin_x = random.randint(50, WIDTH - 50)

    # Отображение очков (в правом верхнем углу)
    text = font.render(f"Score: {score}", True, (255, 255, 255))
    text_rect = text.get_rect(topright=(WIDTH - 10, 10))
    screen.blit(text, text_rect)

    # Обновление экрана
    pygame.display.update()
    clock.tick(30)

pygame.quit()
