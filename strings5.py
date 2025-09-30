# F-строка

name = 'Дмитрий'
surname = 'Дмитриев'

my_slice = name[:3]
# string = f'Привет, {name} {surname}!'

print(f'Привет, {name} {surname}!')
# print(dir(''))
# print(help(''.find))
print(name.index('тр'))

if 'тр' in name:
    print(f'Вхождение "тр" есть в строке "{name}"')  # Вхождение "тр" есть в строке "Дмитрий"

"""
'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 
'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 
'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 
'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 
'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 
'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 
'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 
'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 
'upper', 'zfill']
"""
