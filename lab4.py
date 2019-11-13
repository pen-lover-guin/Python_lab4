# 25.1
from random import choice
from string import ascii_letters, digits


symbols = 'ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz23456789'


def generate_password(m):
    password = ''
    while len(password) < m:
        flag = choice([1, 2])
        if flag == 1:
            symbol = choice(ascii_letters)
        else:
            symbol = choice(digits)
        if symbol in symbols and symbol not in password:
            password += symbol
    return password


def main(n, m):
    passwords = []
    for i in range(n):
        passwords.append(generate_password(m))
    return passwords


# print('Случайный пароль из 7 символов:', generate_password(7))
# print('10 случайных паролей длиной 15 символов:')
# print(*main(10, 15), sep='\n')


# 25.2
from random import choice
from string import digits, ascii_lowercase, ascii_uppercase


symbols = 'ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz23456789'


def generate_password(m):
    password = ''
    while len(password) < m:
        flag = choice([1, 2, 3])
        if flag == 1:
            symbol = choice(digits)
        elif flag == 2:
            symbol = choice(ascii_lowercase)
        else:
            symbol = choice(ascii_uppercase)
        if symbol in symbols and symbol not in password:
            password += symbol
    return password


def main(n, m):
    passwords = []
    for i in range(n):
        passwords.append(generate_password(m))
    return passwords


# print('Случайный пароль из 7 символов:', generate_password(7))
# print('10 случайных паролей длиной 15 символов:')
# print(*main(10, 15), sep='\n')


# 26.1
from PIL import Image


def gradient(color):
    new_image = Image.new('RGB', (512, 200), (0, 0, 0))
    pixels = new_image.load()
    r, g, b = 0, 0, 0
    if color == 'R':
        for i in range(512):
            r += 1
            for j in range(200):
                pixels[i, j] = r, g, b
    new_image.save('res.png', 'PNG')


# gradient('R')


# 26.2
from PIL import ImageDraw, Image


def board(num, size):
    new_image = Image.new('RGB', (num * size, num * size), (255, 255, 255))
    draw = ImageDraw.Draw(new_image)
    for i in range(num):
        for j in range(num):
            if (i + j) % 2 == 0:
                draw.rectangle((i * size, j * size, i * size + size - 1, j * size + size - 1), fill='black')
    new_image.save('res.png', 'PNG')


board(8, 50)


# 27.1
from PIL import Image


def make_preview(size1, size2, n_colors):
    image = Image.open('uPvow.jpg')
    new_image = image.resize((size1, size2), Image.NEAREST)
    new_image.quantize(colors=n_colors)
    new_image.save('new.bmp', 'BMP')


make_preview(600, 600, 64)

# 27.2
from PIL import Image


def image_filter(pixels, n, m, value):
    """Увеличение яркости"""
    for x in range(n):
        for y in range(m):
            r = pixels[0] + value
            g = pixels[1] + value
            b = pixels[2] + value
            return r, g, b


# image = Image.open('s1200.jpg')
# x1, y1 = image.size
# res1 = Image.new('RGB', (x1, y1), (0, 0, 0))
# pixels1 = image.load()
# pixels2 = res1.load()
# for i in range(x1):
#     for j in range(y1):
#         pixels2[i, j] = image_filter(pixels1[i, j], x1, y1, 50)
# res1.save('res_filter.png', 'PNG')
