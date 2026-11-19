class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        
        def bfs(limit):
            q = deque([(0, 0)])
            visited = set()
            visited.add((0, 0))
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            while q:
                r, c = q.popleft()
                if r == m - 1 and c == n - 1:
                    return True
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < m and 0 <= nc < n:
                        if (nr, nc) not in visited:
                            diff = abs(heights[r][c] - heights[nr][nc])
                            if diff <= limit:
                                visited.add((nr, nc))
                                q.append((nr, nc))
            return False
        low = 0
        high = max(max(row) for row in heights)
        while low < high:
            mid = (low + high) // 2
            if bfs(mid):
                high = mid
            else:
                low = mid + 1
        return low