def swap(data):
    new = ''
    for i in data:
        if i == 'N':
            new += 'W'
        elif i == 'W':
            new += 'N'
        elif i == 'E':
            new += 'S'
        else:
            new += 'E'
    return new


if __name__ == '__main__':
    for case in range(int(input())):
        n = int(input())
        old = input()
        print('Case #{}: {}'.format(case + 1, swap(old)))
