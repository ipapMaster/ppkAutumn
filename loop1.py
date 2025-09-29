# Циклы (DRY - Don't repeat Yourself)
# for count in range(s, s, s)
# s - start (0 - по умолчанию)
# s - stop (не включая)
# s - step (1 - по умолчанию)
# for i in range(10) -> ... in range(0, 10, 1)
import turtle

count = 0  # Число фигур
sides = 0
N = 10
M = 5

turtle.speed(0)  # мгновенная скорость

# переносим "черепаху" на 50 вверх и на 30 влево
turtle.penup()
turtle.goto(-30, 50)
turtle.pendown()

while count < N:  # 8
    while sides < M:  # 4
        turtle.forward(100)
        turtle.right(360 / M)
        sides += 1
    turtle.right(360 / N)
    count += 1
    sides = 0

turtle.mainloop()
