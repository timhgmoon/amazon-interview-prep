# taken off leetcode from user felixmorales95 for studying purposes(NOT MY WORK)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if not root.left and not root.right:
            return True
        
        depth_left = 0
        depth_right = 0
        
        if root.left:
            depth_left = self.get_depth(root.left, 1)

        if root.right:
            depth_right = self.get_depth(root.right, 1)
        
        print(depth_left)
        print(depth_right)
        if depth_left > depth_right + 1:
            return False

        if depth_left < depth_right - 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def get_depth(self, node: Optional[TreeNode], current_depth: int):
        if not node.left and not node.right:
            return current_depth
        else:
            left_depth = 0
            right_depth = 0
            if node.left:
                left_depth = self.get_depth(node.left, current_depth+1)
            if node.right:
                right_depth = self.get_depth(node.right, current_depth+1)
            return max(left_depth, right_depth)
        
