class Solution(object):
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        list = []
        list1 = []
        res = 0
        for i in range(len(A)):
            if A[i] == 1:
                list.append(i)
        if len(list) < S:
            return 0
        if S == 0:
            zero = 0
            for i in A:
                if i == 0:
                    zero += 1
                else:
                    list1.append(zero)
                    zero = 0
            if zero > 0:
                list1.append(zero)
            for i in list1:
                res += i*(i+1)/2
            return res

        for i in range(len(list)-S+1):
            l = 0
            r = 0
            if i == 0:
                l = list[0] - 0
            else:
                l = list[i] - list[i-1] - 1
            if i == len(list)-S:
                r = len(A)-list[-1]-1
            else:
                r = list[i+S] - list[i+S-1] - 1
            res += (l+1)*(r+1)
        return res




if __name__ == '__main__':
    # begin
    s = Solution()

    print s.numSubarraysWithSum([0,0,0,0], 0)