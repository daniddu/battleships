ships = [5,3,3,2,2,2]
#if input not in ships, try again (size not left, sizes {} left)
ships.remove(5)#remove input
print(ships)
x = 0


class ship:
    def __init__(self, length, orientation, location, listl): 
            self.length = length
            self.orientation = orientation
            self.location = location
            self.listl = listl
            
    def __str__(self):
        return f"{self.length}, {self.orientation}, {self.location}"

length = int(input("Enter length: "))
orientation = input("Enter ori: ")
y = int(input("enter row (A-J): "))
x = int(input("enter col: "))
location = (x,y)
battleship1 = ship(length, orientation, location)
print(battleship1)


'''

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
        '''
