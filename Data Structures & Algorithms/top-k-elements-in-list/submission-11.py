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
        
        res = []
        while len(res) < k:
            res.append(heapq.heappop(heap)[1])
        return res