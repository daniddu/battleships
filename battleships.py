import random

def create_abc_user():
    abc = {}
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(26):
        abc[alphabet[i]] = i
    return abc

def create_abc_pc():
    abc = {}
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(26):
        abc[i] = alphabet[i]
    return abc

def init_board():
    y_numbers = 5
    board = []
    for i in range(y_numbers):
        board.append(["."]*y_numbers)
    return board

def print_board_user(board_user, abc):
    row = 0
    print(" ", "1", "2", "3", "4", "5") #unschoen
    for line in board_user:
        print([key for key in abc.keys()][row], "|".join(line))
        row +=1

def print_board_pc(board_pc, abc):
    row = 0
    print(" ", "1", "2", "3", "4", "5") #unschoen
    for line in board_pc:
        print(abc[row], "|".join(line))
        row +=1
     
    #return board


def set_ships_user(board_user, ships_user):
    abc = create_abc_user() 
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print_board_user(board_user, abc)

    #print(board_user)
    #ships_user = []
    #print(abc)
    while True:
        row_num = input("enter row of ship: ")
        if not row_num in alphabet:
            print("is not in it")
            continue
        else:
            y = int(abc[row_num])
            print(y)
        if y > 4:
            print("out of range")
            continue
        else:
            print("ok")
            while True:
                try:
                    column_num = int(input("enter column of ship: "))
                    if type(column_num) == int:
                        x = column_num-1
                        print(x)
                        if x > 5:
                            print("out of range")
                        else:
                            break  
                except ValueError:
                    print("enter number")
           
        if y < 5 and x < 5:
                if board_user[y][x] == ".":
                    board_user[y][x] = "o"
                    ships_user.append([y,x])
                        
                elif board_user[y][x] == "o":
                    print("already taken")
                    continue
                    

        print_board_user(board_user,abc)
        print(board_user)
        print(ships_user)
   
        print("next")
        return board_user, ships_user           
   

def set_ships_pc(board_pc, ships_pc):
    abc = create_abc_pc()
    #print_board_pc(board, abc)
    #print(board_pc)

    #ships_pc = []
    while True:

        y = random.randrange(0, 5)
        x = random.randrange(0, 5)
        print(y,x)
                    
        if board_pc[y][x] == ".":
            board_pc[y][x] = "o"
            ships_pc.append([y,x])

        elif board_pc[y][x] == "o":
            print("already take")
            continue

    #print_board_pc(board_pc, abc) 
        print(board_pc)
        print(ships_pc)    
        return board_pc, ships_pc
    
def check_num_ships(ships_user, ships_pc, board_user, board_pc):
    #ships_user = set_ships_user(ships_user, board_user)
    #ships_pc = set_ships_pc(ships_pc, board_pc)
    while len(ships_user) < 2 and len(ships_pc) < 2:
        set_ships_user(board_user, ships_user)
        set_ships_pc(board_pc, ships_pc)
    return board_user, board_pc

def set_board():
    print("lets play battleships!", "\n")
    board_user = init_board()
    abc = create_abc_user()
    print_board_user(board_user, abc)
    board_pc = init_board()
    print(board_pc)
    print(board_pc)
    ships_user = []
    ships_pc = []
    print("4")

    check_num_ships(ships_user, ships_pc, board_user, board_pc)
    return board_user, board_pc, ships_user, ships_pc


def user_guess(board_pc, ships_pc, guessing_board):

    y = int(input("guess y: "))
    x = int(input("guess x: "))

    if guessing_board[y][x] == "/":
        print("already guessed")
    if board_pc[y][x] == "o":
        guessing_board[y][x] = "X"
        board_pc[y][x] = "X"
        ships_pc.remove([y,x])
        print("hit it!")
        print(ships_pc)
    elif board_pc[y][x] == ".":
        guessing_board[y][x] = "/"
        print("nope")
    return board_pc, ships_pc, guessing_board

def pc_guess(board_user, ships_user):

    y = random.randrange(0, 5)
    x = random.randrange(0, 5)

    if board_user[y][x] == "/":
        print("pc, already guessed")
    if board_user[y][x] == "o":
        board_user[y][x] = "X"
        ships_user.remove([y,x])
        print("hit it, pc!")
        print(ships_user)
    elif board_user[y][x] == ".":
        board_user[y][x] = "/"
        print("nope")
    return board_user, ships_user

def guessing(board_user, board_pc, ships_user, ships_pc):
    abc = create_abc_pc()
    guessing_board = init_board()

    while len(ships_user) > 0 and len(ships_pc) > 0:
        board_pc, ships_pc, guessing_board = user_guess(board_pc, ships_pc, guessing_board)
        print(guessing_board)
        print_board_pc(guessing_board, abc)
        board_user, ships_user = pc_guess(board_user, ships_user)
        print(board_user, ships_user)


    
    return board_pc, ships_pc, guessing_board, board_user, ships_user
   

def play_battleship():
    board_user, board_pc, ships_user, ships_pc = set_board()
    board_pc, ships_pc, guessing_board, board_user, ships_user = guessing(board_user, board_pc, ships_user, ships_pc)
    
    #while score_user > 0 and score_pc > 0:
        #user_guess()
        #pc_guess()

play_battleship()