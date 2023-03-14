# ----------Игра "Крестики-Нолики"------- ------
import time
import os


def clear_console():  #
    clear = os.system('cls')  # Очистка консоли от устаревшей информации
    return clear  #


desk = [[' ', 'a', 'b', 'c'],  #
        ['1', ' ', ' ', ' '],  # Игровое поле
        ['2', ' ', ' ', ' '],  #
        ['3', ' ', ' ', ' ']]  #

hod_dict = {'a': 1, 'b': 2, 'c': 3}  # Словарь для перевода строки в число
igrok = None

while igrok not in ("x", "o"):
    clear_console()
    igrok = input("Чем будет играть первый игрок? x - за крестики, o - за нолики ")
if igrok == "x":
    mast = 1
    turn = "Ходят крестики. Ход в формате строка-столбец: "
else:
    mast = 2
    turn = "Ходят нолики. Ход в формате строка-столбец: "


def tablo():  # Функция распечатывания игрового поля
    for el1, el2, el3, el4 in desk:
        if el2 == 'a':
            print(el1, el2, el3, el4)
        else:
            print(el1, el2, el3, el4, sep="|")
    return ""


print(tablo())
while not ((desk[1].count("x") == 3) or  #
           (desk[2].count("x") == 3) or  # Проверка три в ряд Х в строках
           (desk[3].count("x") == 3) or  #

           (desk[1].count("o") == 3) or  #
           (desk[2].count("o") == 3) or  # Проверка три в ряд О в строках
           (desk[3].count("o") == 3) or  #

           (desk[1][1] == "x" and desk[2][1] == "x" and desk[3][1] == "x") or  #
           (desk[1][2] == "x" and desk[2][2] == "x" and desk[3][2] == "x") or  # Проверка три в ряд Х в столбцах
           (desk[1][3] == "x" and desk[2][3] == "x" and desk[3][3] == "x") or  #

           (desk[1][1] == "o" and desk[2][1] == "o" and desk[3][1] == "o") or  #
           (desk[1][2] == "o" and desk[2][2] == "o" and desk[3][2] == "o") or  # Проверка три в ряд О в столбцах
           (desk[1][3] == "o" and desk[2][3] == "o" and desk[3][3] == "o") or  #

           (desk[1][1] == "x" and desk[2][2] == "x" and desk[3][3] == "x") or  # Диагональ Х
           (desk[3][1] == "x" and desk[2][2] == "x" and desk[1][3] == "x") or  #

           (desk[1][1] == "o" and desk[2][2] == "o" and desk[3][3] == "o") or  # Диагональ О
           (desk[3][1] == "o" and desk[2][2] == "o" and desk[1][3] == "o")):  #
    if desk[1].count(" ") == 0 and desk[2].count(" ") == 0 and desk[3].count(" ") == 0:
        mast = None
        break
    position = input(turn)
    if position not in ('1a', '1b', '1c', '2a', '2b', '2c', '3a', '3b', '3c'):  # Проверка введенных координат
        clear_console()
        print(tablo())
        continue
    else:
        first_position = int(position[0])
        second_position = position[1]
        second_position = hod_dict[second_position]
        if desk[first_position][second_position] != " ":
            print("Данная ячейка занята. Выберите, пожалуйста, другую")
            time.sleep(2)
            clear_console()
            print(tablo())
            continue
    if mast % 2 != 0:
        desk[first_position][second_position] = "x"
        turn = "Ходят нолики. Ход в формате строка-столбец: "
        mast += 1
    else:
        desk[first_position][second_position] = "o"
        turn = "Ходят крестики. Ход в формате строка-столбец: "
        mast += 1
    clear_console()
    print(tablo())
if mast is None:
    clear_console()
    print(tablo())
    print("Ничья!")
elif mast % 2 != 0:
    print("Победили нолики!")
else:
    print("Победили крестики!")
time.sleep(4)
# -----------------------
