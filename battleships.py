import random

def create_abc_user():
    abc = {}
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(26):
        abc[alphabet[i]] = i
    return abc, alphabet

def create_abc_pc():
    abc = {}
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(26):
        abc[i] = alphabet[i]
    return abc, alphabet

def init_board():
    y_numbers = 5
    board = []
    for i in range(y_numbers):
        board.append(["."]*y_numbers)
    return board

def print_board_user(board, abc):
    row = 0
    print(" ", "1", "2", "3", "4", "5") #unschoen
    for line in board:
        print([key for key in abc.keys()][row], "|".join(line))
        row +=1

def print_board_pc(board, abc):
    row = 0
    print(" ", "1", "2", "3", "4", "5") #unschoen
    for line in board:
        print(abc[row], "|".join(line))
        row +=1
     
    #return board


def set_ships_user(board):
    abc, alphabet = create_abc_user() 
    print_board_user(board, abc)
    print(board)
    
    ships_user = []
    print(abc)
    while True:
        row_num = input("enter row of ship: ")
        if not row_num in alphabet:
            print("is not in it")
            continue
        else:
            y = abc[row_num]
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
                        if x > 5:
                            print("out of range")
                        else:
                            break  
                except ValueError:
                    print("enter number")
           
        if 0 <= y < 5 and 0 <= x < 5:
            if board[y][x] == ".":
                board[y][x] = "o"
                ships_user.append([y,x])
                break
            elif board[y][x] == "o":
                print("already taken")
                continue
    
    print_board_user(board,abc)
    print(ships_user)    
    print(board)   
    return board, ships_user           
   

def set_ships_pc(board):
    abc = create_abc_pc()
    print(abc)
    print_board_pc(board, abc)
    print(board)

    ships_pc = []
    while True:
        y = random.randrange(0, 5)
        x = random.randrange(0, 5)
        print(y,x)
                
        
        if board[y][x] == ".":
            board[y][x] = "o"
            ships_pc.append([y,x])
            break
        elif board[y][x] == "o":
            print("already taken")
            continue
    
    print_board_pc(board, abc) 
    print(ships_pc)    
    return board, ships_pc
    
def check_num_ships(board):
    ships_user = set_ships_user(board)
    ships_pc = set_ships_pc(board)
    while len(ships_user) < 2 and len(ships_pc) < 2:
        set_ships_user(board, ships_user)
        set_ships_pc(board, ships_pc)
    return board

def set_board():
    board = init_board()
    print(board)
    set_ships_user(board)
    set_ships_pc(board)
    check_num_ships(board)


set_board()

def play_battleship():
    set_board()
    set_ships_user()
    #user_guess()
    #pc_guess()