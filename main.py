import random
import os
def get_field():
    return [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""]
    ]

def print_field(field):
    for row in field:
        print(row)

def check_draw(listt):
    item_to_check = [list[0]]
    for item in listt:
        if item not in item_to_check:
            return False
    return True

def get_list(field):
    lst = []
    for row in field:
        for item in row:
            lst.append(item)
    return lst

def check_row(field):
    for row in field:
        if row[0] == row[1] == row[2]:
            if row[0] == "X":
                return "X"
            elif row[0] == "O":
                return "O"
    return False

def check_if_won(var, field):
    if var == "X":
        print("Player 1 Won")
        for row in field:
            print(row)
        quit()
    elif var == "O":
        print("Player 2 Won")
        for row in field:
            print(row)
        quit()

def check_collom(field):
    for n in range(3):
        collom = [field[0][n], field[1][n], field[2][n]]
        if collom[0] == collom[1] == collom[2]:
            if collom[0] == "X":
                return "X"
            elif collom[0] == "O":
                return "O"
    return False

def check_diagonal(field):
    diagonal1 = [field[0][0], field[1][1], field[2][2]]
    diagonal2 = [field[0][2], field[1][1], field[2][0]]
    diagonal1_same = diagonal1[0] == diagonal1[1] == diagonal1[2]
    diagonal2_same = diagonal2[0] == diagonal2[1] == diagonal2[2]
    
    if diagonal1_same == True:
        if diagonal1[0] == "X":
            return "X"
        elif diagonal1[0] == "O":
            return "O"
    
    if diagonal2_same == True:
        if diagonal2[0] == "X":
            return "X"
        elif diagonal2[0] == "O":
            return "O"
    return False

def computer_turn(field):
    new_field = field
    while True:
        first = random.randint(0, 2)
        second = random.randint(0, 2)
        if field[first][second] == "":
            new_field[first][second] = "O"
            return new_field

def check_all(field):
    row_true = check_row(field)
    check_if_won(row_true, field)
    collom_true = check_collom(field)
    check_if_won(collom_true, field)
    diagonal_true = check_diagonal(field)
    check_if_won(diagonal_true, field)
    return False


os.system("cls")
print("WELCOME TO TICTACTOE BY HIMNEYDV8")
field = get_field()

while True:
    print_field(field)

    while True:
        coordinates = input("Place your X using coordinates: ").split(" ")
        coordinates = [int(x) for x in coordinates]
        if field[coordinates[0]][coordinates[1]] == "":
            field[coordinates[0]][coordinates[1]] = "X"
            break
        else:
            print("Not Possible")

    os.system("cls")
    
    won = check_all(field)

    field = computer_turn(field)

    

    lst = get_list(field)

    if check_draw(lst):
        print("Draw!")
        quit()