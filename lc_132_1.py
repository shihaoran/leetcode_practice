class Solution(object):
    dic = {}
    num = 0

    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.dic = {}
        a = self._minCut(s)
        return a


    def _minCut(self, s):
        self.num += 1
        if self.num % 1000000 == 0:
            print self.num
        if self.dic.has_key(s):
            return self.dic[s]
        if len(s) == 1:
            self.dic[s] = 0
            return 0
        f = True
        for i in range(len(s)/2):
            if s[i] != s[-i-1]:
                f = False
        if f:
            self.dic[s] = 0
            return 0
        _min = len(s)
        for i in range(1, len(s)):
            _min = min(_min, self._minCut(s[:i])+self._minCut(s[i:])+1)
        self.dic[s] = _min
        return _min

if __name__ == '__main__':
    # begin
    s = Solution()
    print s.minCut("apjesgpsxoeiokmqmfgvjslcjukbqxpsobyhjpbgdfruqdkeiszrlmtwgfxyfostpqczidfljwfbbrflkgdvtytbgqalguewnhvvmcgxboycffopmtmhtfizxkmeftcucxpobxmelmjtuzigsxnncxpaibgpuijwhankxbplpyejxmrrjgeoevqozwdtgospohznkoyzocjlracchjqnggbfeebmuvbicbvmpuleywrpzwsihivnrwtxcukwplgtobhgxukwrdlszfaiqxwjvrgxnsveedxseeyeykarqnjrtlaliyudpacctzizcftjlunlgnfwcqqxcqikocqffsjyurzwysfjmswvhbrmshjuzsgpwyubtfbnwajuvrfhlccvfwhxfqthkcwhatktymgxostjlztwdxritygbrbibdgkezvzajizxasjnrcjwzdfvdnwwqeyumkamhzoqhnqjfzwzbixclcxqrtniznemxeahfozp")