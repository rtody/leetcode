class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        #print(A)
        flp_inv_matrix = list()
        for row in range(0, len(A)):
            flip_list = list()
            inverse_list = list()
            for idx in range(0, len(A[row])):
                flip_list.append(A[row][len(A[row]) - 1 - idx])
                inverse_list.append(1 - flip_list[idx])
            flp_inv_matrix.append(inverse_list)
        print(flp_inv_matrix)
        return flp_inv_matrix

solution = Solution()
solution.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]])
