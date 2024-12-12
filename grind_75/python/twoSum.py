from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map: dict[int, int] = {}
        for i in range(len(nums)):
            if nums[i] in map:
                return [map[nums[i]], i]
            else:
                map[target - nums[i]] = i
        return [0, 0]
