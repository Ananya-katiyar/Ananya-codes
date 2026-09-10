# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        if root is None:
            return []
        def helper(root, res):
            if root.left is None and root.right is None:
                res.append(root.val)
                if sum(res) == targetSum:
                    ans.append(res.copy())
                return
            res.append(root.val)
            if root.left:
                helper(root.left, res.copy())
            if root.right:
                helper(root.right, res.copy())
        helper(root, [])
        return ans