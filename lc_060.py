class Solution(object):
    count = 0
    res = ''
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        pos = []
        set = [i for i in range(1, n+1)]
        res = ''
        i = 1
        k -= 1
        while i <= n:
            pos.insert(0, k % i)
            k /= i
            i += 1
        for index in pos:
            res += str(set[index])
            set = set[:index] + set[index+1:]
        return res


class Solution1(object):
    count = 0
    res = ''
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        set = []
        for i in range(1, n+1):
            set.append(i)
        self.helper('', set, k)
        return self.res

    def helper(self, step, set, k):
        if len(set) == 0 or self.count >= k:
            self.count += 1
            if self.count == k:
                self.res = step[:]
            return
        for i in range(len(set)):
            self.helper(step+str(set[i]), set[:i]+set[i+1:], k)
            if self.count >= k:
                return




if __name__ == '__main__':
    # begin
    s = Solution()
    print s.getPermutation(3, 3)