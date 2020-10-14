def my_func1(**kwargs):
    a = kwargs.get("first")**kwargs.get("second")
    return a


def my_func2(**kwargs):
    b = kwargs.get("first")
    i = 1
    while i < abs(kwargs.get("second")):
        b = b*kwargs.get("first")
        i += 1
    a = 1/b
    return a


x = float(input("Введите первое число (что возводим?): "))
y = int(input("Введите отрицательную степень: "))
if y < 0:
    print(f"Функция через оператор '**': {my_func1(first=x, second=y)}")
    print(f"Функция через цикл: {my_func2(first=x, second=y)}")
else:
    print("Степень должна быть отрицатеотная!")
