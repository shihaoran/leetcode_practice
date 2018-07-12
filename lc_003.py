class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        c_list = [-1] * 255
        _len = 0
        max_len = 0
        i = 0
        for c in s:
            if c_list[ord(c)] > -1:
                index = c_list[ord(c)]
                for j in range(len(c_list)):
                    if c_list[j] <= index and c_list[j] > -1:
                        c_list[j] = -1
                        _len = _len - 1

            c_list[ord(c)] = i
            _len = _len + 1
            if _len > max_len:
                max_len = _len
            i = i + 1

        return max_len

if __name__ == '__main__':
    # begin
    s = Solution()
    print s.lengthOfLongestSubstring('vqblqcb')