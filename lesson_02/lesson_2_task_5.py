def month_to_season(n):
    if 0 < n < 3 or n > 11:
        print("Зима")
    elif 2 < n < 6:
        print("Весна")
    elif 5 < n < 9:
        print("Лето")
    elif 8 < n < 12:
        print("Осень")
    else:
        print("Неверный месяц")


n = 11
month_to_season(n)
