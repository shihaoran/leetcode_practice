class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        l = 0
        sum = 0
        for i in S:
            if i == ')':
                if l == 0:
                    sum += 1
                else:
                    l -= 1
            else:
                l += 1
        return sum + l



if __name__ == '__main__':
    # begin
    s = Solution()

    print s.minAddToMakeValid("()))(()()())))))((")