class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        l = []
        for a in asteroids:
            if a > 0 or len(l) == 0:
                l.append(a)
            else:
                while len(l) > 0 and l[-1] > 0:
                    if l[-1] == abs(a):
                        l.pop()
                        break
                    if l[-1] > abs(a):
                        break
                    if l[-1] < abs(a):
                        l.pop()
                        continue
                else:
                    l.append(a)
        return l



if __name__ == '__main__':
    # begin
    s = Solution()

    print s.asteroidCollision([-2, -1, 1, 2])