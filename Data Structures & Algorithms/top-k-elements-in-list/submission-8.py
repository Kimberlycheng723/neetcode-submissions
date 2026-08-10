class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        for num in nums:
            dict[num] = dict.get(num, 0) + 1

        heap = []
        for num in dict.keys():
            heapq.heappush(heap, (dict[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        result = []
        while len(result) < k:
            result.append(heapq.heappop(heap)[1])
        return result