class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = str(num)
        l = []
        prev = 10
        idx_f = -1
        idx_s = -1
        for idx, c in enumerate(s):
            c = int(c)
            if c > prev:
                for i, v in enumerate(l):
                    if v < c:
                        idx_f = i
                        idx_s = idx
                        break
                break
            else:
                l.append(c)
                prev = c
        if idx_s != -1:
            str_list = list(s)
            temp = str_list[idx_s]
            str_list[idx_s] = str_list[idx_f]
            str_list[idx_f] = temp
            s = ''.join(str_list)

        return int(s)



if __name__ == '__main__':
    # begin
    s = Solution()

    print s.maximumSwap(9973)