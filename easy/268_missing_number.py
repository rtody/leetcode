class Solution:
    def missingNumber(self, num):
        """
        :type nums: List[int]
        :rtype: int
        """
        complete_num = list(range(len(num) + 1))
        missnum = sum(complete_num) - sum(num)
        print(missnum)
        return missnum

solution = Solution()
solution.missingNumber([0])
