# minimum time visiting all points

"""
On a 2D plane, there are n points with integer coordinates points[i] = [xi, yi] 

Return the minimum time in seconds to visit all the points in the order given by points.

Rules:
    - in 1 second you can either
        - move vertically by one unit
        - move horizontally by one unit, or 
        - move diagonally (sqrt(2)) by one unit 
    - you have to visit the points in the same order as they appear in the array    
    - you are allowed to apss through points that appear later in theorder, but these do not count as visits

Input:  points = [[1,1] , [3,4], [-1,0]]
Output: 7

Explanation: one optimal path is [1,1] -> [2,2] -> [3,3]
"""

# SOLUTION 1
def solution1(coordinates):
    time = 0
    for i in range(0, len(coordinates)-1):
        x,y = coordinates[i] 
        x_next, y_next = coordinates[i+1]
        max_diff = max(abs(x - x_next), abs(y - y_next))
        time += max_diff
    return time

points = [[1,1], [3,4], [-1,0]]
print(solution1(points))