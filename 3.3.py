def my_func(a, b, c):
    x = [a, b, c]
    x.remove(min(x))
    return sum(x)


user_input = list(input("Введите 3 числа через пробел: ").split())
new_list = list()
for i in user_input:
    new_list.append(int(i))
print(my_func(new_list[0], new_list[1], new_list[2]))
