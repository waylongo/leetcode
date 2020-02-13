from typing import List


class Solution:
    def exist(self, A: List[List[str]], word: str) -> bool:

        for i in range(len(A)):
            for j in range(len(A[0])):
                if self.dfs(A, i, j, word, 0):
                    return True
        return False

    def dfs(self, A, i, j, word, index):
        if i < 0 or i > len(A) - 1 or j < 0 or j > len(A[0]) - 1:
            return False

        if A[i][j] != word[index]:
            return False

        if index == len(word) - 1:
            return True

        tmp = A[i][j]
        A[i][j] = "#"
        res = self.dfs(A, i - 1, j, word, index + 1) or \
              self.dfs(A, i + 1, j, word, index + 1) or \
              self.dfs(A, i, j - 1, word, index + 1) or \
              self.dfs(A, i, j + 1, word, index + 1)
        A[i][j] = tmp
        return res

if __name__ == "__main__":
    board = \
    [
        # ['A', 'B', 'C', 'E'],
        # ['S', 'F', 'C', 'S'],
        # ['A', 'D', 'E', 'E']
        ['A']
    ]
    print(board)
    sol = Solution()
    res = sol.exist(board, "B")
    print(res)