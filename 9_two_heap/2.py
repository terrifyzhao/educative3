from heapq import *


class SlidingWindowMedian:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def find_sliding_window_median(self, nums, k):
        result = []

        start = 0
        for i in range(0, len(nums)):
            num = nums[i]
            if not self.max_heap or -self.max_heap[0] >= num:
                heappush(self.max_heap, -num)
            else:
                heappush(self.min_heap, num)

            self.rebalance_heaps()

            if i >= k - 1:

                if len(self.min_heap) == len(self.max_heap):
                    result.append((self.min_heap[0] - self.max_heap[0]) / 2)
                else:
                    result.append(-self.max_heap[0])

                remove_num = nums[start]
                if remove_num <= -self.max_heap[0]:
                    self.remove(self.max_heap, -remove_num)
                else:
                    self.remove(self.min_heap, remove_num)
                self.rebalance_heaps()
                start += 1
        return result

    def remove(self, heap, num):
        index = heap.index(num)
        heap[index] = heap[-1]
        del heap[-1]
        heapify(heap)

    def rebalance_heaps(self):
        if len(self.max_heap) > len(self.min_heap) + 1:
            heappush(self.min_heap, -heappop(self.max_heap))
        elif len(self.max_heap) < len(self.min_heap):
            heappush(self.max_heap, -heappop(self.min_heap))


def main():
    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median(
        [1, 2, -1, 3, 5], 2)
    print("Sliding window medians are: " + str(result))

    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median(
        [1, 2, -1, 3, 5], 3)
    print("Sliding window medians are: " + str(result))


main()
