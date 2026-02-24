"""
Given a rectangular RxC grid of integers,
 grid, with R > 0 and C > 0, 
 return a new grid with the same dimensions where each cell [r, c] 
 contains the maximum in the subgrid with [r, c] in the top-left corner and [R-1, C-1] in the bottom-right corner.


Example 1:
grid =  [[1, 5, 3],
         [4,-1, 0],
         [2, 0, 2]]
Output: [[5, 5, 3],
         [4, 2, 2],
         [2, 2, 2]]

Example 2:
grid =  [[5]]
Output: [[5]]
Explanation: For a 1x1 grid, each cell's subgrid is just itself.

Example 3:
grid =  [[1, 2, 3]]
Output: [[3, 3, 3]]
Explanation: For a single row, each cell's subgrid includes all elements to
its right.

"""

def calculate_max(grid, r,c):
    R = len(grid)
    C = len(grid[0])
    max_num = 0
    for row in range(r, R):
        for col in range(c, C):
            max_num = max(grid[row][col], max_num)

    return max_num


def subgrid_maximums_optimal(grid):
  R, C = len(grid), len(grid[0])
  res = [row.copy() for row in grid]
  for r in range(R - 1, -1, -1):
    for c in range(C - 1, -1, -1):
      if r + 1 < R:
        res[r][c] = max(res[r][c], res[r + 1][c])
      if c + 1 < C:
        res[r][c] = max(res[r][c], res[r][c + 1])
  return res


def transform_matrix(grid):
    R = len(grid)
    C = len(grid[0])
    for row in range(R):
        for col in range(C):
            grid[row][col] = calculate_max(grid, row, col)

    return grid

grid = [[1, 5, 3],
        [4, -1, 0],
        [2, 0, 2]]

print(transform_matrix(grid))