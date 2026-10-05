from address import Address
from mailing import Mailing

from_add = Address('692337', 'Арсеньев', 'Калининская', '14', '2')
to_add = Address('694955', 'Владивосток', 'Ленинская', '15', '35')
mailing1 = Mailing(to_add, from_add, track='rt45656778', cost=565)

print(f"Отправление {mailing1.track} из {from_add} в {to_add}. Стоимость "
      f"{mailing1.cost} рублей.")