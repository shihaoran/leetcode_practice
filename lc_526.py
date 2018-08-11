class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        self.cache = {}
        return self.helper(tuple(range(1, N+1)))

    def helper(self, x):
        count = 0
        if len(x) == 1:
            return 1
        if self.cache.has_key(x):
            return self.cache[x]

        for i in range(len(x)):
            if len(x) % x[i] == 0 or x[i] % len(x) == 0:
                count += self.helper(x[:i]+x[i+1:])
        self.cache[x] = count
        return count


if __name__ == '__main__':
    # begin
    s = Solution()
    print s.countArrangement(3)