Урок 1.


Вывести таблицу умножения в виде. 
1 x 1 = 1
1 x 2 = 2
..
1 x 10 = 10
— 
2 x 1 = 2
2 x 2 = 4
…
N x 10 = 10N

Параметр N задается с клавиатуры (или в виде аргумента скрипта, по желанию)
Между разделами вывести разделитель в виде 5 девисов 

Реализовать функцию print_directory_contents(path). Функция принимает имя директории и выводит ее содержимое, включая содержимое всех поддиректории (рекурсивно вызывая саму себя). Использовать os.walk нельзя, но можно использовать os.listdir и os.path.isfile

Разработать целочисленный генератор случайных чисел. В функцию передавать начальную и конечную границу диапазона генерации (выдавать значения из диапазона включая концы). Заполнить этими данными словарь. Ключи словаря должны создаваться по шаблону: “elem_<номер_элемента>”, а значене сгенеренное случайное число.  Вывести содержимое словаря. 
(Усложненный вариант по желанию*): Не использовать стандартный модуль python random.

Написать программу «Банковский депозит». 
Клиент банка делает депозит на определенный срок. 

В зависимости от суммы и срока вклада определяется процентная ставка: 
1000–10000 руб (6 месяцев — 5 % годовых, год — 6 % годовых, 2 и более года — 5 % годовых). 
10000–100000 руб (6 месяцев — 6 % годовых, год — 7 % годовых, 2 и более года – 6.5 % годовых). 
100000–1000000 руб (6 месяцев — 7 % годовых, год — 8 % годовых, 2 и более года — 7.5 % годовых). 

Проценты начисляются на депозит в конце каждого месяца.

Необходимо написать функцию, в которую будут передаваться параметры: сумма вклада и срок вклада (в месяцах), а на выходе возвращать сумму вклада на конец срока.

Усовершенствовать программу «Банковский депозит». Третьим аргументом в функцию должна передаваться фиксированная ежемесячная сумма пополнения вклада. Считаем, что клиент вносит средства в последний день каждого месяца, кроме первого и последнего. Если 3м аргументом передан 0, то вызов должен быть совпадать с задачей 4.

Урок 2


Создать два класса. Первый — родительский (ItemDiscount), должен содержать статическую информацию о товаре: название и цену. Второй — дочерний (ItemDiscountReport), должен содержать функцию (get_parent_data), отвечающую за отображение информации о товаре в одной строке вида (“{название товара} {цена товара}”). Создать экземпляры родительского класса и дочернего. Распечатать информацию о товаре.
Инкапсулировать оба параметра (название и цену) товара родительского класса. Убедиться, что при сохранении текущей логики работы программы будет сгенерирована ошибка выполнения. Усовершенствовать родительский класс таким образом, чтобы получить доступ к защищенным переменным. Результат выполнения заданий 1 и 2 должен быть идентичным. 
Реализовать возможность переустановки значения цены товара в родительском классе. Проверить, распечатать информацию о товаре.
Реализовать расчет цены товара со скидкой. Величина скидки должна передаваться в качестве аргумента в дочерний класс. Выполнить перегрузку методов конструктора дочернего класса (метод __init__, в который должна передаваться переменная — скидка), и перегрузку метода __str__ дочернего класса. В этом методе должна пересчитываться цена и возвращаться результат — цена товара со скидкой. Чтобы все работало корректно, не забудьте инициализировать дочерний и родительский классы (вторая и третья строка после объявления дочернего класса). 
Проверить на практике возможности полиморфизма. Необходимо разделить дочерний класс ItemDiscountReport на два класса. Инициализировать классы необязательно. Внутри каждого поместить функцию get_info, которая в первом классе будет отвечать за вывод названия товара, а вторая — его цены. Далее реализовать вызов каждой из функции get_info.


Урок 3


Написать программу, которая будет содержать функцию для получения имени файла из полного пути до него. При вызове функции в качестве аргумента должно передаваться путь и имя файла с расширением. В функции необходимо реализовать поиск имени файла (с расширением), а затем «выделение» имени файла (без расширения). Расширений может быть несколько (например testfile.tar.gz).
Написать программу, которая запрашивает у пользователя ввод числа. На введенное число она отвечает сообщением, целое оно или дробное. Если дробное — необходимо далее выполнить сравнение чисел до и после запятой. Если они совпадают, программа должна возвращать значение True, иначе False.
Создать два списка с различным количеством элементов. В первом должны быть записаны ключи, во втором — значения. Необходимо написать функцию, создающую из данных ключей и значений словарь. Если ключу не хватает значения, в словаре для него должно сохраняться значение None. Если есть  значения, которым не хватило ключей, их необходимо отбросить. 
Написать программу, в которой реализовать две функции. В первой должен создаваться простой текстовый файл. Если файл с таким именем уже существует, выводим соответствующее сообщение и завершаем работу. Необходимо открыть файл и создать два списка: с текстовой и числовой информацией. Для создания списков использовать генераторы. Применить к спискам функцию zip(). Результат выполнения этой функции должен должен быть обработан и записан в файл таким образом, чтобы каждая строка файла содержала текстовое и числовое значение (например example345). Вызвать вторую функцию. В нее должна передаваться ссылка на созданный файл. Во второй функции необходимо реализовать открытие файла и простой, построчный вывод содержимого. 
Расширить программу из п. 4:
Усовершенствовать первую функцию из предыдущего примера. Необходимо во втором списке часть строковых значений (выбирается случайно) заменить на значения типа 345example (в обратном порядке, число и строка). (То есть вы переделываете функцию записи в файл так, чтобы она иногда меняла запись на 345example)
Реализовать функцию поиска определенных подстрок в файле по следующим условиям: вывод первого вхождения, вывод всех вхождений.
Реализовать функцию замену всех найденных подстрок на новое значение и вывод измененных строк. (это ДВЕ ОТДЕЛЬНЫЕ функции которые ВЫВОДЯТ значения, не записывают и не модифицируют файлы)
