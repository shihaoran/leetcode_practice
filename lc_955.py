class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        res = 0
        pre = [0] * (len(A) -1)
        for i in range(len(A[0])):
            preTemp = pre[:]
            for j in range(len(A)-1):
                if A[j][i] > A[j+1][i] and pre[j] == 0:
                    res += 1
                    break
                preTemp[j] |= A[j][i] < A[j+1][i]
            else:
                pre = preTemp
        return res





if __name__ == '__main__':
    # begin
    s = Solution()

    print s.minDeletionSize(["xc","yb","za"])