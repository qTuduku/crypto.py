import PySimpleGUI as sg
from crypto import *
from pyperclip import *


def check_key(key: str, mod: str, cipher) -> bool:
    if cipher == 'Атбаш' or (cipher == 'Вернам' and mod == 'Шифрование'):
        if key != '':
            print('::Этому шифру не нужен ключ::')
            return False
        else:
            return True
    elif cipher == 'Виженер' or (cipher == 'Вейнар' and mod == 'Дешифрование'):
        if key.isalpha():
            return True
        else:
            print('::Неправильный буквенный ключ::')
            return False
    else:
        if key.isdigit():
            return True
        else:
            print('::Неправильный числовой ключ::')
            return False


def check_message(message: str, mod: str, lang: str) -> bool:
    dict_eng = {
        x for x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'}
    dict_ru = {
        x for x in 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'}
    if message == '':
        print('::Введено пустое сообщение::')
        return False
    elif mod == 'Шифрование':
        if lang == 'Английский':
            if all([message[i] not in dict_ru for i in range(len(message))]):
                return True
            else:
                print('::Текст не на Английском языке::')
                return False
        else:
            if all([message[i] not in dict_eng for i in range(len(message))]):
                return True
            else:
                print('::Текст не на Русском языке::')
                return False
    else:
        return True


def copy_message(lang: str):
    if lang == 'Английский':
        return copy(mes[45:])
    else:
        return copy(mes[42:])


sg.theme('Dark')
layout = [[sg.Text("""Программа для шифрования и дешифрования данных"""), sg.Button('FAQ'), sg.Button('Overview of ciphers')],
          [sg.Text('Текст'),
           sg.InputText(),
           sg.Text('Способ шифрования/дешифрования: '),
           sg.Combo(['Цезарь',
                     'Атбаш',
                     'Перестановочный',
                     'Виженер',
                     'Вернам'])],
          [sg.Text('Ключ'), sg.InputText(), sg.Text('Режим работы:   '), sg.Combo(
              ['Шифрование', 'Дешифрование']), sg.Text('Язык:'), sg.Combo(['Русский', 'Английский'])],
          [sg.Output(size=(105, 20))],
          [sg.Submit(), sg.Cancel(), sg.Button('Copy key'),
           sg.Button('Copy converted message')],
          ]
mes = ''
window = sg.Window('Cryptograf', layout)
while True:
    try:
        event, values = window.read()
        if event == 'FAQ':
            print("""Туториал:
    --Цезарь - числовой ключ
    --Атбаш - ключ не нужен
    --Престановочный - числовой ключ
    --Виженер - буквенный ключ
    --Верман - ключ при шифровании создаётся сам
    --Верман - ключ при дешифровании буквенно-числовой
    - После преобразования текста нажмите на кнопку Copy key
    и Copy converted message если хотите передать результат куда то
    - Для выхода из программы нажмите крестик в правом верхнем углу
    программы, либо на кнопку Cancel
    - Для осуществления шифрование/дешифрования нажмите на кнопку
    Submit, программа сообщит если что-то введено неверно""")
        if event == 'Overview of ciphers':
            print("""
Описание шифров будет идти по возрастающей градации их криптостойкости
------------------------------------------------------------------------------------------------------------------------
Шифр Цезаря основан на сдвиге алфавита, на котором было написано сообщение
к примеру буква |а| при сдвиге |1| превращается в |б|
а при сдвиге |-1| в букву |я|
Степень криптостойкости - устарел/не используется
-----------------------------------------------------------------------------------------------------------------------
Шифр Атбаша заменяет каждую букву сообщения на зеркальную ей
он как бы разделяет алфавит на 2 части, а-я б-ю в-э и середина алфавита п-п
Степень криптостойкости - устарел/не используется
-----------------------------------------------------------------------------------------------------------------------
Перестановочный шифр оперирует всеми символами в сообщении и создаёт
новое распределение для них по специальному алгоритму, в худшем случае
сообщение останется таким же, как и было
Степень криптостойкости - некоторые модификации используются до сих пор
-----------------------------------------------------------------------------------------------------------------------
Шифр Виженера создаёт квадрат Виженера и по соответствию заменяет каждый
символ сообщения новым, ключевое слово это один из параметров квадрата
и чем длинее этот ключ, тем лучше результат
Степень криптостойкости - в 20 веке считался невзламываемым, некоторые его
модификации используются до сих пор, им можно зашифровать не ценное сообщение
-----------------------------------------------------------------------------------------------------------------------
Шифр Вернама использует двоичную логику, переводя каждую букву в двоичный код
и составляя случайный равный по длине ключ он применяет побитовое XOR
без знания ключа данный шифр невозможно взломать тк при переборе будут
получены все возможные сообщения такой же длины
Степень криптостойкости - наивысшая, но есть проблемы с передачей ключа
из-за чего шифр не получил большого распространения
------------------------------------------------------------------------------------------------------------------------
""")
        if event == 'Copy key':
            if mes == '':
                print(
                    '::Чтобы скопировать пароль сначала произведите хотя бы одно шифрование/дешифрование::')
            else:
                if values[2] == '':
                    print('::Ключ не может быть пустым сообщением::')
                else:
                    copy(values[2])
                    print('Ключ скопирован в буфер обмена')
        if event == 'Copy converted message':
            if mes == '':
                print(
                    '::Чтобы скопировать сообщение сначала произведите хотя бы одно шифрование/дешифрование::')
            else:
                copy_message(values[4])
                print('Преобразованное сообщение скопировано в буфер обмена')
        if event in (None, 'Exit', 'Cancel'):
            break
        if event == 'Submit':
            if (values[1] not in {'Цезарь', 'Атбаш', 'Перестановочный', 'Виженер', 'Вернам'}) or (
                    values[3] not in {'Шифрование', 'Дешифрование'}) or (values[4] not in {'Русский', 'Английский'}):
                print('::Неверное значение в раскрывающемся списке::')
            elif check_message(values[0], values[3], values[4]) and check_key(values[2], values[3], values[1]):
                lang = True if values[4] == 'Английский' else False
                if values[3] == 'Шифрование':
                    if values[1] == 'Цезарь':
                        mes = caesar_ENCRYP(values[0], lang, int(values[2]))
                        print(mes)
                    elif values[1] == 'Атбаш':
                        mes = atbash_ENCRYP_DECRYP(values[0], lang)
                        print(mes)
                    elif values[1] == 'Перестановочный':
                        mes = permutation_ENCRYP(
                            values[0], lang, int(values[2]))
                        print(mes)
                    elif values[1] == 'Виженер':
                        mes = vigenere_ENCRYP(values[0], lang, values[2])
                        print(mes)
                    elif values[1] == 'Вернам':
                        mes = wernam_ENCRYP(values[0], lang)
                        print(mes)
                else:
                    if values[1] == 'Цезарь':
                        mes = caesar_DECRYP(values[0], lang, int(values[2]))
                        print(mes)
                    elif values[1] == 'Атбаш':
                        mes = atbash_ENCRYP_DECRYP(values[0], lang)
                        print(mes)
                    elif values[1] == 'Перестановочный':
                        mes = permutation_DECRYP(
                            values[0], lang, int(values[2]))
                        print(mes)
                    elif values[1] == 'Виженер':
                        mes = vigenere_DECRYP(values[0], lang, values[2])
                        print(mes)
                    elif values[1] == 'Вернам':
                        mes = wernam_DECRYP(values[0], lang, values[2])
                        print(mes)
    except Exception:
        print('Непредвиденная ошибка')
