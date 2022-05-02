# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        node_list = []
        self.postorder_helper(root, node_list)
        return node_list
    
    def postorder_helper(self, root: Optional[TreeNode], node):
        if not root:
            return
        self.postorder_helper(root.left, node)
        self.postorder_helper(root.right, node)
        
        node.append(root.val)
        
