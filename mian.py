import time
import random
import os


def verify_table():
    v_table = [[] for i in range(3)]
    x_table = [[] for i in range(2)]

    for row_i in range(3):
        row = table[row_i]
        victory = (row[0] == row[1]) & (row[1] == row[2])
        v_table[0].append(row[0])
        v_table[1].append(row[1])
        v_table[2].append(row[2])
        x_table[0].append(row[row_i])
        x_table[1].append(row[2-row_i])
        if (victory):
            return victory

    for column in v_table:
        victory = (column[0] == column[1]) & (column[1] == column[2])
        if (victory):
            return victory

    for x_row in x_table:
        victory = (x_row[0] == x_row[1]) & (x_row[1] == x_row[2])
        if (victory):
            return victory


def play(index):
    if (not(avaiable.count(index))):
        return False
    del avaiable[avaiable.index(index)]

    row = int((index-0.5)//3)
    tile = (index - 1) % 3
    table[row][tile] = TURN_CHAR[turn]

    return True


def update_console():
    os.system('cls')

    if (victory):
        print("Vitória de: ", TURN_TYPE[turn], "\n+---+---+---+")
    elif (draw):
        print("Empate", "\n+---+---+---+")
    else:
        print("Turno de: ", TURN_TYPE[turn], "\n+---+---+---+")

    for row in table:
        print("|", row[0], "|", row[1], "|", row[2], "|")
        print("+---+---+---+")


COMPUTER_TURN = 0
PLAYER_TURN = 1
TURN_TYPE = ("computer", "player")
TURN_CHAR = ("x", "o")

table = [[(j + 1 + (i * 3)) for j in range(3)] for i in range(3)]
avaiable = [i+1 for i in range(9)]
turn = COMPUTER_TURN
first_turn = True


victory = False
draw = False
while((not victory) & (not draw)):
    update_console()

    if (turn == PLAYER_TURN):
        tile = None
        valid = False

        while(not valid):
            try:
                tile = int(input("Escolha um quadrado: "))
                if (avaiable.count(tile)):
                    valid = True
            except:
                tile = None
                valid = False

        play(tile)
    else:
        if (not first_turn):
            tile = avaiable[random.randrange(0, len(avaiable))-1]
            if (not play(tile)):
                pass
                # print(tile)
        else:
            play(5)
            first_turn = False

    victory = verify_table()
    draw = len(avaiable) <= 0
    update_console()

    if (turn == PLAYER_TURN):
        turn = COMPUTER_TURN
    else:
        turn = PLAYER_TURN
    time.sleep(1)
