# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque([root])

        max_sum = float('-inf')
        max_level = 1
        level_num = 0

        while q:
            level = []
            level_num += 1

            for i in range(len(q)):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            cur = sum(level)

            if cur > max_sum:
                max_sum = cur
                max_level = level_num

        return max_level