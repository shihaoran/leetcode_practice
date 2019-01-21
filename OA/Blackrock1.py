class Solution(object):
    num = [100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.1, 0.05, 0.01]
    name = ['ONE HUNDRED', 'FIFTY', 'TWENTY', 'TEN', 'FIVE', 'TWO', 'ONE', 'HALF DOLLAR', 'QUARTER', 'DIME', 'NICKEL',
            'PENNY']

    def b1(self, line):
        res = []
        p, c = line.split(';')
        p = float(p)
        c = float(c)
        if c < p:
            print 'ERROR'
        elif c == p:
            print 'ZERO'
        else:
            i = 0
            v = c - p
            while i < len(self.num):
                if v < self.num[i]:
                    i += 1
                else:
                    res.append(self.name[i])
                    v -= self.num[i]
        sorted(res)
        res = ','.join(res)
        return res





if __name__ == '__main__':
    # begin
    s = Solution()
    print s.b1('0.07;0.1')