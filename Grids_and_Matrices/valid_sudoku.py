

class ValidSudoku:
  
  def solve(self, board):
    return self.valid_rows(board) and self.valid_cols(board) and self.valid_subgrids(board)

  def valid_rows(self, board):
    R, C = len(board), len(board[0])
    for r in range(R):
      seen = set()
      for c in range(C):
        if board[r][c] in seen:
          return False
        if board[r][c] != 0:
          seen.add(board[r][c])
    return True

  def valid_cols(self, board):
    R, C = len(board), len(board[0])
    for c in range(C):
      seen = set()
      for r in range(R):
        if board[r][c] in seen:
          return False
        if board[r][c] != 0:
          seen.add(board[r][c])
    return True

  def valid_subgrid(self, board, r, c):
    seen = set()
    for new_r in range(r, r + 3):
      for new_c in range(c, c + 3):
        if board[new_r][new_c] in seen:
          return False
        if board[new_r][new_c] != 0:
          seen.add(board[new_r][new_c])
    return True

  def valid_subgrids(self, board):
    for r in range(3):
      for c in range(3):
        if not self.valid_subgrid(board, r * 3, c * 3):
          return False
    return True