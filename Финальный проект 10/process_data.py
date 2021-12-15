""" Заявки на продаж
"""

# Підключити функції з модуля 'data_service'
from data_service import get_order, get_dovidnik

# Структура заявок на продаж вихідних даних
zajavka = {
    'tovar_name'        : '',    # Назва товару 
    'number_order'      : 0,     # Номер заказа
    'code_client'       : '',    # Код клієнта
    'number'            : 0,     # Кількість
    'price'             : 0.0,     # Ціна
    'sum'               : 0.0,     # Сума
}


orders = get_order()
dovidniks = get_dovidnik()

def zajavka_sell():
    """ Формування заявок на продаж
    """

    def get_dovidnik_name(dovidnik_code):
        """ Повертає назву засоба по його коду

        Args:
            dovidnik_name ([type]): код засоба

        Returns:
            [type]: назва засобу
        """

        for dovidnik in dovidniks:
            if dovidnik[0] == dovidnik_code:
                return dovidnik[1]

        return "*** Код засобу не знайдений"

    def get_dovidnik_price(dovidnik_price):
        """ Повертає назву засоба по його коду

        Args:
            dovidnik_price ([type]): код засоба

        Returns:
            [type]: назва засобу
        """

        for dovidnik in dovidniks:
            if dovidnik[0] == dovidnik_price:
                return dovidnik[2]

        return "*** Код засобу не знайдений"



    # Накопичувач заявок на продаж
    zajavka_list = []

    for order in orders:

        # Створити копію шаблона
        zajavka_tmp = zajavka.copy()

        zajavka_tmp['tovar_name'] = get_dovidnik_name(order[0])
        zajavka_tmp['number_order'] = order[1]
        zajavka_tmp['code_client'] = order[0]
        zajavka_tmp['number'] = order[3]
        zajavka_tmp['price'] = get_dovidnik_price(order[0])
        zajavka_tmp['sum'] = float(zajavka_tmp['number']) * float(zajavka_tmp['price'])

        zajavka_list.append(zajavka_tmp)

    return zajavka_list

result = zajavka_sell()

for r in result:
    print(r)