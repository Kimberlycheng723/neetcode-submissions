class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, num in enumerate(nums):
            if num > 0:
                break
            if i!=0 and num==nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l<r:
                sum = num + nums[l] + nums[r]
                if sum < 0:
                    l+=1
                if sum > 0:
                    r -= 1
                if sum == 0:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l]== nums[l-1] and l<r:
                        l+=1
        return res

        
        # Create an empty result list
        # Sort the nums
        # for i, number in enumerate (nums):
            # If the number is more than 0, we can end the for loop
            # If it is not the first element, and if the second element is the same as the a, then we can skip it to avoid duplicate
            # Create two pointer (one at i+1, another at the end)
                # While l<r:
                    # sum = a + nums[l] + nums[r]
                    # If the sum < 0:
                        #l += 1
                    # If the sum > 0:
                        # r -= 1
                    # If the sum == 0:
                        # Return the answer [a, nums[l], nums[r]] using append
                        # l += 1
                        # r -= 1
                        # Check for the next l ,if it is the same as the previous l, if yes then skip it to prevent duplicate
