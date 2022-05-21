def get_percent(amount,months):
    if months not in [6, 12, 24]:
        return False
    
    rates = (
        {'begin_sum': 1000, 'end_sum': 10000, 6: 5, 12: 6, 24: 5},
        {'begin_sum': 10000, 'end_sum': 100000, 6: 6, 12: 7, 24: 6.5},
        {'begin_sum': 100000, 'end_sum': 1000000, 6: 7, 12: 8, 24: 7.5},
    )

    for rate in rates:
        if rate['begin_sum'] <= amount < rate['end_sum']:
            return rate[months]

    return False

def deposit(amount, months, charge =0):
    percent = get_percent(amount, months)
    if not percent:
       print('Нет подходящего тарифа')

    total = amount
    for month in range(months):
        profit = total * percent / 100 / 12
        total += profit
        if month !=0 and month != month -1:
            total += charge + charge * percent / 100 / 12

    print (f'Проценты на срок ', months, 'мес.:', round(total, 2))

deposit(amount = int(input('Введите сумму:')), months = int(input('Введите колличество месяцев:')), charge = int(input('Введите фиксированную сумму пополнения:')))
