queen_direction = [[0,1],[1,0],[-1,0],[0,-1], [1,1],[-1,1],[1,-1],[-1,-1]]


def is_valid(grid, r, c):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] != 1

def traverse(board, r, c):
       for index in range(len(queen_direction)):
                new_r = r + queen_direction[index][0]
                new_c = c + queen_direction[index][1]

                while (is_valid(board, new_r, new_c)):
                    board[new_r][new_c] = 1
                    new_r += queen_direction[index][0]
                    new_c += queen_direction[index][1]
     
def queen_reach(board):
    if not board:
         return []
        
    queen_locations = []
    row_size = len(board)
    col_size = len(board[0])

    for row_index in range(row_size):
         for col_index in range(col_size):
              if board[row_index][col_index] == 1:
                   queen_locations.append([row_index, col_index])
    
    for location in queen_locations:
         traverse(board, location[0], location[1])
    
    return board

board = []


result = queen_reach(board)
print(result)