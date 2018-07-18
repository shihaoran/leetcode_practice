class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        len_s = len(s)
        return_list = []
        if len_s > 12 or len_s < 4:
            return []

        for i in range(1, len_s - 2):
            for j in range(i + 1, len_s - 1):
                for k in range(j + 1, len_s):
                    f = True
                    list_a = []
                    list_a.append(s[0:i])
                    list_a.append(s[i:j])
                    list_a.append(s[j:k])
                    list_a.append(s[k:])

                    for a in list_a:
                        if not self.check(a):
                            f = False
                            break
                    if f:
                        return_list.append('.'.join(list_a))

        return return_list

    def check(self, a):
        if len(a) > 3 or len(a) < 1:
            return False
        if len(a) > 1 and a[0] == '0':
            return False
        if int(a) > 255:
            return False
        return True


if __name__ == '__main__':
    # begin
    s = Solution()
    print s.restoreIpAddresses("25525511135")