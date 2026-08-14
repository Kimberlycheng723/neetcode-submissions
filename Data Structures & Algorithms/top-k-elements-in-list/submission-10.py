class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        for num in nums:
            dict[num] = dict.get(num, 0) + 1
        
        arr = []
        for num, count in dict.items():
            arr.append([count, num])
        arr.sort()

        res = []
        for i in range(k):
            res.append(arr.pop()[1])
        return res
        # Create an empty dictionary
        # Loopthrough and put the nums into the dictionary {num: count}
        # Change it to become an array [count, number]
        # Sort the array
        # While i<k
            # Pop up the number in the top of the array