import heapq
# O(nlogk) time


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []

        for i in range(k):
            heapq.heappush(pq, nums[i])

        for num in nums[k:]:
            if num > pq[0]:
                heapq.heappop(pq)
                heapq.heappush(pq, num)

        return pq[0]
