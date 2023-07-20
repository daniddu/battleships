
#print(map_table[0:3])

#x_numbers = 1,2,3,4,5,6,7,8,9,10
#board_shown = [[' ']*8 for x in range(8)] 
#board_hidden = [[' ']*8 for x in range(8)]



def set_board():
    y_numbers = 5
    board = []
    board_hidden = []
    for i in range(y_numbers):
        board.append("."*y_numbers)
        board_hidden.append("."*y_numbers)

    abc = {}
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(y_numbers):
        abc[i] = alphabet[i]
    #print(abc)

    row = 0
    print(" ", "1", "2", "3", "4", "5")
    for line in board:
        print(abc[row], "|".join(line))
        row +=1
    '''
    first_row = []
    first_row.append(" ")
    for num in x_numbers:
        first_row.append(str(num))
    first_row = (" ".join(first_row))
    

    row = []
    for i in range(1, y_numbers+1):
        row.append("|."*y_numbers)
        
    return row
'''

def set_ships():
    board_shown = set_board()
    board_hidden = set_board()

    print(board_shown, '\n', board_hidden)
    #board = [["."]*10 for u in range(10)]
    '''for i in range(2):
        y, x = input("enter location of ship (format: y x): ").split()
        y = int(y)
        x = int(x)
        print(board_hidden[y])
        
        if board[y][x] == ".":
            board[y][x] = "o"
        board = " ".join(board)
        
    return board
'''      

#set_board()

set_ships()
