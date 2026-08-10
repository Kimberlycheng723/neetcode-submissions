class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        for num in nums:
            dict[num] = dict.get(num, 0) + 1

        arr = []
        for number, count in dict.items():
            arr.append([count, number])

        arr.sort()

        result = []
        while len(result) < k:
            result.append(arr.pop()[1])
        
        return result