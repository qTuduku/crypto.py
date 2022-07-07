from random import randint
# Самые часто используемые строки и переменные вынесены в отдельный блок
# переменных.
power_dict_eng, power_dict_ru = 26, 33
say_encryp, say_decryp = 'Зашифрованное сообщение на ', 'Расшифрованное сообщение нa '
say_eng, say_ru = 'Английском языке', 'Русском языке'
key_error = 'Неправильный формат ключа! (введена пустая строка или неправильный тип данных)\n'
input_error = 'Неверный параметр\n'
dict_eng = {x for x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'}
dict_ru = {
    x for x in 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'}

# Функции шифрования названы по шаблону <Оф.название шифра>_<Шифрование и/или Дешифрование>.
# Каждая функция укомплектована обрабатывать ошибки ввода пользователя и
# способна вызывать сама себя.


def vigenere_ENCRYP(m):
    k = input('Введите ключевое слово для шифрования (str): ')
    if k.isalpha():
        m, k = m.upper(), k.upper()
        slow = {
            x for x in 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯABCDEFGHIJKLMNOPQRSTUVWXYZ'}
        shift, power = 'A' if ru_eng else 'А', power_dict_eng if ru_eng else power_dict_ru
        # Реализуется квадрат виженера с помощью представления букв в числах
        # UNICODE.
        k *= len(m) // len(k) + 1
        c = ''.join([chr((ord(j) + ord(k[i])) % power + ord(shift))
                    if j in slow else j for i, j in enumerate(m)])
        return(
            f"{say_encryp}{say_eng if ru_eng else say_ru}: {c}\n")
    else:
        print(key_error)
        return vigenere_ENCRYP(m)


def vigenere_DECRYP(m):
    k = input(
        'Введите ключевое слово, которое использовалось для шифрования (str): ')
    if k.isalpha():
        m, k = m.upper(), k.upper()
        slow = {
            x for x in 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯABCDEFGHIJKLMNOPQRSTUVWXYZ'}
        shift, power = 'A' if ru_eng else 'Џ', power_dict_eng if ru_eng else power_dict_ru
        # Шифрование и Дешифрование есть перемещение по квадрату виженера в числовом виде
        # и отличается только знаком +/- в алгоритме.
        k *= len(m) // len(k) + 1
        c = ''.join([chr((ord(j) - ord(k[i])) % power + ord(shift))
                    if j in slow else j for i, j in enumerate(m)])
        return(
            f"{say_decryp}{say_eng if ru_eng else say_ru}: {c}\n")
    else:
        print(key_error)
        return vigenere_DECRYP(m)


def atbash_ENCRYP_DECRYP(m):
    # Шифр Атбаша не нуждается в ключе и реализуется с помощью словарей с зеркальными буквами
    # шифрование и дешифрование производит один и тот же алгоритм.
    dict_ENG = {'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v', 'f': 'u', 'g': 't', 'h': 's', 'i': 'r', 'j': 'q', 'k': 'p', 'l': 'o',
                'm': 'n', 'n': 'm', 'o': 'l', 'p': 'k', 'q': 'j', 'r': 'i', 's': 'h', 't': 'g', 'u': 'f', 'v': 'e', 'w': 'd', 'x': 'c',
                'y': 'b', 'z': 'a', ' ': ' ', ',': ',', '.': '.'}
    dict_RU = {'а': 'я', 'б': 'ю', 'в': 'э', 'г': 'ь', 'д': 'ы', 'е': 'ъ', 'ё': 'щ', 'ж': 'ш', 'з': 'ч', 'и': 'ц', 'й': 'х', 'к': 'ф',
               'л': 'у', 'м': 'т', 'н': 'с', 'о': 'р', 'п': 'п', 'р': 'о', 'с': 'н', 'т': 'м', 'у': 'л', 'ф': 'к', 'х': 'и', 'ц': 'и',
               'ч': 'з', 'ш': 'ж', 'щ': 'ё', 'ъ': 'е', 'ы': 'д', 'ь': 'г', 'э': 'в', 'ю': 'б', 'я': 'а', ' ': ' ', ',': ',', '.': '.', }
    m, c = m.lower(), ''
    if ru_eng:
        c = ''.join(
            [dict_ENG[word] if word in dict_ENG else word for word in m])
    else:
        c = ''.join([dict_RU[word] if word in dict_RU else word for word in m])
    return(
        f"Итоговое сообщение на {say_eng if ru_eng else say_ru}: {c}\n")


def caesar_ENCRYP(m):
    try:
        k = int(input('Введите значение смещения алфавита (int): '))
        dict_ENG = ' abcdefghijklmnopqrstuvwxyz,.'
        dict_RU = ' абвгдеёжзийклмнопрстуфхцчшщъыьэюя,.'
        dict_RU_ENG = dict_ENG if ru_eng else dict_RU
        # Шифр цезаря реализуется сдвигом индекса буквы по её словарю, шифрование и дешифрование
        # отличаются знаками +/-.
        m, c = m.lower(), ''.join(
            [dict_RU_ENG[(dict_RU_ENG.index(word) + k) % len(dict_RU_ENG)] if word in dict_RU_ENG else word for word in m])
        return(
            f"{say_encryp}{say_eng if ru_eng else say_ru}: {c}\n")
    except ValueError:
        print(key_error)
        return caesar_ENCRYP(m)


def caesar_DECRYP(m):
    try:
        k = int(
            input('Введите значение смещения, которым было закодировано соощение (int): '))
        dict_ENG = ' abcdefghijklmnopqrstuvwxyz,.'
        dict_RU = ' абвгдеёжзийклмнопрстуфхцчшщъыьэюя,.'
        dict_RU_ENG = dict_ENG if ru_eng else dict_RU
        m, c = m.lower(), ''.join(
            [dict_RU_ENG[(dict_RU_ENG.index(word) - k) % len(dict_RU_ENG)] if word in dict_RU_ENG else word for word in m])
        return(
            f"{say_decryp}{say_eng if ru_eng else say_ru}: {c}\n")
    except ValueError:
        print(key_error)
        return caesar_DECRYP(m)


def permutation_ENCRYP(m):
    try:
        k = int(
            input('Введите ключ шифрования (int), меньший чем длина сообщения: '))
        ciphertext = [''] * k
        # Перестановочный шифр использует заполнение матрицы исходными значениями, длина строки определяется ключом
        # шифрованное сообщение записывается по колоннам снизу вверх.
        for coloumn in range(k):
            currentIndex = coloumn
            while currentIndex < len(m):
                ciphertext[coloumn] += m[currentIndex]
                currentIndex += k
        return(
            f"{say_encryp}{say_eng if ru_eng else say_ru}: {''.join(ciphertext)}\n")
    except ValueError:
        print(key_error)
        return permutation_ENCRYP(m)


def permutation_DECRYP(m):
    try:
        k = int(input('Введите ключ, которым было закодировано сообщение (int): '))
        import math
        numOfColumns = int(math.ceil(len(m) / float(k)))
        numOfRows, column, row = k, 0, 0
        numOfShadedBoxes, plaintext = (
            numOfColumns * numOfRows) - len(m), [''] * numOfColumns
        # Дешифрование представляет собой воссоздание оригинальной
        # траспанированной матрицы.
        for symbol in m:
            plaintext[column] += symbol
            column += 1
            if (column == numOfColumns) or (column == numOfColumns -
                                            1 and row >= numOfRows - numOfShadedBoxes):
                column, row = 0, row + 1
        return(
            f"{say_decryp}{say_eng if ru_eng else say_ru}: {''.join(plaintext)}\n")
    except ValueError:
        print(key_error)
        return permutation_DECRYP(m)


def wernam_ENCRYP(m):
    # Шифр Вернама использует алгебру логики (побитовое XOR) и таблицу аски
    # В теории полностью невзламываемый
    len_m = len(m)
    key = [randint(17, 55295) for _ in range(len_m)]
    crypt = [ord(m[i]) ^ key[i] for i in range(len_m)]
    key_human_see = ''.join([chr(number) for number in key])
    crypt_human_see = ''.join([chr(number) for number in crypt])
    return(
        f"""{say_encryp}{say_eng if ru_eng else say_ru}: {crypt_human_see}
Используемый ключ шифрования: {key_human_see}\n""")


def wernam_DECRYP(m):
    len_m = len(m)
    k = input(
        'Введите ключ, которым было закодировано сообщение, его длина равна длине сообщения (str): ')
    if len(k) != len(m):
        print('Ошибка длины ключа\n')
        return wernam_DECRYP(m)
    decryp_humas_see = ''.join([chr(ord(m[i]) ^ ord(k[i]))
                               for i in range(len_m)])
    return(
        f"{say_decryp}{say_eng if ru_eng else say_ru}: {decryp_humas_see}\n")


# Следующий  блок функций фиксирует выбор пользователя на определённом функционале программы.
# При ошибке ввода функция вызывает саму себя.
def get_option():
    option = input("Выберите опцию:\nШифрование - 1\nДешифрование - 0\n")
    if option not in '01' or option == '' or len(option) > 1:
        print(input_error)
        return get_option()
    return option


def get_cipher():
    cipher = input(
        "Выберите метод шифрования|дешифрования:\nШифр Цезаря - 2\nШифр Атбаша - 3\nПерестановочный шифр - 4\nШифр Виженера - 5\nШифр Вернама - 6\n")
    if cipher not in '23456' or cipher == '' or len(cipher) > 1:
        print(input_error)
        return get_cipher()
    return cipher


def get_ru_eng():
    ru_eng = input("Выберите язык:\nАнглийский - 1\nРусский - 0\n")
    if ru_eng not in '01' or ru_eng == '' or len(ru_eng) > 1:
        print(input_error)
        return get_ru_eng()
    ru_eng = int(ru_eng)
    return ru_eng


def get_message():
    # Обрабатывается пустая строка, а так же несоответсвие выбранному языку
    message = input(
        f"Введите сообщение, которое нужно {'закодировать: ' if option=='1' else 'раскодировать: '}")
    if message == '':
        print(f'{input_error}Пустое сообщение\n')
        return get_message()
    elif option == '1':
        if ru_eng:
            if all([message[i] not in dict_ru for i in range(len(message))]):
                return message
            else:
                print(f'{input_error}Текст на русском языке, выбран английский\n')
                return get_message()
        else:
            if all([message[i] not in dict_eng for i in range(len(message))]):
                return message
            else:
                print(f'{input_error}Текст на английском языке, выбран русский\n')
                return get_message()
    else:
        return message

if __name__== "__main__":
    # Цикл, который будет осуществлять функционал программы, вызывая
    # конкретную функцию.
    while True:
        option = get_option()
        cipher = get_cipher()
        ru_eng = get_ru_eng()
        message = get_message()
        choise = option + cipher
        dict = {
            '12': caesar_ENCRYP,
            '02': caesar_DECRYP,
            '13': atbash_ENCRYP_DECRYP,
            '03': atbash_ENCRYP_DECRYP,
            '14': permutation_ENCRYP,
            '04': permutation_DECRYP,
            '15': vigenere_ENCRYP,
            '05': vigenere_DECRYP,
            '16': wernam_ENCRYP,
            '06': wernam_DECRYP}
        # Из опции и выбранного шифра строится индефикатор choise, который
        # является ключом для словаря шифров.
        print(dict[choise](message))
        marker = input(
            'Для выхода из программы введите "q"\nДля продолжения введите любую клавишу\n')
        if marker == 'q':
            break
