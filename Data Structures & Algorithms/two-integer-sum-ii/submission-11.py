class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict = {}
        for i in range (len(numbers)):
            temp = target - numbers[i]
            if temp in dict:
                return [dict[temp], i+1]
            dict[numbers[i]] = i+1
        return []
       