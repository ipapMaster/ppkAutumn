# Рекурсия и фракталы
# Фибоначчи: 0 1 1 2 3 5 8 13 21 34
import turtle as t


def draw_tree(branch_len, t):
    if branch_len > 5:  # Базовый случай рекурсии
        t.forward(branch_len)  # Рисуем ветку
        t.right(20)  # Поворачиваем направо
        draw_tree(branch_len - 15, t)  # Рисуем правую ветвь
        t.left(40)  # Поворачиваем налево
        draw_tree(branch_len - 15, t)  # Рисуем левую ветвь
        t.right(20)  # Возвращаемся в исходное положение
        t.backward(branch_len)  # Возвращаемся к началу ветки


def main():
    t.speed(0)
    t.left(90)  # Начальный поворот вверх
    t.up()  # Поднимаем перо
    t.backward(100)  # Сдвигаем начальную точку
    t.down()  # Опускаем перо
    t.color("green")  # Цвет ветвей
    draw_tree(75, t)  # Рисуем дерево


main()

t.mainloop()

# def factorial(n):  # процедурный способ
#     result = 1
#     for i in range(2, n + 1):
#         result *= i
#     return result


# def factorial_r(n):
#     if n == 0:  # базовое условие - выход из рекурсии (если нет, то stack overflow)
#         return 1
#     else:
#         return n * factorial_r(n - 1)
#
#
# print(factorial_r(4))
