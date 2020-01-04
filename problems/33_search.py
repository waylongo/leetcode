from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            # print(low, high, mid)
            if nums[mid] == target:
                return mid
            elif nums[low] <= nums[mid] <= target:
                low = mid + 1
            elif nums[low] <= target <= nums[mid]:
                high = mid - 1
            elif target <= nums[low] <= nums[mid]:
                low = mid + 1
            elif nums[mid] <= target <= nums[high]:
                low = mid + 1
            elif target <= nums[mid] <= nums[high]:
                high = mid - 1
            elif nums[mid] <= nums[high] <= target:
                high = mid - 1
            else:
                return -1
        return -1


if __name__ == "__main__":
    nums = [1, 3]
    print("original nums is ", nums)
    sol = Solution()
    res = sol.search(nums, 3)
    print("after, the res is ", res)
