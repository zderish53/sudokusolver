
sudokuboard = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]]

def find_zero(sudokuboard):
    for i in range(len(sudokuboard)):
        for j in range(len(sudokuboard[0])):
            if sudokuboard[i][j] == 0:
                    return (i, j)  # row, col

    return None

def works(sudokuboard, coor, num):
    #check row
    for i in range(len(sudokuboard)):
        if num == sudokuboard[i][coor[1]] and i != coor[0]:
            return False
    
    #check col
    for i in range(len(sudokuboard[0])):
        if num == sudokuboard[coor[0]][i] and i != coor[1]:
            return False

    #check square
    squarex = coor[1] // 3
    squarey = coor[0] // 3

    for i in range(squarey*3, squarey*3 + 3):
        for j in range(squarex*3, squarex*3 +3):
            if num == sudokuboard[i][j] and (i, j) != coor:
                return False
    return True

def solve(sudokuboard):
    if not find_zero(sudokuboard):
        return True
    else:
        coor = find_zero(sudokuboard)

    for i in range(1,10):
        if works(sudokuboard, (coor[0], coor[1]), i):
            sudokuboard[coor[0]][coor[1]] = i

            if solve(sudokuboard):
                return True

            sudokuboard[coor[0]][coor[1]] = 0
            
    return False

def print_board(sudokuboard):
    for i in range(len(sudokuboard)):
        print(" \n")
        if i % 3 == 0 and i != 0:
            print("- - -  - - - -  - - - -")
        for j in range(len(sudokuboard[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end = "")
            print(str(sudokuboard[i][j]), end = " ")

print_board(sudokuboard)
solve(sudokuboard)
print("\nsolved board")
print_board(sudokuboard)
