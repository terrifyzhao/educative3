from heapq import *


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def find_next_interval(intervals):
    n = len(intervals)

    result = [0 for _ in range(n)]

    max_start_heap = []
    max_end_heap = []

    for i in range(n):
        heappush(max_start_heap, [-intervals[i].start, i])
        heappush(max_end_heap, [-intervals[i].end, i])

    for i in range(n):
        end, end_index = heappop(max_end_heap)

        result[end_index] = -1

        if -max_start_heap[0][0] >= -end:
            start, index = heappop(max_start_heap)
            while -max_start_heap[0][0] >= -end:
                start, index = heappop(max_start_heap)
            result[end_index] = index

            heappush(max_start_heap, [start, index])

    return result


def main():
    result = find_next_interval(
        [Interval(2, 3), Interval(3, 4), Interval(5, 6)])
    print("Next interval indices are: " + str(result))

    result = find_next_interval(
        [Interval(3, 4), Interval(1, 5), Interval(4, 6)])
    print("Next interval indices are: " + str(result))


main()
