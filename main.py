# python3
# Kristaps Arnolds Kaidalovs 16.grupa 201RDK001

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next, i))
            pass

        if next in ")]}":
            # Process closing bracket, write your code here
            if are_matching((opening_brackets_stack.pop().char), next) == False:
                return i + 1
            pass

    # Ensure there are no remaining unclosed brackets
    if (len(opening_brackets_stack) > 0):
        return opening_brackets_stack.pop().position + 1

    return "Success"

def main():
    input()
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)


if __name__ == "__main__":
    main()
