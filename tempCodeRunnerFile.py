while (True):
    year = int(input('Введите год: '))
    day = 0
    max_month = 0
    while day <31:
        day += 1
        mass = [int(a) for a in str(day)]
        if (mass==[3,0]):
            month = sum(mass)
            month = max_month + month
        if (mass==[2,9]):
            feb = sum(mass)
            ves_feb = sum(mass)
            feb = max_month + feb
        max_month = sum(mass) + max_month
    if ((year % 4) > 0):
        print("Сумма месяцев = " , max_month*7+month*4+feb-ves_feb)
    elif((year % 4) == 0):
        print("Сумма месяцев = " , max_month*7+month*4+feb)