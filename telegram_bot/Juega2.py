from aiogram import Bot, Dispatcher, executor, types
API_TOKEN = ''
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
@dp.message_handler(commands=['start'])

jugador1 = 0
jugador2 = 0
def juega(jugador1, jugador2):
    cantidad = int(input('Введите количество конфет: '))
    jugador1_toma = int(input('Сколько конфет берет первый игрок?'))
    while jugador1_toma > 27:
        print('Введено неверное количество конфет')
        jugador1_toma = int(input('Сколько конфет берет первый игрок?'))
    while jugador1_toma > cantidad:
        print('В стопке недостаночно конфет')
        jugador1_toma = int(input('Сколько конфет берет первый игрок?'))
    else:
        jugador1 += jugador1_toma
        cantidad -= jugador1_toma
        print(f'У первого игрока {jugador1} конфет')    
        print(f'В стопке осталось конфет :{cantidad}')
        if cantidad == 0:
            print('Первый игрок победил! Игра окончена!')
            return
    jugador2_toma = int(input('Сколько конфет берет второй игрок?'))
    while jugador2_toma > 28:
        print('Введено неверное количество конфет')
        jugador2_toma = int(input('Сколько конфет берет второй игрок?'))
    while jugador2_toma > cantidad:
        print('В стопке недостаночно конфет')
        jugador2_toma = int(input('Сколько конфет берет второй игрок?'))
    else:
        jugador2 += jugador2_toma
        cantidad -= jugador2_toma
        print(f'У второго игрока {jugador2} конфет')    
        print(f'В стопке осталось конфет :{cantidad}')
        if cantidad == 0:
            print('Второй игрок победил! Игра окончена!')
            return

juega(0, 0)