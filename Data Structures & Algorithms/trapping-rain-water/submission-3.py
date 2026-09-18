class Solution:
    def trap(self, height: List[int]) -> int:
        if height == []:
            return 0
        
        leftMax = [0] * len(height)
        rightMax = [0] * len(height)

        leftMax[0] = height[0]
        for i in range(1, len(height)):
            leftMax[i] = max(leftMax[i-1], height[i])

        rightMax[len(height)-1] = height[len(height)-1]
        for i in range(len(height)-2, -1, -1):
            rightMax[i] = max(rightMax[i+1], height[i])
        
        res = 0
        for i in range(len(height)):
            res += min(leftMax[i], rightMax[i]) - height[i]
        return res

        # Create an empty leftMax array [0]
        # Create an empty rightMax array [0]

        # Build the leftMax array
        # First one is directly take height[0]
        # for i in range(1, len(height)):
            # Get the max value of the leftMax
        
        # Build the rightMax array
        # Last one is directly take len(height)-1
        # for i in range():
            # Get the max value of the right MAX

        # Create empty res
        # res += min(maxLeft[i], maxRight[i]) - height[i]
