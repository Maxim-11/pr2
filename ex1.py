print("Введите количество повторений: ")
rep = int(input())
print("Введите первое число: ")
num1 = float(input())
i = 0
while i < rep:
    print("Введите второе число: ")
    num2 = float(input())
    print("Введите операцию: ")
    oper = (input())
    if (oper == '+'):
        num1 = num1 + num2
        i+=1
        print(f"Ответ: {num1}")
    elif (oper == "-"):
        num1 = num1 - num2
        i+=1
        print(f"Ответ: {num1}")
    elif (oper == "*"):
        num1 = num1 * num2
        i+=1
        print(f"Ответ: {num1}")
    elif (oper == "/" and num2!=0):
        num1 = num1 / num2
        i+=1
        print(f"Ответ: {num1}")
    else:
        print("Ошибка!")
else:
    print("Работа программы завершена")
    
    
