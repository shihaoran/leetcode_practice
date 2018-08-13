class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        stack = []
        r = [0]*n
        prev = 0
        for l in logs:
            t = l.split(':')
            num = int(t[0])
            time = int(t[2])
            if len(stack) != 0:
                r[stack[-1]] += time - prev
            prev = time
            if t[1] == 'start':
                stack.append(num)
            else:
                r[stack.pop()] += 1
                prev += 1
        return r


if __name__ == '__main__':
    # begin
    s = Solution()

    print s.exclusiveTime(1, ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"])