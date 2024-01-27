from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)
        while low < high:
            mid = (low + high) // 2
            if nums[mid] < nums[mid - 1]:
                return min(nums[mid], nums[0])
            if nums[mid] > nums[low]:
                low = mid
            else:
                high = mid
        return nums[0]
