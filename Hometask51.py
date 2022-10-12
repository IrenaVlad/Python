jugador1 = 0
jugador2 = 0
def juega(jugador1, jugador2):
    cantidad = int(input('Введите количество конфет: '))
    jugador1_toma = int(input('Сколько конфет берет первый игрок?'))
    while 0 <= jugador1_toma > 28:
        print('Введено неверное количество конфет')
        jugador1_toma = int(input('Сколько конфет берет первый игрок?'))
    while jugador1_toma > cantidad:
        print('В стопке недостаночно конфет')
        jugador1_toma = int(input('Сколько конфет берет первый игрок?'))
    else:
        jugador1 = jugador1 + jugador1_toma
        cantidad = cantidad - jugador1_toma
        print(f'У первого игрока {jugador1} конфет')    
        print('В стопке осталось конфет :{cantidad}')
        if cantidad == 0:
            print('Первый игрок победил! n\ Игра окончена!')
            return
    jugador2_toma = int(input('Сколько конфет берет второй игрок?'))
    while 0 <= jugador2_toma > 28:
        print('Введено неверное количество конфет')
        jugador2_toma = int(input('Сколько конфет берет второй игрок?'))
    while jugador2_toma > cantidad:
        print('В стопке недостаночно конфет')
        jugador2_toma = int(input('Сколько конфет берет второй игрок?'))
    else:
        jugador2 = jugador2 + jugador2_toma
        cantidad = cantidad - jugador2_toma
        print(f'У второго игрока {jugador2} конфет')    
        print('В стопке осталось конфет :{cantidad}')
        if cantidad == 0:
            print('Второй игрок победил! n\ Игра окончена!')
            return

