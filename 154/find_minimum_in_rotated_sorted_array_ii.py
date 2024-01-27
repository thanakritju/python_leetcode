from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        cur = nums[0]
        for num in nums[1:]:
            if num < cur:
                return num
        return cur
