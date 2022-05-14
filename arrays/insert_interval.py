class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start = newInterval[0]
        end = newInterval[1]
        res = []
        
        for i in range(len(intervals)):
            current_start = intervals[i][0]
            current_end = intervals[i][1]
            if current_end < start:
                res.append(intervals[i])
            elif current_start > end:
                res.append([start, end])
                start = current_start
                end = current_end
            else:
                start = min(start, current_start)
                end = max(end, current_end)
        res.append([start, end])
        return res
            
