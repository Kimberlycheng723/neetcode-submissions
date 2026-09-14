class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range (len(numbers)):
            temp = target - numbers[i]
            l, r = i+1, len(numbers)-1
            while l<=r:
                mid = (l+r)//2
                if numbers[mid] == temp:
                    return [i+1, mid+1]
                if numbers[mid] < temp:
                    l = mid+1
                if numbers[mid] > temp:
                    r = mid-1
        return []
        # Binary Search
        # Create one pointer from the start and loop through
        # Calculate temp = target - numbers[i]
        # Create another two pointer (i+1 , len(numbers)-1)
            # While l<r:
                # Calculate mid = l+r // 2
                # If the numbers[mid] == temp
                    # Return the answer
                # If the numbers[mid] < temp
                    # l = mid+1
                # If the numebrs [mid] > temp
                    # r = mid-1
        # Return empty array if no answer is found