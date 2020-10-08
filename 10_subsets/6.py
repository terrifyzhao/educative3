class Abbreviation:
    def __init__(self, str, start, count):
        self.count = count
        self.start = start
        self.str = str


from collections import deque


def generate_generalized_abbreviation(word):
    result = []
    queue = deque()
    queue.append(Abbreviation([], 0, 0))
    l = len(word)
    while queue:
        ab = queue.popleft()
        if ab.start == l:
            if ab.count != 0:
                ab.str.append(str(ab.count))
            result.append(''.join(ab.str))
        else:
            queue.append(Abbreviation(list(ab.str), ab.start + 1, ab.count + 1))

            if ab.count != 0:
                ab.str.append(str(ab.count))

            new_word = list(ab.str)
            new_word.append(word[ab.start])
            queue.append(Abbreviation(new_word, ab.start + 1, 0))

    return result


def main():
    print("Generalized abbreviation are: " +
          str(generate_generalized_abbreviation("BAT")))
    print("Generalized abbreviation are: " +
          str(generate_generalized_abbreviation("code")))


main()
