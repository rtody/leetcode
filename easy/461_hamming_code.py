class Solution:
    def hammingDistance(self, x, y):
        if x == y:
            return 0

        if max(x, y) == x:
            big_num = x
            small_num = y
        else:
            big_num = y
            small_num = x

        ham_dist = 0
        while (big_num >= 1):
            b_num_mod_two = big_num % 2
            s_num_mod_two = small_num % 2
            if b_num_mod_two != s_num_mod_two:
                ham_dist = ham_dist + 1
            big_num = (big_num - b_num_mod_two) / 2
            small_num = (small_num - s_num_mod_two) / 2

        print(x, y, ham_dist)
        return ham_dist

solution = Solution()
solution.hammingDistance(10, 4)
