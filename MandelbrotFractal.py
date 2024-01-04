# устанавливаем необходимые библиотеки
import numpy as np
import matplotlib.pyplot as plt

# Задаем размеры изображения
width = 1000
height = 1000

# Задаем границы области, которую мы будем исследовать
real_axis = np.linspace(-2, 1, width)
imaginary_axis = np.linspace(-1.5, 1.5, height)

# Создаем двумерный массив, который будет хранить значения чисел Мандельброта
mandelbrot_set = np.zeros((width, height))

# Проходимся по каждой точке на изображении и вычисляем число Мандельброта
for x in range(width):
    for y in range(height):
        # Преобразуем координаты пикселя в комплексное число
        c = complex(real_axis[x], imaginary_axis[y])
        z = 0
        # Вычисляем число Мандельброта для данной точки
        for i in range(100):
            z = z**2 + c
            if abs(z) > 2:
                mandelbrot_set[x, y] = i
                break

# Отображаем полученный массив как изображение
plt.imshow(mandelbrot_set.T, cmap='hot', interpolation='bilinear', extent=[-2, 1, -1.5, 1.5])
plt.axis('off')
plt.show()
# нужно подождать загрузку картинки
