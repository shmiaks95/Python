from address import Address
from mailing import Mailing


to_address = Address("443000", "Самара", "ул. Пушкина", 10, 7)
from_address = Address("101000", "Москва", "ул. Тверская", 1, 25)

mailing = Mailing(to_address, from_address, 1500, "TRK123456")

print(
    f"Отправление {mailing.track} "
    f"из {mailing.from_address.index}, {mailing.from_address.city}, "
    f"{mailing.from_address.street}, {mailing.from_address.home} - "
    f"{mailing.from_address.flat} "
    f"в {mailing.to_address.index}, {mailing.to_address.city}, "
    f"{mailing.to_address.street}, {mailing.to_address.home} - "
    f"{mailing.to_address.flat}. "
    f"Стоимость {mailing.cost} рублей."
)
