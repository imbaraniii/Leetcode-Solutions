# You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.

# Return the number of servers that communicate with any other server.

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(i, j):
            # If that cell is already visited, we dont move further along that row or col
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == -1:
                return 0
            
            # If encountered a Server
            if grid[i][j] == 1:
                grid[i][j] = -1 # Mark the cell as visited
                count = 1
                # Check that coloumn
                # O(n)
                for col in range(n):
                    if grid[i][col] == 1:
                        count += dfs(i, col)
                # CHeck that Row
                # O(m)
                for row in range(m):
                    if grid[row][j] == 1:
                        count += dfs(row, j)


            grid[i][j] = -1 # Mark the cell as visited
            return count

        server_count = 0 # Result
        # O(m*n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: # If that cell is a server
                    t = dfs(i, j)
                    # We only add to the result only if there are two or more servers in that col or row because only then the connection is possible
                    if t > 1: 
                        server_count += t

        return server_count


# O(m*n)
