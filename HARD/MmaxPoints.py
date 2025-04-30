'''
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

 

Example 1:


Input: points = [[1,1],[2,2],[3,3]]
Output: 3
Example 2:


Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
 

Constraints:

1 <= points.length <= 300
points[i].length == 2
-104 <= xi, yi <= 104
All the points are unique.

'''

from collections import defaultdict

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        if n <= 2:
            return n

        ans = 0
        # iterate over each point as anchor
        for i in range(n):
            slopes = defaultdict(int)
            duplicates = 1  # count the anchor itself
            local_max = 0
            x1, y1 = points[i]

            # compare with every other point
            for j in range(i+1, n):
                x2, y2 = points[j]
                dx = x2 - x1
                dy = y2 - y1

                if dx == 0 and dy == 0:
                    # same point
                    duplicates += 1
                else:
                    # reduce slope to simplest form
                    g = self._gcd(dx, dy)
                    dx //= g
                    dy //= g
                    # ensure unique representation for slope direction
                    if dx < 0:
                        dx, dy = -dx, -dy
                    elif dx == 0:
                        dy = 1
                    elif dy == 0:
                        dx = 1

                    slopes[(dx, dy)] += 1
                    local_max = max(local_max, slopes[(dx, dy)])

            # update global max: points on a line through anchor = local_max + duplicates
            ans = max(ans, local_max + duplicates)

        return ans

    def _gcd(self, a, b):
        # helper to compute greatest common divisor
        while b:
            a, b = b, a % b
        return abs(a)