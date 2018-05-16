class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jewels_list = list()
        sum_jewels = 0

        for jewel in range(0, len(J)):
            # print(jewel)
            jewels_list.append(J[jewel])
        print(jewels_list)

        for stone in range(0, len(S)):
            print(S[stone])
            if S[stone] in jewels_list:
                sum_jewels = sum_jewels + 1

        return sum_jewels

J = "aA"
S = "aAAbbbb"
solution = Solution()
jew_in_st = solution.numJewelsInStones(J, S)

print('Jewels in stone', jew_in_st)
