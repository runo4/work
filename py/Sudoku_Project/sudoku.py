N = {1, 2, 3, 4, 5, 6, 7, 8, 9}
YX = [(y, x) for y in range(9) for x in range(9)]


def candidates(t, y, x):
    return N - {*t[y],
                *[r[x] for r in t],
                *[c for r in t[y - y % 3:y - y % 3 + 3]
                  for c in r[x - x % 3:x - x % 3 + 3]]}


def most_candidate(t):
    return min([(y, x, candidates(t, y, x))
                for y, x in YX
                if t[y][x] == 0] or [(None, None, ())],
               key=lambda yxc: len(yxc[2]))


def do_v2(t):
    y, x, numbers = most_candidate(t)
    if y is None:
        return True
    for n in numbers:
        t[y][x] = n
        if do_v2(t):
            return True
    t[y][x] = 0
    return False


def is_solved(t):
    return all(candidates(t, y, x) == set() for y, x in YX)


def main():
    table = [[9, 0, 6, 7, 0, 5, 4, 0, 2],
             [0, 0, 0, 6, 9, 4, 0, 0, 0],
             [4, 0, 7, 0, 3, 0, 5, 0, 9],
             [2, 5, 0, 3, 7, 1, 0, 8, 6],
             [0, 7, 3, 5, 6, 9, 1, 2, 0],
             [1, 6, 0, 4, 8, 2, 0, 5, 7],
             [7, 0, 1, 0, 2, 0, 6, 0, 5],
             [0, 0, 0, 1, 4, 6, 0, 0, 0],
             [6, 0, 8, 9, 0, 7, 2, 0, 1]]
    print(*table, sep='\n')
    print("↓")
    do_v2(table)
    print(*table, sep='\n')
    print("この解答は正しいです" if is_solved(table) else "この解答は正しくありません")


if __name__ == '__main__':
    main()
