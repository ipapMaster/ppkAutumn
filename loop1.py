# Циклы (DRY - Don't repeat Yourself)
import turtle

count = 0
sides = 8

while count < sides:
    turtle.forward(100)
    turtle.right(360 / sides)
    count += 1  # инкремент счётчика

turtle.mainloop()
