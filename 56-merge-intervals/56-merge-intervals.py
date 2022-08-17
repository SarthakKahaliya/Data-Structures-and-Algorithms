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
        
#         i = 1
#         while i < len(intervals):
#             currInterval = intervals[i]
#             lastInterval = intervals[i-1]
#             if lastInterval[last] >= currInterval[start]:
#                 intervals[i] = [lastInterval[start], max(lastInterval[last], currInterval[last])]
#                 intervals.pop(i-1)
#             else:
#                 i += 1
                
#         return intervals