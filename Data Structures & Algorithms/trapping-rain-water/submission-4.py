class Solution:
    def trap(self, height: List[int]) -> int:
        if height == []:
            return 0
        
        n = len(height)
        maxLeft = [0] * n
        maxRight = [0] * n
        
        maxLeft[0] = height[0]
        for i in range(n):
            maxLeft[i] = max(maxLeft[i-1], height[i])

        maxRight[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            maxRight[i] = max(maxRight[i+1], height[i])

        res = 0
        for i in range(n):
            res += min(maxLeft[i], maxRight[i]) - height[i]
        return res
        

        # Create an empty res
        # Loop through i
            # res = min(maxLeft[i], maxRight[i]) - height[i]
        # return the res