# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        node_list = []
        self.inorder_helper(root, node_list)
        return node_list
    
    def inorder_helper(self, root: Optional[TreeNode], node):
        if not root:
            return
        self.inorder_helper(root.left, node)
        node.append(root.val)
        self.inorder_helper(root.right, node)
    
        
        
        
        
