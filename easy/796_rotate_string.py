class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if A == B:
            print('True')
            return True

        len_A = len(A)
        while(len_A):
            # print('len', len_A)
            # print('A', A)
            A = A[1:] + A[0]
            len_A = len_A - 1
            # print('len', len_A)
            # print('A', A)
            if A == B:
                print('True')
                return True
        print('False')
        return False

solution = Solution()
solution.rotateString('abcde', 'cdeab')
