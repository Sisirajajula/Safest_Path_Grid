#Breadth-First Search + Binary Search
from collections import deque
class Solution:
    dir = [(0, 1),(0, -1),(1, 0), (-1, 0)]
    def isValidCell(self, grid, i, j):
        n = len(grid)
        return 0 <= i < n and 0 <= j < n
    def isValidSafeness(self, grid, min_safe):
        n = len(grid)
        if grid[0][0] < min_safe or grid[n - 1][n - 1] < min_safe:
            return False
        traversal_queue = deque([(0, 0)])
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True
        #BFS to find a valid path
        while traversal_queue:
            curr = traversal_queue.popleft()
            if curr[0] == (n - 1) and curr[1] == (n - 1):
                return True
            for d in self.dir:
                di, dj = curr[0] + d[0], curr[1]+ d[1]
                if self.isValidCell(grid, di, dj) and not visited[di][dj] and grid[di][dj] >= min_safe:
                    visited[di][dj] = True
                    traversal_queue.append((di, dj))
        return False
    def maximumSafenessFactor(self, grid) -> int:
        n = len(grid)
        thief = deque()
        for i in range(n):
            for j in range(n):
                if(grid[i][j] == 1):
                    thief.append((i, j))
                    grid[i][j] = 0
                else:
                    grid[i][j] = -1 
        while thief:
            size = len(thief)
            while size > 0:
                curr = thief.popleft()
                for d in self.dir:
                    di, dj = curr[0] + d[0], curr[1]+ d[1]
                    val = grid[curr[0]][curr[1]]
                    if self.isValidCell(grid, di, dj) and grid[di][dj] == -1:
                        grid[di][dj] =val + 1
                        thief.append((di, dj))
                size -= 1
        start, end, res = 0, 0, -1
        for i in range(n):
            for j  in range(n):
                end = max(end, grid[i][j])
        while start <= end:
            mid = start + (end - start) // 2
            if self.isValidSafeness(grid, mid):
                res = mid
                start = mid + 1
            else:
                end = mid - 1
        return res
if __name__ == "__main__":
    # Example grid
    grid = [
        [0, 0, 1],
        [0, 0, 0],
        [0, 0, 0]
    ]

    # Create an instance of the Solution class
    solution = Solution()

    # Calculate the maximum safeness factor
    result = solution.maximumSafenessFactor(grid)

    # Print the result
    print("Maximum safeness factor:", result)
