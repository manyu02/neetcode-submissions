from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k==len(nums):
            return nums
        cntmap= Counter(nums)
        min_heap = []
        for key, value in cntmap.items():
            heapq.heappush(min_heap, (value,key))
            if len(min_heap)>k:
                heapq.heappop(min_heap)
        return [key for value,key in min_heap]
        