from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        idx = 0
        for i in range(len(nums)):
            if i > 0 and i + 1 < len(nums) and nums[i - 1] == nums[i + 1]:
                continue
            nums[idx] = nums[i]
            idx += 1

        print(nums)
        return idx


if __name__ == "__main__":
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(nums)
    sol = Solution()
    res = sol.removeDuplicates(nums)
    print(res)