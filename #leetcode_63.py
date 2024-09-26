# 63. Unique Paths II

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        return self.grid_2(obstacleGrid, m, n, 0, 0, 0, {})

    def grid_2(self, obstacleGrid, m, n, k, l, count, hashmap):
        if k >= m or l >= n:
            return 0
        if obstacleGrid[k][l] == 1:
            hashmap[str(k) + "," + str(l)] = 0
            return 0
        if str(k) + "," + str(l) in hashmap:
            return hashmap[str(k) + "," + str(l)]
        
        if k == m - 1 and l == n - 1:
            return 1
        
        res_1 = self.grid_2(obstacleGrid, m, n, k + 1, l, count, hashmap)
        hashmap[str(k + 1) + "," + str(l)] = res_1
        res_2 = self.grid_2(obstacleGrid, m, n, k, l + 1, count, hashmap)
        hashmap[str(k) + "," + str(l + 1)] = res_2
        count += (res_1 + res_2)
        return count
