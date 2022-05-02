# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.BST(root, -float('inf'), float('inf'))
        
    def BST(self, root: Optional[TreeNode], minVal, maxVal):
        if not root:
            return True
        
        if root.val > minVal and root.val < maxVal:
            left = self.BST(root.left, minVal, root.val)
            right = self.BST(root.right, root.val, maxVal)
            
            return left and right
