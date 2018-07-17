class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        tank = 0
        total = 0
        start = 0
        for i in range(len(gas)):
            tank = tank + gas[i] - cost[i]
            if tank < 0:
                total += tank
                tank = 0
                start = i + 1

        if tank + total < 0:
            return -1
        return start


if __name__ == '__main__':
    # begin
    s = Solution()
    print s.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2])