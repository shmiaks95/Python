from smartphone import Smartphone
catalog = [
    Smartphone("iPhone", "13", "+7 963 125 65 22"),
    Smartphone("Samsung", "Galaxy Note", "+7 919 543 86 55"),
    Smartphone("iPhone", "16 Pro", "+7 917 533 26 00"),
    Smartphone("Xiaomi", "17 Ultra", "+7 920 745 00 14"),
    Smartphone("OPPO", "Find X10", "+7 927 754 18 75")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.number}.")
