import pygame
pygame.init()  # Инициализация Pygame

WIDTH, HEIGHT = 800, 600  # Размеры экрана: ширина 800, высота 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Создание окна
pygame.display.set_caption("Simple Paint in Pygame")  # Название окна

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Начальный цвет — чёрный
current_color = BLACK

# Заливка экрана белым цветом
screen.fill(WHITE)

running = True
shape = "circle"  # Начальная форма — круг

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Если нажата кнопка "Х", окно закроется
            running = False
        
        elif event.type == pygame.KEYDOWN:  # Если нажата клавиша
            if event.key == pygame.K_r:  # Если нажата 'R' — рисовать прямоугольник
                shape = "rect"
            elif event.key == pygame.K_c:  # Если нажата 'C' — рисовать круг
                shape = "circle"
            elif event.key == pygame.K_e:  # Если нажата 'E' — включить ластик
                shape = "eraser"
            elif event.key == pygame.K_1:  # Цвет — чёрный
                current_color = BLACK
            elif event.key == pygame.K_2:  # Цвет — красный
                current_color = RED
            elif event.key == pygame.K_3:  # Цвет — синий
                current_color = BLUE
            elif event.key == pygame.K_4:  # Цвет — зелёный
                current_color = GREEN

        elif event.type == pygame.MOUSEBUTTONDOWN:  # Если нажата кнопка мыши
            x, y = event.pos  # Получаем координаты мыши
            if shape == "circle":  # Если выбрана форма "круг"
                pygame.draw.circle(screen, current_color, (x, y), 20)
            elif shape == "rect":  # Если выбрана форма "прямоугольник"
                pygame.draw.rect(screen, current_color, (x, y, 40, 40))
            elif shape == "eraser":  # Если выбран ластик
                pygame.draw.circle(screen, WHITE, (x, y), 20)
    
    pygame.display.update()  # Обновление экрана

pygame.quit()  # Завершение работы Pygame
