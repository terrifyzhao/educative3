def find_substring(str1, pattern):
    start = 0
    dic = {}
    match = 0
    min_len = 10000
    sub_start = 0
    for p in pattern:
        dic[p] = dic.get(p, 0) + 1

    for i in range(len(str1)):
        s = str1[i]
        if s in dic:
            dic[s] -= 1
            if dic[s] >= 0:
                match += 1

        while match == len(pattern):
            if min_len > i - start + 1:
                min_len = i - start + 1
                sub_start = start

            s = str1[start]
            if s in dic:
                if dic[s] == 0:
                    match -= 1
                dic[s] += 1
            start += 1

    if min_len > len(str1):
        return ''

    return str1[sub_start:sub_start + min_len]


def main():
    print(find_substring("aabdec", "abc"))
    print(find_substring("abdbca", "abc"))
    print(find_substring("adcad", "abc"))
    print(find_substring("abbbbc", "abbc"))


main()
