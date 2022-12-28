import itertools


def my_solution():

    S, k = input().split()
    size_range = itertools.count(start=1, step=1);
    S = ''.join(sorted((list(S))))

    for _ in range(int(k)):
        comb_S = list(itertools.combinations(S, next(size_range)))
        for j in comb_S:
            print(*j, sep='')

if __name__ == '__main__':
    my_solution()