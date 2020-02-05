from typing import List


# not in-place， O（m * n）
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
        firstRowHasZero = not all(A[0])
        for i in range(1, m):
            for j in range(n):
                if A[i][j] == 0:
                    A[i][0] = 0
                    A[0][j] = 0
        print(A)
        # set rows
        for i in range(1, m):
            if A[i][0] == 0:
                A[i] = [0] * n
        # set cols
        for j in range(n):
            if A[0][j] == 0:
                for i in range(m):
                    A[i][j] = 0
        if firstRowHasZero:
            A[0] = [0] * n





if __name__ == "__main__":

    nums = \
        [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    sol = Solution()
    sol.setZeroes(nums)
    print(nums)