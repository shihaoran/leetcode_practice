class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        maxLen = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if len(stack) > 0:
                    if s[stack[-1]] == '(':
                        stack = stack[:-1]
                    else:
                        stack.append(i)
                else:
                    stack.append(i)
        if len(stack) == 0:
            return len(s)
        else:
            r = len(s)
            while len(stack) > 0:
                l = stack[-1]
                stack = stack[:-1]
                maxLen = max(maxLen, r-l-1)
                r = l

            return max(maxLen, r-0)


if __name__ == '__main__':
    # begin
    s = Solution()
    print s.longestValidParentheses(")(((((()())()()))()(()))(")