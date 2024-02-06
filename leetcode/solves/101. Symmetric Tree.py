# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pairIsSym(self, l_root: Optional[TreeNode], r_root: Optional[TreeNode]) -> bool:
        if l_root is None and r_root is not None:
            return False
        
        if l_root is not None and r_root is None:
            return False
        
        if l_root is None and r_root is None:
            return True

        if l_root.val != r_root.val:
            return False
        
        return self.pairIsSym(l_root.left, r_root.right) \
            and self.pairIsSym(l_root.right, r_root.left)
        

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        return self.pairIsSym(root.left, root.right)