number = int(input('Введите число:'))
count = 1
print ("Таблица умножения от числа:", number)
while count <= 10:
    number = number * 1 
    print (number, 'x', count, '=', number * count)
    count += 1
    