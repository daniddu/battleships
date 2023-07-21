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
    abc = {}
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(26):
        abc[alphabet[i]] = i 
    board = init_board()
    print(board)
    ships_user = []
    for i in range(2):
        #user input of ship location
        y = abc[input("enter row of ship: ")]
        x = int(input("enter column of ship: "))
        ships_user.append([y,x])
        print(ships_user)
        if board[y-1][x-1] == ".":
            board[y-1][x-1] = "o"
        elif board[y][x] == "o":
            print("already taken")
    print(board)
    #abc = create_abc()
    
    
    row = 0
    print(" ", "1", "2", "3", "4", "5") #unschoen
    for line in board:
        print([key for key in abc.keys()][row], "|".join(line))
        row +=1
        
       
    return board, ships_user
    

'''
                if y < len(board):
                    print("ok")
                    break
                elif y > len(board):
                    print(len(board))
                    print("no valid value, try again")
            except:
                print("Provide an integer value...")
                continue
'''

                #check if empty
                
    

def set_ships_pc():
    board = set_board()
    print(board)
    for i in range(2):
        #user input of ship location
        y = int(input("enter row of ship "))-1
        x = int(input("enter column of ship: "))-1
        
        print(board[x][y])
        
        #check if empty
        if board[y][x] == ".":
            board[y][x] = "o"

    abc = create_abc()
    row = 0
    print(" ", "1", "2", "3", "4", "5") #unschoen
    for line in board:
        print(abc[row], "|".join(line))
        row +=1
        
    return board


#set_board()

print(set_ships_user())

def play_battleship():
    set_board()
    set_ships_user()
    #user_guess()
    #pc_guess()