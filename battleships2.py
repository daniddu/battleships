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

def init_board(size):
    size = 10 #make it input?
    board = []
    for i in range(size):
        board.append(["."]*size)
    return board

def print_board_user(board_user, abc, size):
    print(" ", end=" ")
    for x in range(1,size+1):
        print(x, end=" ")
    print("")
    row = 0
    for line in board_user:
        print([key for key in abc.keys()][row], "|".join(line))
        row +=1

def print_board_pc(board_pc, abc, size):
    print(" ", end=" ")
    for x in range(1,size+1):
        print(x, end=" ")
    print("")
    row = 0
    for line in board_pc:
        print(abc[row], "|".join(line))
        row +=1

def set_ships_user(length,board_user,ships_user):
    abc = create_abc_user() 
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    size = 10 #size-input fehlt
    ship = []

    while True:
        y_start = input("enter row of ships starting point: ")

        if not y_start.upper() in alphabet:
            print("please enter a character between A and J.")
            continue
        y = int(abc[y_start.upper()])

        if y > size:
            print("out of range.")
            continue
        else:
            while True:
                try:
                    x = int(input("enter column of ships starting point: "))-1
                    if x >= size or x < 0:
                        print("out of range.")
                        continue
                    else:
                        break  
                except ValueError:
                    print("please enter a number.")

        hor_ver = input("horizontal (H) or vertical (V)? ")

        if hor_ver.upper() not in ['H', 'V']:
            print("please enter H or V.")
            #continue

        if hor_ver.upper() == "H":
            if x-1+length >= size:
                print("not enough space, choose another starting point for your ship.")
                continue
        
            checks = False
            for i in range(x, x+length): 
                if board_user[y][i] != ".":
                    checks = True
                    break  
               
            if checks:
                    print("there is a ship, please enter other coordinates.")
                    continue

            for i in range(x,(x+length)):
                board_user[y][i] = "o"
                ship.append([y,i])        
            
        elif hor_ver.upper() == "V":
            if y-1+length >= size:
                print("column not long enough, choose another starting point for your ship")
                continue
        
            checks = False
            for i in range(y, y+length): 
                if board_user[i][x] != ".":
                    print(board_user[i][x])
                    checks = True
                    break 
                else:
                    continue            
                
            if checks:
                    print("there is a ship, please enter other coordinates.")
                    continue

            for i in range(y,(y+length)):
                board_user[i][x] = "o"
                ship.append([i,x])   

        return board_user, ship, abc

def set_ships_pc(length,board_pc,ships_pc):
    abc = create_abc_pc()
    size = 10
    ship = []
  
    while True:
        x = random.randrange(0, size)
        y = random.randrange(0, size)

        l = ["H","V"]
        hor_ver = l[random.randrange(0,2)]

        if hor_ver == "H":
            if x-1+length >= size:
                print("column not ok")
                continue

            checks = False
            for i in range (x, x+length):
                if board_pc[y][i] != ".":
                    checks = True
                    break
                
            if checks:
                    print("there is a ship, please enter other coodinates.")
                    continue

            for i in range(x,(x+length)):
                board_pc[y][i] = "o"
                ship.append([y,i]) 

        elif hor_ver.upper() == "V":
            if y-1+length >= size:
                print("column not long enough, choose other starting point")
                continue
    
            checks = False
            for i in range(y, y+length): 
                if board_pc[i][x] != ".":
                    print(board_pc[i][x])
                    checks = True
                    break
                else:
                    continue
            
            if checks:
                    print("there is a ship, please enter other coodinates.")
                    continue

            for i in range(y,(y+length)):
                board_pc[i][x] = "o"
                ship.append([i,x])   

        return board_pc, ship, abc

   
def set_ships(ships_user, ships_pc, board_user, board_pc, size):
    ships = [5,3] #533222
    for i in ships:
        print("set ship with length {}:".format(i))

        board_user,ship,abc = set_ships_user(i,board_user,ships_user)
        ships_user.append(ship)
        print("\n"+"your placed ships:"+"\n")
        print_board_user(board_user,abc,size)
        print("\n")

        board_pc,ship_pc,abc = set_ships_pc(i,board_pc,ships_pc)
        ships_pc.append(ship_pc)
        #print_board_pc(board_pc,abc,size) #entfernen

    return board_user, board_pc

#setting board and placing ships
def set_board():
    size = int(input("size: "))
    board_user = init_board(size)
    abc = create_abc_user()
    print_board_user(board_user, abc, size)
    board_pc = init_board(size)
    print("")
    ships_user = []
    ships_pc = []
    print("you have to place 6 ships with length 5 (1x), 3 (2x) and 2 (3x).")
    set_ships(ships_user, ships_pc, board_user, board_pc, size)
    return board_user, board_pc, ships_user, ships_pc, size


def user_guess(board_pc, ships_pc, guessing_board, size):
    ships = [5,3]
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

                              
        if guessing_board[y][x] == "/" or guessing_board[y][x] == "X":
            print("already guessed")
        if board_pc[y][x] == "o":
            guessing_board[y][x] = "X"
            board_pc[y][x] = "X"

            for i in range(len(ships_pc)): 
                for o in range(len(ships_pc[i])):
                    if ships_pc[i][o-1] == [y,x]:
                        print(i)
                        print("size of target:",ships[i])
                        print(ships_pc[i][o])
                        ships_pc[i].remove([y,x])
        
        elif board_pc[y][x] == ".":
            guessing_board[y][x] = "/"
            print("nope!")
    
        #print(ships_pc.count([]))
        print("{} of pcs ships sunken.".format(ships_pc.count([]))) #how many left?
        return board_pc, ships_pc, guessing_board

def pc_guess(board_user, ships_user, size):
    ships = [5,3]
    y = random.randrange(0, size)
    x = random.randrange(0, size)

    if board_user[y][x] == "/":
        print("pc, already guessed")
    if board_user[y][x] == "o":
        board_user[y][x] = "X"
        for i in range(len(ships_user)):
            for o in range(i):
                if ships_user[i][o] == [y,x]:
                    print(i)
                    print("size of targ:",ships[i])
                    print(ships_user[i][o])
                    ships_user[i].remove([y,x])
        
    elif board_user[y][x] == ".":
        board_user[y][x] = "/"
        print("not hit!")

    print("{} of users ships sunken!".format(ships_user.count([])))

    return board_user, ships_user

def guessing(board_user, board_pc, ships_user, ships_pc, size):
    abc = create_abc_pc()
    guessing_board = init_board(size)

    while len(ships_user) != ships_user.count([]) and len(ships_pc) != ships_pc.count([]):
        print("it's your turn:")
        board_pc, ships_pc, guessing_board = user_guess(board_pc, ships_pc, guessing_board, size)
        #print(guessing_board)
        #print(ships_pc)
        print("\n"+"your guessing board:"+"\n")
        print_board_pc(guessing_board, abc, size)
        print("pcs turn:")
        board_user, ships_user = pc_guess(board_user, ships_user, size)
    
    return board_pc, ships_pc, guessing_board, board_user, ships_user
   
def play_battleship():
    print("\n"+"========== lets play battleships! ==========", "\n")
    print(" "*16+"__"+"/___")
    print(" "*10+"_____/______|")
    print(" "*2+"_______/_____\_______\_____")
    print(" "*2+"\\"+" "*14+"< "*3+" "*6+"/")
    print("~"*32, "\n")

    board_user, board_pc, ships_user, ships_pc, size = set_board()
    print("\n"+"lets start guessing!"+"\n")
    board_pc, ships_pc, guessing_board, board_user, ships_user = guessing(board_user, board_pc, ships_user, ships_pc, size)
    print(len(ships_pc))
    print("x", ships_pc)
    if len(ships_user) == ships_user.count([]):
        print(len(ships_user),ships_user.count([]))
        print("pc is the winner!") 
    elif len(ships_pc) == ships_pc.count([]):
        print(len(ships_pc),ships_pc.count([]))
        print("you are the winner!")
       

play_battleship()