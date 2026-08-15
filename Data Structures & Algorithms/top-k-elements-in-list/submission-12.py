class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create an empty dictionary
        dict = {}
        for num in nums:
            dict[num] = dict.get(num, 0) + 1
        
        arr = []
        for number, count in dict.items():
            arr.append([count, number])
        arr.sort()

        res = []
        for i in range (k):
            res.append(arr.pop()[1])
        return res

        # Iterate throught the nums and put into the dict {number, count}
        # Create an empty array
        # Put the number, count into array [count, number]
        # Sort the array
        
        # Create an empty result array
        # Pop up the answer at the top to the result array