def division(x, y):
    try:
        x / y
    except ZeroDivisionError:
        print("Нельзя делить на ноль!")
        return
    return print(x / y)


a = float(input("Введите первое число (что делим?): "))
b = float(input("Ввежите второе число (на что делим?): "))
division(a, b)
