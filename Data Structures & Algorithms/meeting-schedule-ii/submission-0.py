"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals]) 
        end = sorted([i.end for i in intervals]) 

        globalMax = 0 
        count = 0 
        s = 0 
        e = 0 
        i = 0 

        while s < len(intervals): 
            if start[s] < end[e]: 
                count += 1
                s += 1 
            else: 
                count -= 1 
                e += 1 
            
            globalMax = max(count, globalMax) 

        return globalMax
        