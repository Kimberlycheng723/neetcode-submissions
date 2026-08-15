class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for index, number in enumerate(nums):
            dict [number] = index
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in dict and dict[diff]!=i:
                return [i, dict[diff]]
            
      