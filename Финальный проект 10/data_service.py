
def get_order():
    """ Повертає вміст файла "orders.txt" у вигляді списка
    Returns:
        order_list - список рядків файла
    """

    with open('./data/orders.txt', encoding="utf8") as order_file:
        order_list = order_file.readlines()

    # Накопичувач замовлень
    order_drive = []

    for line in order_list:
        line_list = line.split(';')
        line_list[3] = line_list[3][:-1]  # Видаляє '\n' в кінці
        order_drive.append(line_list)


    return order_drive


def show_orders(orders):
    """ Виводить список замовлень

    Args:
        orders (list): список замовлень
    """

    # Задати інтервал виводу
    order_code_from = input("З якого кода товару виводити? ")
    order_code_to = input("По який код товару виводити? ")

    # Накопичує кількість виведених рядків
    kol_lines = 0


    for order in orders:
        if order_code_from <= order[0] <= order_code_to:
            print("Код: {:4}  Клієнт: {:7} Номер заказу: {:5}  Кількість: {:4}".format(order[0], order[1], order[2], order[3]))
            kol_lines += 1

    # Перевірити чи був вивід хочаб одного рядка
    if kol_lines == 0:
        print("По Вашому запиту руху засобів нічого не знайдено.")


# orders = get_order()
# show_orders(orders)



def get_dovidnik():
    """ Повертає вміст файла "dovidniks.txt" у вигляді списка

    Returns:
        dovidnik_list - список рядків файла
    """

    with open('./data/dovidniks.txt', encoding="utf8") as dovidnik_file:
        dovidnik_list = dovidnik_file.readlines()

    # Накопичувач довідника основних засобів
    dovidnik_drive = []

    for line in dovidnik_list:
        line_list = line.split(';')
        line_list[2] = line_list[2][:-1]  # Видаляє '\n' в кінці
        dovidnik_drive.append(line_list)


    return dovidnik_drive


def show_dovidniks(dovidniks):
    """ Виводить список довідника

    Args:
        dovidniks (list): список довідника
    """

    # Задати інтервал виводу
    dovidnik_code_from = input("З якого кода довідника виводити? ")
    dovidnik_code_to = input("По який код довідника виводити? ")

    # Накопичує кількість виведених рядків
    kol_lines = 0


    for dovidnik in dovidniks:
        if dovidnik_code_from <= dovidnik[0] <= dovidnik_code_to:
            print("Код: {:4} Найменування: {:53} Ціна: {:6}".format(dovidnik[0], dovidnik[1], dovidnik[2]))
            kol_lines += 1

    # Перевірити чи був вивід хочаб одного рядка
    if kol_lines == 0:
        print("По Вашому запиту довідникіка нічого не знайдено.")


# dovidniks = get_dovidnik()
# show_dovidniks(dovidniks)