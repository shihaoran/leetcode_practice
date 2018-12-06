class Solution(object):
    def pressAForCapsLock(self, message):
        """
        :type s: str
        :rtype: int
        """
        capsStatus = False
        res = ''
        for c in message:
            if c == 'a' or c == 'A':
                capsStatus = not capsStatus
            else:
                if c >= 'a' and c <= 'z' and capsStatus:
                    res += chr(ord(c) + ord('A') - ord('a'))
                elif c >= 'A' and c <= 'Z' and capsStatus:
                    res += chr(ord(c) + ord('a') - ord('A'))
                else:
                    res += c
        return res





if __name__ == '__main__':
    # begin
    s = Solution()
    print s.pressAForCapsLock("\"Baa,Baa?\" said the sheep")