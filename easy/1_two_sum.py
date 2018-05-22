class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for n1 in range(len(nums) - 1):
            if (target - nums[n1]) in nums[n1 + 1:]:
                # Second number starts from n1 + 1
                n2 = nums[n1 + 1:].index(target - nums[n1]) + n1 + 1
                # print(n1, n2)
                return [n1, n2]

solution = Solution()
solution.twoSum([2, 7, 11, 15], 9)
