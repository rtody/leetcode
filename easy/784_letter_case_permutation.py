import itertools

class Solution():
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        lst_of_tup = list()
        lst_of_str = list()
        for c in S:
            if c.isdigit():
                lst_of_tup.append(c)
            else:
                lst_of_tup.append((c.lower(), c.upper()))
        # print(lst_of_tup)

        # Use cartesian product to create the permutation list 
        for x in itertools.product(*lst_of_tup):
            # print(''.join(x))
            lst_of_str.append(''.join(x))
        # print(lst_of_str)

        return lst_of_str

a = "a1b2c3"
solution = Solution()
solution.letterCasePermutation(a)
