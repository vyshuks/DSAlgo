"""
https://leetcode.com/problems/course-schedule-iii/
"""
import heapq

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda c: c[-1])
        heap = []
        heapq.heapify(heap)
        maxtime = 0
        for course in courses:
            time_need, last_day = course
            heapq.heappush(heap, -time_need)
            maxtime+= time_need

            if maxtime > last_day:
                max_dur = -1 * heapq.heappop(heap)
                maxtime-= max_dur

        return len(heap)


            
        
        
        