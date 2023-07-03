import heapq
# keep a heap of k numbers. if the added number is larger than the smallest (top) the heap then replace the top of the heap with that number. This will give you the Kth largest number. 
# Note, heaps only keep the top number as mininal so returning the kth element will not give you that numbers real placement. The object is not sorted. 
class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.min_heap = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        elif val > self.min_heap[0]:
            heapq.heapreplace(self.min_heap, val)
        return self.min_heap[0]


KthLargest(3, [4, 5, 8, 2])
    


