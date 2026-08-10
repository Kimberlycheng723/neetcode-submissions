class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for index, num in enumerate(nums):
            dict[num] = index

        for index, num in enumerate(nums):
            diff = target - num
            if diff in dict and dict[diff]!=index:
                return [index, dict[diff]]
        return []
