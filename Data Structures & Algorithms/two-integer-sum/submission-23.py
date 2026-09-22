class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for index, number in enumerate(nums):
            dict[number] = index
        
        for index, number in enumerate(nums):
            diff = target - number
            if diff in dict and dict[diff]!=index:
                return [index, dict[diff]]
        
        return []