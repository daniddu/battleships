def set_ships_user(length,board_user,ships_user):
    abc = create_abc_user() 
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    size = 10 #size-input fehlt
    ship = []

    while True:
        y_start = input("enter row: ")

        if not y_start.upper() in alphabet:
            print("please enter a character between A and J")
            continue
        y = int(abc[y_start.upper()])

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

        hor_ver = input("ho or ver: ")

        if hor_ver.upper() not in ['H', 'V']:
            print("please enter H or V")
            #continue

        if hor_ver.upper() == "H":
            if x-1+length > size:
                print("not ok")
                continue
        
            checks = False
            for i in range(x, x+length): 
                if board_user[y][i] != ".":
                    checks = True
                    print(y_start, i, "is occ")
                    break
                
            if checks:
                    print("there is a ship, please enter other coodinates.")
                    continue

            for i in range(x,(x+length)):
                board_user[y][i] = "o"
                print_board_user(board_user, abc, size)
                ship.append([y,i])        
            
        elif hor_ver.upper() == "V":
            if y-1+length > size:
                print("not ok")
                continue
        
            checks = False
            for i in range(y, y+length): 
                if board_user[i][x] != ".":
                    print(board_user[i][x])
                    checks = True
                    print(x, i, "is occ")
                    break
                
            if checks:
                    print("there is a ship, please enter other coodinates.")
                    continue

            for i in range(y,(y+length)):
                board_user[i][x] = "o"
                print_board_user(board_user, abc, size)
                ship.append([i,x])   
                print(board_user)   

        return board_user, ship