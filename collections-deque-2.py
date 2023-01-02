# Решение на основе подсказки. Разбор функции getattr()

from collections import deque

N = int(input())
d = deque()

for _ in range(N):
    to_do, *value = input().split()
    getattr(d, to_do)(*value)
print(*d)
