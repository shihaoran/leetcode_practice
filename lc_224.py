class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        sum = [0]
        sign = [1]
        i = 0
        while i < len(s):
            if s[i].isdigit():
                while s[i].isdigit():
                    num *= 10
                    num += int(s[i])
                    if i < len(s) - 1:
                        i += 1
                    else:
                        break
                sum.append(sign.pop() * num + sum.pop())
                num = 0

            if s[i] == '+':
                sign.append(1)
            elif s[i] == '-':
                sign.append(-1)
            elif s[i] == '(':
                sum.append(0)
                sign.append(1)
            elif s[i] == ')':
                sum_ = sum.pop()
                sign_ = sign.pop()
                sum[-1] += sum_*sign_
            i += 1

        return sum[0]





if __name__ == '__main__':
    # begin
    s = Solution()
    print s.calculate('(1+(4+5+2)-3)+(6+8)')