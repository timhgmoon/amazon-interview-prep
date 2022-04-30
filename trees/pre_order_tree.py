# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        nodes = []
        self.preorder(root, nodes)
        return nodes
        
    def preorder(self, root:Optional[TreeNode], nodes):
        if not root:
            return
        
        nodes.append(root.val)
        self.preorder(root.left, nodes)
        self.preorder(root.right, nodes)
