class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        array = []
        for index, number in enumerate(nums):
            array.append([number, index])
        
        array.sort()
        i, j = 0, len(nums)-1
        while i<j:
            sum = array[i][0] + array[j][0]
            if sum < target:
                i += 1
            if sum > target:
                j -= 1
            if sum == target:
                return [min(array[i][1], array[j][1]) , max(array[i][1], array[j][1])]
        return []