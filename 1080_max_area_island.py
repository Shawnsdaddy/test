from typing import (
    List,
)

class Solution:
    """
    @param grid: a 2D array
    @return: the maximum area of an island in the given 2D array
    """
    checked = []
    count = 0
    def max_area_of_island(self, grid: List[List[int]]) -> int:
        # Write your code here
        max_area =0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                max_area = max(self.dfs_get_area(i,j,grid),max_area)
        return max_area

    def dfs_get_area(self, i,j,grid):
        area = 0
        if i<0 or j<0:
            return area
        if i>=len(grid) or j>=len(grid[0]):
            return 0
        if (i,j) in self.checked:
            return 0
        if grid[i][j] == 0:
            return 0
        else:
            area = 1
            self.count+=1;
            print(self.count)
            if(i,j) not in self.checked:
                self.checked.append((i,j))
            left = self.dfs_get_area(i-1,j,grid)
            right = self.dfs_get_area(i +1, j, grid)
            up = self.dfs_get_area(i, j+1, grid)
            down = self.dfs_get_area(i , j-1, grid)
            return area+left+right+up+down