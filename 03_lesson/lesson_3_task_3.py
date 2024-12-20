from Address import Address
from Mailing import Mailing

to_address = Address(620000, "г. Екатеринбург", "ул. Ленина", 165, 18) 
from_address = Address(620800, "г. Москва", "ул. Свердлова", 22, 45)
mailing = Mailing(to_address, from_address, 1200, 1234567890)
print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.town},"      f" {mailing.from_address.street}, {mailing.from_address.home} - {mailing.from_address.kvartira} "
      f"в {mailing.to_address.index}, {mailing.to_address.town}, {mailing.to_address.street}, "      f"{mailing.to_address.home} - {mailing.to_address.kvartira}. Стоимость {mailing.cost} рублей.")