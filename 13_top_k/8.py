from heapq import *


def find_closest_elements(arr, K, X):
    result = []

    min_heap = []

    for i in range(len(arr)):
        heappush(min_heap, [abs(arr[i] - X), i])

    for i in range(K):
        index = heappop(min_heap)[1]
        result.append(arr[index])

    return result


def main():
    print("'K' closest numbers to 'X' are: " +
          str(find_closest_elements([5, 6, 7, 8, 9], 3, 7)))
    print("'K' closest numbers to 'X' are: " +
          str(find_closest_elements([2, 4, 5, 6, 9], 3, 6)))
    print("'K' closest numbers to 'X' are: " +
          str(find_closest_elements([2, 4, 5, 6, 9], 3, 10)))


main()
