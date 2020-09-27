def length_of_longest_substring(str1, k):
    start = 0
    max_len = 0
    dic = {}
    max_repeat = 0

    for i in range(len(str1)):
        s = str1[i]

        dic[s] = dic.get(s, 0) + 1
        max_repeat = max(max_repeat, dic[s])
        while i - start + 1 - max_repeat > k:
            s = str1[start]
            dic[s] -= 1
            start += 1
        max_len = max(max_len, i - start + 1)
    return max_len


def main():
    print(length_of_longest_substring("aabccbb", 2))
    print(length_of_longest_substring("abbcb", 1))
    print(length_of_longest_substring("abccde", 1))


main()
