class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.len = len(nums)

        nums.sort()
        # [...,-102, -99, -54, ..., 0]
        if max(nums) == 0:
            maxProd = 0
            # print(maxProd)
            return maxProd

        # [0, 3, ..., 129] or [...,-113, -95, -44, ..., -2]
        if nums[0] >= 0 or nums[self.len - 1] < 0:
            maxProd = nums[self.len - 1] * nums[self.len - 2] * nums[self.len - 3]
            # print(maxProd)
            return maxProd

        # have only one negetive number
        if nums[0] < 0 and nums[1] >= 0:
            maxProd = nums[self.len - 1] * nums[self.len - 2] * nums[self.len - 3]
            # print(maxProd)
            return maxProd

        # have more than one negetive number
        #   strategy one - takes two negetive number and one max number
        maxProd_p1 = nums[0] * nums[1] * nums[self.len - 1]
        #   strategy two - takes biggest three numbers
        maxProd_p2 = nums[self.len - 1] * nums[self.len - 2] * nums[self.len - 3]
        maxProd = max(maxProd_p1, maxProd_p2)
        # print(maxProd)
        return maxProd

solution = Solution()
solution.maximumProduct([-1000,-1000,1000])
