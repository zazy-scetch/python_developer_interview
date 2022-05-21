import random

s = int(input('Введите начальное число:'))
n = int(input('Введите начальное число:'))

def random_generator(s,n) -> ([],{}):
    if s == 0:
        print('Использовать 0 нельзя, значение изменено на 1.')
        s = 1
    rand_list = []
    count = 1
    while count <= n:
        random_el = random.randrange(s, n)
        rand_list.append(random_el)
        count += 1

    rand_dict = {}
    for i in rand_list:
        rand_dict[f'elem_{i}'] = i

    return rand_list, rand_dict

rand_gen = random_generator(s,n)

print('Список случайных чисел:', rand_gen[0], '\nСловарь случайных чисел:', rand_gen[1])
