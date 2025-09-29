# Методы строк
# string = input().strip().lower() - цепочка вызовов
string = 'язЫк pyThon'

print(string.lower())  # все буквы маленькие
print(string.upper())  # все буквы большие
print(string.title())  # все слова с большой
print(string.capitalize())  # только первая буква большая
print(string.strip('я'))  # убрать символы в начале и в конце
# rstrip, lstrip