class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = []
        for index, number in enumerate(nums):
            arr.append([number, index])
        arr.sort()

        i = 0
        j = len(nums) - 1
        while i<j:
            cur = arr[i][0] + arr[j][0]
            if cur == target:
                return [min(arr[i][1], arr[j][1]), 
                        max(arr[i][1], arr[j][1]) ]
            elif cur < target:
                i += 1
            else:
                j-=1
      