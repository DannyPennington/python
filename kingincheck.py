import numpy as np
def king_is_in_check(chessboard):
    import numpy as np
    threat = np.zeros((8,8))
    for y in range(8):
        for x in range(8):
            # Pawn threat:
            if chessboard[y][x] == "♟":
                if x == 0:
                    threat[y+1][x+1] = 1
                elif x == 7:
                    threat[y+1][x-1] = 1
                elif y == 7:
                    a = 0
                else:
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
            
            #Bishop time
            if chessboard[y][x] == "♝":
                # Up left threat
                y2 = y
                x2 = x
                for i in range(y+1):
                    for j in range(x+1):
                        while x2>0 and y2>0:
                            threat[y2-1][x2-1] = 1
                            x2 -= 1
                            y2 -=1
                # Up right threat
                y2 = y
                x2 = x
                for i in range(y+1):
                    for j in range(x+1):
                        while y2>0 and x2 < 7:
                            threat[y2-1][x2+1] = 1
                            x2 += 1
                            y2 -= 1
                # Down right threat
                y2 = y
                x2 = x
                for i in range(y+1):
                    for j in range(x+1):
                        while y2 < 7 and x2 < 7:
                            threat[y2+1][x2+1] = 1
                            x2 += 1
                            y2 += 1
                # Down left threat
                y2 = y
                x2 = x
                for i in range(y+1):
                    for j in range(x+1):
                        while y2 < 7 and x2 > 0:
                            threat[y2+1][x2-1] = 1
                            x2 -= 1
                            y2 += 1

            # Queen threat (Combined Rook and Bishop)
            if chessboard[y][x] == "♛":
                threat[y][:] = 1
                threat[0][x] = 1
                threat[1][x] = 1
                threat[2][x] = 1
                threat[3][x] = 1
                threat[4][x] = 1
                threat[5][x] = 1
                threat[6][x] = 1
                threat[7][x] = 1
                # Up left threat
                y2 = y
                x2 = x
                for i in range(y+1):
                    for j in range(x+1):
                        while x2>0 and y2>0:
                            threat[y2-1][x2-1] = 1
                            x2 -= 1
                            y2 -=1
                # Up right threat
                y2 = y
                x2 = x
                for i in range(y+1):
                    for j in range(x+1):
                        while y2>0 and x2 < 7:
                            threat[y2-1][x2+1] = 1
                            x2 += 1
                            y2 -= 1
                # Down right threat
                y2 = y
                x2 = x
                for i in range(y+1):
                    for j in range(x+1):
                        while y2 < 7 and x2 < 7:
                            threat[y2+1][x2+1] = 1
                            x2 += 1
                            y2 += 1
                # Down left threat
                y2 = y
                x2 = x
                for i in range(y+1):
                    for j in range(x+1):
                        while y2 < 7 and x2 > 0:
                            threat[y2+1][x2-1] = 1
                            x2 -= 1
                            y2 += 1

            # Get King position
            if chessboard[y][x] == "♔":
                kingX = x
                kingY = y
    # Now the threat board should be set up, just need to compare king position to see if it is in check
    if threat[kingY,kingX] == 1:
        return True
    else:
        return False

import numpy as np
chessboard = [
            [' ',' ','q',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            ['K',' ',' ',' ',' ',' ',' ',' ']]
threat = np.zeros((8,8))
for y in range(8):
    for x in range(8):
        if chessboard[y][x] == "K":
                kingX = x
                kingY = y
        # Queen threat (Combined Rook and Bishop)
        if chessboard[y][x] == "q":
            threat[y][:] = 1
            threat[0][x] = 1
            threat[1][x] = 1
            threat[2][x] = 1
            threat[3][x] = 1
            threat[4][x] = 1
            threat[5][x] = 1
            threat[6][x] = 1
            threat[7][x] = 1
            # Up left threat
            y2 = y
            x2 = x
            for i in range(y+1):
                for j in range(x+1):
                    while x2>0 and y2>0:
                        threat[y2-1][x2-1] = 1
                        x2 -= 1
                        y2 -=1
            # Up right threat
            y2 = y
            x2 = x
            for i in range(y+1):
                for j in range(x+1):
                    while y2>0 and x2 < 7:
                        threat[y2-1][x2+1] = 1
                        x2 += 1
                        y2 -= 1
            # Down right threat
            y2 = y
            x2 = x
            for i in range(y+1):
                for j in range(x+1):
                    while y2 < 7 and x2 < 7:
                        threat[y2+1][x2+1] = 1
                        x2 += 1
                        y2 += 1
            # Down left threat
            y2 = y
            x2 = x
            for i in range(y+1):
                for j in range(x+1):
                    while y2 < 7 and x2 > 0:
                        threat[y2+1][x2-1] = 1
                        x2 -= 1
                        y2 += 1

print(threat)
if threat[kingX,kingY] == 1:
    print("Check")
else:
    print("No check")      
