import heapq

class Solution:
    def maxScore(self, nums1, nums2, k):
        pairs = list(zip(nums2, nums1))
        pairs.sort(reverse=True)  # sort by nums2 desc

        heap = []
        total = 0
        ans = 0

        for min_val, val in pairs:
            heapq.heappush(heap, val)
            total += val

            if len(heap) > k:
                total -= heapq.heappop(heap)

            if len(heap) == k:
                ans = max(ans, total * min_val)

        return ans
        