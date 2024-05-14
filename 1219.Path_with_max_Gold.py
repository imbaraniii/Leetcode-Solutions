# In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

# Return the maximum amount of gold you can collect under the conditions:
# *Every time you are located in a cell you will collect all the gold in that cell.
# *From your position, you can walk one step to the left, right, up, or down.
# *You can't visit the same cell more than once.
# *Never visit a cell with 0 gold.
# *You can start and stop collecting gold from any position in the grid that has some gold.

def getMaximumGold(grid) -> int:
        # This function uses backtracking to find all the possible paths for a particular index element.
        def backtracking_possible_paths(row, coloumn, sum):
            if not 0 <= row < rowL or not 0 <= coloumn < colL or grid[row][coloumn] == 0:
                return sum
            
            visited_gold = grid[row][coloumn]
            sum += visited_gold
            grid[row][coloumn] = 0
            # Finds the max sum possible in different routes
            fin_sum = max(backtracking_possible_paths(row+1, coloumn, sum), 
                            backtracking_possible_paths(row-1, coloumn, sum),
                            backtracking_possible_paths(row, coloumn+1, sum),
                            backtracking_possible_paths(row, coloumn-1, sum))

            grid[row][coloumn] = visited_gold
            return fin_sum

        rowL = len(grid)
        colL = len(grid[0])
        maxGold = 0

        for row in range(rowL):
            for col in range(colL):
                # Backtracking to find the best path which produces the max Gold.
                maxGold = max(maxGold, backtracking_possible_paths(row, col, 0))

        return maxGold

grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
ans = getMaximumGold(grid)
print(ans)

# 82.76%