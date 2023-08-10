ships = [5,3,3,2,2,2]
#if input not in ships, try again (size not left, sizes {} left)
print(len(ships))
ships.remove(5)#remove input
print(len(ships))


class Ship:
    def __init__(self, length, location): 
            self.length = length
            self.location = location
            
    def __str__(self):
        return f"{self.length}, {self.location}"
    
    
ships_user = []

def create_ships(length,y_start,x_start,y_end,x_end):
    if y_start == y_end:
         print("horizontal")
    else:
         print("vertical")

    location = (y_start,x_start)
    ship = Ship(length, location)
    ships_user.append(ship)
    return "ship: " + str(ships_user), Ship

for i in range(0,2):
    create_ships(input("enter length: "),input("enter startrow: "),input("enter startcol: "),input("enter endrow: "),input("enter endcol: "))

for i in range(0,2):
     print("length of ship {}: {};".format(i+1, ships_user[i].length), ships_user[i])

'''

        

length = int(input("Enter length: "))
orientation = input("Enter ori: ")
y = int(input("enter row (A-J): "))
x = int(input("enter col: "))
location = (x,y)
battleship1 = ship(length, orientation, location)
print(battleship1)




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
