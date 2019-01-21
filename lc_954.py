class Solution(object):
    r = False
    cnt = 0
    def canReorderDoubled(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        dic = {}
        cnt = 0
        for n in A:
            if dic.has_key(n):
                dic[n] += 1
            else:
                dic[n] = 1
        A = sorted(A)
        for n in sorted(A, key=lambda x: abs(x)):
            if dic[n] > 0:
                if n == 0:
                    if dic[n] == 1:
                        return False
                if dic.has_key(2*n) and dic[2*n] > 0:
                    dic[n] -= 1
                    dic[2*n] -= 1
                    cnt += 2
        if cnt == len(A):
            return True
        return False


    def helper(self, set, canJump):
        if len(set) <= 5:
            self.cnt += 1
        if len(set) == 0:
            return True
        res = False
        if canJump:
            res = res or self.helper(set[1:], False)
        #flag = False
        for i in range(1, len(set)):
            if set[i] == 2 * set[0]:
                res = res or self.helper(set[1:i] + set[i + 1:], canJump)
                '''
                flag = True
                if res:
                    return True
                elif self.r:
                    return False
                '''
            if set[0] % 2 == 0 and set[i] == set[0] / 2:
                res = res or self.helper(set[1:i] + set[i + 1:], canJump)

        return res





if __name__ == '__main__':
    # begin
    s = Solution()

    print s.canReorderDoubled([1,2,1,-8,8,-4,4,-4,2,-2])