import pygame
import datetime

pygame.init()
WIDTH, HEIGHT = 1100, 920
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey's clock")

# Загрузка изображений
clock_img = pygame.image.load("clock.png")
clock_face = pygame.transform.scale(clock_img, (WIDTH, HEIGHT))
hand_right = pygame.image.load("rightarm.png")  # Минутная стрелка
hand_left = pygame.image.load("leftarm.png")    # Секундная стрелка

WHITE = (255, 255, 255)
clock = pygame.time.Clock()
running = True

# Смещение угла — если стрелки изначально направлены вправо
OFFSET = 90  # Если нужно, можешь поменять на -90, 180 и т.д., в зависимости от картинки

while running:
    screen.fill(WHITE)
    screen.blit(clock_face, (0, 0))

    # Получение текущего времени
    now = datetime.datetime.now()
    seconds = now.second + now.microsecond / 1_000_000
    minutes = now.minute + seconds / 60

    # Расчёт углов с учётом смещения
    minute_angle = - (minutes * 6) - OFFSET
    second_angle = - (seconds * 6) - OFFSET

    # Поворот стрелок
    rotated_right_hand = pygame.transform.rotate(hand_right, minute_angle)
    rotated_left_hand = pygame.transform.rotate(hand_left, second_angle)

    # Центровка
    rh_rect = rotated_right_hand.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    lh_rect = rotated_left_hand.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    # Отображение стрелок
    screen.blit(rotated_right_hand, rh_rect.topleft)
    screen.blit(rotated_left_hand, lh_rect.topleft)

    pygame.display.update()

    # Обработка закрытия окна
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)

pygame.quit()
