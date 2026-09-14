class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        for i in range (len(nums)):
            count[nums[i]] -= 1
            if i>0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, len(nums)):
                count[nums[j]] -= 1
                if j-1>i and nums[j] == nums[j-1]:
                    continue
                target = -nums[i]-nums[j]
                if count[target] > 0:
                    res.append([nums[i], nums[j], target])
            
            for j in range(i+1, len(nums)):
                count[nums[j]] += 1
        return res
        # Sort the nums array
        # Create an empty result array
        # Create an empty dictionary
        # Loop through every number and put number, count in dict
        # Loop through the nums (i)
            # Update the count for nums(i) in the dict (-1)
            # Loop through the nums (j)
                # Update the count for nums(j) in the dict (-1)
                # Find temp = target - nums[i] - nums[j]
                # Check whether temp is in the dict or not
                    # If yes:
                        # Update the count for temp in dict
                        # res.append()
            # Update the count of the j back to normal 

       