# Дополнительно устанавливаемые модули
# Модуль графики PIL (Python Imaging Library - pillow)
# PIP - Python Installation Package
# pip install pillow
# Создание и рисование: Draw из ImageDraw
from PIL import Image, ImageDraw

# создали холст
new_image = Image.new('RGB', (600, 400), (255, 255, 255))

# создаём объект для рисования и указываем на чём рисовать
draw = ImageDraw.Draw(new_image)

# Рисуем два прямоугольника
draw.rectangle((0, 0, 599, 132), (245, 245, 245))
draw.rectangle((0, 133, 599, 266), (0, 0, 255))
draw.rectangle((0, 267, 599, 400), (255, 0, 0))

# Рисуем прямоугольник по контуру толщиной 3 пикселя
# draw.rectangle((0, 0, 599, 399), outline=(0, 0, 255), width=3)
# рисуем линию, разделяющую холст пополам
# draw.line((299, 0, 299, 399), fill=(0, 0, 255), width=3)
# рисуем две диагонали
# draw.line((0, 0, 599, 399), fill=(0, 0, 255), width=3)
# draw.line((599, 0, 0, 399), fill=(0, 0, 255), width=3)

new_image.save('images/flag.jpg')

# оригинальное изображение
# image = Image.open('images/python.jpg')
#
# # создание холста
# new_image = Image.new('RGB', (600, 400), (255, 0, 0))
#
# # cropped = image.crop(
# #     (175, 80, 380, 205)
# # )
# new_size = image.resize((150, 100))
#
# new_image.paste(new_size, (180, 120))
# draw = ImageDraw.Draw(new_image)
# draw.rectangle((180, 120, 330, 220), outline=(0, 0, 255),
#                width=5)
# new_image.save('images/canvas.jpg')
