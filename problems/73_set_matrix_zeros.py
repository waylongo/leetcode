from typing import List


# not in-place
class Solution:
    def setZeroes(self, A: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(A), len(A[0])
        row, col = [], []
        for i in range(m):
            for j in range(n):
                if A[i][j] == 0:
                    row.append(i)
                    col.append(j)
        for i in range(m):
            for j in range(n):
                if i in row or j in col:
                    A[i][j] = 0

class Solution:
    def setZeroes(self, A: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(A), len(A[0])

if __name__ == "__main__":

    nums = \
        [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ]
    sol = Solution()
    sol.setZeroes(nums)
    print(nums)