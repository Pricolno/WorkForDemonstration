# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, 
        root: Optional[TreeNode],
        l_bound: Optional[int] = None,
        r_bound: Optional[int] = None
    ) -> bool:
        if root is None:
            return True
        if l_bound is not None and l_bound > root.val:
            return False
        if r_bound is not None and r_bound < root.val:
            return False

        left_isValid = self.isValidBST(
            root.left,
            l_bound,
            min(r_bound, root.val - 1) if r_bound is not None else root.val - 1
        )
        right_isValid = self.isValidBST(
            root.right,
            max(l_bound, root.val + 1) if l_bound is not None else root.val + 1,
            r_bound
        )

        if not left_isValid or not right_isValid:
            return False
        if root.left is not None and root.left.val >= root.val:
            return False
        
        if root.right is not None and root.right.val <= root.val:
            return False

        return True
