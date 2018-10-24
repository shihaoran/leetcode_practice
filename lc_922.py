class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        list_e = []
        list_o = []
        res = []
        for i in A:
            if i % 2 == 1:
                list_o.append(i)
            else:
                list_e.append(i)
        for i in range(len(A)):
            if i % 2 == 0:
                res.append(list_e[i/2])
            else:
                res.append(list_o[i / 2])
        return res



if __name__ == '__main__':
    # begin
    s = Solution()

    print s.sortArrayByParityII([4,2,5,7])