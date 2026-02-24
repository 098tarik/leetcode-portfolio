
"""
Example 1:
grid =  [[-1,  2,  3],
         [ 4,  0,  0],
         [-2,  0,  9]]
Output: [[15, 14, 12],
         [11,  9,  9],
         [ 7,  9,  9]]

Example 2:
grid =  [[5]]
Output: [[5]]
Explanation: For a 1x1 grid, each cell's subgrid is just itself.

Example 3:
grid =  [[1, 2, 3]]
Output: [[6, 5, 3]]
Explanation: For a single row, each cell's subgrid includes all elements to
its right.

"""

def calculate_max(grid, r,c):
    R = len(grid)
    C = len(grid[0])
    max_sum = 0
    for row in range(r, R):
        for col in range(c, C):
            max_sum += grid[row][col]

    return max_sum

def subgrid_sums_optimal(grid):
  R, C = len(grid), len(grid[0])
  res = [row.copy() for row in grid]
  for r in range(R - 1, -1, -1):
    for c in range(C - 1, -1, -1):
      if r + 1 < R:
        res[r][c] += res[r + 1][c]
      if c + 1 < C:
        res[r][c] += res[r][c + 1]
       if r + 1 < R and c + 1 < C:  # subtract doublecounted subgrid
        res[r][c] -= res[r + 1][c + 1]
  return res


def transform_matrix(grid):
    R = len(grid)
    C = len(grid[0])
    for row in range(R):
        for col in range(C):
            grid[row][col] = calculate_max(grid, row, col)

    return grid

grid =  [[-1,  2,  3],
         [ 4,  0,  0],
         [-2,  0,  9]]

print(transform_matrix(grid))