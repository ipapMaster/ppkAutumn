# Пользователь 12 раз вводит числа - температуру воздуха
# Подсчитать количество "прохладных" (менее 10),
# 		                "нормальных" (от 10 до 21)
#                        и "жарких" (остальных) значений
hot_counter = 0
norm_counter = 0
cold_counter = 0
for i in range(12):
    temp_air = int(input('введите температуру воздуха '))
    if temp_air < -273:
        print('ERROR')
        break          #не о чем больше с таким пользователем разговаривать, прекращаем цикл

    if temp_air < 10:
        cold_counter += 1
    elif 10 <= temp_air <= 21:
        norm_counter += 1
    else:
        hot_counter += 1
print(f'холодных: {cold_counter}, нормальных: {norm_counter}, жарких: {hot_counter}')