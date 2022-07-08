import math
from random import randint

# Самые часто используемые строки и переменные вынесены в отдельный блок
# переменных.
say_encryp, say_decryp = 'Зашифрованное сообщение на ', 'Расшифрованное сообщение нa '
say_eng, say_ru = 'Английском языке', 'Русском языке'
say_key_error = 'Неправильный формат ключа! (введена пустая строка или неправильный тип данных)\n'
say_input_error = 'Неверный параметр\n'
dict_eng = {x for x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'}
dict_ru = {
    x for x in 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'}


# Функции шифрования названы по шаблону <Оф.название шифра>_<Шифрование и/или Дешифрование>.
# Каждая функция укомплектована обрабатывать ошибки ввода пользователя и
# способна вызывать сама себя.

def vigenere_ENCRYP(message: str, ru_eng: bool, key: str) -> str:
    message = message.upper()
    key = key.upper()
    power_dict_eng, power_dict_ru = 26, 33
    slow = {
        x for x in 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯABCDEFGHIJKLMNOPQRSTUVWXYZ'}
    shift, power = 'A' if ru_eng else 'А', power_dict_eng if ru_eng else power_dict_ru
    # Реализуется квадрат виженера с помощью представления букв в числах
    # UNICODE.
    key *= len(message) // len(key) + 1
    c = ''.join([chr((ord(j) + ord(key[i])) % power + ord(shift))
                 if j in slow else j for i, j in enumerate(message)])
    return (
        f"{say_encryp}{say_eng if ru_eng else say_ru}: {c}\n")


def vigenere_DECRYP(message: str, ru_eng: bool, key: str) -> str:
    message = message.upper()
    key = key.upper()
    power_dict_eng, power_dict_ru = 26, 33
    slow = {
        x for x in 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯABCDEFGHIJKLMNOPQRSTUVWXYZ'}
    shift, power = 'A' if ru_eng else 'Џ', power_dict_eng if ru_eng else power_dict_ru
    # Шифрование и Дешифрование есть перемещение по квадрату виженера в числовом виде
    # и отличается только знаком +/- в алгоритме.
    key *= len(message) // len(key) + 1
    c = ''.join([chr((ord(j) - ord(key[i])) % power + ord(shift))
                 if j in slow else j for i, j in enumerate(message)])
    return (
        f"{say_decryp}{say_eng if ru_eng else say_ru}: {c}\n")


def atbash_ENCRYP_DECRYP(message: str, ru_eng: bool) -> str:
    # Шифр Атбаша не нуждается в ключе и реализуется с помощью словарей с зеркальными буквами
    # шифрование и дешифрование производит один и тот же алгоритм.
    dict_ENG = {'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v', 'f': 'u', 'g': 't', 'h': 's', 'i': 'r', 'j': 'q',
                'k': 'p', 'l': 'o',
                'm': 'n', 'n': 'm', 'o': 'l', 'p': 'k', 'q': 'j', 'r': 'i', 's': 'h', 't': 'g', 'u': 'f', 'v': 'e',
                'w': 'd', 'x': 'c',
                'y': 'b', 'z': 'a', ' ': ' ', ',': ',', '.': '.'}
    dict_RU = {'а': 'я', 'б': 'ю', 'в': 'э', 'г': 'ь', 'д': 'ы', 'е': 'ъ', 'ё': 'щ', 'ж': 'ш', 'з': 'ч', 'и': 'ц',
               'й': 'х', 'к': 'ф',
               'л': 'у', 'м': 'т', 'н': 'с', 'о': 'р', 'п': 'п', 'р': 'о', 'с': 'н', 'т': 'м', 'у': 'л', 'ф': 'к',
               'х': 'и', 'ц': 'и',
               'ч': 'з', 'ш': 'ж', 'щ': 'ё', 'ъ': 'е', 'ы': 'д', 'ь': 'г', 'э': 'в', 'ю': 'б', 'я': 'а', ' ': ' ',
               ',': ',', '.': '.', }
    message = message.lower()
    c = ''
    if ru_eng:
        c = ''.join(
            [dict_ENG[word] if word in dict_ENG else word for word in message])
    else:
        c = ''.join(
            [dict_RU[word] if word in dict_RU else word for word in message])
    return (
        f"Итоговое сообщение на {say_eng if ru_eng else say_ru}: {c}\n")


def caesar_ENCRYP(message: str, ru_eng: bool, key: int) -> str:
    dict_ENG = ' abcdefghijklmnopqrstuvwxyz,.'
    dict_RU = ' абвгдеёжзийклмнопрстуфхцчшщъыьэюя,.'
    dict_RU_ENG = dict_ENG if ru_eng else dict_RU
    # Шифр цезаря реализуется сдвигом индекса буквы по её словарю, шифрование и дешифрование
    # отличаются знаками +/-.
    message = message.lower()
    c = ''.join(
        [dict_RU_ENG[(dict_RU_ENG.index(word) + key) % len(dict_RU_ENG)] if word in dict_RU_ENG else word for word in
         message])
    return (
        f"{say_encryp}{say_eng if ru_eng else say_ru}: {c}\n")


def caesar_DECRYP(message: str, ru_eng: bool, key: int) -> str:
    dict_ENG = ' abcdefghijklmnopqrstuvwxyz,.'
    dict_RU = ' абвгдеёжзийклмнопрстуфхцчшщъыьэюя,.'
    dict_RU_ENG = dict_ENG if ru_eng else dict_RU
    message = message.lower()
    c = ''.join(
        [dict_RU_ENG[(dict_RU_ENG.index(word) - key) % len(dict_RU_ENG)] if word in dict_RU_ENG else word for word in
         message])
    return (
        f"{say_decryp}{say_eng if ru_eng else say_ru}: {c}\n")


def permutation_ENCRYP(message: str, ru_eng: bool, key: int) -> str:
    ciphertext = [''] * key
    # Перестановочный шифр использует заполнение матрицы исходными значениями, длина строки определяется ключом
    # шифрованное сообщение записывается по колоннам снизу вверх.
    for coloumn in range(key):
        currentIndex = coloumn
        while currentIndex < len(message):
            ciphertext[coloumn] += message[currentIndex]
            currentIndex += key
    return (
        f"{say_encryp}{say_eng if ru_eng else say_ru}: {''.join(ciphertext)}\n")


def permutation_DECRYP(message: str, ru_eng: bool, key: int) -> str:
    numOfColumns = int(math.ceil(len(message) / float(key)))
    numOfRows, column, row = key, 0, 0
    numOfShadedBoxes, plaintext = (
        numOfColumns * numOfRows) - len(message), [''] * numOfColumns
    # Дешифрование представляет собой воссоздание оригинальной
    # траспанированной матрицы.
    for symbol in message:
        plaintext[column] += symbol
        column += 1
        if (column == numOfColumns) or (column == numOfColumns -
                                        1 and row >= numOfRows - numOfShadedBoxes):
            column, row = 0, row + 1
    return (
        f"{say_decryp}{say_eng if ru_eng else say_ru}: {''.join(plaintext)}\n")


def wernam_ENCRYP(message: str, ru_eng: bool) -> str:
    # Шифр Вернама использует алгебру логики (побитовое XOR) и таблицу аски
    # В теории полностью невзламываемый
    len_m = len(message)
    key = [randint(17, 55295) for _ in range(len_m)]
    crypt = [ord(message[i]) ^ key[i] for i in range(len_m)]
    key_human_see = ''.join([chr(number) for number in key])
    crypt_human_see = ''.join([chr(number) for number in crypt])
    return (
        f"""{say_encryp}{say_eng if ru_eng else say_ru}: {crypt_human_see}
Используемый ключ шифрования: {key_human_see}\n""")


def wernam_DECRYP(message: str, ru_eng: bool, key: str) -> str:
    len_m = len(message)
    if len(key) != len(message):
        print('Ошибка длины ключа\n')
        return 'Ключ не соответсвует по длине сообщению'
    decryp_humas_see = ''.join([chr(ord(message[i]) ^ ord(key[i]))
                                for i in range(len_m)])
    return (
        f"{say_decryp}{say_eng if ru_eng else say_ru}: {decryp_humas_see}\n")



# Следующий  блок функций фиксирует выбор пользователя на определённом функционале программы.
# При ошибке ввода функция вызывает саму себя.
def get_option():
    option = input("Выберите опцию:\nШифрование - 1\nДешифрование - 0\n")
    if option not in '01' or option == '' or len(option) > 1:
        print(say_input_error)
        return get_option()
    return option


def get_cipher():
    cipher = input(
        "Выберите метод шифрования|дешифрования:\nШифр Цезаря - 2\nШифр Атбаша - 3\nПерестановочный шифр - 4\nШифр Виженера - 5\nШифр Вернама - 6\n")
    if cipher not in '23456' or cipher == '' or len(cipher) > 1:
        print(say_input_error)
        return get_cipher()
    return cipher


def get_ru_eng():
    ru_eng = input("Выберите язык:\nАнглийский - 1\nРусский - 0\n")
    if ru_eng not in '01' or ru_eng == '' or len(ru_eng) > 1:
        print(say_input_error)
        return get_ru_eng()
    ru_eng = bool(int(ru_eng))
    return ru_eng


def get_message():
    # Обрабатывается пустая строка, а так же несоответсвие выбранному языку
    message = input(
        f"Введите сообщение, которое нужно {'закодировать: ' if option == '1' else 'раскодировать: '}")
    if message == '':
        print(f'{say_input_error}Пустое сообщение\n')
        return get_message()
    elif option == '1':
        if ru_eng:
            if all([message[i] not in dict_ru for i in range(len(message))]):
                return message
            else:
                print(
                    f'{say_input_error}Текст на русском языке, выбран английский\n')
                return get_message()
        else:
            if all([message[i] not in dict_eng for i in range(len(message))]):
                return message
            else:
                print(
                    f'{say_input_error}Текст на английском языке, выбран русский\n')
                return get_message()
    else:
        return message


def get_str_key():
    key = input('Введите ключ в формате слова/строки (str): ')
    if key.isalpha():
        return key
    else:
        print(say_key_error)
        return get_str_key()


def get_int_key():
    try:
        key = int(input('Введите ключ в формате числа (int): '))
        return key
    except ValueError:
        print(say_key_error)
        return get_int_key()


if __name__ == "__main__":
    # Цикл, который будет осуществлять функционал программы, вызывая
    # конкретную функцию.
    while True:
        option = get_option()
        cipher = get_cipher()
        ru_eng = get_ru_eng()
        message = get_message()
        choise = option + cipher
        str_key, int_key = 'l', 1
        if cipher == '5' or (cipher == '6' and option == '0'):
            str_key = get_str_key()
        else:
            int_key = get_int_key()
        dict = {
            '12': caesar_ENCRYP(message, ru_eng, int_key),
            '02': caesar_DECRYP(message, ru_eng, int_key),
            '13': atbash_ENCRYP_DECRYP(message, ru_eng),
            '03': atbash_ENCRYP_DECRYP(message, ru_eng),
            '14': permutation_ENCRYP(message, ru_eng, int_key),
            '04': permutation_DECRYP(message, ru_eng, int_key),
            '15': vigenere_ENCRYP(message, ru_eng, str_key),
            '05': vigenere_DECRYP(message, ru_eng, str_key),
            '16': wernam_ENCRYP(message, ru_eng),
            '06': wernam_DECRYP(message, ru_eng, str_key)}
        print(dict[choise])
        marker = input(
            'Для выхода из программы введите "q"\nДля продолжения введите любую клавишу\n')
        if marker == 'q':
            break

