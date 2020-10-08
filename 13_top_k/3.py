class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_point(self):
        print("[" + str(self.x) + ", " + str(self.y) + "] ", end='')

    def cal_length(self):
        return self.x * self.x + self.y * self.y

    def __lt__(self, other):
        return self.cal_length() > other.cal_length()


from heapq import *


def find_closest_points(points, k):
    result = []

    for i in range(k):
        heappush(result, points[i])

    for point in points[k:]:
        if point.cal_length() < result[0].cal_length():
            heappop(result)
            heappush(result, point)

    return result


def main():
    result = find_closest_points([Point(1, 3), Point(3, 4), Point(2, -1)], 2)
    print("Here are the k points closest the origin: ", end='')
    for point in result:
        point.print_point()


main()
