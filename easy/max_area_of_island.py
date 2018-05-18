class Solution:
    area = 0
    max_area = 0

    def travel(self, grid, row, col):
        # print('row', row, 'col', col)
        grid[row][col] = 0
        self.area = self.area + 1

        # Toward to Up
        if 0 < row and grid[row-1][col] == 1:
            self.travel(grid, row-1, col)

        # Toward to Left
        if 0 < col and grid[row][col-1] == 1:
            self.travel(grid, row, col-1)

        # Toward to Down
        if row < (len(grid) - 1) and grid[row+1][col] == 1:
            self.travel(grid, row+1, col)

        # Toward to Right
        if col < (len(grid[0]) - 1) and grid[row][col+1] == 1:
            self.travel(grid, row, col+1)

        return self.area

    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                self.area = 0
                if grid[row][col] == 1:
                    a = self.travel(grid, row, col)
                    if self.max_area < a:
                        self.max_area = a
        print(self.max_area)
        return self.max_area

map = [ [0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0] ]
solution = Solution()
solution.maxAreaOfIsland(map)
