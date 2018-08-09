class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = str(n)
        if len(s) <= 1:
            return -1
        pre = s[-1]
        l = [pre]
        for i in range(len(s)-2, -1, -1):
            cur = s[i]
            l.append(cur)
            if int(cur) < int(pre):
                l.sort()
                idx = l.index(cur)
                for j in range(idx, len(l)):
                    if int(l[j]) > int(cur):
                        temp = l[j]
                        del l[j]
                        l.insert(0, temp)
                        r = int(s[0:i] + ''.join(l))
                        if r < 2**31:
                            return r
                        return -1
            else:
                pre = cur
        return -1



if __name__ == '__main__':
    # begin
    s = Solution()
    print s.nextGreaterElement(2147483647)