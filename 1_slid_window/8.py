def find_permutation(str1, pattern):
    start = 0
    dic = {}
    match = 0
    for p in pattern:
        dic[p] = dic.get(p, 0) + 1

    for i in range(len(str1)):
        s = str1[i]
        if s in dic:
            dic[s] -= 1
            if dic[s] == 0:
                match += 1

        if len(dic) == match:
            return True

        if i >= len(pattern) - 1:
            s = str1[start]
            if s in dic:
                if dic[s] == 0:
                    match -= 1
                dic[s] += 1
            start += 1

    return False


def main():
    print('Permutation exist: ' + str(find_permutation("oidbcaf", "abc")))
    print('Permutation exist: ' + str(find_permutation("odicf", "dc")))
    print('Permutation exist: ' + str(find_permutation("bcdxabcdy", "bcdyabcdx")))
    print('Permutation exist: ' + str(find_permutation("aaacb", "abc")))


main()
