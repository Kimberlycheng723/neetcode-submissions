class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Two pointers
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i!=0 and nums[i]==nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l<r:
                sum = nums[i] + nums[l] + nums[r]
                if sum > 0:
                    r -= 1
                if sum < 0:
                    l+= 1
                if sum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l<r and nums[l] == nums[l-1]:
                        l+=1
                        continue
        return res
       
            # Create two pointer (l, r)
            # While the l<r
                # sum = nums[i] + nums[l] + nums[r]
                # If the sum is more than 0
                    # r -= 1
                # If the sum is less than 0
                    # l += 1
                # If the sum is same as 0
                    # add the answer into result array
                    # l+=1
                    # r-=1
                    # If the next l is the same as current l then we can remove duplicate

