<<<<<<< HEAD
num = int(input('Введите число в десятичной системе: '))
print(f'Встроенная функция hex -> \t\t{hex(num)}')


def self_hex(number: int) -> str:
    if not number:
        return '0x0'
    result = ''
    hex_letters = list('0123456789abcdef')
    while number > 0:
        result = hex_letters[number % 16] + result
        number //= 16
    return '0x' + result


print(f'Собственная функция self_hex -> {self_hex(num)}')
=======
num = int(input('Введите число в десятичной системе: '))
print(f'Встроенная функция hex -> \t\t{hex(num)}')


def self_hex(number: int) -> str:
    if not number:
        return '0x0'
    result = ''
    hex_letters = list('0123456789abcdef')
    while number > 0:
        result = hex_letters[number % 16] + result
        number //= 16
    return '0x' + result


print(f'Собственная функция self_hex -> {self_hex(num)}')
>>>>>>> fc537d79d299dbbdd4d3e3de39a9bb001f4bfefc
