def my_func(*args):
    a = list()
    for i in args[0]:
        a.append(int(i))
    a = sum(a)
    return a


result = int()
print("Для завершения программы введите - 'q")
while True:
    user_input = list(input("Введите числа: ").split())
    if user_input.count("q") > 0:
        user_input.remove("q")
        if len(user_input) == 0:
            break
        else:
            result += my_func(user_input)
            print(result)
            break
    else:
        result += my_func(user_input)
        print(result)
        continue
