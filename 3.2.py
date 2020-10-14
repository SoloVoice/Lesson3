def user_info(a, b, c, d, e, f):
    print(f"Имя: {a}, Фамилия: {b}, Дата рождения: {c}, Город: {d}, Почта: {e}, Телефон: {f}")


name = input("Введите имя: ")
surname = input("Введите фамилию: ")
birth = input("Введите дату рождения: ")
city = input("Город проживания: ")
email = input("Адрес электронной почты: ")
phone = input("Номер телефона: ")
user_info(f=phone, e=email, d=city, c=birth, b=surname, a=name)
