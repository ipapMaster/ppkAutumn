n = int(input('введите количество дней '))

left = 'G'
central = 'C'
right = 'V'

for i in range(n):
    #действие Маши
    right, central = central, right
    #действие Тани
    left, central  = central, left

print(left + central + right)