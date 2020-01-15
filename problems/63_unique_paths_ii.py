from typing import List

# O(m * n), tail to head
class Solution:
    def uniquePathsWithObstacles(self, A: List[List[int]]) -> int:

        m, n = len(A), len(A[0])
        dp = [[1 for _ in range(n)] for _ in range(m)]
        if A[m - 1][n - 1] == 1: return 0
        for i in range(m - 2, -1, -1):
            if A[i][n - 1] == 1:
                dp[i][n - 1] = 0
            else:
                dp[i][n - 1] = min(dp[i][n - 1], dp[i + 1][n - 1])
        for i in range(n - 2, -1, -1):
            if A[m - 1][i] == 1:
                dp[m - 1][i] = 0
            else:
                dp[m - 1][i] = min(dp[m - 1][i], dp[m - 1][i + 1])

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if A[i][j] == 1:
                    dp[i][j] = 0
                elif i + 1 < m and j + 1 < n:
                    dp[i][j] = dp[i + 1][j] + dp[i][j + 1]

        return dp[0][0]

# O(m * n), head to tail
class Solution:
    def uniquePathsWithObstacles(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        dp = [[1 for _ in range(n)] for _ in range(m)]

        # starting point
        dp[0][0] = 1 - A[0][0]

        # first column
        for i in range(1, m):
            if A[i][0] == 1:
                dp[i][0] = 0
            else:
                dp[i][0] = min(dp[i - 1][0], 1)

        # first row
        for i in range(1, n):
            if A[0][i] == 1:
                dp[0][i] = 0
            else:
                dp[0][i] = min(dp[0][i - 1], 1)

        for i in range(1, m):
            for j in range(1, n):
                if A[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        print(dp)
        return dp[-1][-1]

# O(n) space
class Solution:
    def uniquePathsWithObstacles(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        dp = [1 for _ in range(n)]
        dp[0] = 1 - A[0][0]
        for i in range(1, n):
            dp[i] = dp[i - 1] * (1 - A[0][i])
        for i in range(1, m):
            dp[0] *= 1 - A[i][0]
            for j in range(1, n):
                dp[j] = (dp[j] + dp[j - 1]) * (1 - A[i][j])

        return dp[-1]

if __name__ == "__main__":

    A = \
        [
            [0]
        ]



    sol = Solution()
    res = sol.uniquePathsWithObstacles(A)
    print(res)
