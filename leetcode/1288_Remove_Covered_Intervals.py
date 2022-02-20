class Solution:
    def removeCoveredIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x:(x[0], -x[1]))
        prevY, remove = -1, 0
        for nxtX, nxtY in intervals:
            if nxtY <= prevY:
                remove += 1
            else:
                prevY = nxtY

        return len(intervals) - remove
