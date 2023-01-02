# вводные для запуска кода из теста 'aabbbccde':

import collections

if __name__ == '__main__':
    s = sorted(input())
    for i in collections.Counter(s).most_common(3):
        print(*i)