class Solution(object):
    def threeSumMulti(self, A, target):
        """
        :type A: List[int]
        :type target: int
        :rtype: int
        """
        res = 0
        A = sorted(A)
        for i in range(len(A)-2):
            if A[i] + A[i+1] + A[i+2] > target:
                break
            sum = target - A[i]
            l = i+1
            r = len(A)-1
            while l < r:
                if A[l] + A[r] < sum:
                    n = l + 1
                    while n < len(A) and A[n] == A[l]:
                        n += 1
                    l = n
                elif A[l] + A[r] == sum:
                    if A[l] == A[r]:
                        res += (r-l)*(r-l+1)/2
                        t = l
                        l = r
                        r = t
                    else:
                        ln = 1
                        rn = 1
                        while l+ln < len(A) and A[l + ln] == A[l]:
                            ln += 1
                        while A[r - rn] == A[r]:
                            rn += 1
                        res += ln * rn
                        l += ln
                        r -= rn
                else:
                    n = r - 1
                    while n > i+1 and A[n] == A[r]:
                        n -= 1
                    r = n
        return res % 1000000007



if __name__ == '__main__':
    # begin
    s = Solution()

    print s.threeSumMulti([2,2,3,2], 7)