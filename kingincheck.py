import numpy as np
def king_is_in_check(chessboard):
    import numpy as np
    threat = np.zeros((8,8))
    for y in range(8):
        for x in range(8):
            # Pawn threat:
            if chessboard[y][x] == "♟":
                threat[y+1][x+1] = 1
                threat[y+1][x-1] = 1

            # Rook threat:
            if chessboard[y][x] == "♜":
                threat[y][:] = 1
                threat[0][x] = 1
                threat[1][x] = 1
                threat[2][x] = 1
                threat[3][x] = 1
                threat[4][x] = 1
                threat[5][x] = 1
                threat[6][x] = 1
                threat[7][x] = 1
            
            # Knight threat:
            if chessboard[y][x] == "♞":
                # No edge cases required
                if 2<= x <= 5 and 2<= y <=5:
                    threat[y+2][x+1] = 1
                    threat[y+2][x-1] = 1
                    threat[y+1][x+2] = 1
                    threat[y+1][x-2] = 1
                    threat[y-2][x-1] = 1
                    threat[y-2][x+1] = 1
                    threat[y-1][x-2] = 1
                    threat[y-1][x+2] = 1
                # Hard coding bottom right corner
                elif y == 7 and x == 7:
                    threat[y-2][x-1] = 1
                    threat[y-1][x-2] = 1
                elif y == 7 and x == 6:
                    threat[y-2][x-1] = 1
                    threat[y-1][x-2] = 1
                    threat[y-2][x+1] = 1
                elif y == 6 and x == 7:
                    threat[y-2][x-1] = 1
                    threat[y-1][x-2] = 1
                    threat[y+1][x-2] = 1
                elif y == 6 and x == 6:
                    threat[y-2][x-1] = 1
                    threat[y-1][x-2] = 1
                    threat[y+1][x-2] = 1
                    threat[y-2][x+1] = 1
                # Bottom left corner
                elif y == 7 and x == 0:
                    threat[y-2][x+1] = 1
                    threat[y-1][x+2] = 1
                elif y == 7 and x == 1:
                    threat[y-2][x+1] = 1
                    threat[y-1][x+2] = 1
                    threat[y-2][x-1] = 1
                elif y == 6 and x == 0:
                    threat[y-2][x+1] = 1
                    threat[y-1][x+2] = 1
                    threat[y+1][x+2] = 1
                elif y == 6 and x == 1:
                    threat[y-2][x+1] = 1
                    threat[y-1][x+2] = 1
                    threat[y+1][x+2] = 1
                    threat[y-2][x-1] = 1

                # Top right corner
                elif y == 0 and x == 7:
                    threat[y+2][x-1] = 1
                    threat[y+1][x-2] = 1
                elif y == 0 and x == 6:
                    threat[y+2][x-1] = 1
                    threat[y+1][x-2] = 1
                    threat[y+2][x+1] = 1
                elif y == 1 and x == 7:
                    threat[y+2][x-1] = 1
                    threat[y+1][x-2] = 1
                    threat[y-1][x-2] = 1
                elif y == 1 and x == 6:
                    threat[y+2][x-1] = 1
                    threat[y+1][x-2] = 1
                    threat[y-1][x-2] = 1
                    threat[y+2][x+1] = 1
                # Top left corner
                elif y == 0 and x == 0:
                    threat[y+2][x+1] = 1
                    threat[y+1][x+2] = 1
                elif y == 0 and x == 1:
                    threat[y+2][x+1] = 1
                    threat[y+1][x+2] = 1
                    threat[y+2][x-1] = 1
                elif y == 1 and x == 0:
                    threat[y+2][x+1] = 1
                    threat[y+1][x+2] = 1
                    threat[y-1][x+2] = 1
                elif y == 1 and x == 1:
                    threat[y+2][x+1] = 1
                    threat[y+1][x+2] = 1
                    threat[y-1][x+2] = 1
                    threat[y+2][x-1] = 1

                elif y == 6:
                    threat[y+1][x+2] = 1
                    threat[y+1][x-2] = 1
                    threat[y-2][x-1] = 1
                    threat[y-2][x+1] = 1
                    threat[y-1][x-2] = 1
                    threat[y-1][x+2] = 1
                elif y == 7:
                    threat[y-2][x-1] = 1
                    threat[y-2][x+1] = 1
                    threat[y-1][x-2] = 1
                    threat[y-1][x+2] = 1
                elif y == 1:
                    threat[y+2][x+1] = 1
                    threat[y+2][x-1] = 1
                    threat[y+1][x+2] = 1
                    threat[y+1][x-2] = 1
                    threat[y-1][x-2] = 1
                    threat[y-1][x+2] = 1
                elif y == 0:
                    threat[y+2][x+1] = 1
                    threat[y+2][x-1] = 1
                    threat[y+1][x+2] = 1
                    threat[y+1][x-2] = 1
                elif x == 6:
                    threat[y+2][x+1] = 1
                    threat[y+2][x-1] = 1
                    threat[y+1][x-2] = 1
                    threat[y-2][x-1] = 1
                    threat[y-2][x+1] = 1
                    threat[y-1][x-2] = 1
                elif x == 7:
                    threat[y+2][x-1] = 1
                    threat[y+1][x-2] = 1
                    threat[y-2][x-1] = 1
                    threat[y-1][x-2] = 1
                elif x == 1:
                    threat[y+2][x+1] = 1
                    threat[y+2][x-1] = 1
                    threat[y+1][x+2] = 1
                    threat[y-2][x-1] = 1
                    threat[y-2][x+1] = 1
                    threat[y-1][x+2] = 1
                elif x == 0:
                    threat[y+2][x+1] = 1
                    threat[y+1][x+2] = 1
                    threat[y-2][x+1] = 1
                    threat[y-1][x+2] = 1
            
            # Bishop threat:
            if chessboard[y][x] == "":
                x =2

            # Queen threat
            if chessboard[x][y] == "♛":
                threat[x][:] = 1
                threat[:][y] = 1


chessboard = [
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ','b',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' ']]
threat = np.zeros((8,8))
for y in range(8):
    for x in range(8):
        #Bishop time
        if chessboard[y][x] == "b":
            # Up left threat
            y2 = y
            while y2-1 >= 0:
                x2 = x
                while x2-1 >= 0:
                    threat[y2-1][x2-1] = 1
                    x2 -= 1
                y2 -= 1
            # Up right threat
            
            #while y2-1 >= 0:
               # while x2-1 >= 0:
                   # threat[y2-1][x+1] = 1
                  #  x2 -= 1
                  #  y2 -= 1

print(threat)