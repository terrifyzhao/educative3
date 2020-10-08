class Parentheses:
    def __init__(self, content, open, close):
        self.content = content
        self.open = open
        self.close = close


from collections import deque


def generate_valid_parentheses(num):
    result = []
    queue = deque()
    queue.append(Parentheses('', 0, 0))
    while queue:
        tmp = queue.popleft()
        if tmp.close == num and tmp.open == num:
            result.append(tmp.content)
        else:
            if tmp.open < num:
                queue.append(Parentheses(tmp.content + '(', tmp.open + 1, tmp.close))
            if tmp.open > tmp.close:
                queue.append(Parentheses(tmp.content + ')', tmp.open, tmp.close + 1))

    return result


def main():
    print("All combinations of balanced parentheses are: " +
          str(generate_valid_parentheses(2)))
    print("All combinations of balanced parentheses are: " +
          str(generate_valid_parentheses(3)))


main()
