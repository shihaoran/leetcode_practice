# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        flagS = False
        flagE = False
        res = []
        if len(intervals) == 0:
            return [newInterval]
        if newInterval.end < intervals[0].start:
            res.append(newInterval)
            flagS = True
            flagE = True
        for i in intervals:
            if flagS == False:
                if i.end >= newInterval.start and i.start <= newInterval.end:
                    flagS = True
                    endTime = max(i.end, newInterval.end)
                    startTime = min(i.start, newInterval.start)
                    res.append(Interval(startTime, endTime))
                else:
                    res.append(i)
            elif flagE == False:
                if newInterval.end < i.start:
                    flagE = True
                    res.append(i)
                else:
                    res[-1].end = max(res[-1].end, i.end)
            else:
                res.append(i)
        if flagS == False:
            res.append(newInterval)
        return sorted(res, key=lambda x: x.start)




if __name__ == '__main__':
    # begin
    s = Solution()
    test = [Interval(1,5), Interval(6,9)]
    print s.insert(test, Interval(0,3))