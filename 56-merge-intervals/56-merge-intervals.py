class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        newIntervals = [intervals[0]]
        start = 0
        last = -1
        
        for i in range(1, len(intervals)):
            interval = intervals[i]
            lastNewInterval = newIntervals[last]
            if lastNewInterval[last] >= interval[start]:
                newIntervals[last] = [lastNewInterval[start],max(lastNewInterval[last], interval[last])]
            else:
                newIntervals.append(interval)
                
        return newIntervals