class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
    
        efforts = [[float('inf')] * n for _ in range(m)]
        efforts[0][0] = 0
        min_heap = [(0, 0, 0)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while min_heap:
            effort, r, c = heapq.heappop(min_heap)
            if r == m - 1 and c == n - 1:
                return effort
            if effort > efforts[r][c]:
                continue                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    new_effort = max(effort, abs(heights[r][c] - heights[nr][nc]))
                    if new_effort < efforts[nr][nc]:
                        efforts[nr][nc] = new_effort
                        heapq.heappush(min_heap, (new_effort, nr, nc))
        return 0
        """def bfs(limit):
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
        return low"""