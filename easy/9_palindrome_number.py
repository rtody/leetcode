class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
            return False

        lst = list()
        while (x):
            rmdr = x % 10
            x = x // 10
            lst.append(rmdr)

        lst_rev = list(lst)
        lst_rev.reverse()
        # print(lst, lst_rev)
        if lst == lst_rev:
            # print('True')
            return True
        else:
            # print('False')
            return False

solution = Solution()
solution.isPalindrome(10)
