import itertools

class Solution:
    def largestTriangleArea(self, points):
        '''
        :type points: List[List[int]]
        :rtype: float
        '''
        max_area = None

        def area(p, q, r):
            # Shoelace algorithm
            rect_area = 1/2 * abs(p[0] * q[1] + q[0] * r[1] + r[0] * p[1]
                                - p[1] * q[0] - q[1] * r[0] - r[1] * p[0])
            return rect_area

        for tri_pts in itertools.combinations(points, 3):
            # print(*tri_pts)
            tri_area = area(*tri_pts)
            if max_area is None or max_area < tri_area:
                max_tri_pts = tri_pts
                max_area = tri_area

        print(max_tri_pts, max_area)
        return max_area

points = [[2,5],[7,7],[10,8],[10,10],[1,1]]
solution = Solution()
solution.largestTriangleArea(points)
