from heapq import *


def schedule_tasks(tasks, k):
    intervalCount = 0
    taskFrequencyMap = {}
    for char in tasks:
        taskFrequencyMap[char] = taskFrequencyMap.get(char, 0) + 1

    maxHeap = []
    # add all tasks to the max heap
    for char, frequency in taskFrequencyMap.items():
        heappush(maxHeap, (-frequency, char))

    while maxHeap:
        wait_list = []
        n = k + 1
        while n > 0 and maxHeap:
            intervalCount += 1
            fre, char = heappop(maxHeap)
            if -fre > 1:
                wait_list.append((fre + 1, char))
            n -= 1

        for fre, char in wait_list:
            heappush(maxHeap, (fre, char))

        if maxHeap:
            intervalCount += n

    return intervalCount


def main():
    print("Minimum intervals needed to execute all tasks: " +
          str(schedule_tasks(['a', 'a', 'a', 'b', 'c', 'c'], 2)))
    print("Minimum intervals needed to execute all tasks: " +
          str(schedule_tasks(['a', 'b', 'a'], 3)))


main()
