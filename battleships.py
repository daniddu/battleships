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
    size = 10 #make it input?
    board = []
    for i in range(size):
        board.append(["."]*size)
    return board, size

def print_board_user(board_user, abc):
    row = 0
    print(" ", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
    for line in board_user:
        print([key for key in abc.keys()][row], "|".join(line))
        row +=1

def print_board_pc(board_pc, abc):
    row = 0
    print(" ", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
    for line in board_pc:
        print(abc[row], "|".join(line))
        row +=1

def set_ships_user(board_user, ships_user, size):
    abc = create_abc_user() 
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    #print_board_user(board_user, abc)

    while True:
        row_num = input("enter row of ship (A-J): ")
        if not row_num.upper() in alphabet:
            print("please enter a character between A and J")
            continue
        else:
            y = int(abc[row_num.upper()])

        if y > size:
            print("out of range")
            continue
        else:
            while True:
                try:
                    x = int(input("enter column of ship: "))-1
                    if x >= size or x < 0:
                        print("out of range")
                        continue
                    else:
                        break  
                except ValueError:
                    print("please enter a number")
           
        if y < size and x < size:
            if board_user[y][x] == ".":
                board_user[y][x] = "o"
                ships_user.append([y,x])
                    
            elif board_user[y][x] == "o":
                print("there is already a ship")
                continue
                    
        print_board_user(board_user,abc) 
        return board_user, ships_user
   

def set_ships_pc(board_pc, ships_pc, size):
    #abc = create_abc_pc()
    while True:
        y = random.randrange(0, size)
        x = random.randrange(0, size)
                    
        if board_pc[y][x] == ".":
            board_pc[y][x] = "o" 
            ships_pc.append([y,x])

        elif board_pc[y][x] == "o":
            print("there is already a ship")
            continue

        print("ships_pc:", ships_pc)    
        return board_pc, ships_pc
    
def set_ships(ships_user, ships_pc, board_user, board_pc, num_ships, size):
    while len(ships_user) < num_ships and len(ships_pc) < num_ships:
        set_ships_user(board_user, ships_user, size)
        set_ships_pc(board_pc, ships_pc, size)
    return board_user, board_pc

#setting board and placing ships
def set_board():
    print("lets play battleships!", "\n")
    board_user, size = init_board()
    print("place your ships:")
    abc = create_abc_user()
    print_board_user(board_user, abc)
    board_pc, size = init_board()
    ships_user = []
    ships_pc = []
    while True:
                try:
                    num_ships = int(input("how many ships do want to use (max. 5)? ")) #check if num and how many (max 5?)
                    if num_ships >= 5 or num_ships < 0:
                        print("out of range")
                        continue
                    else:
                        break  
                except ValueError:
                    print("please enter a number")
    print("place {} ship(s)".format(num_ships))
    set_ships(ships_user, ships_pc, board_user, board_pc, num_ships, size)
    return board_user, board_pc, ships_user, ships_pc


def user_guess(board_pc, ships_pc, guessing_board, size):
    abc = create_abc_user() 
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while True:
        row_num = input("guess y: ")
        if not row_num.upper() in alphabet:
            print("please enter a character between A and J")
            continue
        else:
            y = int(abc[row_num.upper()])

        if y > size:
            print("out of range")
            continue

        while True:
            try:
                x = int(input("guess x: "))-1
                if x >= size or x < 0:
                    print("out of range")
                    continue
                else:
                    break
            except ValueError:
                print("please enter a number")
                              
        if guessing_board[y][x] == "/":
            print("already guessed")
        if board_pc[y][x] == "o":
            guessing_board[y][x] = "X"
            board_pc[y][x] = "X"
            ships_pc.remove([y,x])
            print("hit it!")
        elif board_pc[y][x] == ".":
            guessing_board[y][x] = "/"
            print("nope!")
    
        print("{} ship(s) left to find for you!".format(len(ships_pc)))
        return board_pc, ships_pc, guessing_board

def pc_guess(board_user, ships_user, size):

    y = random.randrange(0, size)
    x = random.randrange(0, size)

    if board_user[y][x] == "/":
        print("pc, already guessed")
    if board_user[y][x] == "o":
        board_user[y][x] = "X"
        ships_user.remove([y,x])
        print("hit it, pc!")
        print(ships_user)
    elif board_user[y][x] == ".":
        board_user[y][x] = "/"
        print("not hit!")

    print("{} ship(s) left to find for pc!".format(len(ships_user)))
    return board_user, ships_user

def guessing(board_user, board_pc, ships_user, ships_pc):
    abc = create_abc_pc()
    guessing_board, size = init_board()

    while len(ships_user) > 0 and len(ships_pc) > 0:
        print("it's your turn:")
        board_pc, ships_pc, guessing_board = user_guess(board_pc, ships_pc, guessing_board, size)
        #print(guessing_board)
        print("your guessing board:")
        print_board_pc(guessing_board, abc)
        print("pcs turn:")
        board_user, ships_user = pc_guess(board_user, ships_user, size)
    
    return board_pc, ships_pc, guessing_board, board_user, ships_user
   
def play_battleship():
    board_user, board_pc, ships_user, ships_pc = set_board()
    board_pc, ships_pc, guessing_board, board_user, ships_user = guessing(board_user, board_pc, ships_user, ships_pc)
    if len(ships_user) == 0:
        print("pc is the winner!") 
    elif len(ships_pc) == 0:
        print("you are the winner!")
       

play_battleship()