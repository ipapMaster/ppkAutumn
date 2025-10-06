# Дополнительно устанавливаемые модули
# Модуль графики PIL (Python Imaging Library - pillow)
# PIP - Python Installation Package
# pip install pillow
from PIL import Image

image = Image.open('images/python.jpg')
pixel = image.load()  # загрузить массив пикселей
r, g, b = pixel[355, 200]
w, h = image.size

print(f'Ширина: {w}, Высота: {h}')
print('Цвет пикселя 355 по X и 200 по Y по каналам:')
print(f'\tКанал R: {r}')
print(f'\tКанал G: {g}')
print(f'\tКанал B: {b}')
print('Инвертируем изображение и пересохраним с новым именем')

for x in range(w):
    for y in range(h):
        r, g, b = pixel[x, y]
        pixel[x, y] = g, b, r

image.save('images/python2.jpg')
# image.show()
