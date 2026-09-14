class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []
        for i in range(len(nums)):
            if nums[i]>0:
                break
            if i>0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l<r:
                sum = nums[i] + nums[l] + nums[r]
                if sum == 0:
                    answer.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
                if sum < 0:
                    l += 1
                if sum > 0:
                    r -= 1
        return answer

       