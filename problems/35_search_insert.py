from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return low


if __name__ == "__main__":
    nums = [1, 3, 5, 6]
    print(nums)
    sol = Solution()
    res = sol.searchInsert(nums, 0)
    print(res)
