from typing import List


class Solution:
    def minPathSum(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])

        for i in range(1, m):
            A[i][0] += A[i-1][0]
        for j in range(1, n):
            A[0][j] += A[0][j-1]
        for i in range(1, m):
            for j in range(1, n):
                A[i][j] += min(A[i-1][j], A[i][j-1])
        return A[-1][-1]


if __name__ == "__main__":

    A = \
        [
            [1, 3, 1],
            [1, 5, 1],
            [4, 2, 1]
        ]



    sol = Solution()
    res = sol.minPathSum(A)
    print(res)