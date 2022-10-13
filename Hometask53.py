def rle_encode(data):
    enconding = ''
    prev_char = ''
    count = 1

    if not data:
        return ''

    for char in data:
        if char != prev_char: #если предыд и текущий символы не совпадают
            if prev_char:
                 # то добавляем посчитанное колв-во символов 
                # и сам символ в расшифровку
                enconding += str(count) + prev_char
            count = 1
            prev_char = char
        else: # увеличиваем счетчик если символы совпадают
            count += 1
    else: # завершение расшифровки
        enconding += str(count) + prev_char
        return enconding

def rle_decode(data):
    decode = ''
    count = ''
    for char in data:
        if char.isdigit(): #если символ число
            count += char # присоединяем его к счетчику
        else: # если символ не число то печатаем необходимое кол-во символов в расшифровку
            decode += char*int(count)
            count = ''
    return decode

if __name__ == '__main__':
    decoder_val = rle_decode('4W3A5S')
    print(decoder_val)
    with open("decode.txt", "r") as file:
        file.write('{decoder_val}')

    with open("encode.txt", "r") as file:
        readfile = file.read()
    encoder_val = rle_encode(readfile)
    print(encoder_val)
        
