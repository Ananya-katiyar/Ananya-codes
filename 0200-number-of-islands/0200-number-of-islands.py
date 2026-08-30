class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        island = 0
        v = set()

        def bfs(sr, sc):
            q = [(sr, sc)]
            v.add((sr,sc))
            d = [(1,0), (-1,0), (0,-1), (0,1)]
            while q:
                r, c = q.pop(0)
                for dr, dc in d:
                    nr = r + dr
                    nc = c + dc
                    if nr < 0 or nr >= m or nc < 0 or nc >= n:
                        continue
                    elif grid[nr][nc] == "0":
                        continue
                    elif (nr,nc) in v:
                        continue
                    q.append((nr, nc))
                    v.add((nr, nc)) 
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i,j) not in v:
                    bfs(i,j)
                    island += 1
        return island