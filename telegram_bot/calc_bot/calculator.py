def calculator(a,b,op):
    try:
        match op:
            case '+':
                msg_text = a + b
            case '-':
                msg_text = a - b
            case '/':
                msg_text = a / b
            case '*':
                msg_text = a * b
    except:
        msg_text = 'Ошибка ввода. Попробуйте еще раз)'

    return msg_text