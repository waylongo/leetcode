from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        res = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            low, high = i + 1, len(nums) - 1
            while low < high:
                three_sum = nums[i] + nums[low] + nums[high]
                if three_sum == target:
                    return three_sum
                elif three_sum < target:
                    low += 1
                else:
                    high -= 1
                if abs(three_sum - target) < abs(res - target):
                    res = three_sum
        return res


if __name__ == "__main__":
    nums = [-1, 2, 1, -4]
    sol = Solution()
    res = sol.threeSumClosest(nums, 1)
    print(res)
