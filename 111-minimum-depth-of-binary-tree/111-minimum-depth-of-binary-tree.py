# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        
        if not root:
            return 0
        
        self.min_depth = float("inf")
        
        def dfs(root, depth):
            if not root:
                return
                
            if not root.left and not root.right:
                self.min_depth = min(self.min_depth, depth)
            else:
                if root.left:
                    dfs(root.left, depth+1)
                if root.right:
                    dfs(root.right, depth+1)
                
        dfs(root, 1)
        
        return self.min_depth