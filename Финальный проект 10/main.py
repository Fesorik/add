""" Головний модуль задачі
- Виводить розрахункову табліцю на екран та в файл
- Виводить первинні данні на екран
"""

import os
from process_data import zajavka_sell
from data_service import show_dovidniks, show_orders, get_dovidnik, get_order

MAIN_MENU = \
""" 
~~~~~~~~   ОБРОБКА ЗАЯВОК НА ПРОДАЖ МЕТОДИЧНОЇ ЛІТЕРАТУРИ   ~~~~~~~~

1 - Вивід таблиці заявок на продаж на екран
2 - Запис таблиці заявок на продаж в файл
3 - Вивід списка замовлень на літературу
4 - Вивід списка довідника товарів
0 - Завершення роботи

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

TITLE = "ЗАЯВКИ НА ПРОДАЖ МЕТОДИЧНОЇ ЛІТЕРАТУРИ ТА ПРОГРАМНИХ ЗАСОБІВ ПО МАГАЗИНУ"

HEADER = \
"""
===============================================================================================================
Найменування товара                                  | Номер заказа | Код клієнта | Кількість | Ціна |  Сума   
===============================================================================================================
"""

FOOTER =  \
'''
===============================================================================================================

'''

STOP_MESSAGE = 'Для продовження натисніть <Enter> '

def show_zajavka(zajavka_list):
    """ Виводить таблицю заявок на продаж

    Args:
        zajavka_list ([type]): Список засобів
    """
    print(f"\n\n{TITLE:^108}")
    print(HEADER)

    for zajavka in zajavka_list:
        print(f"{zajavka['tovar_name']:53}",
              f"{zajavka['number_order']:^14}",
              f"{zajavka['code_client']:^13}",
              f"{zajavka['number']:^11}",
              f"{zajavka['price']:^7}",
              f"{zajavka['sum']:^9}")

    print(FOOTER)


def write_zajavka(zajavka_list):
    """ Записує список заявок у текстовий файл

    Args:
        zajavka_list ([type]): список заявок
    """

    with open('./data/zajavka.txt', 'w') as zajavka_file:
        for zajavka in zajavka_list:
            line = \
               zajavka['tovar_name'] + ';' +                    \
               str(zajavka['number_order']) + ';' +             \
               str(zajavka['code_client']) + ';' +              \
               str(zajavka['number']) + ';' +                   \
               str(zajavka['price']) + ';' +                    \
               str(zajavka['sum'])  + '\n' 
               
            zajavka_file.write(line)  
            
    print('Файл успішно записано...')     

while True:

    # Виводить головне меню
    os.system('cls')
    print(MAIN_MENU)
    command_number = input("Введіть номер команди: ")

    # Обробка команд користувача
    if command_number == '0':
        print('Програма завершила роботу')
        exit(0)

    elif command_number == '1':
        zajavka_list = zajavka_sell()
        show_zajavka(zajavka_list)
        input(STOP_MESSAGE)

    elif command_number == '2':
        zajavka_list = zajavka_sell()
        write_zajavka(zajavka_list)
        input(STOP_MESSAGE)
        
    elif command_number == '3':
        orders = get_order()
        show_orders(orders)
        input(STOP_MESSAGE)
        
    elif command_number == '4':
        dovidniks = get_dovidnik()
        show_dovidniks(dovidniks)
        input(STOP_MESSAGE)