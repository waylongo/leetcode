from typing import List

# https://leetcode.com/problems/rotate-image/discuss/18884/Seven-Short-Solutions-(1-to-7-lines)
class Solution:
    def rotate(self, A: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        A.reverse()
        for i in range(len(A)):
            for j in range(i):
                A[i][j], A[j][i] = A[j][i], A[i][j]


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(matrix)
    sol = Solution()
    sol.rotate(matrix)
    print(matrix)