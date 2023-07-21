def create_abc():
    abc = {}
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(26):
        abc[i] = alphabet[i]
    return abc

def init_board():
    #creates the board-dict
    y_numbers = 5
    board = []
    for i in range(y_numbers):
        board.append(["."]*y_numbers)

    #prints the board
    abc = create_abc()
    row = 0
    print(" ", "1", "2", "3", "4", "5") #unschoen
    for line in board:
        print(abc[row], "|".join(line))
        row +=1
     
    return board


def set_ships_user():
    #board = board
    abc = {}
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(26):
        abc[alphabet[i]] = i 
    board = init_board()
    print(board)
    print(abc)
    #while len(ships_user) < 2:
    
    ships_user = []
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
          
        column_num = input("enter column of ship: ")
        if type(column_num) == int:
            x = int(column_num)-1

        else:
            print("enter integer")
            continue
                          
        if x > 5:
            print("out of range")
            continue
        if 0 <= y < 5 and 0 <= x < 5:
            if board[y][x] == ".":
                board[y][x] = "o"
                ships_user.append([y,x])
                break
            elif board[y][x] == "o":
                print("already taken")
        
    
                
    print(board, ships_user)
    
    
    row = 0
    print(" ", "1", "2", "3", "4", "5") #unschoen
    for line in board:
        print([key for key in abc.keys()][row], "|".join(line))
        row +=1
        
       
    return board, ships_user           
    

def set_ships_pc(board, ships_pc):
    board = board
    abc = {}
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(26):
        abc[alphabet[i]] = i 
    #board = init_board()
    #print(board)
    #while len(ships_user) < 2:
    y = abc[input("pc, enter row of ship: ")]
    x = int(input("pc, enter column of ship: "))-1
    if 0 <= y < 5 and 0 <= x < 5:
        if board[y][x] == ".":
            board[y][x] = "o"
            ships_pc.append([y,x])
        elif board[y][x] == "o":
            print("already taken")
        else:
            print("not valid")
    
    print(board, ships_pc)
    
    row = 0
    print(" ", "1", "2", "3", "4", "5") #unschoen
    for line in board:
        print([key for key in abc.keys()][row], "|".join(line))
        row +=1
    return board, ships_pc
    

def set_board():
    board = init_board()
    print(board)
    ships_user = []
    ships_pc = []
    while len(ships_user) < 2 and len(ships_pc) < 2:
        set_ships_user(board, ships_user)
        set_ships_pc(board, ships_pc)



set_ships_user()

def play_battleship():
    set_board()
    set_ships_user()
    #user_guess()
    #pc_guess()