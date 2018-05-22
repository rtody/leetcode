# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        longest = [0]
        def dfs(root):
            if not root:
                return 0

            # Find the longest connected length of both sides
            left_len, right_len = dfs(root.left), dfs(root.right)

            # If root connects with either side, then one side's length will
            # be counted as following
            left = right = 0
            if root.left and root.left.val == root.val:
                left = left_len + 1
            if root.right and root.right.val == root.val:
                right = right_len + 1
            # The longest path for each node is the sum of longest left and right
            longest[0] = max(longest[0], left + right)
            # Return longest side to the parent node
            return max(left, right)

        dfs(root)
        print(longest[0])
        return longest[0]

"""
    F           5
   / \         / \
  C   E       4   5
 / \   \     / \   \
A   B   D   1   1   5
"""

A = TreeNode(1)
B = TreeNode(1)
C = TreeNode(4)
C.left, C.right = A, B
D = TreeNode(5)
E = TreeNode(5)
E.right = D
F = TreeNode(5)
F.left, F.right = C, E

solution = Solution()
solution.longestUnivaluePath(F)
