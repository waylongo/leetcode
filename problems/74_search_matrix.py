from typing import List


class Solution:
    def searchMatrix(self, A: List[List[int]], target: int) -> bool:
        if not A: return False
        m, n = len(A), len(A[0])
        for i in range(m):
            for j in range(n):
                if A[i][j] == target:
                    return True
        return False

# start from top right
class Solution:
    def searchMatrix(self, A: List[List[int]], target: int) -> bool:
        if not A:
            return False

        row, col = len(A) - 1, 0

        while row >= 0 and col < len(A[0]):
            if A[row][col] == target:
                return True
            elif A[row][col] < target:
                col += 1
            elif A[row][col] > target:
                row -= 1

        return False

class Solution:
    def searchMatrix(self, A: List[List[int]], target: int) -> bool:
        if not A:
            return False
        m, n = len(A), len(A[0])
        low, high = 0, m * n - 1
        while low <= high:
            mid = (low + high) // 2
            val = A[mid // n][mid % n]
            print(low, high, val)
            if val == target:
                return True
            elif val < target:
                low = mid + 1
            elif val > target:
                high = mid - 1

        return False

if __name__ == "__main__":

    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]

    #matrix = []
    sol = Solution()
    res = sol.searchMatrix(matrix, 3)
    print(res)