# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root :
            return []
        queue=deque([root])
        res=[]
        l_r=True
        while queue:
            level=[]
            for i in range(len(queue)):
                node=queue.popleft()
                level.append(node.val)
                if node.left :
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if not l_r:
                level.reverse()
            res.append(level)
            l_r=not l_r
        return res
        