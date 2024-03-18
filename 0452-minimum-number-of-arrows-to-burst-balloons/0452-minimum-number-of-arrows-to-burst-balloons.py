class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda x: x[1])
        a = 1
        e = points[0][1]
    
        for i in points[1:]:
            if i[0] > e:
                a += 1
                e = i[1]
    
        return a

