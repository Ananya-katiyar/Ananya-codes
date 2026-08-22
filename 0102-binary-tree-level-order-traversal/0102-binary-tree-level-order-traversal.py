# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque()
        q.append(root)
        ans = []
        while q:
            temp = []
            n = len(q)
            for i in range(n):
                r = q.popleft()
                if r.left != None:
                    q.append(r.left)
                if r.right != None:
                    q.append(r.right)
                temp.append(r.val)
            ans.append(temp)
        return ans
                

                


