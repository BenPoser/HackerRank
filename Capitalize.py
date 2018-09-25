def solve(s):
    a_string = s.split(' ')
    capitalize = (' '.join((word.capitalize() for word in a_string)))
    return capitalize


if __name__ == '__main__':
    s = input()

    result = solve(s)

    print(result)
