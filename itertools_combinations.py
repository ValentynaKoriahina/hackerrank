import itertools


def my_solution(inp_str = input()):

    S, k = inp_str.split()
    size_range = itertools.count(start=1, step=1);
    S = ''.join(sorted((list(S))))

    for _ in range(int(k)):
        comb_S = list(itertools.combinations(S, next(size_range)))
        for j in comb_S:
            pass
            print(*j, sep='')

if __name__ == '__main__':
    my_solution()