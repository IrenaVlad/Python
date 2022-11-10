from aiogram import Bot, Dispatcher, executor, types
API_TOKEN = '5575898556:AAF8WhWHf1Cm7oargXXftJaD262kYlH2vWE'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

a = 0
b = 0
c = 0
d = 0
op = ''

@dp.message_handler(commands=['/start'])
async def send_welcome(message: types.Message):
    await message.replay("Привет. Для вычислений операций с комплексными числами команда /calc")

@dp.message_handler(commands=['/calc'])
async def send_welcome(message: types.Message):
    await message.reply("Введите первое число")
    dp.register_next_step_handler(message, type_a)

async def type_a(message):
    global a
    a = message.text
    try:
        a = int(a)
        dp.reply_to(message, "Введите второе число: ")
        dp.register_next_step_handler(message, type_b)
    except Exception:
        msg = bot.reply_to(message, 'Нужно ввести число!')
        dp.register_next_step_handler(message, type_a)

def type_b(message):
    global b
    b = message.text
    try:
        b = int(b)
        bot.reply_to(message, "Введите третье число: ")
        bot.register_next_step_handler(message, type_c)
    except Exception:
        msg = bot.reply_to(message, 'Нужно ввести число!')
        bot.register_next_step_handler(message, type_b)

def type_c(message):
    global c
    c = message.text
    try:
        c = int(c)
        bot.reply_to(message, "Введите четвертое число: ")
        bot.register_next_step_handler(message, type_d)
    except Exception:
        msg = bot.reply_to(message, 'Нужно ввести число!')
        bot.register_next_step_handler(message, type_c)

def type_d(message):
    global d
    d = message.text
    try:
        d = int(d)
        bot.reply_to(message, "Введите необходимую операцию +-/*': ")
        bot.register_next_step_handler(message, type_op)
    except Exception:
        msg = bot.reply_to(message, 'Нужно ввести число!')
        bot.register_next_step_handler(message, type_d)

def type_op(message):
    global op
    op = message.text
    msg_text_res = complex_calc.calc(complex(a,b),complex(c,d),op)
    bot.send_message(message.from_user.id, msg_text_res)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True) 