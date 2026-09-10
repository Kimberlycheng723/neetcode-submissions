class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while l<r:
            sum = numbers[l]+numbers[r]
            if sum<target:
                l += 1
            if sum>target:
                r-=1
            if sum == target:
                return [l+1, r+1]
        return []
        # Create two pointer 
        # While the first < second:
            # sum = first+second numbers 
            #if the sum less than target:
                # first +=1
            # if the sum more than target:
                # second -= 1
            # if the sum == target:
                # return [first+1, second+1]
            # return empty array