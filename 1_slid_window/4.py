def fruits_into_baskets(fruits):
    start = 0
    dic = {}
    max_count = 0

    for i in range(len(fruits)):
        f = fruits[i]
        dic[f] = dic.get(f, 0) + 1

        while len(dic) > 2:
            f = fruits[start]
            dic[f] -= 1
            if dic[f] == 0:
                del dic[f]
            start += 1
        max_count = max(max_count, i - start + 1)
    return max_count


def main():
    print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
    print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))


main()
