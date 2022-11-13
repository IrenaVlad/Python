import telebot
import calculator

bot = telebot.TeleBot("5575898556:AAF8WhWHf1Cm7oargXXftJaD262kYlH2vWE")

a = 0
b = 0
c = 0
d = 0
op = ''

@bot.message_handler(commands=['start','help'])
def send_welcome(message):
    text = 'Привет. Для вычислений операций с комплексными числами команда /calc'
    bot.reply_to(message, text)

@bot.message_handler(commands=['calc'])
def send_welcome(message):
    text = 'Введите первое число'
    bot.reply_to(message, text)
    bot.register_next_step_handler(message, type_a)

def type_a(message):
    global a
    a = message.text
    try:
        a = int(a)
        bot.reply_to(message, 'Введите второе число: ')
        bot.register_next_step_handler(message, type_b)
    except Exception:
        msg = bot.reply_to(message, 'Нужно ввести число!')
        bot.register_next_step_handler(message, type_a)

def type_b(message):
    global b
    b = message.text
    try:
        b = int(b)
        bot.reply_to(message, 'Введите третье число: ')
        bot.register_next_step_handler(message, type_c)
    except Exception:
        msg = bot.reply_to(message, 'Нужно ввести число!')
        bot.register_next_step_handler(message, type_b)

def type_c(message):
    global c
    c = message.text
    try:
        c = int(c)
        bot.reply_to(message, 'Введите четвертое число: ')
        bot.register_next_step_handler(message, type_d)
    except Exception:
        msg = bot.reply_to(message, 'Нужно ввести число!')
        bot.register_next_step_handler(message, type_c)

def type_d(message):
    global d
    d = message.text
    try:
        d = int(d)
        bot.reply_to(message, 'Введите необходимую операцию +-/*: ')
        bot.register_next_step_handler(message, type_op)
    except Exception:
        msg = bot.reply_to(message, 'Введите тип операции: +-/*!')
        bot.register_next_step_handler(message, type_d)

def type_op(message):
    global op
    op = message.text
    msg_text_res = calculator.calc(complex(a,b),complex(c,d),op)
    bot.send_message(message.from_user.id, msg_text_res)

bot.polling(non_stop=True)