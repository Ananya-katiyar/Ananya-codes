# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q = deque([(root, None)])
        while q:
            level = {}
            for _ in range(len(q)):
                node, parent = q.popleft()
                if node.val in (x, y):
                    level[node.val] = parent
                if node.left:
                    q.append((node.left, node))
                if node.right:
                    q.append((node.right, node))
            if x in level and y in level:
                return level[x] != level[y]
            if x in level or y in level:
                return False
        return False
            
  