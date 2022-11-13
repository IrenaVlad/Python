import telebot
import config

from telebot import types

bot = telebot.TeleBot("5715310006:AAEXW2SNalz3lS2AZfRmE-dpstuLnH9YiiA")

cell = [' ' for x in range (0,28)]
xorz = 'X'
user_id = ''
sum_candy = 0
def board(cell):
    xorz_board = telebot.types.InlineKeyboardMarkup()
    xorz_board.row( telebot.types.InlineKeyboardButton(f'{cell[0]}', callback_data='0'),
                    telebot.types.InlineKeyboardButton(f'{cell[0]}', callback_data='1'),
                    telebot.types.InlineKeyboardButton(f'{cell[0]}', callback_data='2'),
                    telebot.types.InlineKeyboardButton(f'{cell[0]}', callback_data='3'),
                    telebot.types.InlineKeyboardButton(f'{cell[0]}', callback_data='4'),
                    telebot.types.InlineKeyboardButton(f'{cell[0]}', callback_data='5'),
                    telebot.types.InlineKeyboardButton(f'{cell[0]}', callback_data='6'))

    xorz_board.row( telebot.types.InlineKeyboardButton(f'{cell[0]}', callback_data='7'),
                    telebot.types.InlineKeyboardButton(f'{cell[0]}', callback_data='8'),
                    telebot.types.InlineKeyboardButton(f'{cell[0]}', callback_data='9'),
                    telebot.types.InlineKeyboardButton(f'{cell[0]}', callback_data='10'),
                    telebot.types.InlineKeyboardButton(f'{cell[0]}', callback_data='11'),
                    telebot.types.InlineKeyboardButton(f'{cell[0]}', callback_data='12'),
                    telebot.types.InlineKeyboardButton(f'{cell[0]}', callback_data='13'))

    xorz_board.row( telebot.types.InlineKeyboardButton(f'{cell[0]}', callback_data='14'),
                    telebot.types.InlineKeyboardButton(f'{cell[0]}', callback_data='15'),
                    telebot.types.InlineKeyboardButton(f'{cell[0]}', callback_data='16'),
                    telebot.types.InlineKeyboardButton(f'{cell[0]}', callback_data='17'),
                    telebot.types.InlineKeyboardButton(f'{cell[0]}', callback_data='18'),
                    telebot.types.InlineKeyboardButton(f'{cell[0]}', callback_data='19'),
                    telebot.types.InlineKeyboardButton(f'{cell[0]}', callback_data='20')) 

    xorz_board.row( telebot.types.InlineKeyboardButton(f'{cell[0]}', callback_data='21'),
                    telebot.types.InlineKeyboardButton(f'{cell[0]}', callback_data='22'),
                    telebot.types.InlineKeyboardButton(f'{cell[0]}', callback_data='23'),
                    telebot.types.InlineKeyboardButton(f'{cell[0]}', callback_data='24'),
                    telebot.types.InlineKeyboardButton(f'{cell[0]}', callback_data='25'),
                    telebot.types.InlineKeyboardButton(f'{cell[0]}', callback_data='26'),
                    telebot.types.InlineKeyboardButton(f'{cell[0]}', callback_data='27'))


@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('picture/welcome.webp','rb')
    bot.send_sticker(message.chat_id, sti)
    markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
    item1= types.KeyboardButton("Игра в конфеты")
    markup.add(item1)
    bot.send_message(message.chat_id, "Привет, {0.first_name}!\nЯ - бот для игры с конфетами!", parse_mode='html', reply_markup= markup)
@bot.message_handler(content_types=['text'])
def menu_homework(message):
    global cell, xorz
    cell = [x for x in range (1, 29)]
    if message.text == 'Игра в конфеты':
        bot.send_message(message.chat_id, f'Выберите количество конфет {xorz}', reply_markup=board(cell))
    else:
        bot.send_message(message.chat_id, f'Не знаю что ответить')

@bot.callback_query_handler(func=lambda call: True)
def callback_func(query):
    global cell, xorz, user_id, sum_candy
    data = query.data
    data = int(data) +1
    
    if sum_candy != 100:
        user_id = query.from_iser.id
        sum_candy = sum_candy + data
        if sum_candy != 100:
            bot.edit_message_text(chat_id= query.message.chat.id, message_id=query.message.message.id, text =f'Сумма конфет {sum_candy}', reply_markup=board(cell))
        elif sum_candy == 100:
            bot.edit_message_text(chat_id= query.message.chat.id, message_id=query.message.message.id, text =f'Сумма конфет {sum_candy} , выиграл {user_id}')
        elif sum_candy == 2021:
            bot.edit_message_text(chat_id= query.message.chat.id, message_id=query.message.message.id, text =f'Сумма конфет {sum_candy}')
bot.polling(none_stop= True)
