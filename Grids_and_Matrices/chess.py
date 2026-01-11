
def is_valid(grid, r, c):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] != 1


def chess_move(grid, piece, r, c):
    knight_dirs = [[2,1],[-2,1],[1,2],[-1,2], [2,-1],[-2,-1],[-1,-2],[1,-2]]
    king_direction = [[0,1],[1,0],[-1,0],[0,-1], [1,1],[-1,1],[1,-1],[-1,-1]]
    queen_direction = [[0,1],[1,0],[-1,0],[0,-1], [1,1],[-1,1],[1,-1],[-1,-1]]

    result = []
    if piece == "king":
        for index in range(len(king_direction)):
            new_r = r + king_direction[index][0]
            new_c = c + king_direction[index][1]
            if is_valid(grid,new_r,new_c ):
                result.append([new_r,new_c])
    elif piece == "queen": 
        for index in range(len(queen_direction)):
            new_r = r + queen_direction[index][0]
            new_c = c + queen_direction[index][1]

            while (is_valid(grid, new_r, new_c)):
                result.append([new_r,new_c])
                if new_r > 0:
                    new_r += 1
                else:
                    new_r -= 1
                
                if new_c > 0:
                    new_c += 1
                else:
                    new_c -= 1
    else:
        for index in range(len(knight_dirs)):
            new_r = r + knight_dirs[index][0]
            new_c = c + knight_dirs[index][1]
            if is_valid(grid,new_r,new_c ):
                result.append([new_r,new_c])
    return result

board = [[0, 0, 0, 1, 0, 0],
         [0, 1, 1, 1, 0, 0],
         [0, 1, 0, 1, 1, 0],
         [1, 1, 1, 1, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0]]
piece = "queen"
r = 4
c = 4

result = chess_move(board, piece, r, c)
print(result)