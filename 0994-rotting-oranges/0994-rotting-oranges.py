class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time, fresh = 0, 0
        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append([i,j])
        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        while q and fresh > 0:
            for i in range(len(q)):
                r,c = q.popleft()
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    #if in bound, fresh --> make it rotten
                    if nr < 0 or nr == row or nc < 0 or nc == col or grid[nr][nc] != 1: #rotten already
                        continue # since its already rotten we continue
                    grid[nr][nc] = 2 # if its fresh we make it rotten 
                    q.append([nr,nc])
                    fresh -= 1 #remove fresh one
            time += 1 
        return time if fresh == 0 else -1

