from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.dfs(nums, 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in range(index, len(nums)):
            if i - 1 >= index and nums[i] == nums[i - 1]:
                continue
            self.dfs(nums, i + 1, path + [nums[i]], res)


if __name__ == "__main__":
    nums = [1, 2, 2]
    print(nums)
    sol = Solution()
    res = sol.subsetsWithDup(nums)
    print(res)