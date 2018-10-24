class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """

        for j in range(len(A)):
            list = []
            row = A[j]
            for i in range(len(row) - 1, -1, -1):
                list.append(1 - row[i])
            A[j] = list
        return A

if __name__ == '__main__':
    # begin
    s = Solution()

    print s.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]])