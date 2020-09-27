def find_word_concatenation(str1, words):
    start = 0
    dic = {}
    word_len = len(words[0])
    n = len(words)
    match = 0
    res = []
    for w in words:
        dic[w] = dic.get(w, 0) + 1

    for i in range(0, n * word_len + 1, word_len):
        w = str1[i:i + word_len]
        if w in dic:
            dic[w] -= 1
            if dic[w] == 0:
                match += 1

        if match == len(dic):
            res.append(start)

        if i + word_len >= n * word_len - 1:
            w = str1[start:start + word_len]
            if w in dic:
                if dic[w] == 0:
                    match -= 1
                dic[w] += 1
            start += word_len
    return res


def main():
    print(find_word_concatenation("catfoxcat", ["cat", "fox"]))
    print(find_word_concatenation("catcatfoxfox", ["cat", "fox"]))


main()
