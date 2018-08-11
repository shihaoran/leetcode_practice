class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        l = []
        for c in tokens:
            if c == '+':
                x = l.pop()
                y = l.pop()
                l.append(x+y)
            elif c == '-':
                y = l.pop()
                x = l.pop()
                l.append(x-y)
            elif c == '*':
                x = l.pop()
                y = l.pop()
                l.append(x*y)
            elif c == '/':
                y = l.pop()
                x = l.pop()
                l.append(int(float(x)/y))
            else:
                l.append(int(c))
        return l[-1]

if __name__ == '__main__':
    # begin
    s = Solution()
    print s.evalRPN(["4","3","-"])