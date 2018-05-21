# Definition for a binary tree node.
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) > 0:
            # Select middle position, round up if having even numbers
            mid_pos = len(nums) // 2
            root = TreeNode(nums[mid_pos])

            # have left sub-tree if nodes more than 1
            if len(nums) > 1:
                root.left = self.sortedArrayToBST(nums[:mid_pos])
            # have right sub-tree if nodes more than 2
            if len(nums) > 2:
                root.right = self.sortedArrayToBST(nums[mid_pos+1:])
            # print(root.val, root.left, root.right)
            return root

solution = Solution()
solution.sortedArrayToBST([-10,-3,-1,0,5,9])
