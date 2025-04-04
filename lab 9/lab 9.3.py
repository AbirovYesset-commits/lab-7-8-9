import pygame
import random

pygame.init()  # Инициализация Pygame

WIDTH, HEIGHT = 800, 600  # Ширина и высота окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Создание окна
pygame.display.set_caption("Random Shapes")  # Название окна

WHITE = (255, 255, 255)  # Цвет фона
BLACK = (0, 0, 0)        # Цвет круга
YELLOW = (255, 255, 0)   # Цвет прямоугольника
BLUE = (0, 0, 255)       # Цвет треугольника
RED = (255, 0, 0)        # Цвет ромба
BROWN = (100, 40, 0)     # Цвет квадрата

shapes = []  # Список всех нарисованных фигур

# Функция для генерации случайной позиции
def random_position():
    return random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)

running = True
while running:
    screen.fill(WHITE)  # Очистка экрана (заливка белым)

    # Отрисовка всех фигур из списка
    for shape_type, color, x, y in shapes:

        if shape_type == "circle":
            pygame.draw.circle(screen, color, (x, y), 25)

        elif shape_type == "rectangle":
            pygame.draw.rect(screen, color, (x, y, 100, 50))

        elif shape_type == "triangle":
            pygame.draw.polygon(screen, color, [(x, y), (x - 50, y + 100), (x + 50, y + 100)])

        elif shape_type == "rhombus":
            pygame.draw.polygon(screen, color, [(x, y), (x + 50, y + 50), (x, y + 100), (x - 50, y + 50)])

        elif shape_type == "square":
            pygame.draw.rect(screen, color, (x, y, 50, 50))

    # Обработка событий
    for event in pygame.event.get():

        if event.type == pygame.QUIT:  # Если нажата кнопка "закрыть окно"
            running = False  # Завершить игру

        elif event.type == pygame.KEYDOWN:
            x, y = random_position()  # Случайные координаты для новой фигуры

            if event.key == pygame.K_q:  # Кнопка Q — нарисовать чёрный круг
                shapes.append(("circle", BLACK, x, y))

            elif event.key == pygame.K_w:  # Кнопка W — нарисовать жёлтый прямоугольник
                shapes.append(("rectangle", YELLOW, x, y))

            elif event.key == pygame.K_e:  # Кнопка E — нарисовать синий треугольник
                shapes.append(("triangle", BLUE, x, y))

            elif event.key == pygame.K_r:  # Кнопка R — нарисовать красный ромб
                shapes.append(("rhombus", RED, x, y))

            elif event.key == pygame.K_t:  # Кнопка T — нарисовать коричневый квадрат
                shapes.append(("square", BROWN, x, y))

    pygame.display.update()  # Обновить экран

pygame.quit()  # Завершение игры

    for shape_type, color, x, y in shapes: # All elements of the shapes. 
        
        if shape_type == "circle":
            pygame.draw.circle(screen, color, (x, y), 25)
            
        elif shape_type == "rectangle":
            pygame.draw.rect(screen, color, (x, y, 100, 50))
            
        elif shape_type == "triangle":
            pygame.draw.polygon(screen, color, [(x, y), (x - 50, y + 100), (x + 50, y + 100)])
            
        elif shape_type == "rhombus":
            pygame.draw.polygon(screen, color, [(x, y), (x + 50, y + 50), (x, y + 100), (x - 50, y + 50)])
            
        elif shape_type == "square":
            pygame.draw.rect(screen, color, (x, y, 50, 50))


    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:             # If user push button X
            running = False                       # Programm will stop
            
        elif event.type == pygame.KEYDOWN:
            x, y = random_position()              # Random positions
            
            if event.key == pygame.K_q:           # If user push button Q, then we can see black circle 
                shapes.append(("circle", BLACK, x, y))      # Append black circle to the "shapes" list.
                
            elif event.key == pygame.K_w:         # If user push button W, then we can see yellow rectangle. 
                shapes.append(("rectangle", YELLOW, x, y))  # Append yellow rectangle to the "shapes" list.
                
            elif event.key == pygame.K_e:         # If user push button E, then we can see blue triangle
                shapes.append(("triangle", BLUE, x, y))     # Append blue triangle to the "shapes" list.
                
            elif event.key == pygame.K_r:         
                shapes.append(("rhombus", RED, x, y))
                
            elif event.key == pygame.K_t:  # Квадрат
                shapes.append(("square", BROWN, x, y))

    pygame.display.update()

pygame.quit()
