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
        for i in range (k):
            res.append(heapq.heappop(heap)[1])
        return res

        # Create a empty heap
        # Iterate throught he item in the dictionar
            # add in the item into the heap while the len of heap is less than k

        # Create a result array
        # Heap pop to the array while i<k
            