# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        left=root
        right=root
        lh=0
        rh=0
        while left :
            lh +=1
            left=left.left
        while right:
            rh=rh+1
            right=right.right
        if lh==rh:
            return (2**lh)-1
        return 1+self.countNodes(root.left)+self.countNodes(root.right)
        